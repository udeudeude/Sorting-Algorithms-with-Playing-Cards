---
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
fontsize: 10pt
geometry: "paperwidth=8.5in,paperheight=11in,top=0.75in,bottom=0.70in,left=0.77in,right=0.77in,headsep=0.25in"
header-includes:
  - '\usepackage{graphicx}'
  - '\usepackage{longtable}'
  - '\usepackage{booktabs}'
  - '\usepackage{fancyhdr}'
  - '\usepackage{titlesec}'
  - '\usepackage{xcolor}'
  - '\definecolor{ink}{HTML}{203B3D}'
  - '\titleformat{\section}{\Large\bfseries\sffamily\color{ink}}{}{0pt}{}'
  - '\titleformat{\subsection}{\large\bfseries\sffamily}{}{0pt}{}'
  - '\titleformat{\subsubsection}{\normalsize\bfseries}{}{0pt}{}'
  - '\titlespacing*{\section}{0pt}{12pt}{5pt}'
  - '\titlespacing*{\subsection}{0pt}{8pt}{3pt}'
  - '\titlespacing*{\subsubsection}{0pt}{5pt}{2pt}'
  - '\pagestyle{fancy}'
  - '\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}'
  - '\fancyhf{}'
  - '\fancyhead[LE,RO]{\small\sffamily Sorting Algorithms with Playing Cards}'
  - '\fancyfoot[C]{\thepage}'
  - '\renewcommand{\headrulewidth}{0.3pt}'
  - '\setlength{\headheight}{14pt}'
  - '\setlength{\parskip}{3pt}'
  - '\setcounter{tocdepth}{1}'
---

\begin{titlepage}
\centering
\vspace*{0.35in}
{\Huge\bfseries Sorting Algorithms\par}
\vspace{0.13in}
{\Large with\par}
\vspace{0.13in}
{\Huge\bfseries Playing Cards\par}
\vspace{0.55in}
\includegraphics[width=0.82\textwidth,height=5.3in,keepaspectratio]{illustrations/cover_fan.png}
\vfill
\end{titlepage}


# Contents at a glance
\label{contents}
\begingroup
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\vspace{4pt}\noindent{\sffamily\bfseries\small FOUNDATIONS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent Foundations\dotfill\pageref{foundations}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small ELEMENTARY AND REFINEMENTS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{1}  Selection Sort\dotfill\pageref{alg1}\par
\noindent\textbf{2}  Insertion Sort\dotfill\pageref{alg2}\par
\noindent\textbf{3}  Bubble Sort\dotfill\pageref{alg3}\par
\noindent\textbf{4}  Cocktail Shaker Sort\dotfill\pageref{alg4}\par
\noindent\textbf{5}  Gnome Sort\dotfill\pageref{alg5}\par
\noindent\textbf{6}  Binary Insertion Sort\dotfill\pageref{alg6}\par
\noindent\textbf{7}  Shellsort\dotfill\pageref{alg7}\par
\noindent\textbf{8}  Comb Sort\dotfill\pageref{alg8}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small DIVIDE AND CONQUER}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{9}  Merge Sort\dotfill\pageref{alg9}\par
\noindent\textbf{10}  Quicksort\dotfill\pageref{alg10}\par
\noindent\textbf{11}  Dual-Pivot Quicksort\dotfill\pageref{alg11}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small TREES AND HEAPS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{12}  Tree Sort\dotfill\pageref{alg12}\par
\noindent\textbf{13}  Heapsort\dotfill\pageref{alg13}\par
\noindent\textbf{14}  Tournament Sort\dotfill\pageref{alg14}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small STRUCTURED KEYS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{15}  Counting Sort\dotfill\pageref{alg15}\par
\noindent\textbf{16}  Radix Sort\dotfill\pageref{alg16}\par
\noindent\textbf{17}  Bucket Sort\dotfill\pageref{alg17}\par
\noindent\textbf{18}  Pigeonhole Sort\dotfill\pageref{alg18}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small MOVEMENT CONSTRAINTS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{19}  Cycle Sort\dotfill\pageref{alg19}\par
\noindent\textbf{20}  Pancake Sort\dotfill\pageref{alg20}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small ADAPTIVE AND HYBRID METHODS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{21}  Natural Merge Sort\dotfill\pageref{alg21}\par
\noindent\textbf{22}  Timsort\dotfill\pageref{alg22}\par
\noindent\textbf{23}  Introsort\dotfill\pageref{alg23}\par
\noindent\textbf{24}  Smoothsort\dotfill\pageref{alg24}\par
\vspace{4pt}\noindent{\sffamily\bfseries\small NETWORKS, PILES, AND SPECIAL CASES}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{25}  Bitonic Sort\dotfill\pageref{alg25}\par
\noindent\textbf{26}  Odd-Even Transposition Sort\dotfill\pageref{alg26}\par
\noindent\textbf{27}  Strand Sort\dotfill\pageref{alg27}\par
\noindent\textbf{28}  Patience Sort\dotfill\pageref{alg28}\par
\noindent\textbf{29}  Bogosort\dotfill\pageref{alg29}\par
\noindent\textbf{30}  Stooge Sort\dotfill\pageref{alg30}\par
\vspace{4pt}\noindent\textbf{BEYOND THE ALGORITHMS}\par\hrule
\noindent Designing your own sort\dotfill\pageref{invention}\par
\endgroup
\newpage
\tableofcontents
\newpage
# How to use this book
\label{howto}

Use a standard 52-card deck. Begin with small packets and follow each procedure literally before experimenting with more natural movements. Pencil notes help reveal where comparisons, movements, and workspace become expensive.

## Our exact order

**A–K ♠ → A–K ♡ → A–K ♣ → A–K ♢.** Within each suit, Ace is earliest, King latest. The four suits occur in the order shown. Thus A♠ is first, K♢ is last. A 10-card packet is sorted when its cards appear in the relative order they would occupy in this complete deck. No jokers.

## What does a computer compare?

A computer needs a *key* for each card: the value that decides its place. For our complete order, let suits ♠, ♡, ♣, ♢ have numbers 0, 1, 2, 3, and let ranks A, 2, ..., 10, J, Q, K have numbers 0 through 12. Then

$$\operatorname{key}(card)=13\times\operatorname{suitNumber}+\operatorname{rankNumber}.$$

A♠ has key 0; K♢ has key 51. This representation is useful for the code examples, but the card exercises need only your eyes and the stated order.

## Three settings, not three competing truths

1. **Computer:** an array of 52 records, with comparisons, reads, writes, swaps, and extra storage. A swap is typically several reads and writes.
2. **Table:** a row of face-up cards, with scans, distant exchanges, block slides, piles, and available table area.
3. **In hand:** cards fanned between one or two hands, with limited visible positions, easy insertion, awkward long-distance exchanges, and almost no independent storage.

Some algorithms are inherently ill-suited to being performed entirely in hand. The honest lesson is to recognize that limitation, not to invent a procedure that quietly becomes a different algorithm.

## Understanding algorithmic complexity

**n** means number of items. In this book n=10 for many first exercises and n=52 for a full deck. **n²** means n multiplied by itself: 52²=2,704. A *quadratic* sort is one whose cost grows roughly in proportion to n²; this does **not** assert that it performs exactly 2,704 operations.

**log₂ n** asks how many successive halvings take a positive number to 1. Since 32 = 2⁵, **log₂ 32 = 5**; since 64 = 2⁶, **log₂ 64 = 6**. Fifty-two lies between 32 and 64, so log₂ 52 lies between 5 and 6, approximately **5.70**. Halving 52 gives 26, 13, 6.5, 3.25, 1.625, 0.8125: after five halvings it is still above 1; after six it is below 1. **n log₂ n** is about 296 for 52 cards, but is a *growth-rate landmark*, not a promised 296 comparisons.

**Big-O**, written O(...), describes an asymptotic upper bound on the growth of an operation count, disregarding constant multipliers and lower-order terms. It does **not** say that the exact count equals the expression inside the parentheses. For example, Selection Sort's comparison count is n(n−1)/2: at n=52 that is **1,326**, although its growth is O(n²), and 52² is 2,704. The factor of roughly one-half disappears in Big-O notation. **Ω(...)** gives an asymptotic lower bound, and **Θ(...)** means matching upper and lower bounds.

In performance tables, **best**, **average**, and **worst** refer to different initial arrangements of the **same number of cards**, not different decks. A fully sorted packet can be easiest for Insertion Sort, while a reversed packet is difficult; Selection Sort makes the same number of comparisons in both. This distinction belongs beside the performance analysis because the algorithm, the input order, and the counted operation jointly determine the result.

**Best case** asks which input arrangement makes this specific procedure cheapest. **Average case** needs a stated distribution of inputs, usually uniformly random permutations. **Worst case** asks which arrangement makes it most expensive. Always ask *what is being counted*: comparisons, swaps, writes, physical gestures, or time? Different answers can all be correct.

**Stable** means equal-key records retain their original relative order. Our 52-card order gives every card a distinct key, so to test stability we temporarily sort by **rank only**: 7♠ and 7♡ then have equal keys even though they are different cards. **In-place** means using little additional storage beyond the original array. **Adaptive** means taking advantage of input that is already partly ordered.

## Reading the code examples

Python examples use the numeric card keys 0–51 defined above unless an algorithm specifically works with rank or suit fields. The code is there to reveal the operations that the physical exercise makes visible. It is not necessary to run it to learn the algorithm. A simple implementation may make different storage choices from an optimized library implementation; where this affects complexity, the lesson points it out.

## A worked growth-rate comparison

| Cards (n) | n log₂ n (rounded) | n² | Selection comparisons n(n−1)/2 |
|---:|---:|---:|---:|
| 10 | 33 | 100 | 45 |
| 26 | 122 | 676 | 325 |
| 52 | 296 | 2,704 | 1,326 |
| 104 | 697 | 10,816 | 5,356 |

The **first column** is the number of cards. The next two columns are *mathematical functions*, not measured work. Only the **last column** is an exact count for the specified Selection Sort procedure. It compares 51 remaining cards to the current minimum, then 50, then 49, and so on: **51 + 50 + ... + 1 = 52×51/2 = 1,326**. This count does not change even if the deck is already sorted. Doubling n approximately quadruples n² but increases n log₂ n by only a little more than a factor of two.

\begin{center}
\includegraphics[width=0.92\linewidth,keepaspectratio]{diagrams/successive-halving.pdf}
\end{center}

In the tables below, **¹** marks an expectation over uniformly random arrangements; **†** marks a mathematical growth-function example rather than an exact number of comparisons. Counts such as “shifts,” “swaps,” and “checks” are different operations and should not be compared as though they were interchangeable. For Counting Sort and Radix Sort, the key range **k** and number of passes **d** are stated explicitly.

## Learning routine

Start with 8–12 random cards unless a lesson specifies otherwise. First execute the rule faithfully. Then repeat with the same cards in sorted, reversed, or deliberately structured order. Record comparisons and movements separately. Finally attempt the in-hand variant and note whether it is still the same algorithm.

A *pass* is one traversal of the currently active cards. A *comparison* is one decision of which of two keys comes earlier. A *move* is an item changing position; a *block move* shifts several cards together in one hand gesture. We will never quietly treat a block gesture as a single computer write.



# Foundations: thinking algorithmically
\label{foundations}

## A problem, a procedure, and a promise

A **sorting problem** specifies a collection, a comparison rule, and the result required. An **algorithm** is a finite, unambiguous procedure that works for every permitted input. An **implementation** realizes that procedure in a particular medium. The *same* sorting idea may be implemented with array writes, linked-list pointers, a row of cards, or two hands, but its actual costs differ.

A sorting algorithm must establish two claims: it terminates, and its result is ordered without losing or duplicating items. One useful proof pattern is an **invariant**: something guaranteed to remain true after each step. Selection Sort's completed prefix, Insertion Sort's ordered prefix, and Merge Sort's sorted sublists are examples. State the invariant, show it holds initially, show a step preserves it, and show that termination makes it imply the desired result.

## Total orders and keys

Our canonical order gives every card a distinct key. But a rank-only exercise gives four cards the same key. A *total order* compares every pair consistently: the order must be transitive (if A precedes B and B precedes C, A precedes C) and cannot contradict itself. A comparator that changes its mind can defeat an otherwise correct algorithm. A stable sort preserves the original order of records with equal keys.

## Reading code and pseudocode

A variable is a named storage location. An array position (an **index**) is a numbered slot; Python indexes begin at zero. A loop repeats instructions, and recursion solves a problem by invoking the same method on smaller instances. In pseudocode, `if`, `while`, `for`, and `return` describe control flow rather than a particular programming language. Every Python example operates on comparable keys; for a physical deck, use the key function introduced above.

## What exactly are we counting?

A **comparison** asks which of two keys comes first. A **write** changes a stored value. A **swap** exchanges two positions, often requiring multiple reads and writes. A **move** is medium-dependent: a hand can slide a block in one gesture while an array must write every displaced element. Memory is not free: a temporary pile, a stack of recursion frames, and an output array are all workspace of different kinds.

**Best case** means the least work among permitted inputs of size n; **worst case** the most. **Average case** requires a specified distribution of inputs, often uniform random permutations. Neither describes how long your particular shuffled deck will take. For a fair comparison, hold the deck and the cost model fixed and vary only the algorithm or initial arrangement being studied.

## A disciplined card experiment

Take 10 distinct random cards. Write down their initial order, then use *exactly the same order* for each competing method. Record comparisons and individual movements separately. Repeat on sorted, reverse-sorted, nearly sorted, and duplicate-key (rank-only) packets. To compare 52-card behavior, don't infer precise runtime from an asymptotic formula: measure or derive the operations the implementation actually performs.

\begin{quote}
\textbf{Inventor's notebook.} Before improving a sort, write down what it must preserve, what operation you want to reduce, and what tradeoff you are willing to accept. “Feels faster” is a hypothesis; a reproducible count or proof is evidence.
\end{quote}

# Reading the algorithm profiles
\label{profiles}

Every numbered sorting algorithm begins with the same compact **At a Glance** profile. The five small bars express an *editorial, ordinal assessment*, not a measured speed or a mathematically precise score. **One bar** means generally unfavorable for that purpose; **three** means workable with qualifications; **five** means especially appropriate. Scores are relative within this book. They should prompt a question, not settle an engineering decision.

The eight measures ask different things. **Learning value** rates how much the method teaches about algorithms. **Small packets** considers approximately 10 to 52 items. **Nearly sorted** asks whether existing order helps. **Large random** means large, unstructured inputs on an ordinary sequential computer, with conventional memory and comparison costs. **Low extra memory** rewards small auxiliary storage; it does not mean fewer comparisons. **Tabletop ease** concerns executing the method with cards on a table. **In-hand ease** means actually maintaining the procedure without a table. **Practical relevance** considers whether the algorithm or its central technique is used in real software or specialized systems.

The *usage label* distinguishes production standards, components of production systems, specialized techniques, educational methods, and deliberately impractical examples. A high learning score is entirely compatible with low practical relevance. An algorithm can also be highly relevant in a specialized domain while receiving a low large-random-input score: the assumptions are different.

**Do not read the bars as benchmark results.** For actual computer efficiency, use the chapter's time, memory, and operation-count tables; for cards, use its step-by-step procedures and experiments. The short italic line beneath each profile names its most important qualification. These profiles are a navigational aid, not a replacement for the chapter.

# 1. Selection Sort

\label{alg1}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Teaching classic; niche when writes are costly}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Few swaps, many comparisons}
\endgroup
\end{center}

## Core idea

**Repeatedly select the earliest remaining card and place it at the next fixed position.**

\begin{center}
\includegraphics[width=0.96\linewidth,keepaspectratio]{diagrams/selection-boundary.png}
\end{center}

## History and uses

An elementary procedure with no useful single inventor; still used pedagogically and where writes are expensive.

## Pseudocode

```text
for i = 0 to n-2:
    min_index = i
    for j = i+1 to n-1:
        if key(a[j]) < key(a[min_index]):
            min_index = j
    swap a[i] and a[min_index]
```

## Python example

