---
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
fontsize: 10pt
geometry: "margin=0.75in"
header-includes:
  - "\\usepackage{graphicx}"
  - "\\usepackage{longtable}"
  - "\\setcounter{tocdepth}{2}"
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

| Route | Lessons | Page |
|:---|:---|---:|
| Foundations | How to use the book and read the performance tables | \pageref{howto} |
| Elementary | 1 Selection, 2 Insertion, 3 Bubble | \pageref{alg1} |
| First interlude | Inversions, stability, and what quadratic means | \pageref{interlude-a} |
| Divide and conquer | 4 Merge, 5 Quicksort, Quickselect, 6 Heapsort | \pageref{alg4} |
| Second interlude | Comparison lower bound | \pageref{interlude-b} |
| Non-comparison | 7 Counting, 8 Radix, 9 Bucket | \pageref{alg7} |
| Refinement and hybrids | 10 Shell, 11 Timsort, 12 Introsort, 13 Cycle | \pageref{alg10} |
| Synthesis | Choosing an algorithm | \pageref{synthesis} |
| Reference | Comparison table, glossary, worksheets, field notes | \pageref{reference} |

The next pages give a **detailed contents** with every section and subsection. Algorithm numbers 1–13 belong only to actual sorting algorithms; interludes and Quickselect are intentionally unnumbered.

\newpage


\tableofcontents
\newpage
# How to use this book
\label{howto}

This is a **field-test edition**, written for a learner using an actual 52-card deck. Pencil notes, objections, and awkward physical gestures are part of the experiment, not evidence that you are doing it wrong.

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

## The cost language, before you need it

**n** means number of items. In this book n=10 for many first exercises and n=52 for a full deck. **n²** means n multiplied by itself: 52²=2,704. A *quadratic* sort is one whose cost grows roughly in proportion to n²; this does **not** assert that it performs exactly 2,704 operations.

**log₂ n** means how many times you can approximately halve a problem before reaching one item. For 52, log₂ 52≈5.70. **n log₂ n** is therefore about 296 when n=52. It describes a growth rate, not a promised 296 comparisons.

**Big-O**, written O(...), is an upper bound on how an operation count grows as n becomes large, ignoring fixed multipliers and smaller terms. O(n²) might mean 1,326 comparisons for a particular 52-card algorithm, or 2,500, or fewer. **Ω(...)** gives a lower growth bound. **Θ(...)** means both bounds match. In ordinary performance tables, “best,” “average,” and “worst” describe different starting arrangements, not different decks.

**Best case** asks which input arrangement makes this specific procedure cheapest. **Average case** needs a stated distribution of inputs, usually uniformly random permutations. **Worst case** asks which arrangement makes it most expensive. Always ask *what is being counted*: comparisons, swaps, writes, physical gestures, or time? Different answers can all be correct.

**Stable** means equal-key records retain their original relative order. Our 52-card order gives every card a distinct key, so to test stability we temporarily sort by **rank only**: 7♠ and 7♡ then have equal keys even though they are different cards. **In-place** means using little additional storage beyond the original array. **Adaptive** means taking advantage of input that is already partly ordered.

## A worked growth-rate comparison

| n | n | n log₂ n (rounded) | n² | n(n−1)/2 |
|---:|---:|---:|---:|---:|
| 10 | 10 | 33 | 100 | 45 |
| 26 | 26 | 122 | 676 | 325 |
| 52 | 52 | 296 | 2,704 | 1,326 |
| 104 | 104 | 697 | 10,816 | 5,356 |

The final column is the **exact** number of pairwise comparisons Selection Sort makes. The middle columns are growth-rate landmarks, not precise operation predictions. Notice how doubling n makes n² roughly four times as large, while n log n grows somewhat more than twice as large.

## Learning routine

Start with 8–12 random cards unless a lesson specifies otherwise. First execute the rule faithfully. Then repeat with the same cards in sorted, reversed, or deliberately structured order. Record comparisons and movements separately. Finally attempt the in-hand variant and note whether it is still the same algorithm.

A *pass* is one traversal of the currently active cards. A *comparison* is one decision of which of two keys comes earlier. A *move* is an item changing position; a *block move* shifts several cards together in one hand gesture. We will never quietly treat a block gesture as a single computer write.


