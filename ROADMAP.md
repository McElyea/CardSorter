# Roadmap

The roadmap retires the highest-risk assumptions first. Dates, enclosure styling,
and production cost estimates should wait until real feed-cycle data exists.

Revision 2026-10-31: use the [design review](docs/reviews/2026-10-31_DESIGN_REVIEW.md)
and [comparison bench plan](hardware/prototypes/FEEDER_COMPARISON.md). The software
model is tested; hardware, recognition, and operator timing remain unvalidated.

## Milestone 0 — Standalone single-card feeder

Build an instrumented benchtop comparison using a cardboard hopper and small
replaceable coupons: friction pickup with retard pad/roller first, then stationary
vacuum edge peel on the same transport path. It does not identify or sort cards.

### Required work

- Create adjustable, printable stack presentation and card guides.
- Compare friction/retard settings with vacuum-shoe hole patterns and compliance.
- Share feed rollers and entry/exit sensors; add pump/vent only for vacuum trials.
- Compare Hall idler displacement with suitable ultrasonic double-sheet detection.
- Prove pickup disengagement during lower-nip motion before choosing one shared
  drive; record the added parts required by each feeder candidate.
- Implement the feeder state machine, interlocks, fault stop, and cycle log.
- Make card-contact points visible, cleanable, and quick to change.
- Establish a test matrix spanning ordinary cards, representative curl and wear,
  foils, contamination/static conditions, and eventually common sleeves.

### Exit criteria

- Exactly one card is accounted for on every completed cycle.
- A missing card, double, stall, or abnormal timing stops safely and is logged.
- No visible edge, face, or corner damage appears under a documented inspection
  method.
- The rig completes 10,000 consecutive ordinary-card cycles with zero undetected
  doubles, zero unrecovered jams, and zero observed damage.
- Demonstrate sustained 1,200 cards/hour after reliability is achieved; treat
  1,500–1,800 cards/hour as an optimization target, not permission to weaken the
  reliability criteria.
- Publish test data and failure examples, not only a successful demonstration.
- Select a feeder using damage, silent doubles, interventions, maintenance, cost,
  and noise. Report attempted feeds and failures as well as successful cycles.

## Milestone 1 — Controlled imaging path

- Attach the selected feeder to a controlled, stop-for-capture camera channel.
- Add repeatable lighting and sensor-triggered capture.
- Prove that every physical card produces exactly one usable image and that all
  sensor events reconcile with the feeder log.
- Route every card to one temporary output; recognition may still be mocked.

## Milestone 2 — Local identification

- Build the local database, recognition pipeline, and confidence thresholds.
- Validate name recognition and exact-printing recognition separately on held-out
  physical cards. Include same-art reprints, absent identifiers, old layouts,
  languages, promos, and foils. Report false accepted identities and rejects.
- Keep exact-printing jobs gated until sufficient evidence supports them; offer
  explicit name-only jobs without claiming printing-level correctness.
- Send uncertain, duplicate-image, and unreadable cases to a logical reject result.
- Keep recognition replaceable so mechanical progress is not tied to one model or
  data provider.

## Milestone 3 — Routing prototypes and design review

- Prototype the S4 small sorter's low-inertia selector with four normal positions
  and reject. Compare a compact 2×2 cassette array, a shallow fan, and the earlier
  stacked/nested arrangement using the same release point.
- Compare the medium sorter's eight-position geometry alongside the four-way
  workflow using the same feeder, cassette capacity, and job sets; establish its
  dedicated reject implementation. Simulation and cardboard layout can precede
  detailed selector construction.
- Verify homing/position feedback, route timing, passive card entry, and jam access.
- Run numbered cards through randomized routes and prove output accounting and
  stable arrival order.
- Measure all small-output candidates and the medium radial wedge bins against the
  same criteria: footprint including staging, capacity, operator visits and active
  time, printability, access, reload errors, selector timing, and card damage.
  Test the common cassette interface and pause-before-full replacement protocol.
- Record a design review. Continue both if they serve meaningfully different use
  cases; otherwise explain which design is paused and why rather than deleting it.

## Milestone 4 — Multipass physical sort

- Extend the tested scan-first order planner to the real run manifest, with dense
  ranks as a baseline and recursive distribution only for justified niche jobs.
- Build the operator workflow for labeled-bin collection and reload.
- Prove end-to-end ordering first with numbered cards, then with recognized cards.
- Detect sequence mismatches before release; invalidate and reconcile before
  replanning. Test reversed and swapped cassettes, missing/extra cards, interruption,
  power loss, rejects, chunk order, and resume.
- Implement graded expected-card verification (re-image, reject and continue,
  stop on contradiction). Measure stops per job and verification false accepts on
  confusable printings; reinsert mid-pass rejects without replanning the job.
- Time manual sorting and machine-assisted sorting for the same jobs and accuracy
  goal, counting every scan, visit, reload, overflow, recovery, and verification.

## Milestone 5 — Reproducible open-source release

- Integrate only the feeder, imaging, routing, and cassette interfaces that have
  passed their isolated tests; follow
  [designs/S4_UNIFIED_CARD_PATH.md](designs/S4_UNIFIED_CARD_PATH.md) without erasing
  independent safety evidence.
- Refine the core for support-free FDM printing and commodity hardware.
- Publish editable CAD, printable files, BOM, firmware, desktop software, local
  protocol, assembly instructions, calibration tools, and test fixtures.
- Offer modular hopper/output capacities without changing the sorting engine.
- Run builds on multiple printers by people other than the designers and incorporate
  assembly and tolerance feedback.
- Document known limits for sleeves, card formats, finishes, throughput, noise,
  maintenance, and environmental conditions.

## Deferred until evidence supports them

- Enclosed cosmetic appliance design
- Maximum-capacity magazines
- Sleeve universality
- Air-assist separation
- Parallel/pipelined feeding for peak throughput
- Market-price integrations and other network enrichment
- Manufacturing or retail cost targets

These are useful directions, but none should delay proof that the machine can feed
one card gently and reliably.