```python
def selection(a):
    for i in range(len(a)-1):
        m = min(range(i,len(a)), key=a.__getitem__)
        a[i], a[m] = a[m], a[i]
    return a
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n²) | 45 comparisons | 1,326 comparisons |
| Average | O(n²) | 45 comparisons | 1,326 comparisons |
| Worst | O(n²) | 45 comparisons | 1,326 comparisons |
| Memory | O(1) | constant | constant |
| Stable? | No | No | No |

**For 52 cards:** 1,326 comparisons, regardless of initial order; at most 51 exchanges.


## Strengths, weaknesses, and cautions

Few exchanges, simple invariant. But it ignores pre-existing order and performs quadratic comparisons.

## Cards on a table

Ten face-up cards in a row: scan all remaining cards, mark the earliest, swap with the first unsorted card, and move the boundary right.

## Cards in hand, without a table

Hold a small packet spread in one hand. Scan all unplaced cards, extract the earliest, and put it at the front of a growing sorted packet in your other hand. This preserves the selection idea but replaces swaps with extraction.

## Experiment

Compare a sorted and a shuffled 10-card packet. Both demand 45 comparisons. Try swapping versus extracting and shifting.

## Three-setting checkpoint

Computer: low writes; table: distant swaps are awkward; hands: selecting and transferring is natural, but changes the movement accounting.

### Trace: what is fixed after each pass?

Start with `7♠ 3♠ 9♠ 2♠ 5♠`. The first scan finds 2♠; swap it with 7♠. You now have `2♠ | 3♠ 9♠ 7♠ 5♠`. The bar is the boundary: nothing to its left will ever be reconsidered. The second scan finds 3♠ already at the boundary, so no physical swap is needed. Continue with `2♠ 3♠ | 9♠ 7♠ 5♠`.

This illustrates a **loop invariant**: after k passes, the first k positions contain the k earliest cards, correctly ordered. The proof is simple: each scan selects the earliest card not yet fixed; placing it after the already-fixed cards cannot invalidate them.

### A counting convention that matters

The standard nested-loop implementation compares each remaining candidate to the current minimum. For 52 cards the counts are 51 + 50 + ... + 1 = **1,326**. Some physical descriptions say “scan all 52” and accidentally count the initial sighting as a comparison. Looking at the first candidate establishes a current minimum; the *next* candidate requires the first comparison. Distinguish inspections from comparisons.

### Stable selection by shifting

If you extract the earliest remaining card and shift the intervening cards as a block, you preserve their order. For rank-only sorting this can preserve the order of equal-ranked cards. That is a stable variant, but it no longer has the same few-writes advantage in a computer array. A physical optimization can be a computational pessimization.

### A complete ten-card procedure

Deal ten random cards face-up in a row. Put a pencil immediately to the left of the row as a movable boundary. On pass 1, point to the first card as your *current minimum*, then compare it with each of the other nine. Whenever a card belongs earlier, point to that instead. Only after the ninth comparison do you exchange the minimum with the first position. Slide the pencil one place right. On pass 2, compare the first of the nine remaining cards with the other eight, exchange the winner into position 2, and advance the pencil again. Continue with seven, six, and fewer comparisons until the last card is automatically correct.

**Why it works.** Once you have found the minimum of the unsorted region, no later action can reveal an earlier card in that region: you inspected them all. That minimum can be fixed permanently. This is a particularly transparent *loop invariant*: after every pass, the completed prefix is precisely the corresponding prefix of the final answer.

**What to count.** For ten cards, the passes require 9+8+7+6+5+4+3+2+1 = **45 comparisons**; for 52 cards, 51+50+...+1 = **1,326**. A physical inspection of the first card is not yet a two-card comparison. Count distant swaps separately from inspections and comparisons.

## What should remain in your head

> **Find the next item globally; place it permanently.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/ordered_stacks.png}
\end{flushright}


# 2. Insertion Sort

\label{alg2}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production component; teaching classic}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Excellent on short or nearly ordered packets}
\endgroup
\end{center}

## Core idea

**Build a sorted prefix by inserting each new item into its proper position.**

\begin{center}
\includegraphics[width=0.96\linewidth,keepaspectratio]{diagrams/insertion-shift.png}
\end{center}

## History and uses

A longstanding manual method, important today for small or nearly ordered data and as a hybrid finishing step.

## Pseudocode

```text
for i = 1 to n-1:
    key_item = a[i]
    j = i-1
    while j >= 0 and a[j] > key_item:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key_item
```

## Python example

```python
def insertion(a):
    for i in range(1,len(a)):
        x=a[i]; j=i-1
        while j>=0 and a[j]>x:
            a[j+1]=a[j]; j-=1
        a[j+1]=x
    return a
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n) | 9 comparisons | 51 comparisons |
| Average | O(n²) | 22.5 shifts¹ | 663 shifts¹ |
| Worst | O(n²) | 45 shifts | 1,326 shifts |
| Memory | O(1) | constant | constant |
| Stable? | Yes | Yes | Yes |

**For 52 cards:** Already sorted: 51 key comparisons. Reverse order: 1,326 key comparisons and 1,326 shifts.


## Strengths, weaknesses, and cautions

Adaptive and simple, but expensive when many cards must travel far.

## Cards on a table

Deal ten cards face-up; treat the first as sorted. Lift the next card, slide later cards to the right, and insert into the gap.

## Cards in hand, without a table

Hold a sorted fan in your left hand; draw one card at a time from the right-hand packet and insert into the fan at its correct location. This is the most natural in-hand algorithm.

## Experiment

Compare shuffled, sorted, and reverse-sorted packets. Count comparisons separately from shifting gestures.

## Three-setting checkpoint

Computer: multiple array writes per insertion; table: one block slide may feel cheap; hands: insertion into a fan is exceptionally natural.

### Trace: insert one card without disturbing the rest

Suppose the sorted hand contains `2♠ 5♠ 9♠` and the next card is `7♠`. Compare 7♠ backward: it precedes 9♠, so 9♠ shifts right; it follows 5♠, so stop and insert. The result is `2♠ 5♠ 7♠ 9♠`. Nothing else needed to be compared.

For 52 already-sorted cards, insertion requires **51** unsuccessful “should this shift?” comparisons. In reverse order it makes **1,326** successful comparisons and 1,326 individual shifts. For a uniformly random permutation of 52 distinct cards, the expected number of inversions, and hence shifts, is 52×51/4 = **663**. Comparisons can be slightly more because some insertions finish with a final unsuccessful comparison.

### Why stability comes for free

If two cards share a key, stop shifting when the preceding card has an **equal** key. Do not shift equal-key cards past each other. That small choice preserves their original order, and is why conventional Insertion Sort is stable.

### Worked insertion, including ties

Start with `3♠ 8♠ 5♠ 2♠`. Regard `3♠` as sorted. Insert `8♠` after it, so the sorted prefix is `3♠ 8♠`. Next lift `5♠`: compare with `8♠` (move 8 right), then `3♠` (stop), and put 5 into the gap: `3♠ 5♠ 8♠`. Lift `2♠` and shift all three cards right to insert it at the front. The sorted prefix grows one card at a time.

When sorting **by rank alone**, two sevens have equal keys. To preserve their original suit order, shift a preceding card only when its key is *strictly greater* than the new card's key. Do not shift on equality. This is why conventional Insertion Sort is stable.

**Why it works.** Before inserting the next card, the prefix is already sorted. Shifting only cards later than the newcomer makes one gap in precisely the right place; nothing before or after the gap is left out of order. On an already sorted 52-card packet, there are 51 key comparisons and no shifts. On a reverse-sorted packet there are 1,326 comparisons and 1,326 shifts in this straightforward version. The same quadratic worst-case label conceals an enormous difference in actual work.

## What should remain in your head

> **Existing order is useful information.**



# 3. Bubble Sort

\label{alg3}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Primarily educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Adjacent exchanges reveal inversions}
\endgroup
\end{center}

## Core idea

**Repeatedly repair out-of-order adjacent pairs.**

## History and uses

A classic exchange sort popularized in early computing instruction; mostly pedagogical today.

## Pseudocode

```text
active_end = n-1
repeat:
    swapped = false
    for j = 0 to active_end-1:
        if a[j] > a[j+1]:
            swap a[j] and a[j+1]
            swapped = true
    active_end = active_end-1
until not swapped or active_end <= 0
```

## Python example

```python
def bubble(a):
    for end in range(len(a)-1,0,-1):
        changed=False
        for i in range(end):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                changed=True
        if not changed: break
    return a
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n) | 9 comparisons | 51 comparisons |
| Average | O(n²) | 22.5 swaps¹ | 663 swaps¹ |
| Worst | O(n²) | 45 swaps | 1,326 swaps |
| Memory | O(1) | constant | constant |
| Stable? | Yes | Yes | Yes |

**For 52 cards:** Already sorted: 51 comparisons with early exit. Reverse order: 1,326 comparisons and 1,326 adjacent swaps.


## Strengths, weaknesses, and cautions

Very local and easy to verify; usually much worse than insertion sort.

## Cards on a table

Place ten cards in a row. Compare each adjacent pair; swap if reversed. Repeat, excluding the settled rightmost card each pass.

## Cards in hand, without a table

Spread a packet in one hand. Compare and exchange neighbors with your other hand. The repeated back-and-forth is possible but noticeably cumbersome.

## Experiment

Put A♠ at the far right, then put K♦ at the far left. Compare how far each travels in one left-to-right pass.

## Three-setting checkpoint

Computer: repeated comparisons and swaps; table: local swaps easy but numerous; hands: neighbor exchanges are physically fussy.

### Count the backward pairs before sorting

Use `5♠ 2♠ 4♠`. The pair 5♠/2♠ is backward because 5♠ appears before a card that should precede it. So is 5♠/4♠. The pair 2♠/4♠ is already correct. There are **two inversions**. Bubble Sort performs exactly two swaps on this packet: `5 2 4 → 2 5 4 → 2 4 5`.

Every swap of an inverted *adjacent* pair eliminates exactly one inversion, and does not change the relative order of any other pair. That is why the number of swaps in ordinary Bubble Sort equals the initial inversion count. On a reversed 52-card deck, every pair is inverted: 1,326 swaps. The early-exit version needs only 51 comparisons if the deck is already sorted.

### Why direction matters

On a left-to-right pass, a very late card at the far left can bubble right through many neighbors immediately. A very early card at the far right moves left by only one position in that same pass. You are seeing the algorithm's directionality, not a property of the cards.

### What Bubble Sort is really measuring

An **inversion** is any pair of cards in the wrong relative order, even when they are not neighbors. In `4♠ 2♠ 3♠`, the inversions are `(4♠,2♠)` and `(4♠,3♠)`: two pairs, not just the adjacent pair. If you swap an inverted *adjacent* pair, you remove exactly one inversion without changing the relative order of any other pair. Thus the number of swaps in ordinary adjacent-exchange Bubble Sort equals the initial inversion count.

Try `5♠ 1♠ 4♠ 2♠ 3♠`: list the inverted pairs on paper, then count actual adjacent swaps. They should agree. A sorted packet has zero inversions; a reversed packet of 10 distinct cards has 45. For 52 reversed cards, there are 1,326 inversions, so Bubble Sort must perform that many adjacent swaps. It may perform additional comparisons while discovering that no swaps remain.

**Directional asymmetry.** On a left-to-right pass, a late card near the front can move many positions right by repeated swaps; an early card at the far right usually moves only one position left per pass. This is a property of the direction of scanning, not an inconsistency in the algorithm. Reverse the scan direction and the asymmetry reverses.

## What should remain in your head

> **Local repairs can take many global passes.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_exchange.png}
\end{flushright}


# 4. Cocktail Shaker Sort
\label{alg4}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Primarily educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Two-way bubbling repairs both ends}
\endgroup
\end{center}

## Core idea

Bubble Sort in both directions: sweep left-to-right to place the latest remaining card, then right-to-left to place the earliest.

## History and uses

A bidirectional exchange sort, also called cocktail sort or shaker sort; a simple improvement over one-direction Bubble Sort.

## Pseudocode

```text
Repeat until a sweep makes no swaps: sweep adjacent pairs left-to-right; shrink right boundary; sweep right-to-left; shrink left boundary.
```

## Python example

```python
def cocktail(a):
    lo, hi = 0, len(a)-1
    while lo < hi:
        changed = False
        for i in range(lo, hi):
            if a[i] > a[i+1]: a[i],a[i+1]=a[i+1],a[i]; changed=True
        if not changed: break
        hi -= 1; changed=False
        for i in range(hi, lo, -1):
            if a[i-1] > a[i]: a[i-1],a[i]=a[i],a[i-1]; changed=True
        if not changed: break
        lo += 1
    return a
```

## Performance and interpretation

Best O(n) with early exit; average and worst O(n²); O(1) extra space; stable if equal keys are not swapped.

**For a 10-card packet:** at most 45 adjacent comparisons in the simple shrinking-boundary worst-case count per one-direction pass schedule, but two-direction scheduling varies. **For a full 52-card deck:** quadratic worst-case comparisons, with much faster termination on already ordered cards. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Deal ten cards in a row. On the outward sweep, compare neighboring cards from left to right and swap backward pairs. The latest card settles at the right edge. Now sweep back from right to left; the earliest card settles at the left edge. Move both boundaries inward. Stop after a sweep without exchanges.

## Cards in hand, without a table

A narrow fan can support adjacent exchanges, but repeatedly reversing direction is awkward. Keep a finger marking the current active interval; avoid quietly extracting and reinserting cards.

## Why it works

After a forward sweep, the maximum of the active interval is at its right boundary; after a backward sweep, the minimum is at its left boundary. Those positions can be excluded safely.

### Deeper investigation

**Directional asymmetry.** A forward Bubble Sort pass can push a very late card many places right but moves an early card left by at most one position. The backward sweep of Cocktail Shaker Sort corrects that imbalance. On a packet with one early card stranded at the right, the backward pass can carry it all the way left. On uniformly disordered inputs, the total work remains quadratic.

## Experiment

Put the earliest card at the far right and the latest card at the far left. Compare the number of passes against ordinary Bubble Sort.

## Computer, table, and hand

**Computer:** bidirectional sweeps are easy to index. **Table:** turning the sweep around costs no storage. **Hands:** reverse direction requires physically changing attention.

\begin{quote}
\textbf{Inventor's notebook.} Why does adding a backward sweep help some inputs but not change the quadratic worst case?
\end{quote}

## What should remain in your head

**Bubble Sort in both directions: sweep left-to-right to place the latest remaining card, then right-to-left to place the earliest.**


# 5. Gnome Sort
\label{alg5}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Primarily educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Simple backward walks; many exchanges}
\endgroup
\end{center}

## Core idea

Walk forward while neighboring cards are ordered; step backward and exchange when they are not.

## History and uses

Popularized under the name Gnome Sort by Dick Grune; it is an adjacent-exchange relative of Insertion Sort.

## Pseudocode

```text
Start at position 1. If at the beginning or the preceding card is not later, advance; otherwise swap with the predecessor and step back.
```

## Python example

```python
def gnome(a):
    i=1
    while i < len(a):
        if i==0 or a[i-1] <= a[i]: i+=1
        else: a[i-1],a[i]=a[i],a[i-1]; i-=1
    return a
```

## Performance and interpretation

Best O(n); average/worst O(n²); O(1) extra memory; stable with strict greater-than swaps.

**For a 10-card packet:** an already sorted packet advances after nine neighbor checks. **For a full 52-card deck:** an already sorted deck advances after 51 neighbor checks; reversed input triggers quadratic swaps. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Make a row of ten cards. Put a marker at the second. If the two neighboring cards are in order, move the marker right; otherwise exchange them and move the marker left. At the far left, turn around. Continue until the marker passes the far right.

## Cards in hand, without a table

This is executable in a fan: compare the current card with its neighbor, move backward after a swap. The frequent finger repositioning is its physical cost.

## Why it works

Whenever the marker advances, the prefix behind it is sorted; backward exchanges repair the local violation until that claim is restored.

## Experiment

Compare Gnome Sort with Insertion Sort on the same reversed packet. Count swaps versus block shifts.

## Computer, table, and hand

**Computer:** the index can move backward at negligible overhead. **Table:** a finger can track the current position. **Hands:** the finger and card exchanges repeatedly backtrack.

\begin{quote}
\textbf{Inventor's notebook.} Can two algorithms perform similar logical work yet feel very different in your hands?
\end{quote}

## What should remain in your head

**Walk forward while neighboring cards are ordered; step backward and exchange when they are not.**


# Concept interlude A: Inversions, equal keys, and stability

\label{interlude-a}

An **inversion** is a pair of cards that is backward relative to the desired order, even if the two cards are not adjacent. For example, if 5♠, 2♠, 4♠ lie left-to-right, the backward pairs are **(5♠, 2♠)** and **(5♠, 4♠)**: two inversions. There is no inversion between 2♠ and 4♠. To *write down every backward pair* means to inspect each possible pair and list those where the earlier-positioned card should actually come later.

For six cards there are 15 possible pairs. Examine each once. Bubble Sort eliminates exactly one inversion per adjacent swap, so the number of swaps is exactly the starting inversion count.

An **equal key** is not an identical card. If sorting by rank alone, 7♠ and 7♡ both have key “7.” A **stable** algorithm preserves whichever of those two appeared first. That matters when sorting student records by grade after sorting them by name, or when combining several sorts.

**Exercise:** take 5♠, 7♡, 5♣, 7♢. Sort by rank alone, first using stable Insertion Sort, then using swap-based Selection Sort. Write down the within-rank suit sequence before and after. The ordinary Selection Sort may disturb it.

**In-place** does not mean “requires no work surface.” It means the computer implementation needs only a bounded amount of extra memory. A card-table algorithm may be easy precisely because it uses lots of physical space.

**Quadratic** is shorthand for a growth pattern proportional to n². Selection, Insertion, and Bubble all have quadratic worst cases, but Selection makes the same comparisons even on sorted data, whereas Insertion becomes linear and Bubble can stop after one clean pass.

**Four questions to ask, with actual answers:**

1. *Best case?* What starting arrangement produces least work? For Insertion Sort, already sorted cards.
2. *Average case?* If the 52 cards were randomly shuffled, how much work would a typical run require? For Insertion Sort, about 663 shifts on average (one per inversion).
3. *Worst case?* Which arrangement maximizes the work? For Insertion Sort, reverse order gives 1,326 shifts.
4. *Which operation?* A 20-card block slide is one gesture for a hand but 20 element writes in a straightforward computer array.

**Three-setting test:** Perform Insertion Sort on 10 cards on the table, then in a hand. Do not time yourself initially. Record comparisons, individual shifts, and block gestures. Which cost model best predicts your experience?



### A comparison experiment with a precise question

The instruction “write down every backward pair” means: look at every pair of positions i and j with i before j, and ask whether the card at i belongs **after** the card at j. For `5♠ 2♠ 4♠`, write `(5♠,2♠)` and `(5♠,4♠)`; do not write `(2♠,4♠)`. This is counting inversions, not adjacent pairs only.

When asking about **best**, **average**, and **worst** cases, hold the algorithm, packet size, and counting rule fixed. Best: what arrangement minimizes comparisons? Worst: what arrangement maximizes them? Average: what happens under a stated random model, usually all distinct-card permutations equally likely? Then ask what you are counting: comparisons, array writes, swaps, or hand gestures. Without that last choice, “fastest” is ambiguous.


# 6. Binary Insertion Sort
\label{alg6}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production component; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Fewer key comparisons, not fewer shifts}
\endgroup
\end{center}

## Core idea

Find each insertion position by binary search in the sorted prefix, then shift the intervening block.

## History and uses

A classical optimization of insertion sorting; it reduces comparisons but not the amount of movement in an array.

## Pseudocode

```text
For each next key, binary-search its insertion position in the sorted prefix; shift the intervening items right; place the key.
```

## Python example

```python
def binary_insertion(a):
    for i in range(1,len(a)):
        key=a[i]; lo=0; hi=i
        while lo<hi:
            mid=(lo+hi)//2
            if key < a[mid]: hi=mid
            else: lo=mid+1
        a[lo+1:i+1]=a[lo:i]
        a[lo]=key
    return a