# 1. Selection Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/ordered_stacks.png}
\end{center}
\label{alg1}

## Core idea

**Repeatedly select the earliest remaining card and place it at the next fixed position.**

## History and uses

An elementary procedure with no useful single inventor; still used pedagogically and where writes are expensive.

## Pseudocode

```text
For each unsorted position i, scan positions
i..end for the earliest card; exchange it with
position i.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def selection(a):
    for i in range(len(a)-1):
        m = min(range(i,len(a)), key=a.__getitem__)
        a[i], a[m] = a[m], a[i]
    return a
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n²) |
| Typical/average growth | O(n²) |
| Worst-case growth | O(n²) |
| Extra computer memory | O(1) |
| Stable? | No |

**For 52 cards:** 1,326 comparisons, regardless of initial order; at most 51 exchanges.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Find the next item globally; place it permanently.**


# 2. Insertion Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/cards_in_hand.png}
\end{center}
\label{alg2}

## Core idea

**Build a sorted prefix by inserting each new item into its proper position.**

## History and uses

A longstanding manual method, important today for small or nearly ordered data and as a hybrid finishing step.

## Pseudocode

```text
For each next card, remember it, shift
later-valued cards right, then insert it in the
gap.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

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

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n) |
| Typical/average growth | O(n²) |
| Worst-case growth | O(n²) |
| Extra computer memory | O(1) |
| Stable? | Yes |

**For 52 cards:** Already sorted: 51 key comparisons. Reverse order: 1,326 key comparisons and 1,326 shifts.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Existing order is useful information.**


# 3. Bubble Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_exchange.png}
\end{center}
\label{alg3}

## Core idea

**Repeatedly repair out-of-order adjacent pairs.**

## History and uses

A classic exchange sort popularized in early computing instruction; mostly pedagogical today.

## Pseudocode

```text
Scan adjacent pairs left to right, swapping
backward neighbors. Repeat until a pass makes
no swaps.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

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

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n) |
| Typical/average growth | O(n²) |
| Worst-case growth | O(n²) |
| Extra computer memory | O(1) |
| Stable? | Yes |

**For 52 cards:** Already sorted: 51 comparisons with early exit. Reverse order: 1,326 comparisons and 1,326 adjacent swaps.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Local repairs can take many global passes.**


# Concept interlude A: Inversions, equal keys, and stability

\begin{center}
\includegraphics[width=0.46\linewidth,height=1.15in,keepaspectratio]{illustrations/suit_keys.png}
\end{center}
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


# 4. Merge Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/four_piles.png}
\end{center}
\label{alg4}

## Core idea

**Divide the packet into halves, sort each, then merge sorted packets.**

## History and uses

John von Neumann described the method in 1945; valuable for stable sorting and sequential or external data.

## Pseudocode

```text
Recursively split until singletons; merge by
repeatedly taking the earlier exposed card.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

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

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n log n) |
| Typical/average growth | O(n log n) |
| Worst-case growth | O(n log n) |
| Extra computer memory | O(n) |
| Stable? | Yes |

**For 52 cards:** For 52 distinct cards, ordinary balanced merging uses between 140 and 249 comparisons, depending on order and merge outcomes; not a fixed count.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Sort tiny pieces; combine by merging.**


# 5. Quicksort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/orbital_partition.png}
\end{center}
\label{alg5}

## Core idea

**Choose a pivot, partition into earlier/later cards, then recurse on both sides.**

## History and uses

Tony Hoare devised it in 1959 and published it in 1961; central to efficient general-purpose sorting.

## Pivot and partition: a physical explanation

A **pivot** is a chosen reference card, not necessarily the median. **Partitioning** means inspecting each other card and putting it into EARLIER or LATER relative to the pivot. For pivot 8♡, 3♠ belongs in EARLIER and 2♣ in LATER. Neither group is internally sorted yet. A poor pivot makes one huge group; a good pivot divides the work approximately in half.

The table version creates two piles. An in-place computer partition instead swaps items across a boundary in the original array, saving extra storage but costing exchanges. That is exactly why implementation details matter.

## Pseudocode

