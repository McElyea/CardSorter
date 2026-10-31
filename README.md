# CardSorter

This project explores a reliable, 3D-printable, open-source machine that physically
orders trading cards at a predictable throughput. It is intended to be
reproducible by a hobbyist with a normal FDM printer, commodity purchased
hardware, and an existing computer.

CardSorter is available under the [MIT License](LICENSE). Original code, CAD
designs, printable model exports, and documentation are free to use, modify, and
redistribute, including for commercial use, with the copyright and license notice
preserved. See [licensing details](docs/LICENSING.md) for third-party material.

The primary design is the **R8 reliable sorter**: eight outputs plus reject, with
the card gripped from pickup to pocket and moving at one constant speed.

```text
500-card hopper, constant-force follower
      ↓
pick roller + torque-limited brake roller
      ↓
constant-speed transport nips (thickness + slip sensing)
      ↓
two strobed captures in motion, recognition pipelined
      ↓
indexed router
      ↓
8 pockets + default reject pocket
```

The machine performs a true physical sort, not merely scanning cards or dividing
them into broad categories. Eight outputs are enough because the software orders a
collection over a few planned distribution passes.

## Current status

This repository contains the design record, hobbyist-project research, a tested
sort-planning model, bench-starter printable parts, and a purchased-parts price
estimate. No mechanism has been validated. The first milestone is deliberately
smaller than a full sorter: prove a standalone feeder can deliver exactly one card
per cadence slot, gently, for many thousands of cycles.

The [2026-10-31 reliability rework](docs/reviews/2026-10-31_RELIABILITY_REWORK.md)
made predictable, consistent operation the top priority after card safety. It
replaced the gravity-drop S4 and medium designs with R8. The earlier
[design review](docs/reviews/2026-10-31_DESIGN_REVIEW.md) established scan-first
planned sorting and finite-capacity handling, which R8 keeps.

## Design documents

- [designs/R8_RELIABLE_SORTER.md](designs/R8_RELIABLE_SORTER.md) — primary design
- [DESIGN_PRINCIPLES.md](DESIGN_PRINCIPLES.md) — priorities and engineering rules
- [ARCHITECTURE.md](ARCHITECTURE.md) — topology, timing model, modules, alternatives
- [FEEDER.md](FEEDER.md) — pick/brake roller feeder and comparison candidates
- [SORTING_ALGORITHM.md](SORTING_ALGORITHM.md) — identification and multipass sorting
- [ROADMAP.md](ROADMAP.md) — staged prototypes, beginning with feeder reliability
- [docs/BOM_PRICING.md](docs/BOM_PRICING.md) — purchased-parts price estimate
- [docs/DESIGN_ASSURANCE.md](docs/DESIGN_ASSURANCE.md) — evidence, failure modes, test matrix, and design gates
- [hardware/prototypes/FEEDER_COMPARISON.md](hardware/prototypes/FEEDER_COMPARISON.md) — first physical bench plan
- [hardware/cad/bench-starter](hardware/cad/bench-starter) — first printable parts
- [software/sort_model.py](software/sort_model.py) — reproducible sorting and capacity comparison
- [docs/hobbyist/README.md](docs/hobbyist/README.md) — hobbyist-project research,
  cost barriers, user needs, and engineering lessons
- [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) — where future project work belongs
- [docs/LICENSING.md](docs/LICENSING.md) — project and third-party licensing status

Superseded designs, kept for the record:
[S4 compact](designs/SMALL_SORTER.md),
[S4 unified card path](designs/S4_UNIFIED_CARD_PATH.md), and
[medium radial](designs/MEDIUM_SORTER.md).

## Decision snapshot

- **Purpose:** return the cards themselves in a requested deterministic order.
- **Priority:** card safety and correctness, then predictable throughput and
  positive control. Size and cost are secondary.
- **Outputs:** eight normal pockets plus a default reject pocket, 500-card target.
- **Separation:** pick roller plus torque-limited brake roller; retard pad and
  vacuum remain bench comparisons.
- **Transport:** driven nips from pickup to pocket at one constant speed; no free
  falls.
- **Recognition:** pipelined beside the transport; a late answer sends the card to
  reject. Name and exact-printing accuracy have separate acceptance gates.
- **Health:** slip, signal, and timing trends with cycle-count maintenance.
- **Software:** local/offline-first, with optional network updates and enrichment.
- **Workflow:** scan-first order planning, capacity-aware pocket handling, and
  explicit recovery.
- **Construction:** purchased shafts, bearings, belts, rollers, and extrusion for
  precision; printed brackets and guides; editable CAD.
- **First build:** a standalone, instrumented feeder bench.

## Project areas

| Area | Purpose |
|---|---|
| [designs](designs) | Primary R8 design and superseded alternatives |
| [docs/hobbyist](docs/hobbyist) | Dated research, cost barriers, and source ledger |
| [docs/reviews](docs/reviews) | Design reviews and decision records |
| [hardware](hardware) | CAD, electronics, and physical prototypes |
| [firmware](firmware) | Real-time motor, sensor, and safety control |
| [software](software) | Local recognition, sort planning, and operator interface |
| [tests](tests) | Reliability data, fixtures, simulators, and acceptance results |
| [references/hobbyist-projects](references/hobbyist-projects) | Local third-party research snapshots; not CardSorter source |
