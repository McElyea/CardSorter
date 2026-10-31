# Roadmap

The roadmap retires the highest-risk assumptions first. Dates, enclosure styling,
and production cost targets should wait until real feed-cycle data exists.

Revised 2026-10-31 for the [reliability rework](docs/reviews/2026-10-31_RELIABILITY_REWORK.md)
and the [R8 design](designs/R8_RELIABLE_SORTER.md). The software model is tested;
hardware, recognition, and timing remain unvalidated.

## Milestone 0 — Standalone feeder bench

Build the instrumented [comparison bench](hardware/prototypes/FEEDER_COMPARISON.md):
pick roller plus torque-limited brake roller with a constant-force follower first,
then retard pad and vacuum on the same transport. It does not identify or sort.

### Required work

- Constant-force stack presentation on linear guides, with measured force.
- Pick roller and first transport nip on separate steppers.
- Hall-sensed idler for thickness; AS5600 encoder on an undriven idler for slip.
- Feeder state machine with cadence slots, interlocks, fault stop, and cycle log.
- Card-contact points visible, cleanable, and quick to change.
- Test matrix spanning ordinary cards, curl and wear, foils, contamination/static,
  and eventually common sleeves.

### Exit criteria

- Exactly one card is accounted for on every completed cycle.
- A missing card, double, stall, or abnormal timing stops safely and is logged.
- No visible edge, face, or corner damage under a documented inspection method.
- 10,000 consecutive ordinary-card cycles with zero undetected doubles, zero
  unrecovered jams, and zero observed damage.
- Pick-time spread fits inside the cadence slot at the target rate; skipped slots
  reported per 1,000 cycles.
- Slip trend recorded across the run, with a proposed maintenance threshold.
- Test data and failure examples published, not only a successful demonstration.

## Milestone 1 — Continuous transport and imaging

- Run the card bend test on representative stock; record the minimum radius that
  leaves no residual curl or whitening after repeated bending.
- Build the belt-synchronized transport with nips closer than the card length.
- Add the two-strobe global-shutter capture triggered by a beam sensor.
- Prove every physical card yields exactly one usable image pair at full speed and
  that all events reconcile with the feeder log.
- Add the buffer and route deadline with mocked recognition; inject late answers
  and confirm they produce rejects, not stops.
- Measure cadence adherence over 10,000 cycles.

## Milestone 2 — Local identification

- Build the local database, recognition pipeline, and confidence thresholds.
- Validate name and exact-printing recognition separately on held-out physical
  cards. Include same-art reprints, absent identifiers, old layouts, languages,
  promos, and foils. Report false accepted identities and rejects.
- Measure recognition latency on representative host computers; the 99th
  percentile must fit the route deadline with margin.
- Keep exact-printing jobs gated until evidence supports them; offer explicit
  name-only jobs without claiming printing-level correctness.
- Keep recognition replaceable so mechanical progress is not tied to one model or
  data provider.

## Milestone 3 — Router and pockets

- Choose R-A (driven rotary head) or R-B (gated transport) from the bend test.
- Verify independent position evidence, worst-case move time against the budget,
  and default-to-reject behavior.
- Bench-test pocket stacking candidates for face scuff, stack neatness, and order
  preservation with numbered cards.
- Match head exit nip speed to the transport; show no buckling or drag at handoff.
- Run numbered cards through randomized routes; prove accounting and stable order.
- Test full-pocket pause, chunk replacement, and the 500-card follower force range.

## Milestone 4 — Multipass physical sort

- Extend the tested scan-first planner to the real run manifest.
- Build the operator workflow for labeled pocket collection and reload.
- Prove end-to-end ordering with numbered cards, then with recognized cards.
- Detect sequence mismatches before release; invalidate and reconcile before
  replanning. Test reversed and swapped stacks, missing/extra cards, interruption,
  power loss, rejects, chunk order, and resume.
- Implement graded expected-card verification (second capture, reject and
  continue, stop on contradiction). Measure stops per job and verification false
  accepts on confusable printings; reinsert mid-pass rejects without replanning.
- Measure predictability: estimated versus actual job time, cards per
  intervention, and visits per job. Target: 95% of jobs finish within their
  estimate.
- Time manual sorting and machine-assisted sorting for the same jobs and accuracy
  goal.

## Milestone 5 — Reproducible open-source release

- Integrate only the feeder, transport, router, and pocket interfaces that passed
  their isolated tests.
- Refine printed parts for support-free FDM printing.
- Publish editable CAD, printable files, priced BOM, firmware, desktop software,
  local protocol, assembly instructions, calibration tools, and test fixtures.
- Publish wear-part replacement intervals from endurance data.
- Run builds by people other than the designers and incorporate their feedback.
- Document known limits for sleeves, card formats, finishes, throughput, noise,
  maintenance, and environmental conditions.

## Deferred until evidence supports them

- Automatic recirculation between passes
- Enclosed cosmetic appliance design
- Sleeve universality
- Vacuum or air-assist separation, unless they win the feeder comparison
- Market-price integrations and other network enrichment
- Manufacturing or retail cost targets

None of these should delay proof that the machine can feed one card per slot,
gently and reliably.
