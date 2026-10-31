# S4 Unified Card Path

> **Superseded 2026-10-31.** The [reliability rework](../docs/reviews/2026-10-31_RELIABILITY_REWORK.md)
> replaced the S4 with [R8](R8_RELIABLE_SORTER.md). Its function-combining rules and
> list of functions that must stay independent still apply to R8.

## Status

Candidate integrated architecture for the S4 Compact sorter. This document
captures the layer-by-layer optimization that combines compatible functions while
preserving independent safety evidence. No geometry or performance claim has been
validated.

Revision 2026-10-31: this is now an integration candidate, conditional on the
[design review](../docs/reviews/2026-10-31_DESIGN_REVIEW.md). Friction/retard is the
feeder baseline and vacuum is a challenger. The vacuum-dependent shared drive
below is not a fixed requirement. Scan-first planned sorting supersedes recursive
group processing, and finite-capacity cassettes replace whole-job capacity.

Prototype rigs should remain modular so failures are diagnosable. Only proven
interfaces should be collapsed into combined release parts.

## Central design rule

The final S4 should not be a feeder, scanner, router, and set of bins connected in
series. It should be one continuous controlled card path in which each assembly
performs several compatible functions.

Combine functions when they share a datum, motion, or contact surface. Keep them
independent when one function verifies the safety of another.

```text
UNIVERSAL CARD CASSETTE
  storage + follower + transport shutter
  identity tag + orientation key
                    |
                    v
INSTRUMENTED PEEL-NIP
  vacuum edge peel + retard
  upper feed nip + thickness sensing
                    |
                    v
DUAL-NIP IMAGING CHANNEL
  one motor drives both nips
  edge guides + card registration
  lower nip holds card during recognition
                    |
                    v
INDEXED SELECTOR HUB
  route guide + position code wheel
  service knob + safe reject behavior
                    |
                    v
UNIVERSAL OUTPUT CASSETTES
  cassette mouth is final chute
  follower is anti-bounce and full indicator
```

The intended physical transfers are limited to cassette-to-feed-nip,
feed-nip-to-imaging-nip, imaging-nip-to-selector, and selector-to-cassette. Every
additional uncontrolled fall, gate, roller, or chute seam must justify the skew,
bounce, wear, and jam risk it adds.

## Universal passive cassette

One cassette design should serve as input hopper, output bin, transport container,
and reload unit. Candidate combined functions are:

- Spring or gravity follower for stack presentation
- Card-stack alignment
- Output-stack support and anti-bounce pressure
- Sliding transport shutter
- Mechanically keyed insertion direction
- Visible fill indication
- Passive printed identity and capacity marker
- Replaceable soft landing surface

When docked as input, the shutter exposes only the required feed edge. When docked
as output, it opens fully and its mouth becomes the last section of the card route.
Removing the cassette should retain the stack automatically.

A printed AprilTag or similar fiducial near the mouth could provide cassette
identity, orientation verification, camera scale, perspective reference, and
capacity identification without electronics in the cassette. The feasibility and
camera field of view must be tested.

Use measured 150–250-card cassette candidates. A collection can exceed one cassette
and one machine fill. Reserve destination capacity before release, then pause,
close and label a full route's cassette, replace it, and resume its logical stream.
Route/pass/chunk IDs and direction preserve sort order across physical containers.

## Instrumented peel-nip

This section describes the vacuum challenger. Test it against the friction/retard
baseline on the common bench before selecting a replaceable feeder block.

1. The cassette presents its front card outside the roller tangent.
2. Vacuum bows only the leading edge into a shallow peel recess.
3. The peeled edge enters the upper nip.
4. A soft roller meters the card away from the stack.
5. A passive retard surface holds the next card.
6. Vacuum vents after roller capture.

The upper idler should be mounted on a low-force compliant arm. A magnet and analog
Hall sensor on that arm can measure displacement and therefore estimate card
thickness. Compare it with a suitable ultrasonic double-sheet detector, including
false rejection of thick singles. Vacuum pressure is an acquisition diagnostic,
not independent proof against aligned doubles.

## One drive for two nips

The candidate shared drive synchronizes two nips with one motor and belt. The
friction baseline may require pickup lift, a clutch, or a separate drive; evaluate
that cost explicitly before selecting this architecture:

```text
vacuum shoe
    |
upper nip  ------------+
    |                   | one motor
 imaging window         | one encoder
    |                   |
lower nip  -------------+
    |
 selector
```

The proposed cycle is:

1. Vacuum presents one card to the upper nip.
2. The shared drive advances the card into the imaging channel.
3. The lower nip captures the card before the upper nip releases it.
4. The motor stops at the registered imaging position.
5. The lower nip holds the card during image capture and recognition.
6. The selector moves and independent position evidence confirms the route.
7. The shared drive releases the card through the lower nip.
8. The upper nip also turns, but it cannot acquire the next card because vacuum
   has not presented an edge.

This treats vacuum presentation as the feed clutch. If validated, it eliminates a
second transport motor, powered imaging stop, separate release gate, and
uncontrolled waiting position above the selector.

The upper roller geometry must prove that rotation without vacuum cannot acquire a
card accidentally. Nip spacing must also maintain positive card control through
the entire imaging transfer.

## Imaging datum

The imaging frame should also establish the mechanical relationship among the two
nips, card edge rails, camera, lighting, and selector entrance. The card should be
supported only along narrow border regions, with no clear platen or broad printed
surface over either face.

Two separately controlled LED banks can provide both diffuse identification light
and a one-sided raking-light capture for foils and glare. The camera and lighting
mount to the structural datum, not to the service door. The enclosure provides
light control and guarding but does not determine alignment.

A short 2040 extrusion remains the leading common datum to test. Feed block,
imaging frame, lower nip, and selector axis should all reference it directly so
tolerance does not accumulate across separate printed shells.

## Indexed selector hub

The removable selector hub can combine:

- Two narrow card-support rails
- The moving route guide
- A molded optical position code wheel
- Mechanical limits
- A manual service knob
- Replaceable low-friction contact inserts

The drive may be a positional servo, but its position sensor stays fixed and
electrically independent. A commanded servo angle is not evidence that the route
was reached.

Normal cassette mouths should extend close to the selector and become the final
fixed guides. This minimizes intermediate chutes. Mouths should incorporate air
relief, narrow ribs, an anti-bounce feature, and replaceable soft or low-friction
contact surfaces. The preferred packaging candidates remain a compact 2x2 array
and a shallow fan; both must be compared physically.

## One physical and digital card state

The microcontroller assigns a unique `cycle_id` when acquisition begins. Every
physical and software event uses that identifier:

```text
cycle 1842
  vacuum acquired
  upper nip entered
  thickness accepted
  imaging position reached
  image captured
  identity assigned
  route 3 requested
  route 3 confirmed
  lower nip released
  selector exit detected
  cassette 3 count incremented
```

A late recognition result for one cycle must never route the next card. Firmware
rejects a missing or mismatched identifier. The shared event stream drives safety,
recognition records, output counts, sort planning, operator instructions, recovery,
and reliability analysis.

## Multipass workflow as a hardware requirement

Universal cassettes and their identities are part of the sorting algorithm, not
accessories added later.

1. Inventory the complete collection and its actual order, across input cassettes.
2. Build a stable pass plan from that order and the requested key.
3. Before release, verify each observed key against the expected next item.
4. Track destination route, pass, chunk ordinal, cassette identity, and count.
5. Pause for full outputs and preserve chronological chunk order during replacement.
6. Guide reloading in route order, then chunk order, with a known feed direction.
7. On mismatch, invalidate and reconcile before replanning; rereading alone does
   not repair the old plan. Count all recovery scans and operator actions.

This is what makes four outputs practical for full physical ordering rather than
only four-category sifting.

## Functions that must remain independent

Integration must not erase diagnostic or safety independence:

- Selector actuator versus route-position sensor
- Vacuum-pressure evidence versus physical thickness evidence
- Recognition result versus physical card accounting
- Structural datum versus removable enclosure
- Permanent chassis versus dirty or wearing card-contact inserts
- Motor-current diagnostics versus card-position sensing
- Host intelligence versus firmware safety authority

A single failure must not be able to produce a plausible but incorrect successful
cycle.

## Target mechanism budget

The vacuum-based integrated S4 candidate aims for the following budget. The feeder
comparison can remove the pump/valve or justify a separate pickup drive; select by
measured total performance rather than a fixed actuator count:

- One feed/imaging motor
- One selector servo
- One vacuum pump and fast vent valve
- Two synchronized nip shafts
- One moving selector assembly
- One structural spine
- One universal cassette design
- No conveyor
- No powered imaging gate
- No separate exit motor
- No actuator per output
- No mandatory embedded computer, display, subscription, or network service

This is a target architecture, not authorization to integrate before testing. The
feeder, dual-nip imaging channel, selector, and cassette should first prove their
forces, timing, clearances, and failure behavior in separate fixtures. Stable shared
surfaces can then be merged without carrying unnecessary interfaces into the
release design.
