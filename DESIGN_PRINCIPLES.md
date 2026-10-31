# Design Principles

Revised 2026-10-31 by the [reliability rework](docs/reviews/2026-10-31_RELIABILITY_REWORK.md):
predictable, consistent, dependable operation now outranks compactness and
minimum mechanism.

## Product definition

The project is a **sorter**: it changes the physical order of a collection. A
scanner identifies cards, and a sifter divides cards into categories, but neither
alone satisfies the goal.

A successful machine should accept a mixed stack, identify each card, guide the
operator through any required reloading between passes, and eventually return the
cards in a requested order such as set then collector number or alphabetical by
name. It should do so at a throughput an owner can predict before starting a job.

## Priorities

1. **Card safety and correctness.** No damage, no silent doubles, no card in a
   wrong known-good output. These outrank every other goal.
2. **Predictable throughput.** Run at a fixed cadence. A job's duration should be
   estimable from its card count and plan, and interventions should be counted.
3. **Positive control.** A card is held by driven contact from pickup until it is
   in its output. No free falls, and no broad surfaces that a card must slide over
   under gravity.
4. **Operator attention.** Minimize visits per job and maximize cards between
   visits. Raw cards/hour alone does not measure usefulness.
5. **Offline ownership.** Core feeding, recognition, routing, and sorting must
   continue without an account, subscription, or Internet connection.
6. **Serviceability and observability.** Wear parts have a stated life and swap
   without tools. The machine measures its own drift (slip, signals, timing) and
   asks for maintenance before failure.
7. **Reproducibility.** A hobbyist should be able to print, source, assemble,
   repair, and modify the machine without proprietary manufacturing.
8. **Modularity.** Feeder, transport/imaging, router, and storage are independently
   replaceable and testable.
9. **Size and cost.** Secondary. Spend size, parts, and money where they buy
   consistency, and record what each choice costs.

A mechanism earns its place when it removes variation or protects a card. Prefer
binary or fail-safe actuators, and give every actuator independent position
evidence. Friction feed with a brake roller is the expected separator; vacuum must
win a comparison to return. Exact-printing identification is a separate risk from
feeding and from name recognition.

## Mechanical rules

- Use purchased steel shafts, bearings, belts, and urethane rollers for every
  datum and every card-contact drive surface. Printed parts are brackets, guides,
  covers, and test coupons.
- Space transport nips closer than the card's length in the travel direction so a
  card is always held by at least one nip.
- Keep the card path straight where possible. No bend tighter than the validated
  minimum radius for card stock (see the bend test in
  [docs/DESIGN_ASSURANCE.md](docs/DESIGN_ASSURANCE.md)).
- Present the stack with constant force regardless of how full it is.
- Design routine printed parts for common FDM printers with a build area no larger
  than 220 × 220 mm. Any exceptional larger part must be segmented and keyed.
- Prefer support-free parts, a 0.4 mm nozzle, PLA/PETG, loose and documented
  tolerances, and orientations that do not put critical surfaces on supports.
- Publish native parametric source and STEP in addition to printable STL and
  print-ready 3MF files. See [hardware/cad/README.md](hardware/cad/README.md).
- Minimize unique fasteners and use common items such as M3 screws, heat-set
  inserts, readily available bearings, and commodity motors.
- Make wear surfaces and card-contact parts removable, with a stated replacement
  interval in cycles.
- Provide easy access for clearing a jam without bending or dragging a card.
- Keep the core independent of hopper and pocket capacity.
- A card enters the router only after the route position is independently
  confirmed. Otherwise it goes to the default reject route, or the transport stops
  with the card held.

## Electronics and software rules

- Separate real-time motion/sensor control from card recognition and sort planning.
- Let a microcontroller own actuators, interlocks, cadence, and card-state events.
- Let a USB-connected host computer run vision, the local card database, the sort
  plan, and the operator interface. An embedded computer may be offered but must
  not be mandatory.
- Keep recognition out of the timing loop: the host answers within a deadline or
  the card goes to reject. Host latency must never change the cadence.
- Define a documented local protocol so Windows, Linux, a Raspberry Pi, a mini PC,
  or another capable host can drive the sorter.
- Treat network services as optional sources for database updates, prices, and
  metadata. Loss of the network must not disable the physical machine.
- Fail safe: an unidentified card, conflicting sensor state, or late route command
  goes to reject or stops the transport with every card held.
- Log health signals (slip, double-detect signal, timing, retries) per cycle and
  trend them across jobs.

## Scope discipline

The initial design should establish a reliable path for ordinary unsleeved trading
cards. Warped foils, finishes, dust, static, different stock, and common sleeve
types belong in the test matrix, but universal compatibility must not obscure the
first goal: repeatable single-card feeding at a steady cadence with no damage.

Recognition is not the first engineering risk. The hardest reusable problem is
separating one card from a real stack, repeatedly and on time, despite curl,
adhesion, wear, contamination, and dimensional variation.