```

## Performance and interpretation

O(n log n) comparisons in the worst case, but O(n²) moves and overall O(n²) time for array storage; O(1) extra storage for an in-place shift implementation; stable with upper-bound insertion.

**For a 10-card packet:** the insertion search needs at most four comparisons per key, but may shift up to nine cards. **For a full 52-card deck:** the final insertion search needs at most six comparisons, but may shift up to 51 cards. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Take the next card out of the row. In the sorted prefix, compare it to the middle card, then to the middle of the remaining half, until the insertion slot is known. Slide the block from that slot to the right and insert the key.

## Cards in hand, without a table

A fanned hand makes middle positions accessible, but physical searching may require opening the fan. Compare this with ordinary backward scanning.

## Why it works

Binary search finds the first position after all equal keys; shifting preserves the relative order of the existing prefix.

### Deeper investigation

**Worked comparison.** Imagine the sorted prefix [2, 4, 6, 8, 10, 12, 14] and an incoming 5. Ordinary insertion scans backward past 14, 12, 10, 8, and 6 before finding the slot. Binary search compares 5 with 8, then 4, then 6: three comparisons. But both methods must shift 6, 8, 10, 12, and 14. The comparison saving is real; the movement saving is zero.

## Experiment

Count comparisons and shifted cards separately on ten reversed cards. Did binary search actually reduce physical effort?

## Computer, table, and hand

**Computer:** binary search reduces key comparisons. **Table:** block slides may be one physical gesture. **Hands:** finding the midpoint in a fan may be awkward.

\begin{quote}
\textbf{Inventor's notebook.} If comparisons become logarithmic, why does the entire sort remain quadratic?
\end{quote}

## What should remain in your head

**Find each insertion position by binary search in the sorted prefix, then shift the intervening block.**


# Interlude: Binary search does not move cards

Binary search locates a position in logarithmically many comparisons because each comparison rules out about half the candidate positions. But insertion into an array still shifts all the intervening items. **Searching and moving are different costs.** With 52 cards, a binary search of a sorted prefix needs at most six comparisons to locate a slot, yet moving a card from one end to the other may still shift 51 records. A hand can slide a block as one gesture, illustrating why the best method depends on the physical model.


# 7. Shellsort

\label{alg7}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; historical production}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Gap sequence controls the tradeoff}
\endgroup
\end{center}

## Core idea

**Repair long-distance disorder with gapped insertion sorts, then finish with gap 1.**

## History and uses

Donald Shell published it in 1959; performance depends strongly on gap sequence.

## Pseudocode

```text
for gap in decreasing gaps ending in 1:
    for i = gap to n-1:
        item = a[i]; j = i
        while j >= gap and a[j-gap] > item:
            a[j] = a[j-gap]; j -= gap
        a[j] = item
```

## Python example

```python
def shell(a):
    gap=len(a)//2
    while gap:
        for i in range(gap,len(a)):
            x=a[i]; j=i
            while j>=gap and a[j-gap]>x:
                a[j]=a[j-gap]; j-=gap
            a[j]=x
        gap//=2
    return a
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | Gap-dependent | depends | depends |
| Average | Gap-dependent | depends | depends |
| Worst | O(n²), simple gaps | 100† | 2,704† |
| Memory | O(1) | constant | constant |
| Stable? | No | No | No |

**For 52 cards:** For 52 cards, halving gaps are 26, 13, 6, 3, 1; the exact comparison count depends on input.


## Strengths, weaknesses, and cautions

Can improve insertion without extra storage; gap analysis and nonlocal access are awkward.

## Cards on a table

Lay 12 cards in numbered positions. Gaps 6, 3, 1: sort interleaved groups at each gap, preserving their physical slots.

## Cards in hand, without a table

In one fan, count forward 6 positions and compare distant cards, then repeat at gaps 3 and 1. This is possible but bookkeeping-heavy.

## Experiment

Place the earliest card at the end of a 12-card packet. Compare ordinary insertion with gapped insertion.

## Three-setting checkpoint

Computer: index jumps; table: marked positions help; hands: long-distance comparisons are error-prone.

### What a gap pass actually sorts

For 12 cards and gap 3, treat positions 1,4,7,10 as one subsequence, positions 2,5,8,11 as another, and positions 3,6,9,12 as a third. Insertion-sort each subsequence while leaving its cards in those positions. The resulting row is **3-sorted**: cards separated by three positions are ordered. The entire row is not necessarily sorted.

Now reduce the gap, eventually to 1. The final gap-1 pass is ordinary Insertion Sort, but much of the long-distance disorder has already been removed. Different gap sequences give different worst-case guarantees; there is no honest single “Shellsort takes X comparisons on 52 cards” figure without specifying the gaps and input.

Try 12 cards with gaps 6, 3, 1, then 6, 4, 1. Count comparisons and long-distance movements. The difference is a property of the gap schedule, not an error in your execution.

### Why the gaps actually help

With twelve cards in a row, use gaps **6, 3, 1**. At gap 6, insertion-sort the pairs in positions `(1,7)`, `(2,8)`, and so on. At gap 3, insertion-sort four-card subsequences `(1,4,7,10)`, `(2,5,8,11)`, and `(3,6,9,12)`. At gap 1, perform ordinary Insertion Sort over the entire row. The gap-3 stage guarantees only that each of those three interleaved subsequences is ordered, **not** that the whole row is sorted.

Imagine the earliest card starts in position 12. Ordinary insertion can shift it left through eleven adjacent positions; a gap pass can move it several positions in one comparison-and-shift sequence. The final gap-1 pass then encounters a packet with much of its large-scale disorder already removed.

**Why it works.** The last pass is genuine Insertion Sort, so correctness is guaranteed even if earlier gaps achieved little. Earlier passes are an optimization, not a separate correctness requirement. Performance depends strongly on the gap sequence: a single universal 52-card comparison count for “Shellsort” would be misleading.

## What should remain in your head

> **Repair large-scale disorder before fine adjustments.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_ascending.png}
\end{flushright}


# 8. Comb Sort
\label{alg8}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Primarily educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Large gaps remove distant inversions}
\endgroup
\end{center}

## Core idea

Exchange out-of-order pairs separated by a shrinking gap, finishing with adjacent comparisons.

## History and uses

Described by Włodzimierz Dobosiewicz and later popularized by Stephen Lacey and Richard Box; addresses Bubble Sort’s slow movement of small items trapped near the end.

## Pseudocode

```text
Start with gap n; repeatedly divide gap by about 1.3 (minimum 1); compare and exchange pairs gap apart; finish only after a gap-1 pass makes no swaps.
```

## Python example

```python
def comb(a):
    gap=len(a); changed=True
    while gap>1 or changed:
        gap=max(1,int(gap/1.3)); changed=False
        for i in range(len(a)-gap):
            if a[i]>a[i+gap]:                a[i],a[i+gap]=a[i+gap],a[i]; changed=True
    return a
```

## Performance and interpretation

Typical practical performance is often much better than Bubble Sort; worst case O(n²), O(1) extra space, not stable.

**For a 10-card packet:** a shrinking gap can displace a card seven positions at once. **For a full 52-card deck:** distant swaps can repair large inversions that would require many adjacent passes. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Arrange ten cards in a row and label positions. Begin with a large gap (for example 7), compare positions 1 and 8, then 2 and 9, then 3 and 10. Shrink the gap by approximately 1.3 each round until it reaches one; keep making adjacent passes until no swap occurs.

## Cards in hand, without a table

Distant exchanges in a fan are cumbersome; this makes Comb Sort a good lesson in computer-friendly versus hand-friendly operations.

## Why it works

At gap 1 the algorithm becomes Bubble Sort with an early-exit condition, which guarantees eventual completion.

## Experiment

Place the earliest card at the rightmost position. Compare how many passes Comb Sort and Bubble Sort require to bring it home.

## Computer, table, and hand

**Computer:** index arithmetic makes distant exchanges cheap. **Table:** distant exchanges require reaching across the row. **Hands:** a fan is poorly suited to distant exchanges.

\begin{quote}
\textbf{Inventor's notebook.} Why can a large gap repair a bad inversion much faster than adjacent swaps?
\end{quote}

## What should remain in your head

**Exchange out-of-order pairs separated by a shrinking gap, finishing with adjacent comparisons.**


# Interlude: Recursion and recurrence relations

A recursive algorithm must have a **base case** and must reduce the problem toward it. Merge Sort splits n items into two halves and performs O(n) work merging them: T(n)=2T(n/2)+O(n). There are approximately log₂ n levels, each moving O(n) items, giving O(n log n). Quicksort's balance is data-dependent: T(n)=T(k)+T(n-k-1)+O(n). If k is near n/2, recursion is balanced; if k=0 repeatedly, the sum becomes quadratic.

**Try it:** draw a recursion tree for eight cards, then a lopsided tree in which each partition leaves one card on one side and seven on the other. Count levels and total cards examined.


# 9. Merge Sort

\label{alg9}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production standard; foundational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Predictable work; needs merging workspace}
\endgroup
\end{center}

## Core idea

**Divide the packet into halves, sort each, then merge sorted packets.**

\begin{center}
\includegraphics[width=0.96\linewidth,keepaspectratio]{diagrams/merge-exposed.png}
\end{center}

## History and uses

John von Neumann described the method in 1945; valuable for stable sorting and sequential or external data.

## Pseudocode

```text
merge_sort(a):
    if length(a) <= 1: return a
    split a into left and right halves
    left  = merge_sort(left)
    right = merge_sort(right)
    while both halves have remaining items:
        compare their exposed first items
        append the earlier one to output
    append any remaining half without comparisons
    return output
```

## Python example

```python
def merge_sort(a):
    if len(a)<2: return a[:]
    m=len(a)//2
    l=merge_sort(a[:m]); r=merge_sort(a[m:])
    out=[]
    while l and r:
        out.append(l.pop(0) if l[0]<=r[0] else r.pop(0))
    return out+l+r
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n log n) | ~33† | ~296† |
| Average | O(n log n) | ~33† | ~296† |
| Worst | O(n log n) | ~33† | ~296† |
| Memory | O(n) | ~10 slots | ~52 slots |
| Stable? | Yes | Yes | Yes |

**For 52 cards:** For 52 distinct cards, ordinary balanced merging uses between 140 and 249 comparisons, depending on order and merge outcomes; not a fixed count.


## Strengths, weaknesses, and cautions

Stable and reliable, but needs extra output storage for conventional arrays.

## Cards on a table

Split 8 cards into 4, 2, and 1. Merge pairs, then fours, then eights, taking the earlier exposed card each time.

## Cards in hand, without a table

Hold two already sorted packets, one in each hand, with the next candidate visible at the same edge. Compare exposed cards and feed the earlier to an output packet; a helper or surface makes this much easier.

## Experiment

Merge two presorted 13-card suit packets. Compare against sorting their 26 mixed cards from scratch.

## Three-setting checkpoint

Computer: sequential reads but output memory; table: piles are easy; hands: three simultaneous packets exceed comfortable grip.

### Trace: a merge is not a search of both piles

Suppose two already-sorted piles expose `2♠ 7♠ 10♠` and `4♠ 5♠ 9♠`. Compare only the exposed fronts: 2 versus 4, take 2; then 7 versus 4, take 4; then 7 versus 5, take 5; then 7 versus 9, take 7; then 10 versus 9, take 9; finally append 10. The output is `2 4 5 7 9 10`. You never search an entire pile to find its next minimum: the smallest remaining card is always exposed.

Balanced Merge Sort on 52 distinct cards requires **between 140 and 249 comparisons**, depending on the arrangement, for the usual recursive split-and-merge implementation. The upper bound comes from summing at most (left size + right size − 1) comparisons at each merge. It is much lower than Selection Sort's 1,326. The tradeoff is additional output storage.

### Stability and physical orientation

If sorting by rank alone and both piles expose 7s, choose the 7 from the **left** pile first. The order of equal keys survives. Be explicit about which end of each physical pile is the “front”; reversing a pile while picking it up can accidentally destroy the order you worked to establish.

### The complete eight-card tabletop exercise

Deal eight random cards face-up. Split them into a left packet of four and a right packet of four, preserving the order within each packet. Split each four into two packets of two; split each pair into single cards. Now **merge upward**: compare the exposed cards of neighboring singleton packets and produce four sorted two-card packets; merge those into two sorted four-card packets; finally merge the two fours into one sorted eight-card packet. Keep the next card of each input packet visible, and collect each output without accidentally reversing it.

For example, merging `2♠ 7♠ 10♠` with `4♠ 5♠ 9♠` requires only five comparisons: take 2, 4, 5, 7, 9, then append 10. Once one input packet empties, the remainder of the other is already ordered and can be appended without comparison.

**Why it works.** A singleton is trivially sorted. If two input packets are sorted, the earliest remaining card must be at the exposed front of one of them. Taking the earlier exposed card therefore preserves sorted output. By induction, each merge level is correct. The same argument explains why merging works on disk files or linked lists: only the fronts need to be accessible.

**Implementation warning.** The educational Python example uses `pop(0)` on lists. In Python, that shifts remaining elements and is not an efficient way to implement linear-time merging. A production-style version uses two indices into the left and right arrays, then writes sequentially into an output array. The **algorithm** is O(n log n); an inefficient container operation can make a particular implementation slower.

## What should remain in your head

> **Sort tiny pieces; combine by merging.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/four_piles.png}
\end{flushright}


# 10. Quicksort

\label{alg10}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production standard; foundational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Fast typical partitioning; pivot sensitivity}
\endgroup
\end{center}

## Core idea

**Choose a pivot, partition into earlier/later cards, then recurse on both sides.**

\begin{center}
\includegraphics[width=0.96\linewidth,keepaspectratio]{diagrams/pivot-partition.png}
\end{center}

## History and uses

Tony Hoare devised it in 1959 and published it in 1961; central to efficient general-purpose sorting.

## Pivot and partition: a physical explanation

A **pivot** is a chosen reference card, not necessarily the median. **Partitioning** means inspecting each other card and putting it into EARLIER or LATER relative to the pivot. For pivot 8♡, 3♠ belongs in EARLIER and 2♣ in LATER. Neither group is internally sorted yet. A poor pivot makes one huge group; a good pivot divides the work approximately in half.

The table version creates two piles. An in-place computer partition instead swaps items across a boundary in the original array, saving extra storage but costing exchanges. That is exactly why implementation details matter.

## Pseudocode

```text
quicksort(a):
    if length(a) <= 1: return a
    choose a pivot p
    partition all other items into earlier and later
    return quicksort(earlier) + [p] + quicksort(later)
# For equal keys, use a separate equals group.
```

## Python example

```python
def quick(a):
    if len(a)<2: return a[:]
    p=a[0]
    return quick([x for x in a[1:] if x<p])+[p]+quick([x for x in a[1:] if x>=p])
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n log n) | ~33† | ~296† |
| Average | O(n log n) | ~33† | ~296† |
| Worst | O(n²) | 100† | 2,704† |
| Memory | O(n) in example | ~10 slots | ~52 slots |
| Stable? | No | No | No |

**For 52 cards:** First-card pivot on sorted 52 cards: 1,326 pivot comparisons. Balanced partitions: about 200–250 comparisons, depending on split sizes.


## Strengths, weaknesses, and cautions

Fast on balanced partitions, vulnerable to pathological pivot choices; in-place variants are more intricate.

## Cards on a table

Choose first card as pivot. Deal others into EARLIER and LATER piles; sort each pile by the same rule; join them with the pivot between.

## Cards in hand, without a table

Keep pivot visible in one hand; distribute remaining cards into two held packets. Recursion soon requires extra piles, pockets, or a helper.

