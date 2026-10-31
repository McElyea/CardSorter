# Feeder Comparison Bench

Status: experiment plan, 2026-10-31. No fixture has been built and no physical
results are claimed. Feeder selection is deliberately open.

## Question

Does stationary vacuum edge peel improve card safety and useful uninterrupted
running enough to justify its added hardware compared with friction/retard feed?
Use [FEEDER.md](../../FEEDER.md) as the shared requirement.

## First physical build

Make a cardboard or simple sheet-material hopper with an adjustable follower,
mounted to a rigid scrap base. Use small printed coupons only where geometry must
be repeatable. Establish the full card path with sacrificial cards before detailed
sorter CAD.

Common fixtures and measurements:

- Adjustable stack angle, edge guides, and measured follower force
- Soft driven pickup/transport rollers with accessible pinch points and stop button
- Replaceable retard pad and roller mounts
- Interchangeable vacuum-shoe mount; add pump, vent valve, and pressure sensing
  only for the vacuum trials
- Entry/exit beams and a card-count/event log
- An independently observed single/double ground truth, using video plus physical
  counts and deliberately injected doubles; do not score a detector using itself
- Magnified before/after inspection under fixed lighting and marked card IDs
- Space for Hall displacement and ultrasonic transmitter/receiver measurements

## Candidate order

1. F1: friction pickup and adjustable retard pad.
2. F2: same fixture with a compliant or torque-limited retard roller.
3. V1: fixed vacuum edge peel, retard, and roller handoff.

Keep card cohorts, transport speed, capacity, and scoring common. Tune on a separate
calibration cohort; lock and record settings before evaluation. Alternate candidate
order and use matched sacrificial cohorts so wear introduced by the first method
does not bias later methods. Log changes, cleaning, and failed trials.

## Experiment stages

| Stage | Work | Gate |
|---|---|---|
| Geometry | Hand-feed numbered cards; inspect force, bend, and access | Continuous control and recoverable jams |
| Calibration | Establish pickup/retard force and timing per candidate | Repeatable documented settings |
| Screen | At least 200 attempts per candidate at 1-card, half, and full loads | Every attempt classified; no observed damage |
| Challenge | Mixed stock, wear, curl, foils; aligned/offset injected doubles | Report miss and false-reject rates by cohort |
| Integration | Release lower nip while acquisition is disabled | No unsolicited next-card pickup |
| Endurance | Selected unchanged configuration, 10,000 ordinary-card cycles | Roadmap criteria and complete intervention log |

Screening counts are a way to find defects cheaply, not reliability claims. Reject
damaging settings immediately and document them. Extend the challenge cohort based
on observed failure modes. Sleeves require a separate profile and evaluation.

## Detector comparison

Use the same known singles and doubles for the Hall-sensed idler and a suitable
through-transmission ultrasonic sheet detector. Record raw signal distributions
and select thresholds using calibration data only. Evaluate on held-out cards.

Measure aligned and offset doubles, foil/stock variation, drift after cleaning,
and contact damage. Characterize single-card false rejects as carefully as missed
doubles. A distance-ranging ultrasonic module is not an equivalent substitute.

## Log and decision

Each run records fixture revision, settings, card cohort, measured thickness range,
hopper load, environmental conditions, cycle_id, timing, raw detector values,
ground-truth card count, detected faults, human interventions, damage, and cleaning.
Report attempts and failed attempts, not only completed feeds.

Compare total parts cost, setup minutes, active human minutes, cards between
interventions, downtime, noise under one measurement method, and wear. A simple
phone sound-level reading can compare trials but should not be presented as a
calibrated absolute noise rating.

Both candidates must meet the same damage and silent-double requirements. Prefer
the simpler mechanism when their practical performance is comparable. Adopt
vacuum only after a repeatable, documented benefit warrants the added burden.
No exact improvement threshold is set before baseline data exists; record the
selection rationale and uncertainty explicitly.

## Capacity mockup alongside the bench

Build physical 150-, 200-, and 250-card stack gauges from measured stock. Include
follower travel, wall thickness, curl, removal access, and staging space. Time
loading, removing, labeling, and concatenating cassettes. Compare a 200-card visit
interval with the actual interruptions caused by the feeder and full outputs.

The person building this fixture must supply the physical hardware and results;
the repository currently contains the experiment plan and mathematical model only.
