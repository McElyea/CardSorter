# Design Review — 2026-10-31

## Outcome

The supplied critique identified material gaps in the September design. Revise
sorting, capacity, feeder selection, and recognition before committing to CAD.
Keep local host recognition, microcontroller interlocks, cycle IDs, independent
route evidence, and the standalone feeder milestone.

## Evidence and reproducibility

The review supplied a Python script named `passes.py` from a temporary Claude
scratchpad. It was read and executed locally; its results were reproduced. The
durable implementation is now [sort_model.py](../../software/sort_model.py), with
[tests](../../tests/test_sort_model.py). The model extends the comparison to dense
ranks, duplicate keys, finite-capacity chunks, and a reload-error counterexample.
It does not depend on the temporary script.

At seed 1, after shuffling 1,000 and then 5,000 distinct cards, the supplied merge
example produces these results:

| Job | Planned passes including scan: 4 / 8 outputs | Scan + dense ranks: 4 / 8 |
|---|---|---|
| Random 1,000; R=506 | 6 / 4 | 6 / 5 |
| Random 5,000; R=2,487 | 7 / 5 | 8 / 6 |
| Sorted 2,000 plus 100 shuffled newcomers; R=101 | 5 / 4 | 7 / 5 |

Catalog radix at an illustrative 100,000 ranks needs 9 / 6 distributions. Balanced
recursive splitting of 1,000 distinct keys has 341 / 561 internal group feeds and
5,000 / 3,976 card cycles. These group feeds are not directly comparable to full
collection passes, physical cassette loads, or operator visits.

## Decisions and qualifications

1. **Sort workflow:** replace preferred recursive distribution with scan-first
   planning from observed order. Keep dense-rank radix as a simpler baseline.
   Minimum-pass claims apply only to the stated stable distribution model. R counts
   descents of input positions in target order, not ordinary adjacent ascending
   runs. See [SORTING_ALGORITHM.md](../../SORTING_ALGORITHM.md).
2. **Recovery:** reidentification is necessary evidence, not automatic repair.
   Detect a sequence mismatch, invalidate the plan, reconcile the whole collection,
   and replan. Repeated consistent identity errors remain undetected without
   independent ground truth.
3. **Capacity:** remove the requirement that each output hold the entire job.
   Prototype 150–250-card cassettes and ordered spill chunks. In the random-1,000
   model with capacity 200, the 4-way / 8-way plans require 42 / 26 input chunk
   loads, 43 / 29 output chunks, and 24 / 4 mid-route replacements, including the
   inventory scan, preserving partially filled cassettes between passes without
   repacking. These are actions/chunks, not visits.
4. **Value metric:** track active human minutes, visits, card transfers between
   visits, and total elapsed time alongside throughput. At an assumed three seconds
   per card, 6,000 cycles take five machine-hours; input depletion at 200 cards
   occurs after ten minutes. Manual sorting speed and comparative labor savings
   require measurement; the claim that the machine is slower is not yet proven.
5. **Feeder:** use friction plus retard as the baseline, vacuum edge peel as a
   challenger. The shared-motor design depends on pickup disengagement, so it cannot
   be frozen independently of the feeder choice.
6. **Double sensing:** compare Hall displacement and suitable through-transmission
   ultrasound. Scanner precedent supports testing; it does not establish performance
   on foils, thick stock, or sleeves.
7. **Recognition:** separate name-level and exact-printing gates. Measure false
   accepted printing identities and ambiguity coverage on hard same-art cohorts.
   Preserve set-and-number sorting as a goal with an explicit unresolved risk.
8. **Medium design:** compare 4- and 8-way workflows now using the same job and
   capacity. The random-1,000 example saves 33% of cycles with eight outputs; the
   merge example saves 20%. The benefit is substantial but not universally two
   passes or 33–40%. A single radial selector already appears in Project-O; make
   no novelty claim for that arrangement.

## Supporting external evidence

- [Dave Bayer's combinatorics notes](https://www.math.columbia.edu/~bayer/S02/combinatorics/notes.1.31.pdf):
  inverse descents and rising sequences. Our minimum-pass construction is a
  derivation under explicit stable-bucket assumptions, independently tested locally.
- [Ricoh scanner cleaning layout](https://www.pfu.ricoh.com/global/scanners/erg/cleaning-7030.html):
  industrial use of pick/brake rollers and ultrasonic sensors. Archived technical
  precedent, not a current component recommendation or trading-card qualification.
- [Ricoh multifeed detection conditions](https://www.pfu.ricoh.com/global/scanners/erg/conditions-7030.html):
  material/thickness limits, leading-edge blind region on that model, and thick-card
  false positives. These motivate testing rather than copying its limits.

Existing hobbyist sources remain in [the source ledger](../hobbyist/SOURCES.md).

## Next physical action

Build the [cardboard-and-coupon feeder comparison bench](../../hardware/prototypes/FEEDER_COMPARISON.md),
beginning with friction/retard. No integrated frame or enclosure CAD is justified
until pickup control, double detection, and practical cassette handling are tested.

## Follow-up gap check

A second pass over the revised documents found and closed these gaps:

- **Verification noise:** a single inconclusive read no longer invalidates the plan.
  [SORTING_ALGORITHM.md](../../SORTING_ALGORITHM.md) now defines graded
  expected-card verification: re-image, reject and continue, stop on contradiction.
- **Mid-pass rejects:** removing a card during a stable distribution leaves the
  rest correctly ordered (now a simulator test). Rejects are reinserted by guided
  placement or a newcomer merge.
- **Sort keys:** restored normalization rules, including non-integer collector numbers.
- **Software deliverables:** restored in [software/README.md](../../software/README.md),
  including the USB protocol and versioned database updater.
- **Stale feeder wording:** the medium comparison table and P0 backlog in
  [DESIGN_IMPLICATIONS.md](../hobbyist/DESIGN_IMPLICATIONS.md) now list
  friction/retard as the baseline.

## Repository state

At review time the repository had no commits and all authored files were untracked.
This review adds durable simulation code and design corrections, but is not a Git
checkpoint or backup. No commit or remote publication was created.
