# Feeder Comparison Bench

Status: experiment plan, revised 2026-10-31 for the
[reliability rework](../../docs/reviews/2026-10-31_RELIABILITY_REWORK.md). No fixture
has been built and no physical results are claimed.

## Question

Does a pick roller with a torque-limited brake roller, fed by a constant-force
follower, deliver exactly one card per cadence slot with a repeatable pick time and
no damage? Do a retard pad or stationary vacuum edge peel do better on safety or
predictability? Use [FEEDER.md](../../FEEDER.md) as the shared requirement.

## First physical build

Mount the feeder to a short length of 2020 extrusion or a rigid scrap base, with a
cardboard or printed hopper. Use small printed coupons only where geometry must be
repeatable. Establish the card path with sacrificial cards before detailed sorter
CAD. Purchased parts for this bench are priced in
[../../docs/BOM_PRICING.md](../../docs/BOM_PRICING.md).

Common fixtures and measurements:

- Constant-force follower on two 8 mm rods with measured force at empty, half,
  and full; adjustable stack angle and edge guides
- Pick roller on its own stepper; first transport nip on a second stepper
- Brake roller mount (scanner aftermarket set with printed adapter) and a retard
  pad mount
- Interchangeable vacuum-shoe mount; add pump, vent valve, and pressure sensing
  only for vacuum trials
- Hall sensor and magnet on the first idler arm; AS5600 encoder on an undriven idler
- Beam sensors at the feeder exit and after the first nip, with a card-count and
  timing log
- Independently observed single/double ground truth, using video plus physical
  counts and deliberately injected doubles; do not score a detector using itself
- Magnified before/after inspection under fixed lighting and marked card IDs
- Emergency stop and accessible pinch points

## Candidate order

1. F2: pick roller plus torque-limited brake roller (expected).
2. F1: pick roller plus adjustable retard pad.
3. V1: fixed vacuum edge peel, retard, and roller handoff.

Presentation: run F2 with the constant-force follower (P1) first. Try the motorized
lift (P2) only if P1 shows force or pick-time drift across the stack.

Keep card cohorts, transport speed, capacity, and scoring common. Tune on a separate
calibration cohort; lock and record settings before evaluation. Alternate candidate
order and use matched sacrificial cohorts so wear from one method does not bias the
next. Log changes, cleaning, and failed trials.

## Experiment stages

| Stage | Work | Gate |
|---|---|---|
| Geometry | Hand-feed numbered cards; inspect force, bend, and access | Continuous control and recoverable jams |
| Calibration | Set pick speed, brake torque or pad force, follower force | Repeatable documented settings |
| Screen | At least 200 attempts per candidate at 1-card, half, and full loads | Every attempt classified; no observed damage |
| Cadence | Pick on a fixed slot at the target rate | Pick-time spread fits inside the slot; skipped slots logged |
| Challenge | Mixed stock, wear, curl, foils; aligned/offset injected doubles | Report miss and false-reject rates by cohort |
| Endurance | Selected unchanged configuration, 10,000 ordinary-card cycles | Roadmap criteria, complete intervention log, slip trend |

Screening counts find defects cheaply; they are not reliability claims. Reject
damaging settings immediately and document them. Extend the challenge cohort based
on observed failure modes. Sleeves require a separate profile and evaluation.

## Detector comparison

The Hall-sensed idler is the default. Record its raw signal for known singles and
doubles; select thresholds on calibration data only and evaluate on held-out cards.
Add a through-transmission ultrasonic sheet detector only if the Hall sensor misses
aligned doubles or false-rejects thick singles in the challenge stage; a
distance-ranging ultrasonic module is not an equivalent substitute.

## Log and decision

Each run records fixture revision, settings, card cohort, measured thickness range,
hopper load, environmental conditions, `cycle_id`, pick time, slip, raw Hall values,
ground-truth card count, detected faults, skipped slots, human interventions,
damage, and cleaning. Report attempts and failed attempts, not only completed feeds.

Compare parts cost, setup minutes, active human minutes, cards between
interventions, pick-time spread, downtime, noise under one measurement method, and
wear. A phone sound-level reading can compare trials but should not be presented as
a calibrated absolute noise rating.

All candidates must meet the same damage and silent-double requirements. Keep F2
unless another candidate is repeatably better on safety or predictability. Record
the selection rationale and uncertainty explicitly.

## Capacity mockup alongside the bench

Print the [stack gauges](../cad/bench-starter) and measure your stock's real card
thickness. The R8 target is 500 cards per hopper and pocket; add 500 to
`CAPACITIES` in the generator to print a 500-card gauge. Time loading, removing,
and combining pocket stacks in route order.

The person building this fixture must supply the physical hardware and results;
the repository currently contains the experiment plan and mathematical model only.