```text
Choose pivot; place each other card into an
earlier or later group; recursively sort both
groups; concatenate.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def quick(a):
    if len(a)<2: return a[:]
    p=a[0]
    return quick([x for x in a[1:] if x<p])+[p]+quick([x for x in a[1:] if x>=p])
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n log n) |
| Typical/average growth | O(n log n) |
| Worst-case growth | O(n²) |
| Extra computer memory | O(n) in this example |
| Stable? | No |

**For 52 cards:** First-card pivot on sorted 52 cards: 1,326 pivot comparisons. Balanced partitions: about 200–250 comparisons, depending on split sizes.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Partition first; recurse on smaller problems.**


# Side expedition: Quickselect (not a sort)

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_mountain.png}
\end{center}
\label{quickselect}

Quickselect answers “Which card would be kth if I sorted everything?” without sorting everything. Choose a pivot, partition into earlier/later piles, and keep **only** the pile containing the target position. Adjust the target position when discarding the earlier pile and pivot.

**Try it:** From 15 random cards, find the 8th card in sorted order. If the EARLIER pile contains seven cards, the pivot is the answer. If it contains more, search EARLIER for the same target rank. If fewer, search LATER for target rank minus (size of EARLIER + 1).

Expected time is O(n) for good pivot behavior; naive pivots permit O(n²) worst cases. In hand, the partitioning works for one round, but repeated pile storage quickly becomes awkward. **Lesson:** solve only the problem you actually need solved.


# 6. Heapsort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/house_of_cards.png}
\end{center}
\label{alg6}

## Core idea

**Maintain a complete binary tree whose parent is never earlier than its children.**

## History and uses

J. W. J. Williams published heapsort in 1964; Floyd improved heap construction. Heaps are essential for priority queues.

## Pseudocode

```text
Build max-heap bottom-up; exchange root with
last active item; shrink heap; sift new root
down; repeat.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def heap_sort(a):
    import heapq
    h=list(a); heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n log n) |
| Typical/average growth | O(n log n) |
| Worst-case growth | O(n log n) |
| Extra computer memory | O(1) in-place version |
| Stable? | No |

**For 52 cards:** 52-card in-place heapsort has order-of-hundreds of comparisons; a precise count depends on input and heap implementation.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Maintain enough partial order to extract the next extreme.**


# Concept interlude B: Why comparisons have a lower bound

\begin{center}
\includegraphics[width=0.46\linewidth,height=1.15in,keepaspectratio]{illustrations/cards_pyramid.png}
\end{center}
\label{interlude-b}

If you may learn order only by comparing two distinct items, each comparison answers a yes/no question. With n distinct cards there are n! (n factorial) possible orders. For three cards, 3!=6. For five cards, 5!=120.

A sequence of comparisons can be pictured as a branching **decision tree**. A tree of height h has at most 2^h leaves, so distinguishing n! arrangements requires

$$2^h\ge n!,\qquad h\ge\log_2(n!).$$

That quantity grows as **Ω(n log n)**. It is a worst-case lower bound for *comparison-based* sorting. It does not say every input requires that many comparisons, nor does it say all algorithms have identical constants.

For five distinct cards, six comparisons distinguish at most 64 cases, but there are 120 possible orders. Some arrangement therefore needs at least seven comparisons. For 52 cards the information-theoretic lower bound is **at least 226 comparisons** (ceil(log₂(52!))).

Counting, Radix, and Bucket Sort do not violate this theorem: they use the card's rank or suit as an **address** into a known set of possibilities, rather than learning everything through binary comparisons.


# 7. Counting Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_columns.png}
\end{center}
\label{alg7}

## Core idea

**Use each key as an index into counters, then reconstruct output.**

## History and uses

A standard distribution technique for bounded integer keys, especially when the key range is modest.

## Pseudocode

