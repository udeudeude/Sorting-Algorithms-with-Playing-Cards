# Sorting Algorithms with Playing Cards

A hands-on course for learning sorting algorithms with a standard 52-card deck while comparing two different worlds of algorithmic cost: **what is efficient for a computer** and **what is efficient for human hands at a table**.

The current manuscript is **Learner Field-Test Edition 0.3**. It is deliberately complete before it is polished: the first learner will print it, work through it with cards, and use that experience to drive the teaching edition.

## Canonical deck order

All full-deck exercises use:

**A–K ♠ → A–K ♥ → K–A ♣ → K–A ♦**

## Curriculum

1. Selection Sort
2. Insertion Sort
3. Bubble Sort
4. Concept Interlude: inversions, stability, in-place sorting, adaptiveness, cost models
5. Merge Sort
6. Quicksort
7. Quickselect
8. Heaps and Heapsort
9. Concept Interlude: the Ω(n log n) comparison-sorting lower bound
10. Counting Sort
11. Radix Sort
12. Bucket Sort
13. Shellsort
14. Timsort
15. Introsort
16. Cycle Sort
17. Synthesis and strategy selection

## Project structure

The current print manuscript is [`drafts/0.3/book.md`](drafts/0.3/book.md). The modular Quarto chapters below are an earlier source edition, not the source used for the 0.3 downloads.

- `index.qmd` — introduction, canonical ordering, and learning method
- `part-1-simple-sorts.qmd` — Selection, Insertion, Bubble, Concept Interlude I
- `part-2-divide-partition-heaps.qmd` — Merge, Quick, Quickselect, Heap, Concept Interlude II
- `part-3-noncomparison-and-gaps.qmd` — Counting, Radix, Bucket, Shell
- `part-4-hybrids-and-synthesis.qmd` — Timsort, Introsort, synthesis
- `appendix.qmd` — reference tables, vocabulary, printable experiment sheet, field-note prompts
- `_quarto.yml` — Quarto book configuration

## Printable downloads

These downloads are built from the current 0.3 manuscript and become available after the automated release publisher succeeds:

- [Download the complete course (standard PDF)](https://github.com/udeudeude/Sorting-Algorithms-with-Playing-Cards/releases/download/learner-draft-0.3/sorting-algorithms-with-playing-cards.pdf)
- [Download the printer-ready folded booklet (PDF)](https://github.com/udeudeude/Sorting-Algorithms-with-Playing-Cards/releases/download/learner-draft-0.3/sorting-algorithms-booklet-print.pdf)
- [Download the small-page booklet for reading (PDF)](https://github.com/udeudeude/Sorting-Algorithms-with-Playing-Cards/releases/download/learner-draft-0.3/sorting-algorithms-booklet-pages.pdf)

The printer-ready booklet is imposed two-up on **US-letter landscape sheets**. Print double-sided, **flip on short edge**, at actual size. Fold each set of up to eight sheets separately into signatures, then stack them in sequence. The small-page booklet PDF is intended for screen reading or manual printing, not automatic duplex imposition.

## Rebuild the PDFs

Install [Quarto](https://quarto.org/) (for its bundled Pandoc), a LaTeX distribution with XeLaTeX, and PyMuPDF. The [release workflow](.github/workflows/publish-pdfs.yml) renders `drafts/0.3/book.md` twice (standard and compact-page formats) and imposes the latter into a duplex booklet with `scripts/impose_booklet.py`. The workflow checks the document and page geometry before uploading release assets.

The 0.3 manuscript references a cover art file that is not committed. The release build preserves the typographic title page but omits that missing picture rather than substituting unrelated artwork.

## Status

**Learner Field-Test Edition 0.3** is a field-test manuscript, not a finished publication. The source is intentionally modular so lessons, exercises, diagrams, and explanatory interludes can be revised independently after actual use.

## Suggested GitHub repository description

> Learn sorting algorithms hands-on with a standard deck of playing cards, comparing physical and computational models of sorting.
