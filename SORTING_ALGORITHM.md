# Identification and Sorting

Revised 2026-10-31 following the [design review](docs/reviews/2026-10-31_DESIGN_REVIEW.md).
The former preferred recursive distribution workflow is superseded.

## Objective and operating modes

Optimize operator attention, cards processed between visits, and correct final
order alongside card cycles. A logical pass over the collection can require many
physical cassette loads.

- One-pass categorization: name, set when confirmed, or other requested categories.
- Preferred exact-sort candidate: inventory scan followed by stable distributions
  planned from the observed order.
- Simple comparison/fallback: scan then stable radix on dense ranks of present keys.
- Recursive ordered-range splitting: optional niche workflow; not the default
  until its operator load count is acceptable.

## Identification is a separate correctness gate

Recognition must report evidence for the requested identity level. Card name or
art recognition does not prove the exact printing. Set, collector number,
language, and finish may require different evidence and must not share a single
undifferentiated confidence score.

Use the visible set/number line where present, with OCR checked against candidate
metadata. Evaluate same-art reprints, absent or illegible identifiers, older layouts,
promos, languages, and foils separately. Some distinctions may be invisible from
the selected view. Retain an ambiguous candidate set and request review or reject;
do not force an exact-printing result.

Support name-level sorting as an explicit mode, while exact-printing recognition
remains a separate release gate for set-and-collector-number jobs. Offline local
data and models remain required; optional network updates stay outside the feed
control loop.

Reidentifying on every pass detects some inconsistencies, but cannot detect a
recognizer that consistently assigns the same wrong printing. Measure confidently
wrong accepted identities against independently established ground truth, as well
as rejects and coverage. Repeated observations of one card are correlated.

## Inventory scan

Record the complete ordered input sequence, canonical keys, ambiguity, cassette
IDs, counts, feed direction, and image references. Inventory collection may span
multiple cassettes; it needs a documented order-preserving chunk protocol too.

Freeze the key definition and database revision for the job. Resolve unknowns
before planning an exact complete sort. Equal keys retain scan occurrence order
for stable planning; occurrence IDs are bookkeeping, not marks that a camera can
necessarily distinguish on physically identical cards.

## Sort keys

The host converts the requested order into a deterministic tuple of normalized
fields, for example:

```text
(set order, collector number, language, finish)
```

Every field needs a documented, versioned normalization rule:

- **Set order:** user-selected release order or normalized code order, taken from
  the frozen database revision. Normalize code case and aliases.
- **Collector number:** not an integer. Parse a numeric part plus documented
  prefixes and suffixes (for example `12a`, `12b`, star or promo markers). Define
  their order explicitly. Never fall back to locale-dependent string comparison.
- **Name:** Unicode normalization and case folding, with a documented rule for
  multi-face, split, and similar cards.
- **Language and finish:** a fixed enumeration order.

Cards with equal keys are equivalent; ties keep scan order. A card with any
required field unknown or ambiguous receives no normal key. Resolve or reject it
before planning.

## Planned stable distributions

Let target order be a stable sort of the scanned keys. Read the original input
positions in that target order. Start a new rising sequence whenever the next
position is smaller than the preceding position:

```text
R = 1 + number of descents in original positions read in target order
p = smallest integer such that k^p >= R
total full traversals = one inventory scan + p distributions
```

An empty job takes zero traversals; an already sorted nonempty job needs only the
inventory scan, if its collection preserves order. R is not the number of adjacent
ascending runs seen while reading the input. For example, input [0,2,4,1,3,5] has
two adjacent ascending runs but three rising sequences by this definition.

Assign each occurrence its sequence label 0 through R-1. Stable radix distribution
on those labels, least significant digit first, sorts the job. Each output must
preserve feed order, or a known mechanical reversal must be normalized before
reloading. Collect routes in digit order, with chronological chunks within each.

Within this model, p is minimal: p stable k-way distributions supply at most k^p
ordered labels. Every descent in target-order input positions requires a boundary
between labels; the sequence-label construction attains this bound. This is a
minimum for this particular operation model, not for every possible manual
shuffle, reversible stack mechanism, merge algorithm, or capacity-constrained
workflow.

