# Learner Edition 0.9: source archive

This directory preserves the complete 0.9 reading and half-letter Markdown manuscripts, including thirty algorithm profiles and the comparison matrix.

**Status: source archived, publication incomplete.** The original illustration files, build scripts and two approved PDF binaries are not yet committed here. The relative image references in these manuscripts require the preserved original illustration collection; do not silently replace them with generated approximations.

Original conversation artifacts:
- Sorting-Cards-0.9-READING.pdf (64 pages)
- Sorting-Cards-0.9-BOOKLET-LONG-EDGE.pdf (96 logical pages, 24 duplex sheets)
- Sorting-Cards-0.9-SOURCE.zip (editable source and artwork)

These artifact names identify the original outputs; they are **not** working repository download links.

The approved publication manifest remains 0.5. No release or website update is authorized until the exact PDF pair is present, verified, and the source/assets are recoverable.

## Required next actions

1. Recover and commit original illustration and diagram files with reproducible build/imposition scripts.
2. Rebuild and compare both PDFs to the original 0.9 artifacts; retain exact originals when reproducibility is imperfect.
3. Stage PDFs under `editions/0.9/` and update `current-edition.json` with page counts and SHA-256 checksums.
4. Run `scripts/validate_edition.py`, then publish via the existing GitHub Actions workflow.
5. Verify release assets and Exhibition links from the public site.

**Never publish an older edition under a newer version tag.**