## Experiment

Try sorted and shuffled packets with first-card pivot. A bad pivot leaves one huge pile and one empty pile.

## Three-setting checkpoint

Computer: in-place partition can avoid new arrays; table: dealing piles is natural; hands: recursive storage becomes a bottleneck.

### Pivot and partition are operations, not decorations

A **pivot** is one selected card used as a reference. A **partition** separates the other cards into those earlier and later than that pivot. Take `8♠ 3♠ 10♠ 2♠ 9♠` with 8♠ as pivot. Partition into `3♠ 2♠ | 8♠ | 10♠ 9♠`. The left and right groups are not yet sorted, but every left card precedes the pivot and every right card follows it. Therefore the pivot's *rank among these five* is now fixed: it will be third.

A good pivot divides a packet into roughly equal pieces. A bad pivot, such as always choosing the earliest card of an already sorted packet, produces one empty side and one side only one card smaller. For 52 cards that naive pattern makes **1,326** pivot comparisons, matching quadratic growth. Balanced partitioning typically takes only a few hundred comparisons, but the exact number depends on the partition scheme and pivot choices.

### Why the implementation matters

Dealing into two piles is easy to follow but requires space for extra packets. Partitioning an array in place instead uses indices and exchanges, reducing auxiliary storage while increasing the importance of which cards are touched and moved. Both preserve the pivot principle; they do not have the same movement costs.

### Follow a pivot all the way through

Take `7♠ 2♠ 9♠ 4♠ 5♠ 1♠ 8♠`. Choose `5♠` as the **pivot**, the reference value against which you compare every other card. A **partition** is the division into cards earlier than 5 (`2,4,1`) and later than 5 (`7,9,8`). Neither side is yet sorted. Sort the earlier group recursively, then the later group, and concatenate `1,2,4 | 5 | 7,8,9`. The pivot is in its final *rank position* as soon as partitioning finishes, even though the two sides still require work.

**Why it works.** All elements on the left precede the pivot; all on the right follow it. If each side is sorted, their concatenation with the pivot is sorted. The algorithm relies on this partition invariant, not on any particular way of moving cards.

**Pivot quality matters.** If a pivot divides 52 cards into roughly 26 and 25, recursion stays shallow. If a first-card pivot is always the earliest card of an already sorted packet, it produces partitions of sizes 0 and 51, then 0 and 50, and so forth: 1,326 pivot comparisons for the simple version. On a table, dealing into two piles is natural but needs workspace; an in-place computer partition may instead swap across boundaries. These are implementations of the same partitioning principle with different movement and memory costs.

## What should remain in your head

> **Partition first; recurse on smaller problems.**



# Side expedition: Quickselect (not a sort)
\label{quickselect}

Quickselect answers “Which card would be kth if I sorted everything?” without sorting everything. Choose a pivot, partition into earlier/later piles, and keep **only** the pile containing the target position. Adjust the target position when discarding the earlier pile and pivot.

**Try it:** From 15 random cards, find the 8th card in sorted order. If the EARLIER pile contains seven cards, the pivot is the answer. If it contains more, search EARLIER for the same target rank. If fewer, search LATER for target rank minus (size of EARLIER + 1).

Expected time is O(n) for good pivot behavior; naive pivots permit O(n²) worst cases. In hand, the partitioning works for one round, but repeated pile storage quickly becomes awkward. **Lesson:** solve only the problem you actually need solved.

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/orbital_partition.png}
\end{flushright}


# 11. Dual-Pivot Quicksort
\label{alg11}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production standard in some libraries}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape More intricate partitioning}
\endgroup
\end{center}

## Core idea

Partition around two pivots to produce three regions, then recursively sort those regions.

## History and uses

A well-known Quicksort variant used in some standard-library implementations, including Java primitive-array sorting.

## Pseudocode

```text
Choose two ordered pivots p<=q; partition items into less than p, between p and q, and greater than q; recurse into the three regions.
```

## Python example

```python
def dual_pivot(a):
    if len(a)<2: return a[:]
    p,q=sorted((a[0],a[-1]))
    low=[]; middle=[]; high=[]; equalp=[]; equalq=[]
    for x in a:
        if x<p: low.append(x)
        elif x==p: equalp.append(x)
        elif x<q: middle.append(x)
        elif x==q: equalq.append(x)
        else: high.append(x)
    if p==q: return dual_pivot(low)+equalp+dual_pivot(high)
    return dual_pivot(low)+equalp+dual_pivot(middle)+equalq+dual_pivot(high)
```

## Performance and interpretation

Average O(n log n), worst O(n²) for poor pivots; memory depends on partition implementation; simple pile version is not in-place.

**For a 10-card packet:** one partition can divide the packet into three groups. **For a full 52-card deck:** balanced pivots reduce recursion depth, but bad pivots still create quadratic work. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Choose two cards as pivots and put the earlier one on the left. Deal remaining cards into three piles: earlier than first, between them, and later than second. Recursively sort each pile and concatenate in order.

## Cards in hand, without a table

Holding three independent groups plus pivots is usually impractical without a surface. A second person can act as a temporary pile holder.

## Why it works

Every key in the first region precedes p, every middle key lies between p and q, and every key in the last region follows q; sorting each region suffices.

## Experiment

Compare one-pivot and two-pivot partitioning on the same 15-card packet. Count comparisons per dealt card, not just number of recursive calls.

## Computer, table, and hand

**Computer:** three-way partitioning has constant bookkeeping. **Table:** three labeled piles are easy. **Hands:** three piles plus pivots exceed comfortable workspace.

\begin{quote}
\textbf{Inventor's notebook.} Do more partitions necessarily mean fewer comparisons?
\end{quote}

## What should remain in your head

**Partition around two pivots to produce three regions, then recursively sort those regions.**


# 12. Tree Sort
\label{alg12}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Tree shape and balancing matter}
\endgroup
\end{center}

## Core idea

Insert each key into a binary search tree; traverse the tree in order to output sorted keys.

## History and uses

Closely connected to binary search trees and early data-structure research; illustrates that a sorting algorithm can be built around a reusable search structure.

## Pseudocode

```text
Insert each key into a binary search tree; visit left subtree, node, then right subtree.
```

## Python example

```python
def tree_sort(a):
    tree=None
    def put(t,x):
        if t is None: return [x,None,None]
        if x<t[0]: t[1]=put(t[1],x)
        else: t[2]=put(t[2],x)
        return t
    def walk(t):
        if t is not None:
            yield from walk(t[1]); yield t[0]; yield from walk(t[2])
    for x in a: tree=put(tree,x)
    return list(walk(tree))
```

## Performance and interpretation

Expected O(n log n) on random distinct input; worst O(n²) for an unbalanced tree; O(n) storage. Balanced trees avoid the quadratic height.

**For a 10-card packet:** a balanced tree needs roughly four levels of decisions. **For a full 52-card deck:** a balanced 52-node tree has height around six, but sorted insertion may create a 52-node chain. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Place the first card at the root of a drawn tree. For each next card, compare with the root and go left if earlier or right otherwise, repeating until an empty child slot is reached. Finally collect cards by traversing left subtree, parent, right subtree.

## Cards in hand, without a table

A spatial tree is not a practical one-hand method. The inability to represent pointers physically is the lesson.

## Why it works

Every node’s left subtree contains earlier keys and its right subtree later keys; an in-order traversal must therefore be sorted.

### Deeper investigation

**Balanced versus degenerate.** Insert 5, 3, 7, 2, 4, 6, 8: the resulting tree has height three. Insert 2, 3, 4, 5, 6, 7, 8: every new card travels right, creating a chain of height seven. Both trees contain the same seven keys. Self-balancing trees use rotations to prevent this collapse, but those rotations add structural work not shown in the simple code.

## Experiment

Build trees from sorted and shuffled packets of ten. Compare maximum tree depth and number of comparisons.

## Computer, table, and hand

**Computer:** pointer nodes incur allocations. **Table:** the tree is spatially legible. **Hands:** the tree cannot be held as a stable fan.

\begin{quote}
\textbf{Inventor's notebook.} What goes wrong when the tree becomes a chain?
\end{quote}

## What should remain in your head

**Insert each key into a binary search tree; traverse the tree in order to output sorted keys.**


# 13. Heapsort

\label{alg13}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production component; specialized}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Strong worst-case bound, low extra storage}
\endgroup
\end{center}

## Core idea

**Maintain a complete binary tree whose parent is never earlier than its children.**

## History and uses

J. W. J. Williams published heapsort in 1964; Floyd improved heap construction. Heaps are essential for priority queues.

## Pseudocode

```text
build a max-heap by sifting down parents in reverse order
for end = n-1 down to 1:
    swap heap root with a[end]
    shrink active heap to positions 0..end-1
    sift the new root down, swapping with the larger child
```

## Python example

```python
def heap_sort(a):
    import heapq
    h=list(a); heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n log n) | ~33† | ~296† |
| Average | O(n log n) | ~33† | ~296† |
| Worst | O(n log n) | ~33† | ~296† |
| Memory | O(1) in-place | constant | constant |
| Stable? | No | No | No |

**For 52 cards:** 52-card in-place heapsort has order-of-hundreds of comparisons; a precise count depends on input and heap implementation.


## Strengths, weaknesses, and cautions

Worst-case guarantee and little extra array space; poor locality and difficult manual bookkeeping.

**Implementation note:** The short Python example uses `heapq` and a separate list. It demonstrates heap ordering, but not the in-place Heapsort whose memory bound appears in the table.

## Cards on a table

Use 7 cards as a tree: positions 1 above 2–3, with 4–7 below. Sift parents 3, 2, 1 down; extract root to final rightmost position and restore the heap.

## Cards in hand, without a table

Try a 7-card fan with positions numbered. Parent-child comparisons require jumping across nonadjacent cards; beyond 7 this is impractical without a layout or index guide.

## Experiment

Compare the same seven cards as a visible tree and as one row. Observe that the tree structure is not the same as full sorted order.

## Three-setting checkpoint

Computer: tree is implicit in array indices; table: tree can be drawn; hands: random access is hard.

### A heap is not a sorted tree

For a **max-heap**, the parent must be at least as late as either child. That does not tell you which child is earlier, and it does not tell you the order of the leaves. For example, with a root of K♠, children 8♠ and Q♠ both satisfy the heap rule. The root is the latest card; the second-latest need not be at the left child.

To build a seven-card heap, arrange the cards in a complete tree with positions 1 at the root, 2 and 3 beneath it, and 4–7 as leaves. Process parents **3, 2, 1**, sifting each down against its later child. To sort, exchange the root with the last active position, shrink the heap by one, and sift the replacement root down. Repeating produces an ascending array from left to right.

Heapsort is guaranteed O(n log n) even for adversarial inputs. A single extraction from a 52-card heap descends at most five levels, though building the heap and making decisions among children also costs comparisons. Do not interpret “five levels” as “five comparisons for the entire sort.”

### Build and dismantle a seven-card heap

Lay seven cards at numbered positions in a tree: position 1 at the top; positions 2 and 3 beneath; positions 4 and 5 beneath 2; positions 6 and 7 beneath 3. A **max-heap** requires every parent to be *later* than either child in our canonical order. The children need not be ordered relative to one another.

Build bottom-up: inspect parent 3 and its children 6 and 7; exchange with its later child if needed, continuing down that branch. Do the same for parent 2, then parent 1. Starting with the last parent works because all subtrees below it are already heaps when you repair that parent. The root now holds the latest card.

To extract, exchange the root with the final active position; that card is now permanently sorted at the right. Shrink the active heap, then **sift down** the new root by repeatedly swapping with its later child when needed. Repeat until only one card remains. Try to identify what the heap guarantees after each extraction: the finished suffix is sorted, and the active prefix is a valid max-heap.

**Why it works.** The heap property puts the largest remaining key at the root without fully sorting the rest. Each extraction fixes one final position, and sifting repairs the partial order. A computer represents the tree in a flat array, using children at indices `2i+1` and `2i+2` (zero-based); that representation saves pointers and extra memory but is less obvious to human hands.

## What should remain in your head

> **Maintain enough partial order to extract the next extreme.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/house_of_cards.png}
\end{flushright}


# 14. Tournament Sort
\label{alg14}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Winners emerge from a comparison tree}
\endgroup
\end{center}

## Core idea

Arrange pairwise contests in a tournament tree; the winner is the earliest key, and only the winner’s path needs updating.

## History and uses

Tournament trees are classic selection structures and useful in multiway merging and external sorting.

## Pseudocode

```text
Build a bracket of pairwise minima; output the winner; replace its leaf with infinity and replay only contests on its path; repeat.
```

## Python example

```python
def tournament_sort(a):
    if not a: return []
    n=1
    while n<len(a): n*=2
    t=[(float('inf'),-1)]*(2*n)
    for i,x in enumerate(a): t[n+i]=(x,i)
    for i in range(n-1,0,-1): t[i]=min(t[2*i],t[2*i+1])
    out=[]
    for _ in a:
        value,leaf=t[1]; out.append(value)
        i=n+leaf; t[i]=(float('inf'),-1)
        while i>1:
            i//=2; t[i]=min(t[2*i],t[2*i+1])
    return out
```

## Performance and interpretation

O(n log n) time and O(n) auxiliary tree storage; selection updates cost O(log n).

**For a 10-card packet:** a 16-leaf padded bracket gives four comparison levels per update. **For a full 52-card deck:** a 64-leaf padded bracket gives six comparison levels per update. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Use eight cards in a visible bracket. Compare pairs and advance the earlier card; continue until one champion remains. Remove that card, then replay only the matches affected by its absence.

## Cards in hand, without a table

Requires more simultaneously visible branches than two hands can comfortably hold; a table or paper bracket is the faithful implementation.

## Why it works

Each internal node stores the minimum of its subtree; replacing one leaf can change only nodes along its ancestor path.

### Deeper investigation

**A remembered defeat.** In an eight-card bracket, the eventual winner has directly defeated only three other cards. Once that winner is removed, most of the other comparisons are still valid. The next winner must be found by replaying only the contests along the removed card's path. This is the distinction between a remembered comparison and Selection Sort's repeated full scans.

## Experiment

Compare selecting eight winners by rescanning the whole packet versus updating a tournament bracket. Count only key comparisons.

## Computer, table, and hand

**Computer:** the tournament tree remembers previous comparisons. **Table:** a bracket makes this memory visible. **Hands:** holding the whole bracket is impractical.

\begin{quote}
\textbf{Inventor's notebook.} How much work can be saved by remembering previous comparisons?
\end{quote}

## What should remain in your head

**Arrange pairwise contests in a tournament tree; the winner is the earliest key, and only the winner’s path needs updating.**


# Concept interlude B: Why comparisons have a lower bound

\label{interlude-b}

If you may learn order only by comparing two distinct items, each comparison answers a yes/no question. With n distinct cards there are n! (n factorial) possible orders. For three cards, 3!=6. For five cards, 5!=120.

A sequence of comparisons can be pictured as a branching **decision tree**. A tree of height h has at most 2^h leaves, so distinguishing n! arrangements requires

$$2^h\ge n!,\qquad h\ge\log_2(n!).$$

That quantity grows as **Ω(n log n)**. It is a worst-case lower bound for *comparison-based* sorting. It does not say every input requires that many comparisons, nor does it say all algorithms have identical constants.

For five distinct cards, six comparisons distinguish at most 64 cases, but there are 120 possible orders. Some arrangement therefore needs at least seven comparisons. For 52 cards the information-theoretic lower bound is **at least 226 comparisons** (ceil(log₂(52!))).

Counting, Radix, and Bucket Sort do not violate this theorem: they use the card's rank or suit as an **address** into a known set of possibilities, rather than learning everything through binary comparisons.



# 15. Counting Sort

\label{alg15}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized production standard}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Only when key range is small enough}
\endgroup
\end{center}

## Core idea

**Use each key as an index into counters, then reconstruct output.**

\begin{center}
\includegraphics[width=0.96\linewidth,keepaspectratio]{diagrams/counting-positions.png}
\end{center}

## History and uses

A standard distribution technique for bounded integer keys, especially when the key range is modest.

## Pseudocode

```text
count = array of k zeros
for each item: count[key(item)] += 1
for key = 1 to k-1: count[key] += count[key-1]
for item in input scanned right-to-left:
    position = count[key(item)] - 1
    output[position] = item
    count[key(item)] -= 1
return output
```

## Python example

```python
def counting(a, k=52):
    counts=[0]*k
    for x in a: counts[x]+=1
    out=[]
    for value,n in enumerate(counts): out.extend([value]*n)
    return out
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n+k) | 62 (k=52) | 104 (k=52) |
| Average | O(n+k) | 62 (k=52) | 104 (k=52) |
| Worst | O(n+k) | 62 (k=52) | 104 (k=52) |
| Memory | O(n+k) stable | varies | varies |
| Stable? | Yes* | Yes* | Yes* |

**For 52 cards:** With 52 distinct card-position keys: 52 count increments, 52 cumulative-counter updates, 52 output placements; no pairwise comparisons.


## Strengths, weaknesses, and cautions

Near-linear when key universe is small; wasteful when k is huge or sparse.

## Cards on a table

First practice rank-only sorting: write 13 counters, count ranks, compute cumulative totals, then place cards backward into indexed output slots.

