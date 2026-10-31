# Design Principles

## Product definition

The project is a **sorter**: it changes the physical order of a collection. A
scanner identifies cards, and a sifter divides cards into categories, but neither
alone satisfies the goal.

A successful machine should accept a mixed stack, identify each card, guide the
operator through any required reloading between passes, and eventually return the
cards in a requested order such as set then collector number or alphabetical by
name.

## Priorities

1. **Reliability and card safety.** One-card separation, jam handling, and gentle
   contact matter more than headline speed or recognition features.
2. **Compactness.** Spend vertical space before desk area. Keep the sorting engine
   close to card-sized and let detachable storage determine capacity.
3. **Reproducibility.** A hobbyist should be able to print, source, assemble,
   repair, and modify the machine without proprietary manufacturing.
4. **Offline ownership.** Core feeding, recognition, routing, and sorting must
   continue without an account, subscription, or Internet connection.
5. **Modularity.** Feeder, imaging stage, selector, hopper, and output magazines
   should be independently replaceable and testable.
6. **Minimum mechanism.** Make gravity and passive geometry do work before adding
   motors, belts, axes, or precision parts.
7. **Operator attention.** Compare active human minutes, completed jobs, and cards
   between required visits. Raw cards/hour alone does not measure usefulness.

Friction/retard is the feeder baseline; added vacuum hardware requires comparative
evidence. Exact-printing identification is a separate product risk from feeding
and from name recognition. The four- and eight-output variants must both be judged
using the same finite-capacity workflow.

## Mechanical rules

- Design routine parts for common FDM printers with a build area no larger than
  220 × 220 mm. Any exceptional larger part must be segmented and keyed.
- Prefer support-free parts, a 0.4 mm nozzle, PLA/PETG, loose and documented
  tolerances, and orientations that do not put critical surfaces on supports.
- Publish native parametric source and STEP in addition to printable STL and
  print-ready 3MF files. See [hardware/cad/README.md](hardware/cad/README.md).
- Minimize unique fasteners and use common items such as M3 screws, heat-set
  inserts, readily available bearings, silicone tubing, and commodity motors.
- Make wear surfaces and card-contact parts removable and inexpensive to replace.
- Avoid calibration that depends on a precision-machined frame.
- Provide easy access for clearing a jam without bending or dragging a card.
- Keep the core independent of hopper and bin capacity. Offer interchangeable
  small, normal, and bulk magazines instead of scaling the whole machine.
- Prefer a common keyed cassette interface for input and output so cards do not
  need to be loose-handled between sorting passes.
- Release a card from the controlled imaging path only after the requested route
  has independent position confirmation.

## Electronics and software rules

- Separate real-time motion/sensor control from card recognition and sort planning.
- Let a small microcontroller own actuators, interlocks, and card-state events.
- Let a USB-connected host computer run vision, the local card database, the sort
  plan, and the operator interface. An embedded computer may be offered but must
  not be mandatory.
- Define a documented local protocol so Windows, Linux, a Raspberry Pi, a mini PC,
  or another capable host can drive the sorter.
- Treat network services as optional sources for database updates, prices, and
  metadata. Loss of the network must not disable the physical machine.
- Fail safe: an unidentified card, conflicting sensor state, or late route command
  goes to reject or stops the feed rather than entering a known-good bin.

## Scope discipline

The initial design should establish a reliable path for ordinary unsleeved trading
cards. Warped foils, finishes, dust, static, different stock, and common sleeve
types belong in the test matrix, but universal compatibility must not obscure the
first goal: repeatable single-card feeding with no damage.

Recognition is not the first engineering risk. The hardest reusable problem is
separating one thin card from a real stack, repeatedly, despite curl, adhesion,
wear, contamination, and dimensional variation.
