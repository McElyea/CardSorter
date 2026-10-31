# Reliability Rework — 2026-10-31

## Author direction

The author asked whether the September/October design was the best available and
stated the goal directly: a machine that is **reliable, with predictable
throughput, consistent, and dependable**. The author then directed that the design
documents be reworked around that goal, and that a priced list of all purchased
(not printed) parts be added.

Everything below the author direction is an editorial proposal adopted as the
working design direction. None of it is validated; each item carries a test.

## Finding

The previous design ranked compactness second and "gravity before motors" sixth.
Those choices are cheap and small, but they trade away the properties the author
asked for:

- **Free gravity drops** make timing and landing depend on curl, finish, static,
  and humidity. GlideSorter's sticking cards are the documented example.
- **Stop-for-capture** makes throughput depend on how quickly the host answers,
  so cycle time varies with recognition latency.
- **Small cassettes** (150–250 cards) put the operator in the loop every few
  minutes, which is the largest source of job-time variation.

## Adopted direction

| Topic | Before | After |
|---|---|---|
| Priorities | Safety, then compactness; minimum mechanism | Safety and correctness, then predictable throughput and positive control; size and cost secondary |
| Card control | Rollers to imaging, then gravity drop | Card gripped by driven contact from pickup until it is in its output |
| Motion | Stop, capture, wait for recognition, release | Constant transport speed, fixed cadence, capture in motion |
| Recognition | In the control loop | Pipelined; a late answer sends the card to reject |
| Feeder | Friction/retard vs vacuum, open | Pick roller plus torque-limited brake roller expected; retard pad and vacuum remain comparisons |
| Stack presentation | Spring or gravity follower | Constant-force follower (or motorized lift with top-of-stack sensing) |
| Outputs | 4-way primary candidate, 8-way co-equal | 8 normal outputs plus reject is the primary design |
| Capacity | 150–250-card cassettes | 500-card hopper and pockets as the target |
| Structure | Printed modules on a 2040 spine | Shafts, bearings, belts, urethane rollers, and extrusion for every datum and card contact; printed brackets and guides |
| Health | Fault logging | Slip encoder, signal trends, reference card, cycle-count maintenance |
| Metrics | Cards/hour, operator minutes | Fixed cadence adherence, cards per intervention, job-time estimate accuracy |

The primary design is now [designs/R8_RELIABLE_SORTER.md](../../designs/R8_RELIABLE_SORTER.md).
The S4, S4 unified path, and medium radial documents are retained as superseded
alternatives, per the rule that failed or paused ideas stay in the record.

## What stays

Safety invariants, `cycle_id` accounting, firmware safety authority, offline host
recognition, scan-first stable planning (with its verification and reject rules),
the feeder-first milestone, the CAD format rule, the MIT license, and the
bench-starter fit coupon.

## Costs accepted

- **Size:** nine 500-card pockets around a rotary router suggest roughly
  450–500 mm diameter and about 500 mm height. 250-card pockets would shrink this
  to roughly 350 mm. These are layout estimates, not dimensions.
- **Mechanisms:** four stepper motors (transport, pickup, router head, head exit
  nip) instead of two, plus constant-force springs and linear guides per pocket.
- **Money:** purchased parts estimate about $822–1,309 for the full machine and
  about $333–557 for the first feeder bench, before tax and shipping. See
  [../BOM_PRICING.md](../BOM_PRICING.md).
- **Visit interval:** a faster fixed cadence empties a hopper sooner. At 1 card/s,
  a 500-card hopper lasts about 8 minutes. Jobs finish much sooner, but the machine
  is still not unattended. Automatic recirculation is deferred.

## Open gates

1. **Card bend tolerance** decides between the driven rotary head (R-A) and a
   gated transport with fail-safe default-to-reject (R-B).
2. **Output stacking without face scuffing** has no chosen mechanism.
3. **Speed matching** between the transport and the head exit nip must not buckle
   or drag a card.
4. **Cadence target** of 1 card/s is a test target, not a claim.
5. **Pick timing jitter** must be small enough to hold the cadence slot.

See [../../ROADMAP.md](../../ROADMAP.md) for where each gate is tested.