## Cards in hand, without a table

Without table or writing surface, literal counters and numbered output slots are not realistically manageable. A hand of rank piles is a bucket-sort variant, not Counting Sort.

## Experiment

Use 12 cards including repeated ranks. Verify equal-ranked cards keep their original suit order when using stable backward placement.

## Three-setting checkpoint

Computer: indexed counters excel; table: paper counters workable; hands: the data structure has nowhere to live.

### A complete stable counting example

Sort by **rank only** for this exercise. Start with `3♠ 2♡ 3♣ 2♠`. The counts are 2:2 and 3:2. Cumulative counts give 2→2 and 3→4, meaning the last 2 belongs in output slot 2 and the last 3 in slot 4.

Read input from **right to left**. Put 2♠ in slot 2, 3♣ in slot 4, 2♡ in slot 1, and 3♠ in slot 3. Output: `2♡ 2♠ 3♠ 3♣`. Notice the original order of equal-ranked cards survives.

For 52 cards and 13 possible rank keys, a standard stable implementation makes one pass to count 52 items, processes 13 counters, and makes another pass to place 52 items. The scale is about **52 + 13 + 52 = 117** elementary visits, plus bookkeeping. That is not 117 comparisons: it largely avoids pairwise comparison altogether. With full canonical keys, there are 52 possible values instead of 13.

### Stable Counting Sort, physically and precisely

Temporarily sort by **rank only** so that several cards can have equal keys. Make thirteen counters, labeled A through K. Scan a 12-card packet and tally each rank. Turn the counts into **cumulative counts**: for rank 5, the cumulative count tells you how many cards have rank 5 *or earlier*, so it identifies the final output slot occupied by the last 5.

Now scan the original packet **right to left**. For each card, look up its rank's cumulative count, place it in that numbered output slot, then decrease that count by one. Scanning backward ensures that two equal-ranked cards retain their original order. Verify this with two differently suited 7s. The output row is stable even though no pairwise comparisons were needed.

**Why it works.** Each rank owns a consecutive interval of output slots. Cumulative counts give the end of each interval; decrementing assigns unique slots backward through that interval. This is different from simply dealing cards into rank piles. That convenient physical alternative is bucket/distribution sorting because it stores the records themselves, not just their counts.

With 52 cards and 13 rank values, tallying needs 52 rank reads, cumulative counts need 12 additions, and stable placement needs another 52 rank reads plus indexed writes. The expression O(n+k) describes how these stages grow; it does not mean exactly 65 physical gestures.

## What should remain in your head

> **Use key values as addresses rather than comparing pairs.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_columns.png}
\end{flushright}


# 16. Radix Sort

\label{alg16}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized production standard}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Uses structured fixed-width keys}
\endgroup
\end{center}

## Core idea

**Sort one component of a structured key at a time, using stable passes.**

## History and uses

Developed alongside mechanical and punched-card sorting; still useful for structured numeric and textual keys.

## Pseudocode

```text
for field from least significant to most significant:
    stably sort the records by this field
    preserve the within-field order on collection
return records
```

## Python example

```python
def radix_pairs(a):
    # Each key is (suit_index, rank_index)
    a=sorted(a,key=lambda x:x[1])
    return sorted(a,key=lambda x:x[0])
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(d(n+k)) | 46 (d=2,k=13) | 130 (d=2,k=13) |
| Average | O(d(n+k)) | 46 (d=2,k=13) | 130 (d=2,k=13) |
| Worst | O(d(n+k)) | 46 (d=2,k=13) | 130 (d=2,k=13) |
| Memory | O(n+k) | varies | varies |
| Stable? | Stable passes | Yes | Yes |

**For 52 cards:** For a 52-card deck encoded as two fields, two distribution passes inspect 104 card fields; each pass also has bucket setup/collection costs.


## Strengths, weaknesses, and cautions

Avoids whole-key comparisons, but depends on representation and stable passes.

## Cards on a table

Encode each card as (suit 0–3, rank 0–12). Stable-sort by rank first, then stable-sort by suit. Keep the earlier rank order within each suit.

## Cards in hand, without a table

Deal first into 13 held rank packets, then four suit packets without disturbing within-packet order. This requires far more than two hands, so use temporary pockets or reduce to 8 cards.

## Experiment

Deliberately scramble equal-rank order during the second pass; watch the final result fail.

## Three-setting checkpoint

Computer: arrays of buckets are cheap; table: repeated dealing is natural; hands: too many simultaneous buckets.

### The important subtlety: digit order

Suppose each card has a two-part key `(suit group, rank position)`. To perform **least-significant-field-first** Radix Sort, sort stably by rank position *first*, then stably by suit group. After the suit pass, each suit is grouped together, but its internal rank order remains from the earlier pass because equal-suit cards were not scrambled.

With our canonical order, both suit and rank ascend, so the within-suit rank digit is simply A=0 through K=12 for **all four suits**. No suit-specific reversal is necessary. This is an important consequence of the corrected order.

For a full 52-card deck, two stable counting-style passes over four suit values and 13 rank values require work proportional to `2×52 + 4 + 13`, plus the output passes and cumulative counts. The familiar O(d(n+k)) formula hides the fact that the two digits can have different ranges. When describing the physical version, be clear whether you are preserving order while collecting piles.

### Two stable passes, with a visible test

Our complete card order can be represented by two fields: **suit group** (♠=0, ♡=1, ♣=2, ♢=3) and **rank position** (A=0 through K=12). The suit group is more significant because all ♠ cards precede all ♡ cards regardless of rank.

For a least-significant-field-first radix exercise, first stably distribute the cards by rank position into thirteen labeled positions or piles; collect without reversing any equal-rank group. Next stably distribute by suit group into four positions; collect ♠, then ♡, then ♣, then ♢. The result is the exact canonical order. The second pass groups suits but **must preserve** the rank order established inside each suit by the first pass.

Try four cards `K♠, A♡, A♠, K♡`. After the rank pass they are `A♡, A♠, K♠, K♡` if you retain the original relative order within equal ranks; after the stable suit pass they become `A♠, K♠, A♡, K♡`. If you reverse a pile while collecting, the method may fail even though you chose the right buckets.

**Why it works.** After the first pass, cards are sorted by the less significant field. A stable pass on the more significant field groups its values without disturbing the previous order *within each group*. This argument generalizes to digits of numbers, letters of fixed-length strings, and structured records.

## What should remain in your head

> **Stable component passes assemble full order.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_suits_vertical.png}
\end{flushright}


# 17. Bucket Sort

\label{alg17}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; distribution-dependent}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Good buckets require useful key knowledge}
\endgroup
\end{center}

## Core idea

**Put cards into coarse ordered regions, sort within each, then concatenate.**

## History and uses

Distribution sorting is an old general technique; useful when the input distribution is known or reasonably uniform.

## Pseudocode

```text
create ordered buckets for nonoverlapping key ranges
for each item: append it to its matching bucket
for each bucket in key-range order:
    sort the bucket internally
return the concatenation of the sorted buckets
```

## Python example

```python
def bucket(a, bucket_of):
    b=[[] for _ in range(4)]
    for x in a: b[bucket_of(x)].append(x)
    return sum((sorted(part) for part in b), [])
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n), favorable | 10† | 52† |
| Average | O(n), favorable | 10† | 52† |
| Worst | O(n²), one bucket | 100† | 2,704† |
| Memory | O(n) | ~10 slots | ~52 slots |
| Stable? | Depends | Depends | Depends |

**For 52 cards:** 52 cards in four equal suit buckets: 52 assignments plus four 13-card internal sorts; insertion within each suit takes 312 worst-case key comparisons in total.


## Strengths, weaknesses, and cautions

Exploit known distribution; uneven buckets erase the benefit.

## Cards on a table

Deal into ♠, ♡, ♣, ♢ piles, insertion-sort each 13-card pile, then concatenate in suit order.

## Cards in hand, without a table

Hold four small suit packets in distinct finger positions or use four pockets. With two hands, practical for a few cards, awkward for 52.

## Experiment

Try one bucket versus four; compare how badly the single bucket defeats the intended advantage.

## Three-setting checkpoint

Computer: allocation and locality matter; table: four piles easy; hands: number of piles limits feasibility.

### Bucket sorting is not simply putting everything in its final slot

Make four suit buckets, in canonical order ♠, ♡, ♣, ♢. Deal each card to its suit bucket, then sort the contents of each bucket by rank using Insertion Sort. Finally concatenate the four ordered buckets. This works because every ♠ precedes every ♡, and so on.

With 52 cards, you perform **52 bucket assignments**, then sort four groups of 13. If each suit happens to arrive in reverse rank order, Insertion Sort uses 78 shifts per suit, or **312 shifts total**. If each suit arrives sorted, each requires only 12 key comparisons, or **48 total**. Thus the same distribution step can be followed by very different amounts of internal work.

Compare this with Counting Sort: Counting Sort keeps counts and calculates output positions. Bucket Sort keeps the *actual cards* in separate groups and sorts within them. The physical difference is especially visible on a table.

### Why buckets are not merely four piles
Our canonical order makes a four-bucket exercise easy: deal ♠, ♡, ♣, ♢ into separate regions, insertion-sort each region by rank, then concatenate them in that suit order. But the **bucket assignment** is doing real work. You know in advance that each suit occupies one contiguous interval of the final order; no card in a later bucket can precede a card in an earlier bucket.

For a more revealing experiment, use 20 random cards and divide the canonical 52-position key range into four intervals of 13 positions each. Sort each bucket with Insertion Sort. Then deliberately choose a *bad* bucket mapping that puts all 20 cards into one bucket. You have not broken the algorithm, but you have lost the expected advantage: the local sort now handles the entire input.

**Why it works.** Correctly ordered, nonoverlapping key intervals guarantee that concatenating internally sorted buckets produces a globally sorted result. The near-linear expected behavior sometimes quoted for Bucket Sort depends on a favorable distribution of inputs among buckets; it is not a guarantee for arbitrary input or arbitrary bucket design.

## What should remain in your head

> **Use coarse prior knowledge to make smaller sorts.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/pile_deck.png}
\end{flushright}


# 18. Pigeonhole Sort
\label{alg18}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Direct placement can waste large key ranges}
\endgroup
\end{center}

## Core idea

Provide one slot for every possible key and place each item directly into its corresponding slot.

## History and uses

A direct-address sorting method closely related to Counting Sort; especially natural for a deck whose 52 possible positions are known.

## Pseudocode

```text
Create one hole for each key; distribute items into their holes; read holes in key order.
```

## Python example

```python
def pigeonhole(a, maximum=51):
    holes=[[] for _ in range(maximum+1)]
    for x in a: holes[x].append(x)
    return [x for hole in holes for x in hole]
```

## Performance and interpretation

O(n+k) time and O(n+k) space for n items and k possible keys; if each key is unique, one card per hole.

**For a 10-card packet:** with a key universe of 52, the method still prepares 52 slots for just ten cards. **For a full 52-card deck:** a full deck uses 52 keyed slots and one direct placement per card. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Mark 52 slots (or use a numbered reference strip). Read each card’s canonical key 0–51 and place it directly in the matching slot. Sweep the slots in order to collect the deck.

## Cards in hand, without a table

A 52-position address space cannot be maintained in one hand; the table implementation is far better.

## Why it works

Every key is sent to its designated position, so reading positions in increasing order yields ordered keys.

### Deeper investigation

**Counting is not pigeonholing.** A counter can say 'three cards have rank 7' without storing which three they are. A pigeonhole stores the records themselves in a position indexed by their key. The distinction matters when records carry payloads (such as suits), when stable ordering matters, and when the number of possible keys greatly exceeds the number of records.

## Experiment

Sort a ten-card packet with ten direct-address positions, then with all 52 positions. Compare initialization overhead.

## Computer, table, and hand

**Computer:** direct indexing avoids pairwise comparison. **Table:** slots take substantial table area. **Hands:** no 52-slot address space exists in a fan.

\begin{quote}
\textbf{Inventor's notebook.} Is this even comparison sorting, and what is the price of knowing all possible keys?
\end{quote}

## What should remain in your head

**Provide one slot for every possible key and place each item directly into its corresponding slot.**


# Interlude: Why the lower bound does not forbid direct addressing

A comparison can tell us whether one key precedes another. A bounded integer key can instead serve as an *address*: the card numbered 17 goes straight to slot 17. This changes the model, not the mathematics. Counting, Radix, Bucket, and Pigeonhole methods require a known key structure and often pay for counters, buckets, or auxiliary arrays. A huge sparse key universe may make their setup cost unacceptable.


# 19. Cycle Sort

\label{alg19}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Few writes, costly searching}
\endgroup
\end{center}

## Core idea

**Move each item directly toward its final position, following displacement cycles.**

## History and uses

Cycle sort is known for minimizing writes; useful conceptually when writing data is especially costly.

## Pseudocode

```text
for start = 0 to n-2:
    item = a[start]
    find its final rank-position within a[start..n-1]
    if already correct: continue
    repeat:
        put item into its final slot
        take the displaced item as the new item
        find the displaced item's final slot
    until the cycle returns to start
# Distinct keys assumed here.
```

## Python example

```python
def cycle_sort(a):
    # Distinct keys, in-place; cycle sort minimizes writes.
    n = len(a)
    for start in range(n - 1):
        item = a[start]
        pos = start + sum(x < item for x in a[start+1:])
        if pos == start:
            continue
        while pos != start:
            a[pos], item = item, a[pos]
            pos = start + sum(x < item for x in a[start+1:])
        a[start] = item
    return a
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n²) | ~100† | ~2,704† |
| Average | O(n²) | ~100† | ~2,704† |
| Worst | O(n²) | ~100† | ~2,704† |
| Memory | O(1) | constant | constant |
| Stable? | No | No | No |

**For 52 cards:** At most 52 placements into final positions for distinct cards; comparisons remain quadratic and depend on cycle structure.


## Strengths, weaknesses, and cautions

Very few writes; many comparisons and tricky duplicate handling.

## Cards on a table

Use 7 distinct cards in a numbered row. For the first misplaced card, count how many remaining cards precede it; place it directly in that final slot, lift the displaced card, and continue until the cycle returns.

## Cards in hand, without a table

Hold a spread of 7 with numbered slots. Direct replacement is difficult because a hand must temporarily hold the displaced card. Try a second hand as a one-card buffer.

## Experiment

Count placements versus comparisons, then compare with Selection Sort on the same packet.

## Three-setting checkpoint

Computer: write minimization can matter; table: long-distance replacement is awkward; hands: temporary buffering dominates.

### A displacement cycle, shown explicitly

Take three numbered slots containing `3♠ 1♠ 2♠`. Card 3 belongs in slot 3, displacing card 2. Card 2 belongs in slot 2, displacing card 1. Card 1 belongs in slot 1, closing the cycle. The cycle makes **three final placements**, and none of those cards needs to be moved again.

The hard part is determining each card's final position. The elementary method counts how many remaining cards are earlier, so it still uses quadratic comparisons. The benefit is not speed; it is minimizing writes. On a computer with expensive writes this can matter. With cards, a displaced card must be held safely while another is placed, so the physical implementation can be awkward.

For 52 distinct cards, at most 52 final placements are needed, but a typical direct cycle implementation still makes many hundreds or thousands of comparisons. Be careful: a hand gesture is not a computer write.

### Follow one displacement cycle

Use five distinct cards with keys in the row `3, 1, 5, 2, 4`, where the correct order is `1, 2, 3, 4, 5`. The card 3 belongs in position 3. Put 3 there, lifting the displaced 5 into your spare hand. The 5 belongs in position 5; put it there and lift 4. Put 4 in position 4 and lift 2. Put 2 in position 2 and lift 1. Finally place 1 into the original empty position 1. One cycle is complete, and every card in that cycle has reached its final position.

**Why it works.** With distinct keys, every card has exactly one final position, and the mapping from current positions to final positions decomposes into disjoint cycles. Rotating each cycle places every participating item once. This minimizes writes among methods that explicitly place items into final slots, but finding each destination by counting smaller items can require quadratic comparisons.

**Practical caution.** Duplicate keys complicate the destination calculation; the standard textbook cycle sort needs explicit handling of duplicates. Our canonical 52-card order has distinct keys, so the physical exercise avoids that complication. With cards in hand, holding the displaced card is the one-card temporary buffer that makes the cycle possible.

## What should remain in your head

> **Move each item toward its final slot; count writes, not merely comparisons.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_cycle.png}
\end{flushright}


# 20. Pancake Sort
\label{alg20}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Only prefix reversals are allowed}
\endgroup
\end{center}

## Core idea

Sort using only prefix reversals: flip the first k cards as a single operation.

## History and uses

The pancake-sorting problem is a classic combinatorial puzzle; its constrained operation set reveals that sorting difficulty depends on what moves are permitted.

## Pseudocode

```text
For the largest remaining unsorted key: flip the prefix ending at its position to bring it to the front; flip the entire active prefix to place it at the end; shrink the active prefix.
```

## Python example

```python
def pancake(a):
    a=a[:]
    for size in range(len(a),1,-1):
        j=max(range(size),key=lambda i:a[i])
        if j==size-1: continue
        if j>0: a[:j+1]=reversed(a[:j+1])
        a[:size]=reversed(a[:size])
    return a
