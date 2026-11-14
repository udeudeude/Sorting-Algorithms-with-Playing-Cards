# Reproducible publishing pipeline

## Source of truth

Each edition is archived under `drafts/<version>/` with:
- `reading.md` (US Letter manuscript)
- `booklet.md` (half-letter manuscript)
- `illustrations/` (original image files, not substitutes)
- `diagrams/` (original explanatory figures)

The source documents in `drafts/0.9/` have been preserved. **Their binary artwork has not yet been uploaded.** Therefore the new builder intentionally refuses to produce an unillustrated substitute. This is a preservation safeguard, not a completed publication.

## Build

```sh
python -m pip install pymupdf==1.26.5
# Also install Pandoc, XeLaTeX and the DejaVu fonts.
python scripts/build_edition.py --version 0.9 --output build
```

This builds a reading PDF, a true half-letter booklet imposed two-up on landscape Letter, and `build-report.json` containing page counts and SHA-256 hashes. Reverse sides are rotated 180 degrees for **long-edge duplex printing**.

The GitHub Actions workflow `build-edition.yml` builds and uploads both outputs as review artifacts. It does **not** promote a draft to the public release.

## Approval and publication

1. Review the rendered PDF pages and test the imposition with a physical print.
2. Copy the reviewed PDF bytes into `editions/<version>/`.
3. Update `current-edition.json` with the exact paths, page counts, checksums, and sheet count.
4. Merge to main. The existing `publish-pdfs.yml` validates the manifest and both PDFs, publishes a versioned release, and makes the latest assets discoverable by the Exhibition.
5. Verify both public release URLs and the Exhibition tile.

**Never** update the approved manifest to a version whose binaries are missing or unreviewed. Do not substitute the older 0.3 release's artwork or regenerate approximations.

## Current blocker

The connected GitHub text-file interface cannot transfer local binary files, and the current container cannot reach github.com. The missing original images and PDF binaries must be transferred through a binary-capable route. Until that is solved, this repository contains source and build logic, but not a complete, publishable 0.9 edition.