The rising-sequence/inverse-descent relation is described in
[Bayer's combinatorics notes](https://www.math.columbia.edu/~bayer/S02/combinatorics/notes.1.31.pdf).
The sorter construction and proof above are our derivation, checked by the local
simulator rather than a claimed hardware result.

## Reproduced comparisons

These are deterministic model results, not timing measurements. Catalog size
100,000 is an illustrative comparison parameter, not a current catalog count.
All scan-first counts include the inventory scan; catalog radix needs no initial
scan in this comparison.

| Job | R | Planned 4-way / 8-way | Scan + dense ranks 4-way / 8-way | Catalog radix 4-way / 8-way |
|---|---:|---|---|---|
| Random 1,000 distinct cards | 506 | 6 / 4 | 6 / 5 | 9 / 6 |
| Random 5,000 distinct cards | 2,487 | 7 / 5 | 8 / 6 | 9 / 6 |
| Sorted 2,000 plus 100 shuffled newcomers | 101 | 5 / 4 | 7 / 5 | 9 / 6 |
| Sorted 1,000 | 1 | 1 / 1 | 6 / 5 | 9 / 6 |

Balanced recursive splitting of 1,000 distinct keys requires 341 group feeds with
four outputs, or 561 with eight, before finite-capacity reloads are counted. It
uses 5,000 / 3,976 card cycles. The planned alternative uses 6,000 / 4,000 cycles,
with fewer group changes. The recursive count depends on group sizes and rounding;
more outputs do not always mean fewer internal groups.

Eight outputs save two traversals in the random-1,000 example: 33% of card cycles.
For the merge example they save one of five: 20%. Neither saving is universal, and
selector movement and operator handling must be included in measured comparisons.

## Finite capacity and operator visits

A job of N cards can span many cassettes. The R8 target is 500 cards per hopper and
pocket, subject to thickness and sleeve measurements; the 150–250-card figures
below come from the earlier S4 comparison. Do not require each output to contain
the entire job.

Before accepting another card, reserve capacity for its destination. Stop safely
before a full route, close and label its cassette, replace it, and resume the same
logical output stream. Store route ID, pass ID, chunk ordinal, count, and feed
direction. Reload routes in digit order, then chunks in chronological order.
Never route overflow into another radix bin just because it has space.

At 0.3 mm assumed thickness, 200 cards occupy 60 mm and 1,000 occupy 300 mm along
the stacking axis, before walls, follower, clearance, or curl. These are arithmetic
examples, not validated dimensions.

With a 200-card input at 3 seconds per cycle (earlier S4), input depletion alone
requires attention within ten minutes, and six traversals of 1,000 cards take five
machine-hours. With R8's 500-card hopper at a target 1 card/s, the hopper lasts
about 8 minutes, and four traversals of 1,000 cards take about 67 minutes. Full
outputs or faults can require attention sooner in either case.

Record card cycles, input loads, output chunk removals, mid-route replacements,
minutes between required visits, active human minutes, staging footprint, and
elapsed job time. An action count is not a visit count: one visit may combine
several actions. Compare with measured manual sorting using the same accuracy goal.

The model at [software/sort_model.py](software/sort_model.py) explicitly chunks
outputs and counts replacements. It does not yet model operator arrival, concurrent
cassette changes, actual pickup mechanics, recognition errors, or retry durations.

## Expected-card verification

Recognize each card and compare its key with the expected next key before release.
Matching only the collection's multiset is insufficient. Cassette tags verify the
container, not its contents or order.

After the inventory scan, every read is a verification question: is this card
consistent with the one expected occurrence? That is easier than open
identification, but treating every inconclusive read as a plan-breaking mismatch
would make recognition noise stop the job. Illustratively, 1,000 cards over six
traversals is 6,000 reads; a 0.5% inconclusive rate would cause about 30 stops.
Respond in graded steps:

1. **Consistent:** the evidence supports the expected key at the requested identity
   level. Release to the planned route.
2. **Inconclusive:** use the second capture taken in motion under the alternate
   lighting state. The R8 transport does not stop to re-image.
3. **Still inconclusive, not contradictory:** route to reject and continue the plan.
   The card is resolved later as a mid-pass reject (below).
4. **Contradictory:** the evidence confidently identifies a different key, or two
   consecutive cards are inconclusive or rejected. Hold/stop and recover (below).

Verification must be measured against confusable neighbors, not only clean
matches. For exact-printing jobs, accepting a same-art reprint because it
resembles the expected card is a silent ordering error. Report verification false
accepts separately from open-identification accuracy. Verification must finish
within the route deadline; a late answer is treated as step 3. See
[designs/R8_RELIABLE_SORTER.md](designs/R8_RELIABLE_SORTER.md).

## Mid-pass rejects

A card diverted to reject during a planned distribution does not invalidate the
plan. Stable distributions preserve the relative order of every remaining card, so
the remaining cards still finish in target order without that occurrence. The
simulator checks this. Remove the rejected occurrence from the expected sequence
so later verification skips it, and reconcile counts with the reject route.

Rejected cards keep their scanned identity and target position. Resolve each one
(confirm identity, inspect for damage or doubles), then reinsert:

- **A few rejects:** guided manual insertion after the final pass, showing the
  identities of the neighboring cards on each side.
- **Many rejects:** treat them as newcomers to the sorted collection. Place them
  after it, inventory, and plan; R is at most one more than the number of rejects.

A detected double sends both cards to reject. Each is resolved and reinserted the
same way. Cards rejected during the inventory scan have no trusted key; resolve
them before planning, as above.

## Reload recovery

On a contradictory result: hold/stop, preserve the already-produced chunks and
event log, mark the old plan invalid, and reconcile all remaining, output, and
rejected cards. A conservative recovery inventories the complete current logical
collection in a documented cassette order and creates a fresh plan. Account for
that recovery scan and any extra distributions.

Continuing the old plan after rereading a reversed cassette can still produce an
incorrect result. The simulator includes a counterexample. A detected error can be
recoverable; an undetected error is not harmless. Duplicate equivalence must be
defined by the selected key, with occurrence counts reconciled.

Declare completion only when the final predicted sequence is ordered, counts and
physical transfers reconcile, and there are no unresolved exceptions. A final
physical verification traversal, if required, adds another pass. Recognition
accuracy still limits confidence in the actual physical result.

## Reproduction

From the project root:

```text
python software/sort_model.py
python -m unittest discover -s tests -p "test_*.py" -v
```

Tests cover all permutations through seven cards, duplicate keys, independent
small-state shortest-path checks, finite-capacity spill order, reload errors, and
plan validity after a mid-pass reject.
This is an executable mathematical model; it is not host-control software.
