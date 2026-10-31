# S4 Compact Card Sorter

> **Superseded 2026-10-31.** The [reliability rework](../docs/reviews/2026-10-31_RELIABILITY_REWORK.md)
> replaced this gravity-drop design with [R8](R8_RELIABLE_SORTER.md). It stays in
> the record as the small, low-cost alternative and its rationale.

## Status

Compact candidate, to be compared with the medium design on operator effort and
job time. It combines an experimentally selected feeder with one
four-way selector, reusable card cassettes, local recognition, and a dedicated
reject path. No dimensions or mechanical details have been validated.

The detailed cross-layer integration proposal is recorded in
[S4_UNIFIED_CARD_PATH.md](S4_UNIFIED_CARD_PATH.md). The present document remains the
product-level specification; the unified-path document describes how compatible
functions may be combined after their prototype evidence is available.

## Design intent

The S4 is a near-vertical machine with four normal sort destinations plus reject.
Its core should be only modestly larger than the controlled card path. Hopper and
output capacity come from detachable accessories rather than a larger mechanism.

```text
          removable hopper
                 ↓
       friction/retard or vacuum
                 ↓
        soft feed-roller handoff
                 ↓
        thickness/double check
                 ↓
      edge-supported imaging bay
        camera + fixed lighting
                 ↓
       hold until route confirmed
                 ↓
        five-position selector
       ↙       ↓       ↓       ↘   → reject
     bin 0   bin 1   bin 2   bin 3
        keyed removable cassettes
```

## Physical arrangement

The output cassettes should use a compact 2×2 array or shallow fan beneath the
vertical core. The earlier vertically stacked/nested arrangement remains a test
candidate, but it creates shallow-route and access risks. The router should move
only a small entry vane or short edge-supported chute; the fixed guides do the rest.

The earlier aspirational **core engine** envelope of about 100 mm wide × 120 mm
deep × 200 mm tall remains a mechanism-only lower bound. The honest complete-unit
target is approximately 190–220 mm wide × 200–240 mm deep × 300–350 mm tall.
Camera distance, chute angles, card clearances, jam access, and stiffness take
priority over hitting those targets.

Input and output should share one keyed cassette interface. A retaining gate keeps
a group together while it moves between output and hopper positions, and the key
prevents backward insertion. Test, normal, and bulk cassette depths can trade
capacity for size without changing the engine.

Start with 150-, 200-, and 250-card capacity mockups using measured card thickness.
A larger job spans multiple cassettes. Full destinations require a controlled pause
and ordered chunk replacement; each output need not contain the entire job. Count
off-machine cassette staging and operator access in the size comparison.

Printed modules should mount to a short commodity structural datum. A 2040
aluminum-extrusion spine is the leading option because it is straight, adjustable,
and inexpensive; the prototype should establish whether a printed alternative is
good enough.

## Routing mechanism

- One low-mass printed chute, flap, or finger serves all four normal routes.
- A fifth safe route leads to a clearly separate reject magazine.
- The feed roller holds the imaged card until the requested route is confirmed.
- A positional micro-servo may drive the selector, but independent optical position
  evidence is required before release.
- Gravity supplies the card motion through the selector and into the magazine.

Exact output stacking is open. The 2×2, shallow-fan, and stacked candidates should
be compared with cardboard or rough printed mockups before detailed CAD. Chutes
should use narrow ribs, air channels, and replaceable low-friction strips instead
of broad flat printed surfaces.

## Sorting behavior

The preferred exact-sort candidate inventories the observed order, then applies
planned stable four-way distributions. The reproduced random-1,000 example takes
six traversals including scan, versus four for the medium machine. Recursive group
splitting is no longer preferred because it creates excessive operator loads.
Finite capacity adds physical loads within each logical pass; repeated recognition
requires sequence validation and replanning after reload errors.

Reject is not a radix digit. It catches unidentified cards, suspected doubles,
timing faults, and any card that cannot be routed safely. See
[../SORTING_ALGORITHM.md](../SORTING_ALGORITHM.md).

## Strengths

- Smallest retained practical design
- One selector actuator and a short card path
- Roughly half the fixed-radix passes of a binary-only sorter
- Modular capacities and potentially low printed-part count
- Easy to place beside an existing computer
- Keyed cassettes reduce loose handling and reload mistakes

## Risks and open questions

- Does a 2×2 array, shallow fan, or vertical stack offer the best usable footprint?
- Will every output form a neat stack without broad face contact or trapped air?
- Can reject remain fail-safe within the narrow envelope?
- What is the minimum drop height that still routes warped cards consistently?
- Can the keyed cassette gate preserve order and orientation during every reload?
- Is the tiny aspirational core compatible with controlled camera lighting and
  tool-free jam access?

## Prototype after the feeder

Build only the controlled release, selector, four route positions, reject, and
shallow transparent cassettes. Compare the three output geometries with numbered
sacrificial cards. Measure route accuracy, settling, bounce-out, jams, cassette
handling, and worst-case selector travel before designing the enclosure.

The feeder itself is shared with the medium sorter and remains the first project
milestone. See [../FEEDER.md](../FEEDER.md) and [../ROADMAP.md](../ROADMAP.md).
