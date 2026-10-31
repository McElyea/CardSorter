# Purchased-Parts Price Estimate

Prices gathered **2026-10-31**, in **US dollars**, from US-facing retailers, before
tax and shipping. They cover parts you buy, not parts you print. This is an
estimate for planning the [R8 design](../designs/R8_RELIABLE_SORTER.md) and its
[feeder bench](../hardware/prototypes/FEEDER_COMPARISON.md), not a released bill of
materials. Recheck every price before ordering.

Each range runs from the lowest to the highest credible listing found. **L** means
the price was looked up (see Sources); **E** means an estimate that was not looked
up. Several retailer pages were undated and may be stale; those are noted.

## Summary

| Scope | Low | High |
|---|---:|---:|
| **Full R8 machine** (R-A router, 9 × 500-card pockets) | **$822** | **$1,309** |
| **Milestone 0 feeder bench** | **$333** | **$557** |

Not included: the host computer (owner-supplied), printed parts and filament, tools,
shipping, tax, minimum pack quantities, and spares or failed parts. The earlier
design review's cost-reporting rule asks for three totals; this is the first
("incremental build: owner already has a printer, tools, and host computer").

The biggest cost drivers are the hopper and pocket followers ($216–303), the
urethane rollers ($120–161), and imaging ($80–130). These are where the
reliability-first choices cost money; see "Ways to reduce cost" below.

## Full machine

### Motion and control — $109–173

| Item | Qty | Unit | Extended | Basis |
|---|---:|---:|---:|---|
| RP2040 board with 4 × TMC2209 (BTT SKR Pico) | 1 | $32.99–49.85 | $32.99–49.85 | L |
| NEMA 17 stepper, 59 Ncm (StepperOnline 17HS19-2004S1): transport, pick, router head | 3 | $9.62–14.30 | $28.86–42.90 | L, store page may be stale |
| NEMA 14 stepper (14HS13-0804S): head exit nip | 1 | $8.48–13.05 | $8.48–13.05 | L, may be stale |
| I²C input expander (MCP23017 breakout) | 1 | $3–7 | $3.00–7.00 | E |
| 24 V 150 W supply (Mean Well LRS-150-24) | 1 | $18.40–27.00 | $18.40–27.00 | L |
| Fused IEC inlet with switch, mains cord | 1 | $8–15 | $8.00–15.00 | E |
| Emergency stop, 22 mm mushroom | 1 | $8.95–17.99 | $8.95–17.99 | L |

### Sensing and imaging — $126–203

| Item | Qty | Unit | Extended | Basis |
|---|---:|---:|---:|---|
| Global-shutter USB camera (Arducam OV9281, B0332) | 1 | $49.99–85.00 | $49.99–85.00 | L, Arducam page is old |
| 24 V CRI-90 COB LED strip, 5 m reel (uses under 1 m) | 1 | $28–40 | $28.00–40.00 | L |
| Logic-level MOSFET module (strobe banks) | 2 | $1.00–2.50 | $2.00–5.00 | E |
| IR break-beam sensor pair, 3 mm | 8 | $2.95–4.45 | $23.60–35.60 | L |
| Microswitches (pocket full, cover interlock), pack | 1 | $8–15 | $8.00–15.00 | E |
| Analog Hall sensor (TI DRV5053) | 2 | $0.61–1.31 | $1.22–2.62 | L |
| Neodymium magnet assortment | 1 | $5–10 | $5.00–10.00 | E |
| AS5600 magnetic encoder board (slip) | 1 | $7.99–10.00 | $7.99–10.00 | L |

### Card path mechanics — $262–415

| Item | Qty | Unit | Extended | Basis |
|---|---:|---:|---:|---|
| Urethane feed roller with aluminum insert (SDP/SI) | 12 | $10.00–13.41 | $120.00–160.92 | L high ($13.41, 8-week lead time); low is E |
| Scanner pick + brake roller set, aftermarket (fi-7000 series) | 1 | $13.80–34.11 | $13.80–34.11 | L; genuine kit about £71–122 |
| 8 mm steel rod, 300 mm (nip shafts) | 8 | $4.40–6.93 | $35.20–55.44 | L |
| 608ZZ bearings, 10-pack | 3 | $7.95–8.88 | $23.85–26.64 | L |
| GT2 pulley, 20 tooth, 8 mm bore | 9 | $3.99–7.95 | $35.91–71.55 | L |
| GT2 6 mm belt, 5 m | 1 | $12–25 | $12.00–25.00 | L |
| GT2 idler pulley | 4 | $2–4 | $8.00–16.00 | E |
| 8 mm shaft collar | 12 | $0.70–1.25 | $8.40–15.00 | E |
| 6 in lazy susan bearing (router head) | 1 | $5.15–9.99 | $5.15–9.99 | L |

