# Single-Card Feeder

Revised 2026-10-31. Feeder selection is open. Use a friction pickup with a retard pad
or roller as the comparison baseline. Stationary vacuum edge peel is a challenger
that must earn its extra pump, valve, tubing, maintenance, and noise.

## Shared requirement

Deliver one card gently to the controlled imaging path, with observable entry,
exit, and double-feed evidence. The first physical work is a common benchtop fixture,
not an integrated sorter. See the
[comparison bench plan](hardware/prototypes/FEEDER_COMPARISON.md).

## Candidates

| Candidate | Separation and handoff | Main tradeoff to measure |
|---|---|---|
| F1 baseline | Soft friction pickup, adjustable retard pad, transport nip | Simple parts; pressure, finish, and wear sensitivity |
| F2 baseline variant | Pickup plus compliant or torque-limited retard roller | Less sliding contact possible; extra calibration and parts |
| V1 challenger | Fixed recessed vacuum shoe, passive retard, roller handoff | Potentially gentler separation; pump, release, dust, and noise cost |

Use the same hopper, card cohort, transport path, sensors, and scoring. Record
adjustments and unsuccessful configurations rather than reporting only each
candidate's best demonstration. A mature paper-feeding principle is a credible
baseline, not proof that it is safe for trading cards.

The vacuum concept remains worth testing: a distributed port draws only a leading
edge into a shallow recess, then a roller takes control and the valve vents. A
1–2 mm recess is an initial experiment variable, not an approved bend or tolerance.
Vacuum does not transport the whole card.

## Presentation and transport

Compare near-vertical and inclined stack presentation, follower force, and empty,
half-full, and full stack loads. Keep shoe, retard, and roller contact surfaces
small and replaceable. A simple coupon fixture should permit adjustments without
reprinting the full chassis.

The one-motor, dual-nip proposal in
[designs/S4_UNIFIED_CARD_PATH.md](designs/S4_UNIFIED_CARD_PATH.md) depends on preventing
the upper pickup from acquiring another card while the lower nip releases the
current card. Vacuum presentation was proposed as that clutch. A friction variant
needs independently demonstrated pickup disengagement, a clutch/lift mechanism,
or a separate pickup drive. Leave the drive interface modular until this is proven.

## Double detection

Compare a compliant follower roller with analog Hall displacement sensing against
a suitable through-transmission ultrasonic double-sheet detector. A generic
ultrasonic distance module is not equivalent.

Evaluate singles, deliberately aligned doubles, offset doubles, different stock,
foils, curl, and later sleeves. Log false accepts, false rejects, calibration drift,
detector cost, and contact damage. Optical edge timing is useful for passage and
skew, but cannot reliably identify perfectly aligned doubles. Vacuum pressure
diagnoses acquisition and leakage; it is not independent proof of a single card.

Industrial precedent supports testing both rollers and ultrasound:
[Ricoh's scanner layout](https://www.pfu.ricoh.com/global/scanners/erg/cleaning-7030.html)
includes pick/brake rollers and ultrasonic sensors. Its
[archived detection conditions](https://www.pfu.ricoh.com/global/scanners/erg/conditions-7030.html)
also describe thickness and material restrictions and false positives on thick
plastic cards. These are reasons to characterize trading-card stock, not to assume
a scanner sensor will work unchanged.

## Common cycle

```text
READY
  -> acquisition enabled (friction pickup or vacuum peel)
  -> leading edge confirmed
  -> transport nip captures card
  -> acquisition disengaged / vacuum vented
  -> double check and trailing edge confirmed
  -> destination passage accounted for
  -> READY
```

Missing, contradictory, early, or late events stop the cycle. Assign one cycle_id
at acquisition; do not start another until the current card is reconciled.

## Selection gate

First establish settings on sacrificial calibration cards, then compare candidates
on held-out cohorts at matched speed and stack conditions. Promote vacuum only if
it provides a repeatable improvement in damage, silent doubles, interventions, or
stock range sufficient to justify measured cost, maintenance, noise, and complexity.
Record the tradeoff before choosing a winner.

The selected configuration must pass the 10,000-cycle ordinary-card milestone with
zero undetected doubles and no observed damage, plus the separately reported
challenge matrix. Detected jams, interventions, retries, and downtime remain visible;
a convenient definition of 'successful cycle' must not erase failures.