```

## Performance and interpretation

O(n²) comparisons in the simple maximum-search implementation, at most 2(n−1) prefix flips; O(1) auxiliary storage possible.

**For a 10-card packet:** at most 18 prefix reversals for ten distinct cards. **For a full 52-card deck:** at most 102 prefix reversals for 52 distinct cards. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Lay ten cards in a row. Find the latest remaining card. Reverse the entire prefix ending at it, bringing it to the front. Reverse the entire active prefix to place that card at the right boundary. Shrink the active region.

## Cards in hand, without a table

A packet can be turned over, but turning a packet over changes face orientation. Keep all faces visible by reversing the order of a packet rather than merely flipping it face-down.

## Why it works

Each round permanently places the largest remaining item at the end without disturbing the already finished suffix.

### Deeper investigation

**Orientation matters.** Reversing a packet's order is not the same as turning the packet face-down. For a tabletop simulation, lift the prefix, reverse the order of its individual cards, and replace them all face-up. If you instead rotate a face-up packet in three-dimensional space, you may change which face is visible without reversing the intended left-to-right sequence.

## Experiment

Count flips and individually displaced cards. Compare against Selection Sort’s swaps.

## Computer, table, and hand

**Computer:** a reversal of k items writes O(k) elements in a normal array. **Table:** a whole prefix can be picked up as a block. **Hands:** reversing packet order without turning faces over is fiddly.

\begin{quote}
\textbf{Inventor's notebook.} What if the only allowed operation is a prefix reversal?
\end{quote}

## What should remain in your head

**Sort using only prefix reversals: flip the first k cards as a single operation.**


# Interlude: Permutations and minimum swaps

A permutation describes where every distinct card must move. Follow the destinations: a card at position 1 belongs at 4, the card at 4 belongs at 2, and the card at 2 belongs at 1. Those three positions form a **cycle**. A cycle of length m requires at least m−1 arbitrary swaps to resolve, so the minimum number of swaps over a permutation is n minus its number of cycles. This is different from minimizing comparisons or array writes. Cycle Sort minimizes placements in a different sense: it writes each displaced value directly to its final slot.


# 21. Natural Merge Sort
\label{alg21}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production component; foundational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Existing runs reduce work}
\endgroup
\end{center}

## Core idea

Detect existing ascending runs rather than splitting blindly, then merge those runs.

## History and uses

Natural merging is a foundational adaptive strategy and a direct ancestor of modern run-aware hybrids such as Timsort.

## Pseudocode

```text
Scan to find maximal nondecreasing runs; merge adjacent runs until one remains.
```

## Python example

```python
def natural_merge(a):
    runs=[]; i=0
    while i<len(a):
        j=i+1
        while j<len(a) and a[j-1]<=a[j]: j+=1
        runs.append(a[i:j]); i=j
    def merge(x,y):
        out=[]; i=j=0
        while i<len(x) and j<len(y):
            if x[i]<=y[j]: out.append(x[i]); i+=1
            else: out.append(y[j]); j+=1
        return out+x[i:]+y[j:]
    while len(runs)>1:
        runs=[merge(runs[i],runs[i+1]) if i+1<len(runs) else runs[i]
              for i in range(0,len(runs),2)]
    return runs[0] if runs else []
```

## Performance and interpretation

O(n) when already one ascending run; worst O(n log n), O(n) auxiliary storage; stable if merging chooses the left equal key.

**For a 10-card packet:** a fully sorted packet is recognized in nine adjacent comparisons. **For a full 52-card deck:** a fully sorted deck is recognized in 51 adjacent comparisons, before any merging. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Create three short ordered runs of cards, concatenate them in an unsorted order, and mark each run’s boundary. Merge neighboring runs by comparing only exposed front cards; repeat until one run remains.

## Cards in hand, without a table

Runs are visible in a fan, but holding multiple merge inputs and outputs without a surface quickly becomes impractical.

## Why it works

Every detected run is sorted. Stable merging preserves the order of each run and produces a sorted union; repetition finishes.

### Deeper investigation

**Runs are information.** A packet containing [2, 4, 6, 8 | 1, 3, 5, 7] already consists of two sorted runs. Natural Merge Sort merges them directly. Ordinary top-down Merge Sort might split and recursively sort each half even though neither half needs internal work. The adaptive advantage is not magic: the initial scan must still detect the runs.

## Experiment

Compare the same 20 cards in three long runs versus shuffled. Count run detection comparisons and merge comparisons separately.

## Computer, table, and hand

**Computer:** sequential run detection is cache-friendly. **Table:** runs are visibly grouped. **Hands:** holding multiple runs during merge is difficult.

\begin{quote}
\textbf{Inventor's notebook.} Why throw away order already present in the input?
\end{quote}

## What should remain in your head

**Detect existing ascending runs rather than splitting blindly, then merge those runs.**


# 22. Timsort

\label{alg22}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production standard}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Stable and adaptive; intricate implementation}
\endgroup
\end{center}

## Core idea

**Find already ordered runs, extend short runs, and merge them intelligently.**

## History and uses

Tim Peters developed it for Python in 2002; used in Python list sorting and influential elsewhere.

## Pseudocode

```text
scan input for ascending or descending runs
reverse descending runs; extend short runs stably
push runs onto a stack
while run sizes violate the merge policy:
    merge suitable neighboring runs stably
merge remaining runs until one remains
```

## Python example

```python
def adaptive_run_merge(a):
    # Educational run-aware stable merge, NOT full Timsort.
    if len(a) < 2: return a[:]
    runs = []
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a) and a[j-1] <= a[j]:
            j += 1
        runs.append(a[i:j])
        i = j
    def merge(left, right):
        out = []; i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
        return out + left[i:] + right[j:]
    while len(runs) > 1:
        next_runs = []
        for k in range(0, len(runs), 2):
            next_runs.append(merge(runs[k], runs[k+1])
                             if k+1 < len(runs) else runs[k])
        runs = next_runs
    return runs[0]
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n) | 9 checks | 51 checks |
| Average | O(n log n) | ~33† | ~296† |
| Worst | O(n log n) | ~33† | ~296† |
| Memory | O(n) | ~10 slots | ~52 slots |
| Stable? | Yes | Yes | Yes |

**For 52 cards:** Already sorted 52 cards: a single 52-card run is found with 51 adjacent comparisons; full Timsort has additional implementation-dependent work.


## Strengths, weaknesses, and cautions

Highly adaptive and stable; complex implementation and merge memory.

**Implementation note:** Python `sorted()` calls its built-in Timsort, but the snippet does not implement Timsort from scratch.

## Cards on a table

Construct 20 cards as three ordered runs. Mark run boundaries, extend short runs to length 4 with insertion, then merge the runs.

## Cards in hand, without a table

Look for ascending runs in a fanned hand. Keep run packets separately in two hands, then merge. The run recognition is natural; merging many runs is not.

## Experiment

Compare a packet made of long runs against the same cards shuffled.

## Three-setting checkpoint

Computer: run detection is cheap; table: runs are visible; hands: maintaining several run packets strains workspace.

### Why a run is a piece of free work

A **run** is a contiguous segment already ordered. Take a packet consisting of `2♠ 4♠ 6♠ | 1♡ 3♡ 5♡`. It has two ascending runs even though the whole packet is not sorted. Instead of breaking them into singletons, an adaptive mergesort can merge the two runs directly.

Real Timsort detects ascending or descending runs, reverses descending runs, extends short runs with insertion techniques, and maintains a stack of runs with rules for when to merge. The run-stack policy matters: merging badly sized runs can waste work. Our card exercise models those principles; it does not claim to reproduce every Python implementation detail.

For 52 already sorted cards, recognizing the single ascending run requires **51 adjacent comparisons** in the simplest model, and little or no merging. For 52 random cards, there are typically many short runs and substantially more work. The performance advantage comes from input structure, not magic.

### A faithful small-scale Timsort experiment

Create 20 cards arranged as three ascending **runs**, for example packets of lengths 7, 5, and 8, then place the runs consecutively in a globally unsorted order. A *run* is a contiguous already ordered sequence. Scan left-to-right to detect ascending or descending runs; reverse a descending run to make it ascending. For our miniature exercise, extend any run shorter than four cards with stable insertion sorting, then merge neighboring runs while keeping their sizes reasonably balanced.

Compare with the same cards thoroughly shuffled. The deliberately run-rich input often needs fewer comparisons and merges because the algorithm preserves order already present. Python's production Timsort uses a carefully engineered run stack, minimum run lengths, galloping merges, and other details that this tabletop exercise deliberately simplifies.

**Why it works.** Every detected or extended run is sorted; stable merging of sorted runs produces a longer sorted run. The implementation's merge policy controls efficiency, not basic correctness. For an already sorted packet of 52, detecting the one ascending run requires 51 adjacent comparisons in a simple model; it does not require recursively splitting all 52 into singletons.

## What should remain in your head

> **Do not destroy order the input already gives you.**

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/card_vortex.png}
\end{flushright}


# 23. Introsort

\label{alg23}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Production standard}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Quicksort speed with heap fallback}
\endgroup
\end{center}

## Core idea

**Use Quicksort normally, switch to Heapsort if recursion gets too deep, and insertion-sort tiny pieces.**

## History and uses

David Musser proposed introspective sorting in 1997; widely influential in C++ standard-library sorts.

## Pseudocode

```text
introsort(a, budget):
    if partition is tiny: insertion_sort(a); return
    if budget == 0: heapsort(a); return
    partition around a pivot
    introsort(left, budget-1)
    introsort(right, budget-1)
```

## Python example

```python
def introsort_model(a):
    # Educational hybrid: uses heapq fallback, not in-place.
    import heapq
    from math import log2
    def work(items, depth):
        if len(items) <= 4:
            out = items[:]
            for i in range(1, len(out)):
                x = out[i]; j = i
                while j > 0 and out[j-1] > x:
                    out[j] = out[j-1]; j -= 1
                out[j] = x
            return out
        if depth == 0:
            h = items[:]; heapq.heapify(h)
            return [heapq.heappop(h) for _ in range(len(h))]
        pivot = items[0]
        left = [x for x in items[1:] if x < pivot]
        right = [x for x in items[1:] if x >= pivot]
        return work(left, depth-1) + [pivot] + work(right, depth-1)
    return work(a, 2 * int(log2(max(1, len(a)))))
```

## Performance and the 52-card case

| Measure | Growth | 10 cards | 52 cards |
|:---|:---|---:|---:|
| Best | O(n log n), typical | ~33† | ~296† |
| Average | O(n log n) | ~33† | ~296† |
| Worst | O(n log n) | ~33† | ~296† |
| Memory | O(log n) stack | varies | varies |
| Stable? | No | No | No |

**For 52 cards:** At 52 cards, depth limit often starts at 2 floor(log₂ 52)=10. Exact comparisons depend on pivots and cutoff.


## Strengths, weaknesses, and cautions

Combines fast average behavior and worst-case protection; complex and generally unstable.

**Implementation note:** The Python example delegates to a library sort and is **not** Introsort: Python uses Timsort. It demonstrates only the input/output interface. The full algorithm is specified in the pseudocode and physical exercise; do not use this snippet to benchmark Introsort.

## Cards on a table

Use 16 cards and 8 coins as depth budget. Partition by pivot; spend a coin per recursive level; switch to heap on exhausted depth, insertion on groups of 4 or fewer.

## Cards in hand, without a table

You can partition small groups between two hands, but switching to a heap requires a surface. Mark this as impractical rather than pretending it is effortless.

## Experiment

Use a sorted packet with first-card pivots to force the fallback; compare with shuffled input.

## Three-setting checkpoint

Computer: strategy switches cheap; table: switching representations costs effort; hands: some representations simply do not fit.

### The depth budget is an early-warning system

Introsort begins like Quicksort. Each time partitioning descends another recursive level, reduce the allowed depth. If a large partition survives after the budget is exhausted, stop gambling on pivot balance and use Heapsort for that partition. Tiny partitions are often completed with Insertion Sort because its constant overhead is low.

For 52 cards, a conventional starting budget `2×floor(log₂ 52)` equals **10**. This is not a bound of ten comparisons; it is a bound on how deeply the Quicksort-style partitioning may recurse before the fallback. The overall worst-case growth becomes O(n log n), unlike unguarded Quicksort.

The short Python snippet in this learner draft calls the built-in sort and therefore **does not implement Introsort**. Treat the pseudocode and the three-part card exercise as the model. This is a deliberate limitation to be corrected with a full reference implementation in a later technical appendix.

### A depth budget makes the hybrid intelligible

Start Quicksort on 16 cards, with a depth budget of **eight** (twice the integer part of log₂ 16). Each time you recurse into a partition, reduce that branch's budget by one. If a still-large partition reaches budget zero, abandon Quicksort for that partition and use Heapsort; if a partition is tiny (four cards in our exercise), finish it with Insertion Sort instead.

Test a sorted 16-card packet using the first card as pivot. The partitions are maximally unbalanced, so the budget runs down. Now try a shuffled packet with reasonably balanced pivots. It will often reach the small-partition cutoff before needing the heap fallback.

**Why it works.** Quicksort's typical efficiency is retained while the fallback prevents arbitrarily deep bad recursion from becoming quadratic work. Heapsort guarantees O(m log m) on a remaining partition of size m; Insertion Sort reduces overhead on tiny partitions. The tradeoff is extra control logic and the loss of stability. On the table, switching from two piles to a spatial heap is awkward, whereas in a computer array the same memory can be reinterpreted cheaply.

## What should remain in your head

> **A good algorithm can change algorithms.**



# 24. Smoothsort
\label{alg24}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; historical}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Adaptive heap technique; complex}
\endgroup
\end{center}

## Core idea

Maintain a family of Leonardo-number heaps that adapts to existing order while guaranteeing good worst-case behavior.

## History and uses

Edsger Dijkstra developed Smoothsort in 1981 as an adaptive relative of Heapsort.

## Pseudocode

```text
Partition the array into Leonardo heaps; maintain the heap order while inserting; repeatedly extract the maximum and repair the affected heap structure.
```

## Python example

```python
# Smoothsort is structurally involved. This reference trace
# deliberately exposes the essential operation: sift a heap.
def sift_max(a, root, children):
    while children(root):
        choices=children(root)
        child=max(choices,key=lambda i:a[i])
        if a[root]>=a[child]: break
        a[root],a[child]=a[child],a[root]
        root=child
# This helper is NOT a complete Smoothsort implementation.
```

## Performance and interpretation

Best O(n) for favorable ordered input; worst O(n log n); O(1) auxiliary storage for the classical implementation; not stable.

**For a 10-card packet:** the Leonardo heap sizes 1,1,3,5 can model a ten-card forest. **For a full 52-card deck:** a full 52-card forest still requires intricate heap bookkeeping; exact comparisons depend on order. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Use a diagram of Leonardo heaps with sizes 1, 1, 3, 5, 9. Build a small forest and compare it with an ordinary binary heap. Follow the changes to root values when the next card is inserted; the full production procedure is too intricate to pretend can be faithfully performed in a short tabletop exercise.

## Cards in hand, without a table

Not practical as a literal in-hand sort; analyze why a forest of overlapping structural invariants exceeds hand workspace.

## Why it works

A full proof needs the Leonardo-heap forest invariant and its restoration rules. The essential idea is that heap roots delimit the maximal remaining keys; the chapter flags this as an advanced implementation.

## Experiment

Compare the work of heap repair on sorted versus scrambled small heaps. Explain why this is only a component demonstration, not a measured Smoothsort benchmark.

## Computer, table, and hand

**Computer:** compact encoded heap metadata is essential. **Table:** paper diagrams reveal the structure. **Hands:** the forest is not physically maintainable.

\begin{quote}
\textbf{Inventor's notebook.} How can a heap-based method detect and benefit from presorted input?
\end{quote}

## What should remain in your head

**Maintain a family of Leonardo-number heaps that adapts to existing order while guaranteeing good worst-case behavior.**


# Interlude: Machines, memory, and adversaries

A computer's memory hierarchy favors contiguous scans over unpredictable jumps. Comparisons may be cheap for integers but expensive for long strings or database records. Branch prediction, allocation, cache misses, and recursion overhead all affect real time. An adversarial input is deliberately arranged to trigger a weakness, such as consistently unbalanced Quicksort partitions. Randomization makes that weakness harder to predict, but expected performance is not a deterministic worst-case guarantee.


# 25. Bitonic Sort
\label{alg25}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Parallel/specialized}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Fixed comparator network; not a sequential speed winner}
\endgroup
\end{center}

## Core idea

Use a fixed network of compare-exchange operations to sort a bitonic sequence, then recursively construct bitonic sequences.

## History and uses

Bitonic sorting networks are associated with Kenneth Batcher’s work on parallel sorting in the 1960s.

## Pseudocode

```text
Recursively sort half ascending and half descending to form a bitonic sequence; compare-exchange across half-length distances; recursively merge each half.
```

## Python example

```python
def bitonic(a):
    a=a[:]
    n=len(a)
    if n==0 or n&(n-1): raise ValueError('power-of-two length')
    def merge(lo,k,up):
        if k>1:
            m=k//2
            for i in range(lo,lo+m):
                if (a[i]>a[i+m])==up: a[i],a[i+m]=a[i+m],a[i]
            merge(lo,m,up); merge(lo+m,m,up)
    def sort(lo,k,up):
        if k>1:
            m=k//2; sort(lo,m,True); sort(lo+m,m,False); merge(lo,k,up)
    sort(0,n,True); return a
```