### Hopper and pockets — $216–303

| Item | Qty | Unit | Extended | Basis |
|---|---:|---:|---:|---|
| Constant-force spring (hopper + 9 pockets) | 10 | $9.06–12.00 | $90.60–120.00 | L low (5-pack); high is E |
| 8 mm steel rod, 300 mm (follower guides) | 20 | $4.40–6.93 | $88.00–138.60 | L |
| LM8UU linear bearing | 20 | $1.89–2.20 | $37.80–44.00 | L |

### Frame and hardware — $109–216

| Item | Qty | Unit | Extended | Basis |
|---|---:|---:|---:|---|
| 2020 aluminum extrusion, 500 mm | 10 | $3–7 | $30.00–70.00 | E (listed prices did not state length clearly) |
| 2020 corner brackets with T-nuts, kit | 1 | $25–50 | $25.00–50.00 | L high; low is E |
| M3/M5 screw and nut assortment | 1 | $20–30 | $20.00–30.00 | E |
| M3 heat-set inserts, 100 | 1 | $9–26 | $9.00–26.00 | L (CHF and EUR listings, converted roughly) |
| Wire, connectors, crimp terminals | 1 | $20–30 | $20.00–30.00 | E |
| USB cable | 1 | $5–10 | $5.00–10.00 | E |

## Milestone 0 feeder bench — $333–557

The bench needs a subset: the board, 2 NEMA 17 steppers (pick and first nip),
supply, inlet, e-stop, 4 urethane rollers, the pick/brake roller set, 6 rods,
one 608ZZ pack, 2 LM8UU, 4 pulleys, a belt, 2 constant-force springs, 3 beam
sensors, a Hall sensor, magnets, the AS5600, 2 lengths of 2020, the bracket kit,
fasteners, inserts, wire, and a USB cable. Most of this carries into the full
machine. Pack sizes (for example, constant-force springs sold in fives) can raise
the first order.

## Options and alternatives

| Item | Cost | When it applies |
|---|---:|---|
| Through-transmission ultrasonic double-sheet detector | about $285–1,520 (Pepperl+Fuchs list about $505) | Only if the Hall idler fails the challenge matrix |
| Vacuum comparison kit: diaphragm pump, vent valve, pressure sensor, tubing | about $40–70 (E) | Only for the V1 feeder comparison |
| Motorized hopper lift (P2): extra NEMA 17 plus lead screw | about $20–35 (E) | Only if the constant-force follower drifts |
| Router R-B: one gate actuator per output instead of the rotary head | about $45–135 for 9 solenoids (E), replacing about $23–37 of head motors and bearing | If the bend test selects R-B |
| 250-card pockets instead of 500 | saves roughly $40–70 in rods (E) | If the 450–500 mm footprint is too large |

## Tools for a new builder

Not looked up; rough estimate **$105–210**: soldering iron with heat-set insert
tips, crimper, digital calipers, multimeter, and hex drivers.

## Ways to reduce cost

- **Rollers:** urethane tubing sleeved over printed or aluminum hubs could replace
  some purchased rollers. Test for consistency before adopting; this is exactly
  the variation the rework is trying to remove.
- **Followers:** one rod plus a keyed printed slide per pocket instead of two rods.
  Measure follower force drift before and after.
- **Pocket count and size:** fewer or smaller pockets reduce springs, rods, and
  bearings, at the cost of more passes or visits.
- **LED strip:** a single 1 m length or LED bar instead of a 5 m reel.

## Sources

Retrieved 2026-10-31. Third-party marketplace listings were used only as ranges.

