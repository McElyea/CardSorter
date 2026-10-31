# R8 Reliable Sorter

## Status

Primary design as of the 2026-10-31
[reliability rework](../docs/reviews/2026-10-31_RELIABILITY_REWORK.md). Eight normal
outputs plus reject, positive card control, and a fixed cadence. No geometry,
speed, or reliability figure here has been validated; every number is a target or
a layout estimate with a test attached.

## Design intent

Make throughput a property of the machine, not of card condition, host latency,
or how often someone walks past. The card is gripped from pickup to pocket, moves
at one constant speed, and is photographed in motion. Recognition runs alongside
the transport; a late answer costs one reject, never a stopped machine.

```text
   500-card hopper ── constant-force follower
          │
   pick roller (stepper) + brake roller (torque limiter)
          │
   ┌─ transport nips, one stepper, GT2 belt ─────────────┐
   │   Hall idler (thickness)   encoder idler (slip)     │
   │   beam → strobe A (diffuse) → strobe B (raking)     │
   │   buffer ≥ 2 cadence slots                          │
   └─────────────────────────────────────────────────────┘
          │
   router (R-A rotary head or R-B gates), indexed
          │
   pockets 0–7 (500 cards each) + reject (default)
```

## Subsystems

### Feeder

- Pick roller on its own stepper, engaged once per cadence slot.
- Brake roller on a torque limiter: a single card overcomes the limiter and passes;
  a second card is held back. Aftermarket scanner pick/brake roller sets are the
  first source to test (see [../FEEDER.md](../FEEDER.md)).
- Constant-force spring follower on linear guides. A motorized lift with a
  top-of-stack sensor is the alternative if spring friction proves inconsistent.
- Hopper target 500 cards (about 153 mm of stack at 0.305 mm per card).

### Transport and imaging

- One NEMA 17 stepper drives every transport nip shaft through a GT2 belt, so all
  nips share one surface speed.
- Urethane-covered driven rollers against spring-loaded idlers. Nip spacing at most
  about 70 mm for cards travelling 88 mm edge first.
- Hall sensor and magnet on the first idler arm measure thickness for double
  detection. An AS5600 magnetic encoder on an undriven idler compares card speed
  with motor speed; rising slip means roller wear or contamination.
- A beam sensor triggers two strobes on the global-shutter camera: diffuse for
  identification, raking for foils and glare. At 250 mm/s, a 50 µs flash blurs
  about 12 µm.
- The buffer between camera and router holds at least two cadence slots, so the
  host has at least 2 s at the target cadence.

### Router

| Candidate | How it works | Strengths | Risks |
|---|---|---|---|
| **R-A: driven rotary head** | Short guided head with its own exit nip turns on a turntable bearing to one of nine positions; slotted index wheel and beam confirm position | Compact radial layout; card path needs only a gentle incline; one positioning axis | Head drive needs a rotating cable or limited-rotation wrap; worst-case move must fit the budget |
| **R-B: gated transport** | Spring-return gates along a gently curved transport; no gate energized means the card runs to reject at the end | Fail-safe by default; binary actuators; no position ambiguity | Needs card bending; machine grows long; one actuator per output |

The [card bend test](../docs/DESIGN_ASSURANCE.md) decides. If trading-card stock
tolerates a gentle radius repeatedly with no residual curl or whitening, R-B's
fail-safe default is attractive. Otherwise R-A.

R-A move budget at 1 card/s: a card passing through a 60 mm head at 250 mm/s takes
about 0.6 s including its own length, leaving about 0.4 s for the worst-case move.
That is tight; the cadence target may drop to 0.75 card/s for R-A. The deadline and
budget are firmware constants checked on every cycle.

### Pockets

- Nine removable pockets (8 normal + reject), 500-card target, keyed.
- Constant-force follower on two 8 mm rods with linear bearings.
- Full switch at the end of follower travel, behind software counting with
  capacity reserved before release.
- **Open problem: stacking without face scuffing.** Candidates to bench-test:
  1. Driven entry into a slot held open by entry lips, against a low-force follower.
  2. A soft impeller or paddle stacker per pocket, all driven from one shaft.

  Score each on face scuff (magnified inspection), stack neatness, and order
  preservation with numbered cards.

### Controller

RP2040 board with four onboard TMC2209 drivers (transport, pick, head rotation,
head exit nip for R-A), I²C input expander, analog input for the Hall sensor,
MOSFET strobe output, e-stop, and cover interlock. The host connects over USB.

## Throughput and operator visits

Model results from [../software/sort_model.py](../software/sort_model.py) for 1,000
random distinct cards, 8 outputs, 500-card capacity: 4 traversals including the
inventory scan, 4,000 card cycles.

| | Previous S4 (4-way, 200-card, 3 s stop-and-go) | R8 target (8-way, 500-card, 1 card/s) |
|---|---|---|
| Card cycles | 6,000 | 4,000 |
| Machine time | about 5 hours | about 67 minutes |
| Time between hopper refills | about 10 minutes | about 8 minutes |
| Hopper refills, if pocket chunks are combined in route order | about 30 | about 8 |
| Separate input chunk loads, without combining (model) | 42 | 20 |

A faster machine empties its hopper sooner. R8 shortens the job and cuts total
visits, but it is still attended. These figures assume the target cadence holds and
exclude feeder faults; the roadmap measures both.

## Mechanism budget

- 4 steppers: transport, pick, router head, head exit nip (R-A); R-B swaps the head
  motors for one gate actuator per output
- 1 torque-limited brake roller
- 10 constant-force followers (hopper + 9 pockets)
- 1 global-shutter camera, 2 strobed LED banks
- About 8 beam sensors, 1 Hall sensor, 1 slip encoder, 1 index sensor, 9 full
  switches, e-stop, cover interlock
- No vacuum, no free-fall routing, no per-card host round trip in the timing loop

Purchased parts are priced in [../docs/BOM_PRICING.md](../docs/BOM_PRICING.md).

## Risks and open questions

- Does the brake roller hold a steady pick time across stock, wear, and humidity?
- What bend radius can card stock take repeatedly without damage?
- Can output stacking avoid face scuffing at 500 cards?
- Does the head exit nip match transport speed closely enough to avoid buckling or
  drag at the handoff?
- What is the host's 99th-percentile recognition latency, and does it fit the
  deadline with margin?
- Does continuous transport raise or lower card damage compared with stop-and-go?
- Is a 450–500 mm footprint acceptable, or should pockets drop to 250 cards?

## Prototype order

1. Feeder bench: pick plus brake roller, constant-force presentation, Hall and slip
   sensing. See [../hardware/prototypes/FEEDER_COMPARISON.md](../hardware/prototypes/FEEDER_COMPARISON.md).
2. Card bend test and continuous transport/imaging bench.
3. Router (R-A or R-B per the bend test) and pocket stacking bench.
4. Integrated endurance machine.
