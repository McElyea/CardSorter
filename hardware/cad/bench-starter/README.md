# Bench-Starter Parts (r1)

First printable parts for the [feeder comparison bench](../../prototypes/FEEDER_COMPARISON.md)
and its capacity mockup. They check your printer and real card stacks before any
feeder or sorter CAD exists. They are not validated sorter parts.

## Files

| Part | Purpose | Size (mm) |
|---|---|---|
| `cs_fit_coupon_r1` | M3 screw and heat-set insert hole fit; printed card-slot gaps | 96 × 36 × 8 |
| `cs_stack_gauge_150_r1` | 150-card stack mockup with fill ticks | 55 × 69 × 47 |
| `cs_stack_gauge_200_r1` | 200-card stack mockup with fill ticks | 70 × 69 × 47 |
| `cs_stack_gauge_250_r1` | 250-card stack mockup with fill ticks | 85 × 69 × 47 |

Each part is exported from [bench_starter.py](bench_starter.py), the parametric
source, as:

- `3mf/`: open this in Bambu Studio, PrusaSlicer, OrcaSlicer, or Cura.
- `stl/`: the same geometry for any slicer.
- `step/`: for editing in CAD. Not for printing.

All files are in millimetres and already in print orientation: flat on the bed,
open side up. The 3MF files carry geometry, units, and orientation only. Print
settings are below.

## Print settings

- PLA, 0.4 mm nozzle, 0.2 mm layers
- 3 walls, 15% infill, no supports
- A brim is optional. Every part has a 0.4–0.6 mm bottom chamfer against
  elephant's foot.

Print the fit coupon first. It's small, and it shows whether the printer holds
the tolerances that the gauges and later parts depend on.

## Using the fit coupon

- **Holes (front row):** 2.9 mm for M3 screws threading into plastic; 3.2 and
  3.4 mm for M3 clearance; 4.0 and 4.2 mm as pilots for M3 heat-set inserts
  (check your insert brand's recommended hole). Record which hole gives a snug
  self-tap, a free clearance fit, and a good insert set.
- **Slots (back row):** 0.4 to 1.2 mm gaps, open at the back edge. Try one card,
  then two stacked cards, in each. Record the narrowest slot that passes one card
  freely and whether any slot passes one card but stops two. Very narrow slots may
  print closed; that tells you your printer's minimum gap.

## Using the stack gauges

Cards stand on their 63 mm edge and stack along the long axis. The inside is 1 mm
wider than a standard 63 mm card, with 4 mm of extra length for curl, a follower,
and lifting the stack out. The finger notch is on one side; fill ticks are on the
other rim, every 25 cards, deeper every 100.

The ticks assume 0.305 mm per card. Measure your own stock: stack 50 cards,
measure with calipers, and divide by 50. If it differs, change `CARD_T` in
`bench_starter.py` and regenerate. Also try sleeved cards; they will not fit
the stated count.

Record how full each gauge feels, how easy the stack is to remove, and the
footprint against the 150–250-card capacity question in the bench plan. Put
results in [../../prototypes](../../prototypes).

## Regenerating

From the project root, with CadQuery 2.x on Python 3.10–3.13:

```text
python hardware/cad/bench-starter/bench_starter.py
```

The project's main CAD tool is still undecided (see [../README.md](../README.md)).
This CadQuery script is the parametric source for these starter parts only.