## Performance and interpretation

O(n log² n) comparisons for power-of-two n, O(log² n) network depth with parallel comparators; fixed comparison pattern.

**For a 10-card packet:** the next valid network size is 16, not ten, unless padded. **For a full 52-card deck:** a power-of-two network would pad 52 inputs to 64. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Use exactly eight cards and numbered positions. Follow a printed eight-input bitonic network stage by stage, comparing prescribed pairs simultaneously when possible. Each comparator sends the earlier key toward its indicated ascending output.

## Cards in hand, without a table

Two hands can execute one comparator at a time but cannot realize parallel comparisons; the network’s advantage depends on hardware or multiple people.

## Why it works

A bitonic sequence has a monotone-up then monotone-down shape; the compare-exchange half-step separates low and high halves, and recursive merges finish them.

### Deeper investigation

**Eight-input network sketch.** The compare-exchange stages of a bitonic network are fixed in advance. One possible stage schedule (zero-based positions) compares pairs at distances 1, then 2, then 1, then 4, then 2, then 1. The direction of individual comparators alternates in early stages to build bitonic runs; the final three stages direct all comparisons toward ascending order. Because disjoint pairs within a stage can operate simultaneously, depth differs from total comparison count.

## Experiment

Run the same network on sorted, reversed, and random eight-card inputs. Count comparisons: the network makes the same number every time.

## Computer, table, and hand

**Computer:** fixed compare-exchange stages can run in parallel. **Table:** a drawn network makes stages explicit. **Hands:** one person cannot execute disjoint comparisons simultaneously.

\begin{quote}
\textbf{Inventor's notebook.} Can comparisons be scheduled before we even see the data?
\end{quote}

## What should remain in your head

**Use a fixed network of compare-exchange operations to sort a bitonic sequence, then recursively construct bitonic sequences.**


# 26. Odd-Even Transposition Sort
\label{alg26}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Parallel/specialized; educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Local compare-exchanges across phases}
\endgroup
\end{center}

## Core idea

Alternate parallel comparisons of odd-indexed neighbor pairs and even-indexed neighbor pairs.

## History and uses

A classic sorting-network and parallel-algorithm example closely related to Bubble Sort.

## Pseudocode

```text
Repeat n phases: on odd phases compare (1,2),(3,4),...; on even phases compare (2,3),(4,5),...; swap backward pairs.
```

## Python example

```python
def odd_even(a):
    a=a[:]
    for phase in range(len(a)):
        for i in range(phase%2,len(a)-1,2):
            if a[i]>a[i+1]: a[i],a[i+1]=a[i+1],a[i]
    return a
```

## Performance and interpretation

O(n²) total comparisons, O(n) parallel phases, O(1) auxiliary storage; stable with strict comparisons.

**For a 10-card packet:** ten phases suffice, with five or four disjoint neighbor comparisons per phase. **For a full 52-card deck:** 52 phases suffice, with 26 or 25 disjoint comparisons per phase. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Line up eight cards. Phase A: compare pairs 1–2, 3–4, 5–6, 7–8. Phase B: compare 2–3, 4–5, 6–7. Alternate for eight phases.

## Cards in hand, without a table

Adjacent exchanges are feasible, but you cannot compare several disjoint pairs at once without helpers.

## Why it works

Each phase removes local inversions at its active boundaries; after n alternating phases, no item can remain displaced beyond its correct position.

### Deeper investigation

**Parallel-work example.** Eight cards require eight alternating phases. A phase compares either four disjoint pairs or three disjoint pairs. One person performs those comparisons sequentially; several people could perform them at once. The algorithm has quadratic total work but only linear parallel depth. That is a real improvement in the appropriate machine model, not a faster one-person card exercise.

## Experiment

Recruit a second person to perform disjoint comparisons simultaneously. Compare elapsed rounds with sequential Bubble Sort.

## Computer, table, and hand

**Computer:** disjoint comparisons can be parallelized. **Table:** several people can operate independent pairs. **Hands:** one person gains no parallel speedup.

\begin{quote}
\textbf{Inventor's notebook.} What matters more for parallel work: total operations or critical-path depth?
\end{quote}

## What should remain in your head

**Alternate parallel comparisons of odd-indexed neighbor pairs and even-indexed neighbor pairs.**


# 27. Strand Sort
\label{alg27}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Primarily educational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Extract sorted strands, then merge}
\endgroup
\end{center}

## Core idea

Extract an increasing subsequence from the input, then merge it into a growing sorted output.

## History and uses

A distribution/merge hybrid often presented as a linked-list-friendly teaching algorithm.

## Pseudocode

```text
Scan input left-to-right, extract an increasing strand, merge it into sorted output; repeat until input empty.
```

## Python example

```python
def strand(a):
    remaining=a[:]; out=[]
    def merge(x,y):
        z=[]
        while x and y:
            if x[0]<=y[0]: z.append(x.pop(0))
            else: z.append(y.pop(0))
        return z+x+y
    while remaining:
        strand=[remaining.pop(0)]; rest=[]
        for x in remaining:
            if x>=strand[-1]: strand.append(x)
            else: rest.append(x)
        remaining=rest; out=merge(out,strand)
    return out
```

## Performance and interpretation

Best near O(n) for one sorted strand under suitable list operations; worst O(n²), additional output storage O(n). Python list pop(0) adds movement overhead.

**For a 10-card packet:** a sorted packet forms one strand. **For a full 52-card deck:** a sorted deck forms one strand; reversed input forms 52 single-card strands. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Scan a ten-card row left to right. Extract the first card, then each later card not earlier than the last selected card, building one ordered strand. Merge that strand into the output pile. Repeat with the leftover cards.

## Cards in hand, without a table

Holding a strand and an output while scanning leftovers is possible only for small packets; a table is much easier.

## Why it works

Each strand is increasing by construction; merging two sorted sequences preserves order, and every input item is eventually extracted.

## Experiment

Compare one already sorted row against a reverse-sorted row. Count strands extracted.

## Computer, table, and hand

**Computer:** linked lists make extraction inexpensive. **Table:** a strand can be physically lifted out. **Hands:** holding all strands and output needs extra space.

\begin{quote}
\textbf{Inventor's notebook.} What if the useful structure is a subsequence rather than a contiguous run?
\end{quote}
## What should remain in your head

**Extract an increasing subsequence from the input, then merge it into a growing sorted output.**


# 28. Patience Sort
\label{alg28}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Specialized; foundational}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Piles reveal longest increasing subsequences}
\endgroup
\end{center}

## Core idea

Deal each card onto the leftmost pile whose top is at least as late as that card; then extract minima with a multiway merge.

## History and uses

Inspired by the patience card game; closely connected to longest increasing subsequences and the patience-sorting technique.

## Pseudocode

```text
For each key, place it on the leftmost pile with top >= key, or create a new pile; then repeatedly output the smallest exposed pile top.
```

## Python example

```python
def patience(a):
    piles=[]
    for x in a:
        lo=0; hi=len(piles)
        while lo<hi:
            m=(lo+hi)//2
            if piles[m][-1]>=x: hi=m
            else: lo=m+1
        if lo==len(piles): piles.append([])
        piles[lo].append(x)
    import heapq
    heap=[(p[-1],i) for i,p in enumerate(piles)]
    heapq.heapify(heap); out=[]
    while heap:
        x,i=heapq.heappop(heap); out.append(x); piles[i].pop()
        if piles[i]: heapq.heappush(heap,(piles[i][-1],i))
    return out
```

## Performance and interpretation

O(n log n) with binary-search pile placement and a heap-based final merge; O(n) storage; stability needs additional tie-handling.

**For a 10-card packet:** a sorted packet produces ten piles and a reversed packet one pile. **For a full 52-card deck:** a sorted deck produces 52 piles, a reversed deck one. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Deal ten cards into piles: place each on the leftmost pile whose top is no earlier than the incoming card, otherwise start a new pile to the right. To finish, repeatedly take the earliest exposed top card across all piles.

## Cards in hand, without a table

This is perhaps the most card-native of the advanced methods, but many simultaneous piles still require a table.

## Why it works

Pile tops increase left to right, and each pile decreases from bottom to top; its exposed top is therefore its earliest remaining member. Merging exposed minima yields sorted output.

### Deeper investigation

**Longest increasing subsequence.** Deal 3, 1, 4, 2, 5. The pile-top sequence changes as follows: [3], [1], [1,4], [1,2], [1,2,5]. There are three piles, matching the length of an increasing subsequence such as 1,2,5. This connection is deeper than a sorting trick: patience sorting gives an efficient method for studying subsequences.

## Experiment

Count the number of piles for a sorted row and a reverse-sorted row. Relate the count to the longest increasing subsequence.

## Computer, table, and hand

**Computer:** binary search locates pile positions. **Table:** piles are a natural card-table structure. **Hands:** 52 piles cannot fit in the hands.

\begin{quote}
\textbf{Inventor's notebook.} Why is the number of piles connected to increasing subsequences?
\end{quote}

## What should remain in your head

**Deal each card onto the leftmost pile whose top is at least as late as that card; then extract minima with a multiway merge.**


# Interlude: Sorting networks and parallel depth

In a sorting network, every comparator's pair of positions is fixed before any keys are seen. Two disjoint comparators can run simultaneously. **Work** counts total comparisons; **depth** counts sequential stages. A network can have more total work than a sequential sort but much lower depth on parallel hardware. Eight human volunteers could compare four independent pairs simultaneously, while one person must perform them sequentially.


# 29. Bogosort
\label{alg29}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Deliberately impractical}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Random retries are not a useful general method}
\endgroup
\end{center}

## Core idea

Repeatedly shuffle the entire packet until it happens to be sorted.

## History and uses

A deliberately absurd randomized algorithm, useful for distinguishing correctness, expected cost, and practical feasibility.

## Pseudocode

```text
While the sequence is not sorted: randomly permute it; stop once all adjacent pairs are in order.
```

## Python example

```python
import random
def bogosort(a, limit=100000):
    a=a[:]
    for _ in range(limit):
        if all(a[i-1]<=a[i] for i in range(1,len(a))): return a
        random.shuffle(a)
    raise TimeoutError('iteration budget exhausted')
```

## Performance and interpretation

Under independent uniform random shuffles, expected approximately n! trials (with a full check costing O(n)); unbounded worst-case runtime; O(1) or O(n) shuffle workspace by implementation.

**For a 10-card packet:** ten distinct cards have 10!=3,628,800 permutations, so uniform random trials expect that many checks. **For a full 52-card deck:** 52! is about 8.07×10^67 permutations; a full-deck trial is absurd. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Use only three cards. Shuffle and inspect until they appear in order. Record how many attempts you needed. Do not try 52: 52! is astronomically large.

## Cards in hand, without a table

This is trivially executable in hand for three cards and utterly impractical for a full deck.

## Why it works

Every permutation has positive probability, so the probability of never reaching sorted order approaches zero; this is probabilistic termination, not a finite worst-case guarantee.

### Deeper investigation

**Expected trials versus guarantees.** Three distinct cards have six permutations. If every shuffle is independent and uniformly random, the probability of success on each check is 1/6, so the expected number of checks until success is six. But no finite number of trials guarantees success: after a million failures, the next shuffle still has probability 1/6 of success. This distinguishes expected time from worst-case termination.

## Experiment

Repeat the three-card trial twenty times and calculate the average attempts. Compare with the theoretical expectation of six trials when each attempt is an independent uniform permutation.

## Computer, table, and hand

**Computer:** random shuffle can be implemented but expected runtime explodes. **Table:** three-card experiments are feasible. **Hands:** shuffling is easy but progress is not cumulative.

\begin{quote}
\textbf{Inventor's notebook.} Why is “eventually works” a poor efficiency guarantee?
\end{quote}

## What should remain in your head

**Repeatedly shuffle the entire packet until it happens to be sorted.**


# 30. Stooge Sort
\label{alg30}

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabular}{@{}l l l l@{}}
\multicolumn{4}{@{}l}{\textsf{\footnotesize\bfseries AT A GLANCE}\quad\textsf{\scriptsize Deliberately impractical}} \\
\hline
\textsf{\scriptsize Learning value} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Low extra memory} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{ink}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Small packets} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Tabletop ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Nearly sorted} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize In-hand ease} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\textsf{\scriptsize Large random} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} & \textsf{\scriptsize Practical relevance} & \textcolor{ink}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}}\textcolor{gray!30}{\rule{0.70em}{0.42em}} \\
\end{tabular}
\par\vspace{2pt}{\footnotesize\itshape Recursive overlap creates excessive work}
\endgroup
\end{center}

## Core idea

Recursively sort overlapping two-thirds portions three times, a striking example of expensive recursion.

## History and uses

A deliberately inefficient recursive sorting algorithm often used to demonstrate that recursion alone does not confer efficiency.

## Pseudocode

```text
If first key is later than last, swap them; for n>2 sort first 2/3, last 2/3, then first 2/3 again.
```

## Python example

```python
def stooge(a):
    a=a[:]
    def go(i,j):
        if a[i]>a[j]: a[i],a[j]=a[j],a[i]
        if j-i+1>2:
            t=(j-i+1)//3
            go(i,j-t); go(i+t,j); go(i,j-t)
    if a: go(0,len(a)-1)
    return a
```

## Performance and interpretation

Recurrence T(n)=3T(2n/3)+O(1), giving O(n^log_(3/2)3), approximately O(n^2.71); recursion depth O(log n).

**For a 10-card packet:** the cost grows approximately as 10^2.71, a growth benchmark near 513. **For a full 52-card deck:** the corresponding growth benchmark for 52 is roughly 45,000, not an exact call count. These figures describe the stated model, not universal elapsed times.

## Cards on a table

Use six cards and mark overlapping two-thirds windows. Exchange endpoints if backward, then sort the first window, the last window, and the first again. Trace the recursive calls on paper.

## Cards in hand, without a table

The overlapping windows and deep recursion are difficult to remember without written state. That is part of the lesson.

## Why it works

The three overlapping calls ensure every element is brought into the correct region, but the repeated overlapping work makes the recurrence expensive.

### Deeper investigation

**A recurrence worth solving.** Three recursive calls operate on overlapping subproblems of approximately two-thirds the previous size. If T(n) is the number of elementary operations, then T(n) ≈ 3T(2n/3)+constant. Solving for a power n^p requires 3(2/3)^p=1, so p=log_(3/2)3≈2.71. The overlap creates more work than ordinary quadratic growth.

## Experiment

Count recursive calls for three, six, and nine cards and compare against Merge Sort’s splitting pattern.

## Computer, table, and hand

**Computer:** recursive overlap creates repeated work. **Table:** overlapping windows can be marked. **Hands:** remembering recursion state is burdensome.