```text
Count occurrences; compute cumulative counts;
scan input backward and place each record at
its counted output position.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def counting(a, k=52):
    counts=[0]*k
    for x in a: counts[x]+=1
    out=[]
    for value,n in enumerate(counts): out.extend([value]*n)
    return out
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n+k) |
| Typical/average growth | O(n+k) |
| Worst-case growth | O(n+k) |
| Extra computer memory | O(n+k) stable variant |
| Stable? | Yes if stable version |

**For 52 cards:** With 52 distinct card-position keys: 52 count increments, 52 cumulative-counter updates, 52 output placements; no pairwise comparisons.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Use key values as addresses rather than comparing pairs.**


# 8. Radix Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_suits_vertical.png}
\end{center}
\label{alg8}

## Core idea

**Sort one component of a structured key at a time, using stable passes.**

## History and uses

Developed alongside mechanical and punched-card sorting; still useful for structured numeric and textual keys.

## Pseudocode

```text
Stable-sort by least significant field, then by
next field, continuing to most significant.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def radix_pairs(a):
    # Each key is (suit_index, rank_index)
    a=sorted(a,key=lambda x:x[1])
    return sorted(a,key=lambda x:x[0])
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(d(n+k)) |
| Typical/average growth | O(d(n+k)) |
| Worst-case growth | O(d(n+k)) |
| Extra computer memory | O(n+k) |
| Stable? | Yes with stable passes |

**For 52 cards:** For a 52-card deck encoded as two fields, two distribution passes inspect 104 card fields; each pass also has bucket setup/collection costs.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Stable component passes assemble full order.**


# 9. Bucket Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/pile_deck.png}
\end{center}
\label{alg9}

## Core idea

**Put cards into coarse ordered regions, sort within each, then concatenate.**

## History and uses

Distribution sorting is an old general technique; useful when the input distribution is known or reasonably uniform.

## Pseudocode

```text
Distribute to ordered buckets; sort each
bucket; concatenate in bucket order.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def bucket(a, bucket_of):
    b=[[] for _ in range(4)]
    for x in a: b[bucket_of(x)].append(x)
    return sum((sorted(part) for part in b), [])
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n) favorable assumptions |
| Typical/average growth | O(n) favorable assumptions |
| Worst-case growth | O(n²) with insertion in one bucket |
| Extra computer memory | O(n) |
| Stable? | Depends on internal sort |

**For 52 cards:** 52 cards in four equal suit buckets: 52 assignments plus four 13-card internal sorts; insertion within each suit takes 312 worst-case key comparisons in total.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Use coarse prior knowledge to make smaller sorts.**


# 10. Shellsort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_ascending.png}
\end{center}
\label{alg10}

## Core idea

**Repair long-distance disorder with gapped insertion sorts, then finish with gap 1.**

## History and uses

Donald Shell published it in 1959; performance depends strongly on gap sequence.

## Pseudocode

```text
For gaps decreasing to 1, insertion-sort each
interleaved subsequence of positions separated
by the gap.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

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

| Property | What it means here |
|:---|:---|
| Best-case growth | Gap-dependent |
| Typical/average growth | Gap-dependent |
| Worst-case growth | O(n²) for simple gaps |
| Extra computer memory | O(1) |
| Stable? | No |

**For 52 cards:** For 52 cards, halving gaps are 26, 13, 6, 3, 1; the exact comparison count depends on input.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Repair large-scale disorder before fine adjustments.**


# 11. Timsort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_vortex.png}
\end{center}
\label{alg11}

## Core idea

**Find already ordered runs, extend short runs, and merge them intelligently.**

## History and uses

Tim Peters developed it for Python in 2002; used in Python list sorting and influential elsewhere.

## Pseudocode

```text
Detect runs; reverse descending runs; extend
short runs with insertion; merge under run-size
rules.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def timsort_model(a):
    # Built-in Timsort interface.
    return sorted(a)
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n) |
| Typical/average growth | O(n log n) |
| Worst-case growth | O(n log n) |
| Extra computer memory | O(n) |
| Stable? | Yes |

**For 52 cards:** Already sorted 52 cards: a single 52-card run is found with 51 adjacent comparisons; full Timsort has additional implementation-dependent work.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Do not destroy order the input already gives you.**


# 12. Introsort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_stack.png}\end{center}
\label{alg12}

## Core idea

**Use Quicksort normally, switch to Heapsort if recursion gets too deep, and insertion-sort tiny pieces.**

## History and uses

David Musser proposed introspective sorting in 1997; widely influential in C++ standard-library sorts.

## Pseudocode

```text
Quicksort with depth budget; when exhausted use
heapsort; for tiny partitions use insertion.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def introsort_model(a):
    # Conceptual sketch: production implementations use
    # an in-place partition, heap fallback and insertion cutoff.
    return sorted(a)
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n log n) typical |
| Typical/average growth | O(n log n) |
| Worst-case growth | O(n log n) |
| Extra computer memory | O(log n) stack typical |
| Stable? | No |

