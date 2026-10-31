# Cost Barriers

Last reviewed: **2026-09-06**

## Commercial price anchors

These prices explain why hobbyists continue building their own machines. They are a
dated snapshot and should be rechecked before using them in any public comparison.

| Product/project | Price at review | Additional cost or status | Source |
|---|---:|---|---|
| CardMill Starter | $575 preorder | Estimated January 2027 fulfillment; shipping estimated separately at $40–60 in the continental US | [BackerKit preorder](https://cardmill.backerkit.com/hosted_preorders), [FAQ](https://cardmill.backerkit.com/faq) |
| CardMill Heavy Lifter | $750 preorder | Same crowdfunding/fulfillment caveat | [BackerKit preorder](https://cardmill.backerkit.com/hosted_preorders) |
| Roca Sifter | $799 | $300/year subscription | [TCGplayer announcement](https://seller.tcgplayer.com/press-center/tcgplayer-expands-suite-of-card-sorting-devices-with-launch-of-roca-sifter) |
| SortSwift Super Sorter Mini | $8,999 | $199/month machine-recognition subscription | [SortSwift](https://sortswift.com/features/super-sorter) |
| SortSwift Super Sorter | $24,999 | $199/month machine-recognition subscription | [SortSwift](https://sortswift.com/features/super-sorter) |
| Magic Sorter software | €300/year | Recognition/software subscription; hardware purchase is separate | [Magic Sorter](https://magic-sorter.com/the-software) |
| GlideSorter planned kit | Approximately €1,500 | Still in development/closed testing; estimate may change | [GlideSorter](https://glidesorter.com/) |
| BBG printable files | $55 | Digital geometry/build package only; electronics, printing, Pi, and recognition remain | [Etsy listing](https://www.etsy.com/listing/4357367379/mtg-card-sorter-stl-files-raspberry-pi) |

CardMill is the nearest announced mainstream consumer price, but it is still a
crowdfunded preorder rather than an ordinary in-stock machine. A hobby builder
explicitly described $575 as the price he wanted to beat. Other community members
said they would pay a reasonable one-time amount but were tired of subscription or
scan-token systems.

## Why printed machines still become expensive

### 1. Actuator count

An inexpensive servo is cheap only once. Examples from current projects:

- Project-O: one feeder servo plus one rotating-chute servo
- Mault: three positional servos per sorting module plus one feeder servo
- GlideSorter: nine platform servos plus two continuous-rotation motors
- BBG: ten servos plus three stepper motors
- Moss Machine: multiple XYZ and feeder motors, endstops, and vacuum controls

Actuators also incur driver channels, power capacity, wiring, fasteners, calibration,
noise, heat, replacements, and new failure modes. Reducing output actuator count is
therefore more important than saving a small amount of filament.

### 2. Dedicated computation

BBG specifies a 4 GB Raspberry Pi 4. Raspberry Pi's April 2026 product brief lists
that model at $100 before storage, camera, power supply, case, or cooling. By
comparison, an ESP32 development board is available around $15 from a mainstream
maker supplier. Sources: [Raspberry Pi product brief](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008344-DS-1-raspberry-pi-4-product-brief),
[ESP32 board](https://www.adafruit.com/product/3269).

This supports our split architecture: a low-cost controller manages real-time
motion and safety, while the owner supplies an existing PC, mini PC, or optional Pi
for recognition and workflow.

### 3. Recognition services

BBG documents that AWS Rekognition and remotely hosted alternatives normally incur
usage cost. Local Ollama eliminates the fee but can be slow and less accurate on a
Pi without a GPU. Magic Sorter and commercial machines demonstrate how recognition
can become a permanent subscription attached to otherwise-owned hardware.

Offline recognition is therefore both an ownership principle and a cost-control
feature. Online pricing and database updates can remain optional.

### 4. Mechanical iteration

Printed prototypes hide costs in failed parts and labor:

- GlideSorter redesigned and reprinted all sorting platforms after discovering
  that cards could stick instead of sliding.
- Its feeder needed repeated separator changes to balance doubles against stalls.
- Timprovised's creator reports roughly thirty singulator iterations.
- Large printed frames can warp or accumulate scale error; BBG used a commodity
  pegboard as the dimensional backbone to avoid that problem.

Small, interchangeable test coupons for shoes, rollers, retard pads, ramps, and
gate surfaces reduce both filament waste and rebuild time.

### 5. Tools and sourcing

A complete build cost includes more than the published electronics:

- Printer access and filament
- Failed-print allowance
- Soldering iron, insert tips, crimper, wire tools, calipers, and multimeter
- Fastener assortments, inserts, wire, connectors, tubing, and spares
- Camera, lighting, power supplies, storage, and cables
- Shipping, taxes, and minimum package quantities
- A computer capable of the selected recognition method
- Assembly, calibration, troubleshooting, and maintenance time

Projects often publish a parts list without a total landed cost. Our project should
publish both, with prices dated and region identified.

### 6. Risk to the cards

For collectors, a damaged card can cost more than the machine. Community comments
repeatedly express fear of using home-built devices on anything except bulk cards.
That risk blocks adoption even if the hardware is inexpensive.

The appropriate response is evidence: documented contact forces where practical,
high-resolution before/after inspection, diverse stock and sleeve tests, fault
photographs, and long cycle runs with zero *undetected* doubles or damage.

### 7. Human operating cost

Throughput and workflow determine whether an inexpensive sorter saves time:

- Four seconds per card is 15 minutes for 225 cards before reload activity.
- Nine seconds per card is 30 minutes for 200 cards.
- Multipass sorting multiplies physical card cycles and requires reliable bin-order
  preservation.
- A confusing reload instruction can invalidate an entire sort.

Output count is therefore a user-time tradeoff, not merely a hardware feature. The
small and medium machines should be compared using total session time, including
collection and reload—not cards per minute alone.

## What appears inexpensive

Project-O's guide estimates approximately 400 g of PLA ($8–12) and 14 print hours.
Its electronics list is only an ESP32, two servos, webcam, sensor, power supply, and
small hardware. It does not publish a complete purchased-cost total, so this is not
proof of a final price. It does demonstrate that a radial single-selector machine
can make plastic and motor count comparatively minor.

## Cost-reporting requirements for our project

Publish at least three separate totals:

1. **Incremental build:** owner already has a printer, tools, and host computer.
2. **New hobbyist build:** includes tools, reasonable minimum order quantities, and
   failed-print allowance.
3. **Turnkey kit equivalent:** printed parts, prepared wiring, tested electronics,
   packaging, and assembly/support labor.

Each total should separate the shared feeder/imaging engine, the small four-way
output module, and the medium eight-way output module. Recurring core fees should
remain zero.

