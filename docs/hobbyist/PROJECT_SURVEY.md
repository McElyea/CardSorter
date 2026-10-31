# Hobbyist Project Survey

Last reviewed: **2026-09-06**

## GlideSorter

**Sources:** [project site](https://glidesorter.com/),
[hardware test](https://glidesorter.com/en/blog/read/4-hardware-sorting-test),
[calibration notes](https://glidesorter.com/en/blog/read/3-let-the-calibration-begin)

GlideSorter is a hobby-origin project moving toward a partially assembled DIY kit.
Its published target is six normal slots plus one unknown slot, a 400-card feeder,
25–30 cards per minute, local recognition, a 319 × 459 × 295 mm enclosure, and an
estimated price near €1,500. The project was in closed testing at the review date.

The mechanism uses three sorting platforms, each with three servo drives, plus two
continuous-rotation motors, three IR sensors, two fans, and two lighting channels.
Cards move through tiered platforms: each stage can send a card left or right or
drop it to the next level. This packs several routes into height rather than a long
horizontal row.

The build log supplies unusually useful failure information:

- Tightening the feeder separator cured doubles but could prevent feeding entirely.
- MTG cards eventually ran at about 28 cards/minute; the developer later reached
  33/minute and considered 30/minute sustainable.
- Some cards stuck on a platform because insufficient air entered beneath the flat
  card, creating more friction than gravity could overcome. The affected platforms
  had to be redesigned and reprinted.
- New Pokémon cards sometimes stuck, possibly from surface adhesion or static.
- Thicker/stiffer One Piece cards and smaller glossy Yu-Gi-Oh! cards required flat
  stock and additional load on the pressure roller in that prototype.
- Servo endpoints must be calibrated carefully to avoid stalled gears and heat.
- The developer built dedicated calibration and mechanical stress-test software
  before integrating recognition.

Software ideas include local on-device identification, local-network control from a
phone or computer, reusable sort presets, an explicit unknown route, configurable
price sources, and game-specific metadata rules. A second lighting mode was being
tested for foil detection.

**Lesson for us:** tiered gravity routing supports the small-sorter concept, but
flat printed surfaces need deliberate air relief and every additional platform adds
actuators and calibration. The feeder history strongly supports our separate
singulation milestone.

## Mault / Magic Vault

**Sources:** [source repository](https://github.com/dishwasher-detergent/mault),
[MakerWorld model](https://makerworld.com/en/models/3066180-tcg-card-sorting-machine)

Mault is a current open-source scanner/sorter with editable Fusion 360 source and a
print-ready 3MF. The model is designed to be printable even on a Bambu A1 Mini,
with a modified bin arrangement. The software is MIT-licensed; the hardware models
have a separate CC BY-NC-SA 4.0 license.

Its feed mechanism is a continuous-rotation servo driving a roller with six rubber
O-rings. The hopper includes an adjustable wall/roller loaded by a spring and screw;
the builder tunes it to pass one card. An IR sensor reports hopper state. Camera
capture waits for a card to settle in a calibrated region.

Sorting uses repeated modules arranged as a staircase. Each module contains:

- A bottom trapdoor that passes an unmatched card to the next module
- A paired side-paddle mechanism
- A pusher capable of sending a selected card left or right
- Three positional SG90 servos
- One IR sensor at the module gate

The published three-module build therefore uses nine positional servos, one
continuous feeder servo, four IR sensors, a PCA9685 servo board, a controller,
external 6 V power, and numerous fasteners. The structure is mechanically modular,
but cost, wiring, calibration, and failure modes grow with module count.

The software is more ambitious than most hobby builds. It provides configurable
rule trees, multiple games and collections, scan history, live monitoring, Discord
notifications, draggable camera-region calibration, hardware calibration, and
hosted or fully self-hosted operation. Recognition uses SigLIP embeddings and
PostgreSQL with pgvector. The local installation works offline but is a much larger
software stack than a simple desktop application.

**Lesson for us:** Mault demonstrates compact modular routing and excellent
calibration UX. It also shows why our designs should use one low-inertia selector
instead of three actuators for every pair of destinations.

## Project-O

**Sources:** [project page](https://www.christopherrichter.de/projects/project-o),
[repository](https://github.com/rurfy/project-o),
[hardware guide](https://github.com/rurfy/project-o/blob/master/docs/hardware.md)

Project-O is the closest public match to our medium sorter. It documents ten radix
bins plus reject in a circular ring approximately 340 mm in outside diameter. A
central column holds the hopper and camera window; an SG90 swiper presents the
bottom card; a continuous-rotation servo turns a lightweight chute; and a slotted
encoder wheel with an IR sensor supplies position feedback.

The guide claims a 2–3 second cycle with about 200 ms recognition and roughly
500 ms worst-case chute travel. It uses a six-pass least-significant-digit radix
sort over a canonical One Piece set/card key. Between passes, the operator collects
digit bins in order and reloads the stack.

Published physical estimates include:

- Ten normal bins plus a visibly distinct reject bin
- About 150 mm radius / 340 mm outside diameter
- Approximately 100 cards per bin and 200 in the hopper
- Four snap-fit bin-ring segments sized for a 256 mm print bed
- Approximately 400 g of PLA, quoted at $8–12
- Approximately 14 print hours
- One ESP32, two servos, webcam, IR sensor, 5 V supply, acrylic window, and fasteners

The optical wheel has one wider home slot and ten ordinary index slots. This is an
inexpensive way to recover position after startup and avoid relying only on timed
continuous-servo movement.

The weakest documented area is the feeder. A 1.5 mm slot is described as the
default even though the guide acknowledges that two ordinary cards can fit. A
flexible printed finger is intended to hold the following card, while sleeved cards
need a different gap. No published long-duration singulation result was found.

The repository was small and new at review time, with no license file visible.
Treat it as a valuable design reference, not independently validated hardware and
not material that can automatically be copied.

**Lesson for us:** the radial chute, segmented ring, dedicated reject, operator-led
radix process, and cheap position index all support the medium design. Its feeder
weakness is exactly where our stationary vacuum edge peel could contribute.

## BBG TCG Sorter

**Sources:** [software repository](https://github.com/ItsN80/bbg-tcg-sorter),
[paid model listing](https://www.etsy.com/listing/4357367379/mtg-card-sorter-stl-files-raspberry-pi)

BBG routes cards through nine configurable bins and one catch-all reject bin. Its
software is AGPLv3, while the printable model package and assembly material are a
$55 digital purchase at the review date.

The hardware list includes a Raspberry Pi 4 with camera, a PCA9685 driver, ten
micro servos, three small steppers with driver boards, two optical sensors,
addressable lighting, an external 5 V supply, and printed parts. Each of nine
flappers has an individually calibrated open/closed angle.

An especially good structural idea is using a standard IKEA Skådis pegboard as a
large, flat, inexpensive reference frame. This avoids printing one large flat panel
that could warp or accumulate dimensional error. The creator also publishes free
printer scale-test pieces before the user buys the model package.

The software offers configurable bin rules and a web UI. Recognition can use AWS,
a hosted DigitalOcean service, or an Ollama-compatible model. The creator notes
that hosted providers generally cost money, while local Ollama avoids per-scan fees
but may be slow and less accurate without capable hardware.

**Lesson for us:** standard flat reference hardware and a printable calibration
coupon are worth adopting as principles. The actuator count, required Pi, and
recognition-provider complexity illustrate costs our architecture should avoid.

## Fourteen-bucket rotational hobby build

**Source:** [creator's project post](https://www.reddit.com/r/magicTCG/comments/1jy5cj2/automated_mtg_card_sorter/)

This first-person build uses a central card stack surrounded by fourteen buckets.
A Raspberry Pi and Arduino pull one card into a photo chamber, send the image to an
external recognition server, and release it to a selected bucket. The creator says
it accepts ordinary cards and perfect-fit sleeves and had processed about 50,000
cards at the time of the post.

The recognition model was trained on augmented reference images plus a smaller set
of camera images. A separate classifier attempts foil detection. A REST API and web
interface combine physical sorting with scan history, collection management, and
deck-management functions.

The external server is important: the creator considered the Pi insufficient for
the chosen embedding model. That moves cost out of the machine but creates a
service dependency. Community questions also focused on a reported nine-second
cycle, damage risk, source capacity, multiple-pass handling, build cost, and whether
the design would be released.

No complete public build package was identified during this review.

**Lesson for us:** a radial layout can handle many destinations and sleeves, but a
local protocol should not require a remote recognition server. Inventory and deck
workflows are valuable companions to physical sorting.

## Timprovised sorter

**Source:** [creator's Raspberry Pi community post](https://www.reddit.com/r/raspberryDIY/comments/1ubg1gu/i_made_a_thing/)

This recent home build combines a Raspberry Pi 3B+, Arduino Nano, fixed-focus
camera, and salvaged stepper/rail hardware from a hobby laser. The creator reports
approximately four seconds per card and about 99% recognition accuracy, with nine
configurable normal bins and a tenth low-confidence reject route.

Recognition begins with an 8 × 8 image hash and uses OCR on the name region as a
tie-breaker. The interface saves bin presets, exports CSV, warns about full bins,
and can isolate high-value cards. The software is based on card identity and
metadata rather than being mechanically tied to MTG.

The most relevant mechanical detail is the creator's “singulator.” It mimics hand
dealing: one surface pushes while a pressure gate holds the next card. The creator
reports spending the first month and roughly thirty versions on this subsystem.

This build is partly enabled by salvaged hardware and had not yet become a released
open build at review time. The creator's stated aim is to beat the roughly $575
consumer price point.

**Lesson for us:** simple hashes plus OCR may be a strong low-compute recognition
baseline. More importantly, the feeder effort again validates building an isolated
singulation rig before the sorter.

## Open Sorts

**Source:** [Open Sorts repository and build notes](https://github.com/kbelenky/open_sorts)

Open Sorts is an older GPLv3 design built from LEGO and readily available
electronics. It uses two hopper stages, three motors, five reflective IR sensors,
an Arduino, and a host computer. Cards ultimately go to left or right baskets and
are reloaded in a prescribed order for repeated sorting passes.

The primary hopper is allowed to release multiple cards. The secondary hopper does
final singulation through an adjustable gap between powered lower wheels and fixed
upper wheels. After feeding, its motor briefly reverses to discourage a following
card. This separation of bulk presentation from final one-card metering is a useful
architecture even though its materials differ from ours.

The build notes expose several practical problems:

- The gap must be adjusted between double-feeding and stalling.
- The camera mount shifts when the machine moves, forcing perspective recalibration.
- Cards never land in precisely the same camera pose.
- LEGO and the electrical components were not cheap.
- The author suggested replacing the chassis with laser-cut or printed material.

The project explicitly warns about potential card damage and recommends testing
with disposable cards.

**Lesson for us:** two-stage separation and reverse/retard behavior are worth
testing. The fixed camera and structural reference must be substantially more rigid.

## Moss Machine

**Source:** [Moss Machine repository](https://github.com/KairiCollections/Moss-Machines-Magic-the-Gathering-sorting)

Moss Machine explores the feature-rich end of hobby construction. It documents a
34-tray system with X/Y/Z stepper motion, endstops, dual vacuum control, an Arduino
Mega, camera lighting, retry logic, periodic homing, and a desktop GUI. The
recognition system uses per-channel perceptual hashes, parallel workers, caching,
and a unified local database intended to support hundreds of card games.

This is innovative in recognition breadth, recovery controls, and tunability. It
also recreates the expensive gantry topology: each card incurs acquisition,
multi-axis travel, release, and return, while the machine needs many calibration
parameters and a large tray field.

**Lesson for us:** borrow confidence reporting, logs, local data, retries, and
periodic calibration concepts. Do not borrow the XYZ transport architecture for a
compact hobby machine.

## Adjacent low-cost tools

The [Ultimate Card Scanner Stand](https://makerworld.com/models/1110574-ultimate-card-scanner-stand-for-pokemon-mtg)
is manual rather than an automated sorter, but it reveals useful low-cost design
choices: a phone acts as the computer/camera, cards slide under gravity, sleeved and
unsleeved trays are interchangeable, and a bottom opening allows quick removal of
the scanned deck. Users report that white filament improves border detection and
that lighting/reflectivity remain significant.

Manual organizers also demonstrate that sloped compartments and card-width packing
can fit several piles into a small area without powered mechanisms. They are useful
references for detachable output magazines, not substitutes for a true sorter.

