# System Architecture

Revised 2026-10-31 by the [reliability rework](docs/reviews/2026-10-31_RELIABILITY_REWORK.md).
The primary design is the [R8 reliable sorter](designs/R8_RELIABLE_SORTER.md): eight
normal outputs plus reject, with positive card control and a fixed cadence.

## Topology

```text
        ┌──────────────────────────────┐
        │ 500-card hopper,             │
        │ constant-force follower      │
        └──────────────┬───────────────┘
                       ↓
     pick roller (own drive) + torque-limited brake roller
                       ↓
     transport nips, one motor, belt-synchronized, constant speed
        ├─ Hall idler: thickness / double check
        ├─ encoder idler: slip measurement
        └─ beam trigger → two strobed captures in motion
                       ↓
     buffer section: card keeps moving while the host recognizes it
                       ↓
     router: pre-positioned, independently indexed
                       ↓
     driven entry into one of 8 pockets or the default reject pocket
```

Every arrow is a driven transfer. A card is always held by at least one nip until
its trailing edge enters the pocket mouth.

## Card flow

1. The hopper's constant-force follower presents the stack with the same force
   whether it holds 500 cards or one.
2. At each cadence slot, the controller engages the pick roller. The brake roller,
   on a torque limiter, lets one card pass and holds back a second.
3. The first transport nip captures the card; the pick roller stops. The card now
   moves at the transport's constant speed.
4. A Hall-sensed idler measures thickness. An encoder on an undriven idler measures
   card speed against motor speed (slip).
5. A beam sensor triggers two strobed captures as the card passes: diffuse light
   for identification and raking light for foil and glare.
6. The card continues through a buffer at least two cadence slots long while the
   host identifies it and returns a route, tagged with the card's `cycle_id`.
7. The router moves to the route only after the answer arrives, and an independent
   index sensor confirms the position before the card's leading edge reaches it.
   No answer by the deadline: the router stays at reject. Router position unknown:
   the transport stops, with every card still held.
8. The router drives the card into its pocket. An arrival sensor confirms entry and
   the pocket count increments.

## Timing model

```text
cadence T = card pitch / transport speed
route deadline = time from capture to router entry  (≥ 2 T)
router move budget = T − time for one card to pass through the router
```

Initial test targets, not claims: transport 250 mm/s, card pitch 250 mm, so
T = 1 s and 3,600 cards/hour at full cadence. A card that misses its deadline costs
one reject, not a stopped machine. Throughput changes only when the controller
deliberately skips a slot (pick retry, full pocket, operator pause), and every
skipped slot is logged.

## Modules and interfaces

### Feeder

Hopper, constant-force follower, pick roller with its own drive, brake roller with
torque limiter, first transport nip, and early sensors. It must work as a
standalone bench rig. See [FEEDER.md](FEEDER.md).

### Transport and imaging

One stepper drives all transport nip shafts through a GT2 belt. Nip spacing is
shorter than the card's length in the travel direction. The imaging station
provides fixed edge guides, two strobed LED banks, and a global-shutter camera.
Image processing happens on the host.

### Router

Two candidates, chosen by the card bend test:

- **R-A, driven rotary head:** a short guided head carrying its own exit nip
  rotates to one of nine positions (8 + reject) on a turntable bearing, indexed by
  a slotted wheel and sensor. One positioning motor, one head drive motor.
- **R-B, gated transport:** a straight or gently curved transport with spring-return
  gates. With no gate energized, the card runs to the reject pocket at the end of
  the line, so loss of power or a missing command fails safe. Needs card bending.

### Pockets

Nine removable pockets (8 normal + reject), 500-card target, each with a
constant-force follower on linear guides and a full switch. Software also counts
cards and reserves capacity before release, so the switch is a backup. The
stacking mechanism is open; see the R8 design.

### Control split

```text
host computer                       microcontroller board
────────────────                    ─────────────────────────────
local card recognition     USB      cadence, pick, transport, router
local/updateable database  ⇄        Hall, slip, beams, index, full
sort plan and pass state             interlocks, e-stop, strobe timing
operator prompts, health trends      cycle_id event stream
```

A 3D-printer-class board with an RP2040 and four TMC2209 drivers covers the four
steppers; an I²C expander adds inputs. Initial protocol vocabulary:
`START cadence`, `STOP`, `ROUTE cycle_id n`; events `PICKED`, `THICKNESS`,
`CAPTURED`, `ROUTE_CONFIRMED`, `ARRIVED pocket`, `SLOT_SKIPPED reason`, `SLIP`,
`JAM`, `FULL pocket`. Every per-card message carries `cycle_id`; a missing or
mismatched route never authorizes a normal route. Recognized key and expected
sequence position must agree before a normal route, with capacity reserved.

### Health monitoring

Per cycle: pick-to-capture time, slip, Hall signal, capture quality, route latency,
and retries. Per job: trends against the machine's own history, a reference card at
job start, and maintenance prompts by cycle count.

## Packaging

A 2020 aluminum-extrusion frame carries the shafts and the router. Printed parts
hold guides, sensors, and covers. Layout estimates for R-A: nine 500-card pockets
around the router suggest roughly 450–500 mm diameter and about 500 mm height;
250-card pockets roughly 350 mm. These are directions, not released dimensions.

## Alternatives not retained as primary designs

| Alternative | Advantage | Why it is not primary |
|---|---|---|
| Gravity-drop S4 and medium radial ([designs](designs)) | Small, few motors, cheap | Timing and landing vary with card condition; stop-for-capture ties throughput to recognition latency |
| Vacuum edge peel feeder | Possibly gentle separation | Pump, valve, dust, and noise; must win the bench comparison first |
| XY gantry with moving vacuum head | Routes to many positions | Every card pays for lift, travel, placement, and return |
| Binary-only sorter | Smallest gate and two bins | Many more passes and operator loads |
| Rotating output cassette rack | Fixed card path | Accelerates heavy card stacks on every route change |
| Automatic recirculation | Unattended multipass jobs | Large mechanism; deferred until the single-pass machine is proven |
