# CardSorter

This project explores a compact, 3D-printable, open-source machine that physically
orders trading cards. It is intended to be reproducible by a hobbyist with a
normal FDM printer, commodity hardware, and an existing computer.

Two physical designs are being retained for development. They share the same
feeder, imaging stage, electronics, and local software:

```text
modular hopper
      ↓
tested single-card separator
      ↓
feed-roller handoff
      ↓
card sensors and camera
      ↓
gravity drop
      ↓
route selector
      ├─ SMALL / S4: 4 outputs + reject, compact cassette array
      └─ MEDIUM: 8 outputs + reject, radial removable bins
```

The machine will perform a true physical sort, not merely scan cards or divide
them into broad value categories. A small number of outputs is sufficient because
the software can order a collection over multiple distribution/radix-sort passes.

## Current status

This repository now contains the consolidated design discussion, hobbyist-project
research, and scaffolding for the mechanical, electrical, firmware, and software
work. No mechanical design has been validated yet. The first milestone is
deliberately smaller than a full sorter: prove a standalone feeder can gently
dispense exactly one card at a time for many thousands of cycles.

The [2026-10-31 design review](docs/reviews/2026-10-31_DESIGN_REVIEW.md) revises the
default to scan-first planned sorting, finite-capacity cassettes, and a friction/
retard feeder baseline compared against vacuum. A tested mathematical simulator
now exists; recognition, firmware, CAD, and physical performance remain unproven.

## Design documents

- [designs/SMALL_SORTER.md](designs/SMALL_SORTER.md) — S4 compact four-way candidate
- [designs/S4_UNIFIED_CARD_PATH.md](designs/S4_UNIFIED_CARD_PATH.md) — layer-by-layer integrated S4 architecture
- [designs/MEDIUM_SORTER.md](designs/MEDIUM_SORTER.md) — eight-way radial turret
- [DESIGN_PRINCIPLES.md](DESIGN_PRINCIPLES.md) — product goals and engineering constraints
- [ARCHITECTURE.md](ARCHITECTURE.md) — shared system layout, modules, and alternatives
- [FEEDER.md](FEEDER.md) — friction/retard baseline and vacuum challenger
- [SORTING_ALGORITHM.md](SORTING_ALGORITHM.md) — local identification and multipass sorting
- [ROADMAP.md](ROADMAP.md) — staged prototypes, beginning with feeder reliability
- [docs/hobbyist/README.md](docs/hobbyist/README.md) — hobbyist-project research,
  cost barriers, user needs, and engineering lessons
- [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) — where future project work belongs
- [docs/LICENSING.md](docs/LICENSING.md) — project and third-party licensing status
- [docs/DESIGN_ASSURANCE.md](docs/DESIGN_ASSURANCE.md) — evidence, failure modes, test matrix, and design gates
- [hardware/prototypes/FEEDER_COMPARISON.md](hardware/prototypes/FEEDER_COMPARISON.md) — first physical bench plan
- [software/sort_model.py](software/sort_model.py) — reproducible sorting and capacity comparison

## Retained designs

| Design | Normal outputs | Intended form | Main tradeoff |
|---|---:|---|---|
| Small / S4 Compact | 4 + reject | Near-vertical core over a compact detachable cassette array | Smaller core target; more traversals for many jobs |
| Medium | 8 + reject | Vertical core above removable radial wedge bins | Fewer passes and less reloading, but a wider base |

The S4 is the compact product candidate. Its earlier
stacked/nested output layout remains a prototype comparison, while a compact 2×2
or shallow-fan cassette arrangement is the leading configuration. The medium
sorter is a co-equal workflow candidate because fewer passes may justify the larger
footprint. Compare both by operator attention and job time. Neither has validated
dimensions yet.

## Decision snapshot

- **Purpose:** return the cards themselves in a requested deterministic order.
- **Topology:** compact vertical, gravity-driven core.
- **Outputs:** small has four destinations; medium has eight; both require reject.
- **Separation:** friction/retard baseline; stationary vacuum edge peel must earn selection in comparative tests.
- **Transport:** rollers take over immediately; gravity does most subsequent movement.
- **Software:** local/offline-first, with optional network updates and enrichment.
- **Construction:** printable geometry, editable CAD, replaceable modules, and commodity parts.
- **First build:** a standalone, instrumented single-card feeder test rig.
- **Workflow:** scan-first order planning, capacity-aware cassette handling, and explicit recovery.
- **Recognition:** name and exact-printing accuracy have separate acceptance gates.

## Project areas

| Area | Purpose |
|---|---|
| [designs](designs) | Retained small and medium physical concepts |
| [docs/hobbyist](docs/hobbyist) | Dated research, cost barriers, and source ledger |
| [hardware](hardware) | CAD, electronics, and physical prototypes |
| [firmware](firmware) | Real-time motor, sensor, and safety control |
| [software](software) | Local recognition, sort planning, and operator interface |
| [tests](tests) | Reliability data, fixtures, simulators, and acceptance results |
| [references/hobbyist-projects](references/hobbyist-projects) | Local third-party research snapshots; not CardSorter source |