- BTT SKR Pico: [cnx-software launch price](https://www.cnx-software.com/2022/01/27/btt-skr-pico-a-raspberry-pi-rp2040-based-3d-printer-control-board/?amp=1), [Fabreeko listing](https://m.reach.dog/shop/fabreeko/products/btt-pico-board), [SpecPicks Amazon tracker](https://specpicks.com/product/B09MYKL9MP)
- NEMA 17: [StepperOnline 17HS19-2004S1](https://omc-stepperonline.com/nema-17-bipolar-59ncm-84oz-in-2a-42x48mm-4-wires-w-1m-cable-and-connector.html), [eBay US](https://www.ebay.com/p/23027417399)
- NEMA 14: [StepperOnline 14HS13-0804S](https://www.omc-stepperonline.com/nema-14-bipolar-1-8deg-18ncm-25-5oz-in-0-8a-5-4v-35x35x34mm-4-wires-14hs13-0804s)
- Mean Well LRS-150-24: [Digi-Key](https://www.digikey.com.br/en/products/detail/mean-well-usa-inc/LRS-150-24/7705015)
- E-stop: [Zoro Dayton 22 mm](https://www.zoro.com/dayton-emergency-stop-push-button-22-mm-1no1nc-red-30g254/i/G4985583/)
- Camera: [Arducam B0332](https://www.arducam.com/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi.html), [Fruugo listing](https://www.fruugo.ca/ov9281-1mp-usb-camera-module-for-raspberry-pi-compact-usb-global-shutter-ideal-for-robotics-and-vision-projects/p-419649911)
- LED strip: [Toolboom 24 V RA90 COB](https://toolboom.com/en/cob-led-strip-light-480-leds-ra90-cool-white-dc-24v-5-m), [Connevans](https://media.connevans.co.uk/product/38802888/MX156665/Cool-White--CW--IP20-24V-Seamless-COB-LED-Strip-5m)
- IR break-beam: [Adafruit 2167](https://www.adafruit.com/product/2167), [Jameco](https://www.jameco.com/z/2167-Adafruit-Industries-IR-Break-Beam-Sensors-with-Premium-Wire-Header-Ends-3mm-LEDs_2508431.html)
- DRV5053: [Digi-Key](https://www.digikey.com/en/products/detail/texas-instruments/DRV5053EAQDBZR/5015735)
- AS5600: [Walmart listing](https://www.walmart.com/ip/AS5600-Magnetic-Encoder-Module-Magnetic-Induction-Angle-Measurement-Sensor-Module-FOC-12Bit-High-Precision-Sensor/13679563896)
- Urethane rollers: [SDP/SI A 7T 5MUR2510](https://shop.sdp-si.com/a-7t-5mur2510.html)
- Scanner rollers: [eBay pick/brake rollers](https://www.ebay.de/itm/252804980081), [eBay roller and shaft kit](https://www.ebay.de/itm/177193649341), [genuine kit CON-3670-400K](https://www.thescannershop.com/consumable-kit-for-fujitsu-fi-7000-series/)
- 8 mm rods and LM8UU: [Makerstore smooth rod](https://makerstore.cc/product-tag/smooth-rod/), [Prusa LM8UU](https://www.prusa3d.com/pl/produkt/linear-bearing-lm8uu/)
- 608ZZ: [VXB 10-pack](https://vxb.com/products/10-pack-608zz-bearing-8x22x7-sealed-ball-bearings)
- GT2 pulley and belt: [Adafruit pulley](https://adafruit.com/product/1252), [PB Select pulley](https://www.partsbuilt.com/gt2-pulley-r2-c2-robo), [Zyltech belt](https://www.zyltech.com/steel-reinforced-gt2-t2-timing-belt-6mm)
- Lazy susan bearing: [Bearwood 6 in](https://bearwood.com/product4929.html), [Zoro 6 in](https://www.zoro.com/triangle-mfg-co-square-6-in-steel-lazy-susan-ball-bearing-swivel-4006c/i/G305831092/)
- Constant-force springs: [Zoro 5-pack](https://www.zoro.com/spec-constant-force-spring-301-ss-pk5-cf0250052/i/G012748027/), [McMaster-Carr catalog](https://www.mcmaster.com/products/ribbon-springs)
- 2020 extrusion and brackets: [OpenBuilds V-Slot 20x20](https://us.openbuilds.com/v-slot-20x20-linear-rail), [Home Depot bracket kit](https://www.homedepot.com/p/KIWDZFU-10Sets-2020-Corner-Bracket-Connectors-for-Aluminum-Extrusion-Profile-6mm-Slot-Industrial-Projects-Silver-22PH005323/336433971)
- Heat-set inserts: [CNC Kitchen at 3DJake](https://www.3djake.com/cnc-kitchen/heat-set-insert-for-m3-threaded-inserts)
- Ultrasonic double-sheet: [Pepperl+Fuchs Canada](https://pepperl-fuchs.com/canada/en/classid_188.htm), [Wolf Automation](https://www.wolfautomation.com/ultrasonic-sensor-double-sheet-detector-3-pnpxno), [L-com](https://www.l-com.com/ultrasonic-double-sheet-sensor-cylindrical-m18-threaded-ni-plated-brass-3-pnp-nc-sensing-range-20-60-mm-2-m-flying-lead-cable-pxus-184003e3)
