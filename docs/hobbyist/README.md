# Hobbyist Card-Sorter Research

Last reviewed: **2026-09-06**

This folder preserves research into hobbyist, open-source, and 3D-printed trading-card
sorters. It records mechanisms worth studying, problems builders encountered, costs
that exclude ordinary collectors, desired applications, and implications for this
project's small and medium designs.

The sources include creator sites, source repositories, build guides, model-sharing
pages, and first-person community posts. Published specifications and reliability
numbers are creator claims unless explicitly described as independent results.

## Research documents

- [PROJECT_SURVEY.md](PROJECT_SURVEY.md) — detailed notes on each relevant build
- [COST_BARRIERS.md](COST_BARRIERS.md) — commercial price anchors and hidden DIY costs
- [USER_NEEDS.md](USER_NEEDS.md) — applications and expectations expressed by builders/users
- [DESIGN_IMPLICATIONS.md](DESIGN_IMPLICATIONS.md) — what the research means for our designs
- [SOURCES.md](SOURCES.md) — dated source ledger and licensing cautions

## Headline conclusions

1. **Singulation is the common hard problem.** Friction gaps oscillate between
   double-feeding and not feeding. Several builders spent substantial iteration on
   the feeder before the rest of the machine worked.
2. **Plastic is rarely the main cost.** Motors, motor count, cameras, dedicated
   computers, power electronics, failed iterations, software services, and the
   builder's time dominate.
3. **One moving selector is unusually cost-efficient.** Project-O's radial chute
   reaches ten sort bins plus reject with one feeder servo and one chute servo.
   This closely resembles our medium sorter.
4. **Stacked gravity routing is viable but surface design matters.** GlideSorter
   and Mault demonstrate compact tiered paths, while also exposing sticking,
   calibration, and actuator-count problems relevant to our small sorter.
5. **True ordering is rare.** Most projects perform one-pass categorization by
   price, color, rarity, type, or set. Project-O and Open Sorts are notable for
   using repeated distribution/radix passes to physically order cards.
6. **Offline ownership is a meaningful differentiator.** Users object to scan
   tokens and subscriptions, and some builds expose a choice between paid hosted
   recognition and slower local processing.
7. **Credible card-safety evidence is missing.** Community concern is driven by
   valuable-card damage. A published cycle log and inspection protocol would be a
   stronger contribution than another short successful demo.

## Project map

| Project | General topology | Outputs | Especially relevant to |
|---|---|---:|---|
| GlideSorter | Tiered gravity platforms | 6 + reject | Small sorter, feeder and chute friction |
| Mault | Modular staircase of trapdoors/paddles/pushers | Configurable; published guide uses 7 | Small sorter, modular outputs and calibration |
| Project-O | Rotating chute over a radial ring | 10 + reject | Medium sorter and radix sorting |
| BBG TCG Sorter | Sloped multi-flapper path on a rigid pegboard | 9 + reject | Low-cost framing and provider choice |
| 14-bucket hobby build | Rotational central-stack machine | 14 | Radial packaging, sleeves, inventory integration |
| Timprovised sorter | Linear rail/stack system with mechanical singulator | 9 + reject | Feeder iteration and user-facing presets |
| Open Sorts | Two-stage friction feed and binary routing | 2 | Separating bulk presentation from final singulation |
| Moss Machine | XYZ gantry with vacuum and many trays | 34 | Feature ceiling and complexity to avoid |

## How to use this research

The documents are design input, not a mandate to copy another machine. Before
reusing geometry or code, check the source's current license. Reproduce useful
principles with original implementation unless the license is explicitly compatible
with this project's intended open-source terms.

Convert research observations into requirements and experiments through
[../DESIGN_ASSURANCE.md](../DESIGN_ASSURANCE.md). The integrated design response is
recorded in [../../designs/S4_UNIFIED_CARD_PATH.md](../../designs/S4_UNIFIED_CARD_PATH.md).
