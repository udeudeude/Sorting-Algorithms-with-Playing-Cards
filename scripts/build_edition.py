#!/usr/bin/env python3
"""Build an edition from its preserved source and original artwork.

Fails closed: never replaces missing illustrations, and never publishes by itself.
Requires pandoc, xelatex, and PyMuPDF.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
ASSET_RE = re.compile(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}|!\[[^]]*\]\(([^)]+)\)")


def run(args, cwd):
    subprocess.run(args, cwd=cwd, check=True)


def required_assets(source):
    text = source.read_text(encoding="utf-8")
    paths = {m.group(1) or m.group(2) for m in ASSET_RE.finditer(text)}
    return {Path(p) for p in paths if not p.startswith(("https://", "http://"))}


def check_assets(directory, sources):
    missing = sorted({
        str(directory / item)
        for source in sources
        for item in required_assets(source)
        if not (directory / item).is_file()
    })
    if missing:
        raise RuntimeError("Missing original artwork. Refusing substitute/rebuild:\n" + "\n".join(missing))
    print("Original illustration/diagram references checked.")


def impose(half_path, output):
    source = fitz.open(half_path)
    n = len(source)
    padded = ((n + 3) // 4) * 4
    out = fitz.open()
    for k in range(padded // 4):
        for side, (left, right) in enumerate((
            (padded - 2*k, 1 + 2*k),
            (2 + 2*k, padded - 1 - 2*k),
        )):
            page = out.new_page(width=792, height=612)
            for number, rect in (
                (left, fitz.Rect(0, 0, 396, 612)),
                (right, fitz.Rect(396, 0, 792, 612)),
            ):
                if number <= n:
                    page.show_pdf_page(rect, source, number - 1)
            if side == 1:
                page.set_rotation(180)
    out.save(output, garbage=4, deflate=True)
    return n, padded // 4


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "build")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9]+\.[0-9]+(?:\.[0-9]+)?", args.version):
        raise SystemExit("Invalid version")
    source_dir = ROOT / "drafts" / args.version
    sources = [source_dir / "reading.md", source_dir / "booklet.md"]
    if not all(p.is_file() for p in sources):
        raise SystemExit("Missing complete reading/booklet manuscript pair")
    check_assets(source_dir, sources)
    outdir = args.output.resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    reading = outdir / "Sorting-Algorithms-with-Playing-Cards.pdf"
    half = outdir / "half-letter-intermediate.pdf"
    booklet = outdir / "Sorting-Algorithms-with-Playing-Cards-Booklet-LONG-EDGE.pdf"
    for source, target in zip(sources, (reading, half)):
        run(["pandoc", source.name, "--pdf-engine=xelatex", "--standalone",
             "-o", str(target)], cwd=source_dir)
    logical, sheets = impose(half, booklet)
    with fitz.open(reading) as doc:
        pages = len(doc)
    with fitz.open(booklet) as doc:
        assert len(doc) == sheets * 2
        assert all(page.rotation == 180*(i % 2) for i, page in enumerate(doc))
    report = {
        "version": args.version,
        "reading": {"file": reading.name, "pages": pages, "sha256": sha256(reading)},
        "booklet": {"file": booklet.name, "sheets": sheets, "logical_pages": logical,
                    "pdf_pages": sheets*2, "sha256": sha256(booklet)},
    }
    (outdir / "build-report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
