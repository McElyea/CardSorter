# Medium Card Sorter

> **Superseded 2026-10-31.** The [reliability rework](../docs/reviews/2026-10-31_RELIABILITY_REWORK.md)
> replaced this gravity-drop radial design with [R8](R8_RELIABLE_SORTER.md), which
> keeps its eight outputs and radial layout but drives each card into its pocket.

## Status

Retained design; preferred when reducing sort passes is worth a larger desktop
footprint. No dimensions or mechanical details have been validated.

Following the 2026-10-31 review, evaluate this alongside S4 on completed-job time,
operator visits, active human minutes, and cassette staging area. It shares the
friction/retard baseline and vacuum comparison with the small model.

## Design intent

The medium sorter keeps the same compact vertical feed and imaging column as the
small design, but places eight removable wedge-shaped output bins around one rotary
selector. It avoids both an XY gantry and a long row of conveyor gates.

```text
              removable hopper
                     ↓
           tested single-card separator
                     ↓
              feed-roller handoff
                     ↓
           sensors + camera/lighting
                     ↓
               gravity drop
                     ↓
            light rotary selector

                     [0]
                [7]       [1]
             [6]     core    [2]       + reject
                [5]       [3]
                     [4]

             removable radial wedge bins
```

The design discussion used roughly 250 × 250 × 400 mm as an initial overall size
target. The output bins will dominate the footprint and their useful capacity may
force a larger base. The target should remain provisional until full-size card
mockups establish real chute and access clearances.

## Physical arrangement

- Hopper, feeder, camera, and short drop path form a central vertical column.
- A small servo or stepper rotates only a lightweight selector, not a card stack.
- Eight wedge-shaped magazines pack radially around or below the selector.
- Each magazine is individually removable; changing capacity should alter magazine
  depth/height rather than the shared engine.
- Printed segments should fit a 220 × 220 mm bed. The base may assemble from keyed
  sections if a single printable part would violate that constraint.

## Reject route

The earlier medium concept requires eight normal outputs plus reject, but the exact
reject geometry was not resolved. It must be designed explicitly rather than
quietly consuming one of the eight radix bins. Candidates for testing are:

1. A small ninth catch pocket at a default/fail-safe selector position.
2. A straight-through or overflow path separate from the radial ring.
3. Stop-before-drop behavior for faults detected early enough, backed by a physical
   reject route for late or uncertain cases.

The chosen implementation must not enlarge or complicate the machine enough to
erase the advantage of the radial design.

## Sorting behavior

The eight bins support scan-first planned stable distributions and dense-rank
radix fallback. For the reproduced random-1,000 job, scan plus routing takes four
traversals versus S4's six. For sorted 2,000 plus 100 newcomers, it takes four
versus five. Savings depend on the observed order and key definition.

The eight-way design therefore reduces collection/reload work and total card
handling. It still provides full deterministic ordering rather than merely eight
permanent categories. See [../SORTING_ALGORITHM.md](../SORTING_ALGORITHM.md).

Use the same 150–250-card capacity candidates and ordered overflow replacement
rules as S4. Eight routes can reduce output pressure, but do not extend a fixed
input hopper's refill interval. Name-level and exact-printing jobs have separate
recognition gates.

## Strengths

- Fewer card traversals for many jobs; quantify using the actual order
- One light selector instead of eight independently powered gates
- Short, mostly gravity-driven card path
- Dense output arrangement compared with a linear eight-bin conveyor
- Shared feeder, imaging, controller, and software with the small model

## Risks and open questions

- What bin capacity is possible before the radial base becomes too wide?
- Can every bin be removed without disturbing neighbors or the central engine?
- Do wedge bins form clean card stacks at all eight approach angles?
- Can one selector reach worst-case positions inside the available card interval?
- Where should the dedicated fail-safe reject path live?
- Does the circular base print as a single part or reliable keyed segments?
- Is the reduced pass count valuable enough in real workflows to justify the
  increased footprint and part count?

## Prototype after the feeder

Start with a flat routing demonstrator: the rotary selector, eight shallow wedge
bins, and a temporary reject catcher. Drop numbered sacrificial cards from a fixed
height at the intended cadence. Measure route accuracy, settling, bounce-out,
order preservation, selector travel time, and access for clearing failures.

Compare those measurements directly with the small four-way prototype before
committing to detailed enclosure CAD. The feeder is shared and remains the first
project milestone. See [../FEEDER.md](../FEEDER.md) and
[../ROADMAP.md](../ROADMAP.md).
