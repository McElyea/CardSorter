# Single-Card Feeder

Revised 2026-10-31 by the [reliability rework](docs/reviews/2026-10-31_RELIABILITY_REWORK.md).
The expected feeder is a pick roller with its own drive plus a torque-limited brake
roller, fed by a constant-force stack follower. A retard pad and stationary vacuum
edge peel remain comparisons; each must beat the expected feeder to replace it.

## Requirement

Deliver exactly one card per cadence slot into the transport, gently, with a
repeatable pick time and observable entry, exit, thickness, and slip evidence.
The first physical work is a benchtop fixture, not an integrated sorter. See the
[comparison bench plan](hardware/prototypes/FEEDER_COMPARISON.md).

Predictability is part of the requirement: the time from pick command to the card
reaching the first transport nip must vary little enough that the card lands in
its cadence slot every time.

## Candidates

| Candidate | Separation and handoff | Main tradeoff to measure |
|---|---|---|
| **F2 expected** | Pick roller plus brake roller on a torque limiter, then transport nip | The standard of high-reliability sheet feeders; brake roller sourcing and fit |
| F1 comparison | Pick roller plus adjustable retard pad | Fewer parts; more sensitive to pressure, finish, and wear |
| V1 comparison | Fixed recessed vacuum shoe, passive retard, roller handoff | Possibly gentler; pump, valve, dust, and noise cost |

How the brake roller works: it sits against the pick roller on a torque limiter.
With one card between them, friction from the moving card exceeds the limiter and
the brake roller turns with it. With two cards, card-to-card friction is lower than
the limiter, so the brake roller holds the second card back. It tolerates variation
in thickness and friction better than a fixed gap.

Aftermarket scanner pick/brake roller sets (for example, those for Fujitsu/Ricoh
fi-7000-series scanners) are the first source to test. They include the torque
limiter but will need printed adapters. Record fit, wear, and limiter torque.

Use the same hopper, card cohort, transport path, sensors, and scoring for every
candidate. Record adjustments and unsuccessful configurations, not only each
candidate's best demonstration. A mature paper-feeding principle is a credible
starting point, not proof that it is safe for trading cards.

## Stack presentation

| Option | How | Tradeoff |
|---|---|---|
| **P1 expected** | Constant-force spring follower on linear guides | Same force full or empty; guide friction must stay low |
| P2 alternative | Motorized lift with a top-of-stack sensor | Force set by control; one more motor and sensor |

Measure pick force and pick time at one card, half full, and full. An ordinary
compression spring or gravity follower changes force by two orders of magnitude
across a 500-card stack and is not acceptable for the expected design.

## Pickup drive

The pick roller has its own stepper and runs only during a cadence slot. This
replaces the earlier one-motor dual-nip proposal, which needed vacuum as a clutch.
The pick roller must stop or freewheel once the first transport nip captures the
card, so it never pulls the next card early.

## Double detection

The Hall-sensed idler is the default detector: a magnet on the first transport
idler arm and an analog Hall sensor measure displacement, which tracks thickness.
A through-transmission ultrasonic double-sheet detector is an optional bench
comparison. Industrial units cost roughly $285–1,520 (see
[docs/BOM_PRICING.md](docs/BOM_PRICING.md)), so it joins the design only if the
Hall sensor fails the challenge matrix. A generic ultrasonic distance module is not
equivalent.

Evaluate singles, deliberately aligned doubles, offset doubles, different stock,
foils, curl, and later sleeves. Log false accepts, false rejects, calibration drift,
and contact damage. Optical edge timing is useful for passage and skew, but cannot
reliably identify perfectly aligned doubles.

Industrial precedent supports both the brake roller and ultrasound:
[Ricoh's scanner layout](https://www.pfu.ricoh.com/global/scanners/erg/cleaning-7030.html)
includes pick/brake rollers and ultrasonic sensors. Its
[archived detection conditions](https://www.pfu.ricoh.com/global/scanners/erg/conditions-7030.html)
also describe thickness and material restrictions and false positives on thick
plastic cards. These are reasons to characterize trading-card stock, not to assume
a scanner part will work unchanged.

## Slip and wear

An AS5600 magnetic encoder on an undriven transport idler measures how fast cards
actually move. Compare it with commanded motor speed on every cycle. Rising slip is
the early warning for roller wear or contamination; set a maintenance threshold
from bench data.

## Cycle

```text
SLOT
  -> pick roller on
  -> leading edge at first nip (pick time recorded)
  -> transport nip captures card; pick roller off
  -> thickness accepted; slip recorded
  -> trailing edge clears feeder
  -> card handed to transport with its cycle_id
NEXT SLOT
```

A missing, contradictory, early, or late event stops the cycle. A pick that misses
its slot is retried in the next slot and logged as a skipped slot. Assign one
`cycle_id` at pick; never start another pick until the current card is accounted
for.

## Selection gate

Establish settings on sacrificial calibration cards, then compare candidates on
held-out cohorts at matched speed and stack conditions. Score damage, silent
doubles, interventions, pick-time spread, skipped slots, stock range, maintenance,
cost, and noise. Replace F2 only with a candidate that is repeatably better on
safety or predictability.

The selected configuration must pass the 10,000-cycle ordinary-card milestone with
zero undetected doubles and no observed damage, plus the separately reported
challenge matrix. Detected jams, interventions, retries, and skipped slots remain
visible; a convenient definition of "successful cycle" must not erase failures.
