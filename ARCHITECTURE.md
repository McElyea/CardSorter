# System Architecture

## Shared topology

The project retains two sizes built around one compact vertical sorting engine.
The small model has four normal destinations; the medium model has eight. Both
need a reject path.

```text
        ┌───────────────────┐
        │  removable hopper │
        └─────────┬─────────┘
                  ↓
        interchangeable separator
                  ↓
          powered feed rollers
                  ↓
      entry sensor → camera → exit sensor
                  ↓
           short gravity chute
                  ↓
       lightweight route selector
                  ↓
       removable output magazines
```

The selector may be a rotating or tilting printed chute, flap, or finger. It moves
only a light part through a short distance. The exact geometry is not yet frozen;
the architectural decision is one compact selector rather than a long row of
independent powered gates.

Reject is a real additional route, used for low-confidence identification, detected
doubles, unexpected timing, calibration/test cards, and other exceptions. The
mechanism should prefer reject—or stop feeding—when routing is not known in time.

The two retained arrangements are specified separately:

- [designs/SMALL_SORTER.md](designs/SMALL_SORTER.md): the S4 compact candidate,
  four-way selector with a 2×2 or shallow-fan cassette array plus reject.
- [designs/S4_UNIFIED_CARD_PATH.md](designs/S4_UNIFIED_CARD_PATH.md): the proposed
  integrated cassette, peel-nip, dual-nip imaging, and selector architecture.
- [designs/MEDIUM_SORTER.md](designs/MEDIUM_SORTER.md): eight-way radial turret
  with removable wedge bins plus reject.

## Card flow

1. The modular hopper presents a consistent stack face to the feeder.
2. The selected separator isolates one card. Friction/retard is the baseline;
   stationary vacuum edge peel is a challenger under comparison.
3. Feed rollers capture the card, pickup disengages (or vacuum vents), and the
   rollers establish controlled speed and spacing.
4. Sensors confirm entry while the card pauses in an edge-supported imaging bay.
5. The host identifies the card and requests a route. The controller confirms the
   selector position before releasing the card: no confirmed route, no release.
6. The feed roller advances the card into a short gravity path, where the selector
   directs it into a normal sort magazine or reject.

Gravity should do most of the transport after separation. Powered sections exist
where positive control is needed for handoff, imaging, and spacing—not as a
machine-length conveyor.

## Modules and interfaces

### Feeder module

Contains stack presentation, interchangeable pickup/retard features, feed rollers,
and early card sensors. The vacuum variant adds shoe, valve, and pump connections.
It must be usable as a standalone comparison rig. See [FEEDER.md](FEEDER.md).

### Imaging module

Provides a fixed card plane, controlled lighting, a camera, and entry/exit sensing.
Its mechanical interface should allow camera or lighting upgrades without changing
the feeder or selector. Image processing occurs on the host computer.

### Routing module

Contains one fast, low-inertia selector and position feedback or a homing feature.
Its route count and output geometry depend on the selected design. Reject should
be easy to empty and visually distinct from normal outputs.

### Storage modules

Hoppers and output magazines are detachable accessories. The current S4 direction
uses one keyed cassette interface for input and output so a group can move between
passes without loose handling or accidental reversal. Different depths can support
portable test stacks, ordinary use, or bulk use without enlarging the core engine.
Card guides and magazine mouths should be replaceable for later sleeve or
card-format support.

Collection size is independent of cassette size. Prototype 150–250-card capacities
with a safe full-bin stop and ordered replacement chunks. Reserve space before
releasing a card and preserve route/pass/chunk order across replacements. Do not
assume every output must hold the whole collection.

### Control split

```text
host computer                       microcontroller
────────────────                    ─────────────────────────
local card recognition     USB      feed cycle and interlocks
local/updateable database  ⇄        motors, valve, and selector
sort plan and pass state             entry/exit/double sensors
operator reload prompts              jam and position events
```

A small command/event vocabulary is enough initially: `FEED`, `ROUTE n`, `STOP`,
`CARD_READY`, `CARD_ENTERED_CAMERA`, `CARD_EXITED_CAMERA`, `JAM`, and
`SELECTOR_POSITION`. The protocol is conceptual until the feeder timing is known.
Every per-card command and event must carry cycle_id; late or mismatched commands
cannot authorize release. Recognized key and expected sequence position must also
agree before normal-route release, with destination capacity reserved.

## Packaging strategy

Both designs should be desktop appliances with detachable storage. The earlier
small-engine target of roughly 100 × 120 × 200 mm remains a useful lower bound for
the mechanism alone, but it is not a credible envelope for useful storage and jam
access. The complete S4 target is approximately 190–220 mm wide, 200–240 mm deep,
and 300–350 mm tall. The medium concept initially targets roughly 250 × 250 ×
400 mm. These are design directions, not released dimensions.

Printed modules should reference a compact commodity structural datum rather than
depending on a large flat print. A short 2040 aluminum-extrusion spine is the
current recommendation to test; an all-printed alternative may be retained if it
proves equally straight and serviceable.

## Alternatives not retained as primary designs

| Alternative | Advantage | Why it is not a primary design |
|---|---|---|
| XY gantry with moving vacuum head | Routes directly to many arbitrary positions | Every card pays for lift, X/Y travel, placement, and return; large, slow, and mechanically demanding |
| Long conveyor with many diverter gates | High throughput and many one-pass categories | Desk-length frame, belts, multiple gates, and more alignment/wear than this compact project needs |
| Binary-only sorter | Smallest possible gate and two bins | Roughly twice as many passes as four-way sorting, creating excessive operator handling for large key spaces |
| Rotating output cassette | Extremely simple fixed card path | Repeatedly accelerates increasingly heavy card stacks; less attractive than moving a few grams of chute |

The small design captures much of binary's compactness while halving its pass
count. The medium radial design exchanges a wider base for fewer passes. Both keep
the hopper and magazines modular so the sorting engine is not dictated by how many
cards an owner wants sitting in a bin.
