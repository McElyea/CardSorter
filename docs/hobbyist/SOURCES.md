# Source Ledger

Last reviewed: **2026-09-06**

This ledger records the primary pages used for the hobbyist survey. Prices,
development status, availability, repository contents, and licenses can change.
Recheck the original source before making purchasing, licensing, or public-market
claims.

## Hobbyist and open-source projects

| Source | Type | Used for | Cautions |
|---|---|---|---|
| [GlideSorter home](https://glidesorter.com/) | Creator site | Published size, capacity, routes, rate, local recognition, estimated kit price, timeline | Product remains in development; numbers are targets/claims |
| [GlideSorter hardware test](https://glidesorter.com/en/blog/read/4-hardware-sorting-test) | Creator build log | Doubles, gap tuning, card variation, weights, achieved test rate | First-party observations, not independent testing |
| [GlideSorter calibration](https://glidesorter.com/en/blog/read/3-let-the-calibration-begin) | Creator build log | Actuator/sensor counts, servo calibration, platform sticking and reprint | First-party observations |
| [GlideSorter presets](https://glidesorter.com/en/blog/read/5-main-app-interface-and-sorting-presets) | Creator build log | Desired sort modes and local-network UI | Some features were planned at publication |
| [Mault repository](https://github.com/dishwasher-detergent/mault) | Source/build repository | Mechanism, software stack, self-hosting, protocol, calibration, model source | Fast-moving project; root software license and CAD license differ |
| [Mault MakerWorld model](https://makerworld.com/en/models/3066180-tcg-card-sorting-machine) | Creator model page | Printability, model availability, A1 Mini variation | Community model page; verify latest revision |
| [Project-O creator page](https://www.christopherrichter.de/projects/project-o) | Creator portfolio | Architecture and algorithm summary | High-level first-party description |
| [Project-O repository](https://github.com/rurfy/project-o) | Source/build repository | Radix controller, CAD/source structure, route count | New/small repository; no license file was visible at review time |
| [Project-O hardware guide](https://github.com/rurfy/project-o/blob/master/docs/hardware.md) | Build guide | Dimensions, BOM, print estimate, chute, encoder, feeder details | Documented estimates and claims were not independently validated |
| [BBG repository](https://github.com/ItsN80/bbg-tcg-sorter) | Source/build repository | Hardware list, software, provider choices, calibration | Printable geometry is not included under the same open repository terms |
| [BBG model listing](https://www.etsy.com/listing/4357367379/mtg-card-sorter-stl-files-raspberry-pi) | Creator sales page | $55 file price, pegboard frame, print test, local/hosted recognition choices | Digital files only; price can change |
| [Fourteen-bucket sorter post](https://www.reddit.com/r/magicTCG/comments/1jy5cj2/automated_mtg_card_sorter/) | First-person creator post and discussion | Radial machine, perfect-fit sleeves, external recognition, inventory tools, claimed 50k scans, user concerns | No complete public build was found; comments mix creator and community claims |
| [Timprovised sorter post](https://www.reddit.com/r/raspberryDIY/comments/1ubg1gu/i_made_a_thing/) | First-person creator post and discussion | Singulator iterations, salvaged hardware, hash/OCR approach, presets, rate | Recent evolving build; source/build package not yet identified |
| [Open Sorts repository](https://github.com/kbelenky/open_sorts) | Source/build repository | Two-stage feed, gap adjustment, sensors, reload workflow, calibration issues | Older design; LEGO rather than printed chassis |
| [Moss Machine repository](https://github.com/KairiCollections/Moss-Machines-Magic-the-Gathering-sorting) | Source/build repository | Large gantry comparison, local database, recognition/retry concepts | Very broad claims; calibration/build responsibility remains with user |
| [Ultimate Card Scanner Stand](https://makerworld.com/models/1110574-ultimate-card-scanner-stand-for-pokemon-mtg) | Model/community page | Manual low-cost workflow, removable sleeve trays, white background, deck removal | Scanner stand, not an automatic physical sorter |

## Commercial and cost references

| Source | Used for | Cautions |
|---|---|---|
| [CardMill preorder](https://cardmill.backerkit.com/hosted_preorders) | Current preorder tiers, accessories, estimated shipping date | Crowdfunded product; specifications and delivery can change |
| [CardMill FAQ](https://cardmill.backerkit.com/faq) | Shipping estimate and workflow details | Dated FAQ; recheck before quoting |
| [TCGplayer Roca Sifter announcement](https://seller.tcgplayer.com/press-center/tcgplayer-expands-suite-of-card-sorting-devices-with-launch-of-roca-sifter) | $799 MSRP and $300 annual plan | Seller-focused product; pricing may change |
| [SortSwift Super Sorter](https://sortswift.com/features/super-sorter) | $8,999 Mini, $24,999 full model, $199/month machine plan | Vendor claims and current pricing |
| [Magic Sorter software](https://magic-sorter.com/the-software) | €90/3 months, €165/6 months, €300/year | Software subscription only |
| [Raspberry Pi 4 product brief](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008344-DS-1-raspberry-pi-4-product-brief) | April 2026 list prices | Board only; excludes accessories, taxes, and shipping |
| [Adafruit ESP32 development board](https://www.adafruit.com/product/3269) | $15 reference price for a mainstream ESP32 board | Other compatible boards may cost less or more |
| [Adafruit continuous micro servo](https://www.adafruit.com/product/2442) | $7.50 reference and current/torque information | One representative branded part, not a required selection |

## Licensing notes observed at review time

- Mault software: MIT.
- Mault `3d model` directory: CC BY-NC-SA 4.0.
- BBG software: AGPLv3; printable files sold separately.
- Open Sorts: GPLv3.
- Moss Machine repository states CC BY-NC-SA 4.0.
- Project-O: no license file visible in the reviewed repository.

These notes are not legal advice. A repository being public does not grant a right
to copy unlicensed material. Preserve attribution and keep our implementation
original unless compatibility is deliberately reviewed.

## Local research snapshot

For closer inspection during this review, public repositories were cloned into
[`references/hobbyist-projects`](../../references/hobbyist-projects). They are local
third-party research snapshots, not CardSorter source. Recorded revisions:

- Mault: `0a0fe54f5f82644c8dacb21bd218fc835b1c9b58`
- Project-O: `5e8726f6f8c5c9944cc7d37541bdf87f4ca4d3f4`

Future reviews should record new revisions and summarize material changes instead
of silently replacing this dated snapshot.

## 2026-10-31 design-review additions

The [design review](../reviews/2026-10-31_DESIGN_REVIEW.md) records the supplied sort
simulation, reproduced results, and revised design decisions. Primary technical
references consulted in that review:

- [Bayer's combinatorics notes](https://www.math.columbia.edu/~bayer/S02/combinatorics/notes.1.31.pdf): rising sequences and inverse descents.
- [Ricoh scanner layout](https://www.pfu.ricoh.com/global/scanners/erg/cleaning-7030.html): pick/brake rollers and ultrasonic sensors; archived precedent.
- [Ricoh multifeed conditions](https://www.pfu.ricoh.com/global/scanners/erg/conditions-7030.html): material-specific limits and false detections; archived model-specific guidance.

These support experiments and mathematical analysis. They do not qualify any
component for safe trading-card handling or establish a current price.
