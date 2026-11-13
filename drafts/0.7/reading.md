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
  - '\setcounter{tocdepth}{2}'
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
\vspace{5pt}\noindent{\sffamily\bfseries\small FOUNDATIONS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{How to use this book}\nobreak\dotfill\pageref{howto}\par\vspace{1pt}
\vspace{5pt}\noindent{\sffamily\bfseries\small THE ELEMENTARY METHODS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{1}  Selection Sort\nobreak\dotfill\pageref{alg1}\par\vspace{1pt}
\noindent\textbf{2}  Insertion Sort\nobreak\dotfill\pageref{alg2}\par\vspace{1pt}
\noindent\textbf{3}  Bubble Sort\nobreak\dotfill\pageref{alg3}\par\vspace{1pt}
\noindent\textbf{Inversions, stability and cost models}\nobreak\dotfill\pageref{interlude-a}\par\vspace{1pt}
\vspace{5pt}\noindent{\sffamily\bfseries\small DIVIDE, PARTITION AND HEAP}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{4}  Merge Sort\nobreak\dotfill\pageref{alg4}\par\vspace{1pt}
\noindent\textbf{5}  Quicksort\nobreak\dotfill\pageref{alg5}\par\vspace{1pt}
\noindent\textbf{Quickselect: find a rank without sorting}\nobreak\dotfill\pageref{quickselect}\par\vspace{1pt}
\noindent\textbf{6}  Heapsort\nobreak\dotfill\pageref{alg6}\par\vspace{1pt}
\noindent\textbf{The comparison lower bound}\nobreak\dotfill\pageref{interlude-b}\par\vspace{1pt}
\vspace{5pt}\noindent{\sffamily\bfseries\small STRUCTURED KEYS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{7}  Counting Sort\nobreak\dotfill\pageref{alg7}\par\vspace{1pt}
\noindent\textbf{8}  Radix Sort\nobreak\dotfill\pageref{alg8}\par\vspace{1pt}
\noindent\textbf{9}  Bucket Sort\nobreak\dotfill\pageref{alg9}\par\vspace{1pt}
\vspace{5pt}\noindent{\sffamily\bfseries\small REFINEMENT AND HYBRIDS}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{10}  Shellsort\nobreak\dotfill\pageref{alg10}\par\vspace{1pt}
\noindent\textbf{11}  Timsort\nobreak\dotfill\pageref{alg11}\par\vspace{1pt}
\noindent\textbf{12}  Introsort\nobreak\dotfill\pageref{alg12}\par\vspace{1pt}
\noindent\textbf{13}  Cycle Sort\nobreak\dotfill\pageref{alg13}\par\vspace{1pt}
\noindent\textbf{Choosing a sorting strategy}\nobreak\dotfill\pageref{synthesis}\par\vspace{1pt}
\vspace{5pt}\noindent{\sffamily\bfseries\small REFERENCE}\par\vspace{2pt}\hrule\vspace{2pt}
\noindent\textbf{Complexity chart, glossary and worksheets}\nobreak\dotfill\pageref{reference}\par\vspace{1pt}
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


# 1. Selection Sort

\label{alg1}

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

# 4. Merge Sort

\label{alg4}

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

# 5. Quicksort

\label{alg5}

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

\label{quickselect}

Quickselect answers “Which card would be kth if I sorted everything?” without sorting everything. Choose a pivot, partition into earlier/later piles, and keep **only** the pile containing the target position. Adjust the target position when discarding the earlier pile and pivot.

**Try it:** From 15 random cards, find the 8th card in sorted order. If the EARLIER pile contains seven cards, the pivot is the answer. If it contains more, search EARLIER for the same target rank. If fewer, search LATER for target rank minus (size of EARLIER + 1).

Expected time is O(n) for good pivot behavior; naive pivots permit O(n²) worst cases. In hand, the partitioning works for one round, but repeated pile storage quickly becomes awkward. **Lesson:** solve only the problem you actually need solved.

\begin{flushright}
\includegraphics[width=0.27\linewidth,height=0.73in,keepaspectratio]{illustrations/orbital_partition.png}
\end{flushright}

# 6. Heapsort

\label{alg6}

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

# Concept interlude B: Why comparisons have a lower bound

\label{interlude-b}

If you may learn order only by comparing two distinct items, each comparison answers a yes/no question. With n distinct cards there are n! (n factorial) possible orders. For three cards, 3!=6. For five cards, 5!=120.

A sequence of comparisons can be pictured as a branching **decision tree**. A tree of height h has at most 2^h leaves, so distinguishing n! arrangements requires

$$2^h\ge n!,\qquad h\ge\log_2(n!).$$

That quantity grows as **Ω(n log n)**. It is a worst-case lower bound for *comparison-based* sorting. It does not say every input requires that many comparisons, nor does it say all algorithms have identical constants.

For five distinct cards, six comparisons distinguish at most 64 cases, but there are 120 possible orders. Some arrangement therefore needs at least seven comparisons. For 52 cards the information-theoretic lower bound is **at least 226 comparisons** (ceil(log₂(52!))).

Counting, Radix, and Bucket Sort do not violate this theorem: they use the card's rank or suit as an **address** into a known set of possibilities, rather than learning everything through binary comparisons.


# 7. Counting Sort

\label{alg7}

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
# 8. Radix Sort

\label{alg8}

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

# 9. Bucket Sort

\label{alg9}

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

# 10. Shellsort

\label{alg10}

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

# 11. Timsort

\label{alg11}

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
def timsort_model(a):
    # Built-in Timsort interface.
    return sorted(a)
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

# 12. Introsort

\label{alg12}

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
    # Conceptual sketch: production implementations use
    # an in-place partition, heap fallback and insertion cutoff.
    return sorted(a)
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


# 13. Cycle Sort

\label{alg13}

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

# Synthesis: Choosing a strategy

\label{synthesis}

No algorithm wins in every environment. Ask: How many items? Is the input already partly ordered? Are keys bounded? Do equal keys require stability? Are comparisons expensive? Are writes expensive? Is extra memory scarce? Can I maintain several piles? Am I holding the cards or using a table?

For a deck **in hand**, Insertion Sort is a natural default. On a **table**, suit-based Bucket Sort is often the most pleasant route to our exact canonical order. On a **computer**, for a small general-purpose array, a library's adaptive or introspective hybrid is usually preferable to reimplementing any textbook method. If keys are already known integers 0–51, direct indexing can change the problem altogether.

## Final challenge

Shuffle all 52. Before touching the deck, choose (1) a table algorithm, (2) an in-hand algorithm, and (3) a computer algorithm. Explain what makes each efficient in its environment. Then actually perform at least two of the three that you can do physically.

## What the book has been teaching

Sorting is a laboratory for invariants, partial order, recursion, representation, information limits, memory tradeoffs, adaptiveness, and cost models. The card is the same object in all three settings; what changes is the cost of asking about it, storing it, and moving it.


# Reference and field notes
\label{reference}

## Complexity at a glance

In this table **n** is number of cards, **k** is number of available key values or buckets (depending on algorithm), and **d** is the number of digits/fields processed by Radix Sort. With 52 unique card-position keys, n=52 and k=52. With rank-only keys, k=13. For two-field radix sorting, d=2. A **cutoff** is the small partition size where a hybrid changes from one method to another. A **production hybrid** combines algorithms and optimizations in a real software library.

| # | Algorithm | Best | Typical | Worst | Page |
|---:|:---|:---|:---|:---|---:|
| 1 | Selection Sort | O(n²) | O(n²) | O(n²) | \pageref{alg1} |
| 2 | Insertion Sort | O(n) | O(n²) | O(n²) | \pageref{alg2} |
| 3 | Bubble Sort | O(n) | O(n²) | O(n²) | \pageref{alg3} |
| 4 | Merge Sort | O(n log n) | O(n log n) | O(n log n) | \pageref{alg4} |
| 5 | Quicksort | O(n log n) | O(n log n) | O(n²) | \pageref{alg5} |
| 6 | Heapsort | O(n log n) | O(n log n) | O(n log n) | \pageref{alg6} |
| 7 | Counting Sort | O(n+k) | O(n+k) | O(n+k) | \pageref{alg7} |
| 8 | Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | \pageref{alg8} |
| 9 | Bucket Sort | O(n) favorable assumptions | O(n) favorable assumptions | O(n²) with insertion in one bucket | \pageref{alg9} |
| 10 | Shellsort | Gap-dependent | Gap-dependent | O(n²) for simple gaps | \pageref{alg10} |
| 11 | Timsort | O(n) | O(n log n) | O(n log n) | \pageref{alg11} |
| 12 | Introsort | O(n log n) typical | O(n log n) | O(n log n) | \pageref{alg12} |
| 13 | Cycle Sort | O(n²) | O(n²) | O(n²) | \pageref{alg13} |

The growth labels describe computer work under particular models. They do not encode table space or how many packets a hand can comfortably maintain.

## Glossary

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

\vspace{0.6in}