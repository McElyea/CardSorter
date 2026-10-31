# Implications for Our Designs

Last reviewed: **2026-09-06**

Design follow-up **2026-10-31**: the [review](../reviews/2026-10-31_DESIGN_REVIEW.md)
supersedes any preference here for vacuum or recursive sorting. Friction/retard is
the bench baseline; vacuum must demonstrate an advantage. Compare four and eight
outputs by scan-first job time and operator attention with finite cassettes. The
original survey observations below remain dated September research; the medium
comparison table and experimental backlog were updated to match.

## Decisions strengthened by the survey

### Build the feeder first

GlideSorter reported the familiar tradeoff between double-feeding and failing to
feed. Open Sorts requires careful gap adjustment. Timprovised spent roughly thirty
iterations on singulation. Project-O's documented single-card gap can physically
admit two ordinary cards.

The standalone feeder milestone in [../../ROADMAP.md](../../ROADMAP.md) remains the
right first build. Recognition and enclosure design should not conceal feeder
failures.

### Keep vacuum limited to edge separation

None of the surveyed compact printed builds was found using stationary vacuum only
to peel a card edge before a roller handoff. Current approaches rely mostly on:

- A calibrated slot and swiper
- A pressure finger plus pusher
- Opposed or fixed/drive rollers with an adjustable gap
- A spring-loaded hopper wall and friction roller

This identifies an experiment, not evidence that vacuum is a better feeder.
The test should compare it directly with the best passive/friction control rather
than assuming vacuum wins. See [../../FEEDER.md](../../FEEDER.md).

### Use one route selector

Project-O demonstrates the economy of a light rotating chute: ten normal bins plus
reject with one chute actuator. Mault, GlideSorter, and BBG show the opposite
scaling rule—more outputs cause more servos, wires, power, and endpoint calibration.

Both retained designs should therefore keep a single selector:

- [../../designs/SMALL_SORTER.md](../../designs/SMALL_SORTER.md): one four-way chute
  plus reject
- [../../designs/MEDIUM_SORTER.md](../../designs/MEDIUM_SORTER.md): one rotary
  selector over eight radial bins plus reject

### Add positive route-position evidence

Project-O's slotted optical encoder is a valuable low-cost pattern. Timed rotation
alone drifts with voltage, load, temperature, and friction. Our medium selector
should have a home/index signal and sufficient position feedback to prove the chute
is at the commanded bin before release.

For the small design, a normal positional servo may already provide closed-loop
internal control, but an independent home switch or optical confirmation is still
worth comparing against a purely mechanical hard stop.

### Design air into gravity surfaces

GlideSorter discovered that a card lying flat on a printed platform may not admit
enough air underneath to slide reliably. Static was initially suspected, but contact
friction and the trapped interface were sufficient to stop motion.

Candidate surface features for test coupons:

- Narrow raised ribs that reduce contact area
- Shallow longitudinal air channels
- Perforations or vent slots away from card edges
- A slightly crowned surface
- Replaceable low-friction strips
- Steeper angles with a soft, controlled landing

Surface texture, print orientation, layer direction, material, humidity, and card
finish must be part of the test record.

### Use the owner's computer when practical

A dedicated Pi raises cost and can still be too weak for the chosen recognition
model. Our controller/host split should remain:

```text
ESP32 or similar                 existing host computer
────────────────                ─────────────────────────
motors and valve       USB      image recognition
sensor accounting      ⇄        local card database
route interlocks                sort planning and UI
jam-safe state                  logs and recovery
```

An integrated Pi or mini PC can be a convenience option, not a dependency.

### Keep recognition replaceable and local

The surveyed recognition approaches include:

- Small perceptual hashes with OCR tie-breaking
- RGB-channel perceptual hashes and caches
- Learned image embeddings plus vector search
- General vision/OCR services followed by a card database lookup

Simple hashes are fast and inexpensive but struggle with visually similar printings.
Embeddings improve flexibility but increase compute and data complexity. Foils,
promos, languages, alternate art, and near-identical reprints remain difficult.

The physical controller should receive a route and confidence-independent safety
state; it should not know which recognizer produced them. Loss of recognition by a
deadline must send the card to reject or stop feed.

### Treat calibration as a product feature

GlideSorter and Mault both built dedicated actuator/sensor calibration interfaces.
BBG exposes individual flapper angles. Open Sorts documents perspective and gap
calibration problems.

Our system should eventually include:

