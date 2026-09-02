# Sorting Algorithms with Playing Cards

A hands-on course for learning sorting algorithms with a standard 52-card deck while comparing two different worlds of algorithmic cost: **what is efficient for a computer** and **what is efficient for human hands at a table**.

The current manuscript is **Learner Draft 0.1**. It is deliberately complete before it is polished: the first learner will print it, work through it with cards, and use that experience to drive the teaching edition.

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
16. Synthesis and strategy selection

## Project structure

- `index.qmd` — introduction, canonical ordering, and learning method
- `part-1-simple-sorts.qmd` — Selection, Insertion, Bubble, Concept Interlude I
- `part-2-divide-partition-heaps.qmd` — Merge, Quick, Quickselect, Heap, Concept Interlude II
- `part-3-noncomparison-and-gaps.qmd` — Counting, Radix, Bucket, Shell
- `part-4-hybrids-and-synthesis.qmd` — Timsort, Introsort, synthesis
- `appendix.qmd` — reference tables, vocabulary, printable experiment sheet, field-note prompts
- `_quarto.yml` — Quarto book configuration

## Build the printable PDF

Install [Quarto](https://quarto.org/) and a TeX distribution supported by Quarto, then from the repository directory run:

```bash
quarto render --to pdf
```

The generated book will appear under `_book/`.

For a browser version:

```bash
quarto render --to html
```

## Status

**Learner Draft 0.1** is a field-test manuscript, not a finished publication. The source is intentionally modular so lessons, exercises, diagrams, and explanatory interludes can be revised independently after actual use.

## Suggested GitHub repository description

> Learn sorting algorithms hands-on with a standard deck of playing cards, comparing physical and computational models of sorting.
