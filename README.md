# Sorting Algorithms with Playing Cards

An illustrated, hands-on course in thirteen sorting algorithms using a standard 52-card deck. Each method is examined in three settings: on a computer, on a table, and in the hands.

## Current edition: Learner 0.5

**The approved edition is 0.5, not the older 0.3 manuscript or its automatically rendered PDFs.**

The authoritative publication consists of two matching, illustrated PDFs:

1. **Reading edition:** 55 pages, 17 embedded illustrations.
2. **Print booklet:** 36 landscape PDF pages representing 72 imposed booklet pages, on **18 sheets**, with 17 embedded illustrations. **Print landscape, double-sided, flip on the LONG edge, actual size.**

[Browse published releases](https://github.com/udeudeude/Sorting-Algorithms-with-Playing-Cards/releases). **The release is current only when it is version 0.5 or newer.** Older version 0.3 downloads remain available solely as an archive.

The approved 0.5 originals have fixed SHA-256 checksums recorded in [current-edition.json](current-edition.json). Until both originals are committed at the paths in that manifest, the release workflow deliberately publishes nothing instead of substituting an inferior draft.

## Contents

- Selection, Insertion and Bubble Sort
- Inversions, stability and sorting cost models
- Merge Sort, Quicksort, Quickselect and Heapsort
- The comparison-sorting lower bound
- Counting, Radix and Bucket Sort
- Shellsort, Timsort, Introsort and Cycle Sort
- Choosing a strategy, a complexity comparison, a glossary and card exercises

## Canonical deck order

**A–K ♠ → A–K ♥ → A–K ♣ → A–K ♦.** Ace is the earliest rank in each suit; King is the latest. There are no jokers.

## Edition publishing and maintenance

The repository's [current-edition.json](current-edition.json) is the **single source of truth for the currently approved export pair**. Both files must be present and must agree with its hashes, page counts and illustration requirements.

Whenever the book is revised:

1. Work from the latest approved edition **and all subsequent improvements**, never silently regenerate from the historical 0.3 draft.
2. Produce and review both updated PDFs. Check all diagrams, code, tables and print imposition.
3. Place the approved PDFs in a new versioned folder under editions/, update current-edition.json with both file paths, SHA-256 checksums and page counts.
4. Commit the changes to main. [The publisher](.github/workflows/publish-pdfs.yml) verifies the original files, their shared content, illustration count and long-edge booklet orientation, and publishes them together in a versioned GitHub release marked **latest**.
5. The [Exhibition](https://udeudeude.github.io/#project-sorting-cards) discovers that latest release and displays the PDF links automatically, without manual edits or stale hard-coded version numbers.

The publishing job **copies original PDF bytes**. It does not re-typeset them, crop their illustrations, or silently rebuild an older manuscript. The editable source used to produce 0.5 is not yet committed. Until that source is recovered or deliberately reconstructed and reviewed, the two approved PDF exports remain authoritative. This is a real limitation: publishing is automatic **after the updated PDFs are committed**, but authoring new editions from editable source is not yet automatic.

## Earlier source and drafts

The files below remain as a historical development record, **not the current book**:

- [drafts/0.3/book.md](drafts/0.3/book.md) and [drafts/0.3/book-illustrated.md](drafts/0.3/book-illustrated.md): edition 0.3 experiments.
- Older modular course source: index.qmd, part-*.qmd, appendix.qmd, _quarto.yml.
- [Version 0.3 release](https://github.com/udeudeude/Sorting-Algorithms-with-Playing-Cards/releases/tag/learner-draft-0.3): archived output, superseded by 0.5.

The old material must not be used by the release publisher to overwrite the newer teaching edition.