**For 52 cards:** At 52 cards, depth limit often starts at 2 floor(log₂ 52)=10. Exact comparisons depend on pivots and cutoff.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

## Strengths, weaknesses, and cautions

Combines fast average behavior and worst-case protection; complex and generally unstable.

**Implementation note:** The Python example delegates to a library sort and is not an implementation of Introsort; the pseudocode describes the hybrid.

## Cards on a table

Use 16 cards and 8 coins as depth budget. Partition by pivot; spend a coin per recursive level; switch to heap on exhausted depth, insertion on groups of 4 or fewer.

## Cards in hand, without a table

You can partition small groups between two hands, but switching to a heap requires a surface. Mark this as impractical rather than pretending it is effortless.

## Experiment

Use a sorted packet with first-card pivots to force the fallback; compare with shuffled input.

## Three-setting checkpoint

Computer: strategy switches cheap; table: switching representations costs effort; hands: some representations simply do not fit.

## What should remain in your head

> **A good algorithm can change algorithms.**


# 13. Cycle Sort

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/card_cycle.png}
\end{center}
\label{alg13}

## Core idea

**Move each item directly toward its final position, following displacement cycles.**

## History and uses

Cycle sort is known for minimizing writes; useful conceptually when writing data is especially costly.

## Pseudocode

```text
For each cycle start, count items that precede
its item; write item to its final slot,
displace occupant, and repeat until cycle
closes.
```

## Python example

The code uses comparable numeric card keys (0–51) unless a lesson specifies structured keys. Some examples intentionally model the idea rather than the memory-efficient production implementation.

```python
def cycle_sort(a):
    # Distinct keys only; direct-write cycle sort.
    n=len(a)
    for start in range(n-1):
        item=a[start]
        pos=start+sum(x<item for x in a[start+1:])
        if pos==start: continue
        while pos!=start:
            item,a[pos]=a[pos],item
            pos=start+sum(x<item for x in a[start+1:])
        a[start]=item
    return a
```

## Performance and the 52-card case

| Property | What it means here |
|:---|:---|
| Best-case growth | O(n²) |
| Typical/average growth | O(n²) |
| Worst-case growth | O(n²) |
| Extra computer memory | O(1) |
| Stable? | No |

**For 52 cards:** At most 52 placements into final positions for distinct cards; comparisons remain quadratic and depend on cycle structure.

These are counts or bounds for **specified operations and implementations**, not stopwatch predictions. O(n log n) for 52 corresponds to a growth benchmark around 296, not necessarily 296 comparisons.

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

## What should remain in your head

> **Move each item toward its final slot; count writes, not merely comparisons.**


# Synthesis: Choosing a strategy

\begin{center}
\includegraphics[width=0.43\linewidth,height=1.15in,keepaspectratio]{illustrations/hand_sorting.png}
\end{center}
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

**Adaptive:** faster on already ordered or structured inputs. **Auxiliary memory:** storage beyond the input. **Average case:** expectation over an assumed input distribution. **Big-O:** upper asymptotic growth bound. **Bucket:** a region assigned a range of keys. **Comparison:** deciding which of two keys precedes the other. **Cutoff:** threshold where a hybrid switches method. **Equal keys:** two distinct records assigned the same sorting value. **In-place:** little auxiliary storage. **Inversion:** backward pair of items. **Key:** value used for sorting. **Partition:** split into groups around a pivot. **Pivot:** chosen reference card in Quicksort/Quickselect. **Quadratic:** growth proportional to n². **Run:** contiguous ordered segment. **Stable:** equal-key records retain their original relative order. **Worst case:** most expensive input arrangement under the stated model.

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

## Field-test notes

Mark instructions that are ambiguous when attempted literally. Record where a hand-only version changes the algorithm, where a diagram would help, where counting becomes too onerous, where a code example fails to clarify, and where the 52-card numerical example misleads. This is the material for the next teaching edition.