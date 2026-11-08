#!/usr/bin/env python3
"""Impose half-letter pages onto US-letter landscape duplex sheets."""
import argparse
from pathlib import Path

import fitz


def impose(source: Path, destination: Path, sheets_per_signature: int = 8):
    book = fitz.open(source)
    if not book.page_count:
        raise ValueError("Empty PDF")
    imposed = fitz.open()
    capacity = sheets_per_signature * 4
    for first in range(0, book.page_count, capacity):
        actual = min(capacity, book.page_count - first)
        padded = ((actual + 3) // 4) * 4
        for sheet in range(padded // 4):
            spreads = (
                (padded - 1 - 2 * sheet, 2 * sheet),
                (2 * sheet + 1, padded - 2 - 2 * sheet),
            )
            for left, right in spreads:
                page = imposed.new_page(width=792, height=612)
                for local, rectangle in (
                    (left, fitz.Rect(0, 0, 396, 612)),
                    (right, fitz.Rect(396, 0, 792, 612)),
                ):
                    if local < actual:
                        page.show_pdf_page(
                            rectangle, book, first + local, keep_proportion=True
                        )
    if imposed.page_count % 2:
        raise AssertionError("Booklet requires complete duplex sheets")
    destination.parent.mkdir(parents=True, exist_ok=True)
    imposed.save(destination, garbage=4, deflate=True)
    imposed.close()
    book.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--signature-sheets", type=int, default=8)
    args = parser.parse_args()
    if not 1 <= args.signature_sheets <= 16:
        parser.error("--signature-sheets must be 1 through 16")
    impose(args.source, args.destination, args.signature_sheets)
