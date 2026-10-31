# Software

Host software will provide offline-first card recognition, a local card database,
deterministic sort keys, distribution/radix planning, the operator workflow,
simulation, persistent run state, and diagnostics. Network services may enrich
data but cannot be required for core sorting.

## Deliverables

- Local card database with a versioned updater; each job freezes its revision
- Replaceable recognition pipeline reporting evidence per identity level (name,
  printing, language, finish) and a separate expected-card verification mode
- Versioned sort-key normalization (see [SORTING_ALGORITHM.md](../SORTING_ALGORITHM.md))
- Scan-first order planner with dense-rank radix as a baseline
- Capacity-aware operator workflow: chunk labels, reload order, reject resolution
- Persistent run manifest, event log keyed by `cycle_id`, and safe resume
- Documented USB command/event protocol for the microcontroller
- Hardware simulator for development without a machine
- Calibration and diagnostic modes that do not require card recognition

An initial mathematical model now exists in [sort_model.py](sort_model.py). Run
`python software/sort_model.py` from the project root to compare scan-first planned
sorting, dense ranks, catalog radix, and recursive group counts, including cassette
chunks. The model does not drive hardware or identify cards.
