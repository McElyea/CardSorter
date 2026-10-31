# User Needs and Applications

Last reviewed: **2026-09-06**

This list combines features implemented by hobbyist projects with needs expressed
in their community discussions. It distinguishes what users appear to want from
what current machines reliably provide.

## Core job

The common request is simple: load a stack, let the machine identify every card,
physically route the cards, and receive a usable inventory record without handling
each card manually.

Users distinguish several levels of value:

1. **Scan:** identify and catalog each card.
2. **Sift:** separate cards into a few useful categories.
3. **Sort:** produce deterministic physical order, potentially over multiple passes.

Most hobby machines currently reach the first two. True ordering is less common
and is the clearest opportunity for our project.

## Frequently requested sorting applications

- Pull cards above a configurable market-value threshold for sleeving or sale.
- Separate rarity, color, type, mana value, set, finish, or game mechanics.
- Alphabetize by name.
- Order by set and collector number.
- Find one requested card or a list of cards for a deck.
- Separate duplicates, tokens, lands, promos, unknowns, and special treatments.
- Recover a mixed collection after boxes or shelves are disturbed.
- Process bulk collections that have remained unsorted because manual work is too
  time-consuming.
- Create price tiers or purchasing/buylist piles for a small store.

Price is a volatile property. A price-based sort requires an optional fresh data
source, while permanent attributes such as set and collector number must continue
working from the local database.

## Inventory and software applications

- Export CSV compatible with collection, marketplace, or deck-building tools.
- Preserve a searchable scan history with canonical card identifiers.
- Maintain separate collections for an owner, friend, club, or store.
- Save and reuse named bin presets.
- Track collection value without making current prices part of machine control.
- Monitor a long run from another local device.
- Notify on jam, reject, empty hopper, full bin, or completion.
- Pause and resume without losing the physical/digital correspondence.
- Record exactly why a card was rejected and allow manual correction.
- Simulate a sorting plan without hardware.

Mault, BBG, GlideSorter, the fourteen-bucket project, and Timprovised all combine
physical sorting with some subset of these workflow features. The software should
therefore be treated as an ownership and recovery system, not just a start button.

## Hardware expectations

- Accept a useful unattended stack rather than requiring hand feeding.
- Reject uncertain cards instead of contaminating a known-good bin.
- Avoid visible edge, face, corner, or sleeve damage.
- Provide quick, obvious jam access.
- Keep cards in a stable orientation and preserve arrival order.
- Make bin-full state visible or detectable.
- Support ordinary 63 × 88 mm trading cards first.
- Add perfect-fit and common sleeve support where testing proves it safe.
- Allow hopper and output capacity to change without replacing the core machine.
- Fit on a home desk and remain tolerable in noise and appearance.

Sleeve support is especially valuable because users are reluctant to remove
protection from expensive cards. It is also mechanically difficult: sleeves change
thickness, friction, static, dimensions, stiffness, and edge behavior. It should be
a tested compatibility profile, not a vague claim.

## Ownership expectations

Community responses consistently favor:

- A reasonable one-time hardware cost
- No mandatory subscription or scan tokens
- Operation without an Internet connection
- Open software and preferably editable source CAD
- Replaceable commodity electronics
- Ability to modify rules and add games
- A build guide complete enough for someone other than the designer
- Transparent limitations and failure data

Users also care about license terms. “Files available” is not equivalent to open
source if the source CAD is missing, commercial use is prohibited, or only the
software—not the hardware—is openly licensed.

## User groups inferred from the discussions

### Home collector

Values low price, small footprint, card safety, offline operation, saved presets,
and true organization. May accept slower throughput and more passes if the machine
can be left alone safely.

### Bulk collector or reseller

Values unattended capacity, price/rarity extraction, inventory export, reject
handling, and total session throughput. May prefer the medium sorter to reduce
reloads.

### Local game store or club

Values repeatable workflows, multiple users/collections, notifications, maintenance
access, and high card volume. Commercial machines target this group, but their
capital and recurring costs exclude many small stores.

### Maker and contributor

Values commodity parts, editable CAD, documented interfaces, calibration tools,
test fixtures, local APIs, and the ability to improve a module without rebuilding
the whole system.

## Product opportunities

1. A compact machine that performs **true multipass physical ordering**, not only
   one-pass categorization.
2. A feeder with published long-run reliability across real card conditions.
3. One shared engine with small and medium output modules.
4. Offline local recognition that can optionally use a more powerful existing PC.
5. An operator interface that makes multipass reload order nearly impossible to
   misunderstand.
6. A transparent, region-specific, all-in cost model.