\begin{quote}
\textbf{Inventor's notebook.} Why can a recursive algorithm be much worse than a simple quadratic method?
\end{quote}

## What should remain in your head

**Recursively sort overlapping two-thirds portions three times, a striking example of expensive recursion.**


# Synthesis: Choosing a strategy

\label{synthesis}

No algorithm wins in every environment. Ask: How many items? Is the input already partly ordered? Are keys bounded? Do equal keys require stability? Are comparisons expensive? Are writes expensive? Is extra memory scarce? Can I maintain several piles? Am I holding the cards or using a table?

For a deck **in hand**, Insertion Sort is a natural default. On a **table**, suit-based Bucket Sort is often the most pleasant route to our exact canonical order. On a **computer**, for a small general-purpose array, a library's adaptive or introspective hybrid is usually preferable to reimplementing any textbook method. If keys are already known integers 0–51, direct indexing can change the problem altogether.

## Final challenge

Shuffle all 52. Before touching the deck, choose (1) a table algorithm, (2) an in-hand algorithm, and (3) a computer algorithm. Explain what makes each efficient in its environment. Then actually perform at least two of the three that you can do physically.

## What the book has been teaching

Sorting is a laboratory for invariants, partial order, recursion, representation, information limits, memory tradeoffs, adaptiveness, and cost models. The card is the same object in all three settings; what changes is the cost of asking about it, storing it, and moving it.



# Beyond the algorithms: designing your own sort
\label{invention}

## 1. Specify the problem before inventing a solution

Write down the input type, ordering relation, whether equal keys are allowed, whether stability matters, which operations are permitted, and which costs you intend to minimize. For a hand-only algorithm, state whether cards may be placed face-down, whether two hands are allowed, and whether the deck may be temporarily divided. Without these rules, “better” has no precise meaning.

## 2. Find a wasteful operation

Watch an existing sort and ask: which comparisons repeat information already learned? Which cards move back and forth? Which positions are scanned after their final contents are known? Which piles could be processed in parallel? This is the beginning of algorithm design: identifying a *specific* inefficiency and proposing a *specific* mechanism to remove it.

For example, Selection Sort repeatedly scans the remaining region. A tournament tree remembers which candidates previously lost to the minimum. Binary Insertion Sort remembers that a sorted prefix can be searched by halving. Natural Merge Sort remembers runs already present in the input. Each improvement saves one kind of work and often introduces another.

## 3. Construct an invariant

An invariant is a sentence that remains true at a chosen checkpoint. For a proposed sort, write it before writing code. Examples: “everything left of the marker is finished,” “every exposed pile top is the smallest remaining member of its pile,” or “each subtree satisfies the heap property.” Then establish:

1. **Initialization:** why the invariant holds before the first step.
2. **Maintenance:** why every permitted step preserves it.
3. **Termination:** why the procedure cannot continue forever, or what probabilistic guarantee replaces deterministic termination.
4. **Conclusion:** why the invariant plus termination proves the required final order and preservation of all items.

A procedure that merely seems to work on ten shuffled packets has not yet been proved correct.

## 4. Attack your own invention

Test the smallest cases first: empty input, one card, two cards, three cards in every permutation. Then test sorted, reversed, almost sorted, repeated ranks, equal-key stability, and inputs constructed to defeat your choice of pivot or gap. If the sort is deterministic, exhaustively enumerate all permutations of up to six distinct items (6!=720 cases). This is often more revealing than thousands of random large inputs.

**Counterexample exercise.** Propose that “every card needs to move left at most once.” Construct a three- or four-card packet that disproves the claim, or prove the claim under a narrower allowed-operation model.

## 5. Analyze work, memory, and information

Keep separate counts for comparisons, swaps, writes, block movements, and temporary storage. For a nested loop, count the number of inner iterations rather than simply declaring it quadratic. For recursion, draw the call tree and write a recurrence. Distinguish worst-case guarantees from expectations under a specified distribution.

An algorithm that minimizes writes may not minimize comparisons. An algorithm that minimizes total comparisons may not minimize parallel depth. An algorithm optimal on a table may be unusable in one hand. Treat these as separate optimization objectives, not contradictions.

## 6. Benchmark without fooling yourself

Use the same input permutations for competing algorithms. Record implementation language, data representation, hardware, compiler/interpreter, warm-up, and timing method. Repeat trials and report variation. Avoid comparing one carefully optimized library routine with a naïve implementation of another and attributing the difference solely to the abstract algorithm. Where possible, measure operation counts independently of elapsed time.

**Experimental notebook:** hypothesis; input generator; comparison model; code version; expected result; measured results; counterexamples; revised hypothesis. A surprising observation becomes valuable when another person can reproduce it.

## 7. Research whether the idea already exists

Search by *mechanism* as well as by name: “bidirectional adjacent exchange,” “adaptive natural runs,” “minimum writes permutation cycles,” “multi-pivot partition,” “sorting network,” or “heap-based priority selection.” Compare your method against the literature's actual invariants and cost model, not just its title. Independent rediscovery is intellectually valuable even when the method is not historically new.

## 8. What remains open?

Research is not limited to inventing an entirely new universal comparison sort. Productive directions include memory-constrained and external-memory sorting, parallel sorting networks, stable in-place sorting, robust performance under adversarial inputs, energy/write minimization, and human-computer or physical manipulation cost models. Be careful: the general comparison lower bound rules out asymptotically beating n log n comparisons for arbitrary distinct keys, but does not rule out improvements in constants, memory, stability, distribution-sensitive behavior, or specialized key representations.

## 9. Final laboratory: a hand-only sorting algorithm

**Challenge.** Invent a sorting algorithm for a deck held entirely in two hands, without a table. Define whether cards may be split into two packets and whether a temporary single-card buffer is permitted. Write a precise procedure for ten cards, then 52. Demonstrate that every operation is physically possible. Explain why it terminates and why the result is sorted. Compare against ordinary Insertion Sort in the same two-hand model.

Your report should include a diagram of the hand positions, a worked trace, an invariant, a worst-case or expected-cost analysis, and at least one input designed to expose your algorithm's weakness. A genuinely useful invention may optimize *comfort, error rate, or hand travel* rather than the number of comparisons.

## Ten further investigations

1. Can you prove the minimum number of comparisons needed to sort three, four, and five distinct cards?
2. How does the expected number of inversions in a uniformly shuffled n-card packet arise from counting pairs?
3. What is the minimum number of arbitrary swaps needed for a particular permutation?
4. How do duplicate ranks change three-way Quicksort partitioning?
5. Can you construct a comparator that violates transitivity and watch a sort misbehave?
6. How many parallel stages does an eight-input bitonic network need?
7. Can a stable, low-memory sort avoid moving equal-key cards unnecessarily?
8. How does an expensive string comparison change the best algorithm choice?
9. Can you improve a run-aware algorithm when the input is almost sorted in reverse order?
10. What is the smallest change to an existing method that creates a measurable, reproducible improvement under a stated cost model?

# Algorithm profile comparison
\label{profile-matrix}

The ratings use the same five-level editorial scale explained before Selection Sort. They are **not measured timings**. A low score in one column is not an indictment of an algorithm whose intended use lies elsewhere.

\begingroup
\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{longtable}{@{}r p{0.34\linewidth} c c c c@{}}
\toprule No. & Algorithm & Learn & Small & Near & Large \\
\midrule
\endfirsthead
\toprule No. & Algorithm & Learn & Small & Near & Large \\
\midrule
\endhead
1 & Selection Sort & 5 & 3 & 1 & 1 \\
2 & Insertion Sort & 5 & 5 & 5 & 1 \\
3 & Bubble Sort & 5 & 2 & 3 & 1 \\
4 & Cocktail Shaker Sort & 4 & 2 & 3 & 1 \\
5 & Gnome Sort & 4 & 3 & 4 & 1 \\
6 & Binary Insertion Sort & 5 & 5 & 4 & 2 \\
7 & Shellsort & 5 & 5 & 3 & 3 \\
8 & Comb Sort & 4 & 3 & 2 & 1 \\
9 & Merge Sort & 5 & 4 & 4 & 5 \\
10 & Quicksort & 5 & 5 & 2 & 5 \\
11 & Dual-Pivot Quicksort & 4 & 4 & 2 & 5 \\
12 & Tree Sort & 5 & 3 & 2 & 3 \\
13 & Heapsort & 5 & 3 & 2 & 4 \\
14 & Tournament Sort & 5 & 3 & 2 & 4 \\
15 & Counting Sort & 5 & 5 & 5 & 5 \\
16 & Radix Sort & 5 & 4 & 4 & 5 \\
17 & Bucket Sort & 5 & 5 & 3 & 4 \\
18 & Pigeonhole Sort & 4 & 4 & 4 & 4 \\
19 & Cycle Sort & 5 & 3 & 2 & 1 \\
20 & Pancake Sort & 4 & 2 & 1 & 1 \\
21 & Natural Merge Sort & 5 & 4 & 5 & 5 \\
22 & Timsort & 5 & 4 & 5 & 5 \\
23 & Introsort & 5 & 4 & 3 & 5 \\
24 & Smoothsort & 4 & 2 & 5 & 4 \\
25 & Bitonic Sort & 5 & 2 & 1 & 4 \\
26 & Odd-Even Transposition Sort & 4 & 2 & 3 & 1 \\
27 & Strand Sort & 4 & 3 & 4 & 3 \\
28 & Patience Sort & 5 & 4 & 3 & 4 \\
29 & Bogosort & 5 & 1 & 1 & 1 \\
30 & Stooge Sort & 4 & 1 & 1 & 1 \\
\bottomrule
\end{longtable}
\endgroup
\begingroup
\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{longtable}{@{}r p{0.34\linewidth} c c c c@{}}
\toprule No. & Algorithm & Memory & Table & Hand & Use \\
\midrule
\endfirsthead
\toprule No. & Algorithm & Memory & Table & Hand & Use \\
\midrule
\endhead
1 & Selection Sort & 5 & 3 & 2 & 2 \\
2 & Insertion Sort & 5 & 5 & 5 & 5 \\
3 & Bubble Sort & 5 & 3 & 2 & 1 \\
4 & Cocktail Shaker Sort & 5 & 3 & 2 & 1 \\
5 & Gnome Sort & 5 & 4 & 4 & 1 \\
6 & Binary Insertion Sort & 5 & 4 & 4 & 4 \\
7 & Shellsort & 5 & 3 & 2 & 3 \\
8 & Comb Sort & 5 & 3 & 2 & 1 \\
9 & Merge Sort & 2 & 5 & 2 & 5 \\
10 & Quicksort & 4 & 4 & 2 & 5 \\
11 & Dual-Pivot Quicksort & 4 & 3 & 1 & 4 \\
12 & Tree Sort & 2 & 3 & 1 & 3 \\
13 & Heapsort & 5 & 2 & 1 & 4 \\
14 & Tournament Sort & 2 & 4 & 1 & 3 \\
15 & Counting Sort & 2 & 3 & 1 & 5 \\
16 & Radix Sort & 2 & 4 & 2 & 5 \\
17 & Bucket Sort & 2 & 5 & 3 & 4 \\
18 & Pigeonhole Sort & 2 & 4 & 2 & 2 \\
19 & Cycle Sort & 5 & 2 & 1 & 3 \\
20 & Pancake Sort & 5 & 4 & 2 & 2 \\
21 & Natural Merge Sort & 2 & 5 & 2 & 5 \\
22 & Timsort & 2 & 4 & 2 & 5 \\
23 & Introsort & 4 & 3 & 1 & 5 \\
24 & Smoothsort & 5 & 1 & 1 & 2 \\
25 & Bitonic Sort & 2 & 2 & 1 & 4 \\
26 & Odd-Even Transposition Sort & 5 & 3 & 2 & 3 \\
27 & Strand Sort & 2 & 4 & 2 & 2 \\
28 & Patience Sort & 2 & 5 & 4 & 4 \\
29 & Bogosort & 5 & 1 & 1 & 1 \\
30 & Stooge Sort & 5 & 1 & 1 & 1 \\
\bottomrule
\end{longtable}
\endgroup

**Interpretation:** compare ratings within a column first. Then read the relevant chapters: the same method can be excellent for one setting and poor for another.

# Reference and field notes
\label{reference}

## Expanded algorithm index

| # | Algorithm | Central mechanism | Page |
|---:|:---|:---|---:|
| 1 | Selection Sort | See full performance analysis and card exercises | \pageref{alg1} |
| 2 | Insertion Sort | See full performance analysis and card exercises | \pageref{alg2} |
| 3 | Bubble Sort | See full performance analysis and card exercises | \pageref{alg3} |
| 4 | Cocktail Shaker Sort | Bubble Sort in both directions: sweep left-to-right to place the latest… | \pageref{alg4} |
| 5 | Gnome Sort | Walk forward while neighboring cards are ordered; step backward and… | \pageref{alg5} |
| 6 | Binary Insertion Sort | Find each insertion position by binary search in the sorted prefix,… | \pageref{alg6} |
| 7 | Shellsort | See full performance analysis and card exercises | \pageref{alg7} |
| 8 | Comb Sort | Exchange out-of-order pairs separated by a shrinking gap, finishing… | \pageref{alg8} |
| 9 | Merge Sort | See full performance analysis and card exercises | \pageref{alg9} |
| 10 | Quicksort | See full performance analysis and card exercises | \pageref{alg10} |
| 11 | Dual-Pivot Quicksort | Partition around two pivots to produce three regions, then recursively… | \pageref{alg11} |
| 12 | Tree Sort | Insert each key into a binary search tree; traverse the tree in order… | \pageref{alg12} |
| 13 | Heapsort | See full performance analysis and card exercises | \pageref{alg13} |
| 14 | Tournament Sort | Arrange pairwise contests in a tournament tree; the winner is the… | \pageref{alg14} |
| 15 | Counting Sort | See full performance analysis and card exercises | \pageref{alg15} |
| 16 | Radix Sort | See full performance analysis and card exercises | \pageref{alg16} |
| 17 | Bucket Sort | See full performance analysis and card exercises | \pageref{alg17} |
| 18 | Pigeonhole Sort | Provide one slot for every possible key and place each item directly… | \pageref{alg18} |
| 19 | Cycle Sort | See full performance analysis and card exercises | \pageref{alg19} |
| 20 | Pancake Sort | Sort using only prefix reversals: flip the first k cards as a single… | \pageref{alg20} |
| 21 | Natural Merge Sort | Detect existing ascending runs rather than splitting blindly, then… | \pageref{alg21} |
| 22 | Timsort | See full performance analysis and card exercises | \pageref{alg22} |
| 23 | Introsort | See full performance analysis and card exercises | \pageref{alg23} |
| 24 | Smoothsort | Maintain a family of Leonardo-number heaps that adapts to existing… | \pageref{alg24} |
| 25 | Bitonic Sort | Use a fixed network of compare-exchange operations to sort a bitonic… | \pageref{alg25} |
| 26 | Odd-Even Transposition Sort | Alternate parallel comparisons of odd-indexed neighbor pairs and… | \pageref{alg26} |
| 27 | Strand Sort | Extract an increasing subsequence from the input, then merge it into a… | \pageref{alg27} |
| 28 | Patience Sort | Deal each card onto the leftmost pile whose top is at least as late as… | \pageref{alg28} |
| 29 | Bogosort | Repeatedly shuffle the entire packet until it happens to be sorted | \pageref{alg29} |
| 30 | Stooge Sort | Recursively sort overlapping two-thirds portions three times, a… | \pageref{alg30} |

## Glossary

**Amortized analysis:** the average cost per operation over a sequence, even when an individual operation is expensive.

**Adversarial input:** an arrangement chosen to expose an algorithm's weakness.

**Comparison lower bound:** the information-theoretic Ω(n log n) worst-case requirement for sorting arbitrary distinct items using only pairwise comparisons.

**Parallel depth:** the number of sequential stages when independent operations can run simultaneously.

**Permutation cycle:** a closed chain of destination positions, useful for reasoning about minimum swaps.

**Recurrence:** an equation describing recursive cost in terms of smaller problem sizes.

**Sorting network:** a fixed sequence of compare-exchange connections independent of the input values.



The definitions are separated for quick reference. Each includes the practical meaning rather than just a synonym.

**Adaptive.** A sort that performs less work when the input already contains useful order. Insertion Sort can finish an already sorted 52-card packet with only 51 key comparisons.

**Auxiliary memory.** Storage beyond the input itself. A computer may allocate an output array; on a table you might need extra piles; in your hands you may run out of available fingers.

**Average case.** Expected cost over a *specified distribution* of inputs. “Average” is not a promise about your particular shuffle; the assumed randomness matters.

**Best case / worst case.** The least / greatest work an algorithm can require for inputs of the same size, using the specified implementation and counting convention.

**Big-O, O(f(n)).** An asymptotic upper growth bound, up to a constant multiplier. It does not specify exact comparisons or seconds for 52 cards.

**Bucket.** A designated container for a range of possible keys. A ♠ pile is one bucket if the final order groups all ♠ together.

**Comparison.** One decision about whether a key comes before, after, or equals another key. Reading a rank to choose a pile is not necessarily a pairwise comparison.

**Cutoff.** A threshold at which a hybrid switches methods, such as using Insertion Sort for packets of four or fewer cards.

**Equal keys.** Two distinct cards with the same *sorting criterion*. If you sort by rank only, 7♠ and 7♡ have equal keys; under the full canonical order, they do not.

**In-place.** Reorders an input with little extra storage, usually constant-sized workspace. This does not mean the algorithm performs few moves.

**Invariant.** A claim guaranteed to hold after each step or pass. In Selection Sort, everything to the left of the boundary is permanently in final order.

**Inversion.** A pair of cards that appear backward relative to the target. In `5♠ 2♠ 4♠`, the pairs `(5♠,2♠)` and `(5♠,4♠)` are inversions.

**Key.** The value that decides where an item belongs. A full-deck key can encode both suit and rank; a rank-only key ignores suit.

**Logarithm, log₂ n.** Approximately how many times n can be halved until one remains. Since 2⁵ < 52 < 2⁶, log₂ 52 lies between 5 and 6.

**Partition.** Divide items into regions according to a chosen criterion, typically whether they are earlier or later than a pivot.

**Pivot.** A chosen reference card used for partitioning. It is not automatically the median; a poor pivot can produce very uneven subproblems.

**Quadratic.** A growth pattern proportional to n². Doubling the packet size can increase work by about four times for large n.

**Recursion.** Solving a problem by applying the same method to smaller versions of it, with a stopping case such as a one-card packet.

**Run.** A contiguous segment already in ascending or descending order. Timsort searches for these rather than destroying them.

**Stable.** If two cards have equal keys, a stable sort keeps them in their original relative order. Stability is observable when sorting by rank only.

**Swap / shift / block move.** A swap exchanges two positions; a shift moves intervening items; a block move treats several cards as one physical gesture. The computer and card-table costs differ.

**Theta, Θ(f(n)).** A tight asymptotic growth rate, bounded above and below by constant multiples of f(n).

**Omega, Ω(f(n)).** An asymptotic lower growth bound. The comparison-sorting lower bound is Ω(n log n) in the worst case.

## Printable experiment sheet

Algorithm: ________________________ Packet size: ________ Input arrangement: __________________

| Observation | Count or notes |
|:---|:---|
| Comparisons | |
| Swaps | |
| Single-card shifts | |
| Block movements | |
| Piles / workspace | |
| Full passes | |
| Hand-only feasibility | |

**Which actions were cheap on a computer but awkward physically?**

\vspace{0.6in}

**Which physical gestures were cheap but correspond to many computer writes?**

\vspace{0.6in}

**What did the algorithm exploit or fail to exploit about the input?**

\vspace{0.6in}\vspace{0.6in}