- Live sensor state
- Vacuum and timing traces
- Manual feed/vent/roller controls
- Selector homing and per-route test
- Camera exposure, focus, crop, and lighting setup
- Saved profiles for card/sleeve types
- A guided test that accounts for one numbered card at a time

Calibration should be possible without the recognition stack running.

## Specific implications for the small sorter

The tiered designs show that height can replace desk width, but warn against flat
platforms and servo multiplication. Our S4 small sorter should use one moving
selector, not a sequence of powered stages. The current leading output geometry is
a compact 2×2 or shallow-fan cassette array; the earlier stacked/nested layout
remains a prototype comparison rather than a settled choice.

Questions to answer with a cardboard or rough-print mockup:

1. Which of the 2×2, shallow-fan, or stacked layouts produces the smallest usable
   footprint with gentle route angles?
2. Can the card stay off broad flat surfaces and maintain an air gap?
3. Does every output preserve arrival order and form a neat stack?
4. Can a reject path remain passive or fail-safe without widening the machine?
5. Can every magazine be removed and reloaded without reversing the stack?

## Specific implications for the medium sorter

Project-O provides a concrete comparison point for our radial design:

| Feature | Project-O reference | Our medium design question |
|---|---|---|
| Working routes | 10 + reject | Is 8 + reject the better footprint/pass compromise? |
| Outer diameter | About 340 mm | Can eight wider/cleaner bins reduce this materially? |
| Selector | Continuous servo + optical index wheel | Stepper versus servo/encoder reliability and noise |
| Bin ring | Four printed snap-fit segments | Best keyed segmentation for common print beds |
| Feeder | Bottom swiper + gap/finger | Friction/retard baseline versus vacuum edge peel challenger |
| Full ordering | Six-pass decimal radix | Scan-first base-eight planner with operator-safe reload |

The radial routing prototype should initially exclude the feeder and camera. Drop
numbered cards from a fixed height and measure chute positioning, settling, stack
quality, bounce, and worst-case route time.

## Prioritized experimental backlog

### P0 — Singulation comparison fixture

Test three interchangeable methods on the same hopper and roller path:

1. Pressure finger/retard pad plus roller (comparison baseline)
2. Two-stage friction gap with brief reverse/retard motion
3. Vacuum edge peel plus roller handoff (challenger)

Measure detected and undetected doubles, no-feed cycles, jams, card damage, timing,
required adjustment, noise, and performance drift with contamination.

### P1 — Gravity-surface coupons

Test angle, rib pattern, vent geometry, material, layer direction, and card type.
Use a high-frame-rate phone video and a repeatable release fixture. Record release
latency and failures after cards rest on the surface for different durations.

### P2 — Medium rotary routing rig

Compare a small stepper with a continuous servo plus optical indexing. Require
route confirmation before release. Test shallow bins before printing full-capacity
magazines.

### P3 — Small four-way routing rig

Compare 2×2, shallow-fan, and stacked/nested outlet geometry with a dedicated
reject route and a common keyed cassette. Measure total footprint only after jam
access is included.

### P4 — Imaging bench

Compare fixed card registration plus crop against contour/perspective correction.
Test white, gray, and dark chamber surfaces, diffuse lighting, glare, foils, and a
second illumination mode. Keep this independent of routing.

### P5 — Multipass operator simulation

Use numbered paper cards and empty labeled magazines to test scan-first four- and
eight-output reload instructions, including overflow chunks. Count operator actions and deliberate errors. The interface
must prevent silent stack reversal and persist recovery state.

## Contributions that would distinguish this project

- A feeder test fixture usable by other card-machine builders
- Long-run, downloadable reliability logs instead of only demonstration videos
- Original editable CAD with small replaceable wear/test parts
- A complete dated BOM for existing-tool, new-builder, and kit-equivalent scenarios
- One shared feed/imaging engine with two output sizes
- Fully local operation with a documented USB protocol and no recurring core fee
- A simulator for sort planning and operator workflow before hardware exists
- Explicit licenses for software, electronics, documentation, and CAD

## What not to infer

- A working short video does not prove long-term card safety.
- A stated recognition percentage does not reveal exact-printing accuracy or the
  reject rate.
- “Open source” may apply to software while the CAD is paid or noncommercial.
- A low printed-material cost does not equal a low complete build cost.
- More output bins do not automatically improve total workflow if they enlarge the
  machine or increase calibration and failure rates.
