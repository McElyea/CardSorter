# Design Assurance and Evidence-to-Test Process

## Purpose

Hobbyist research should become a verification program rather than an inspiration
board. Every material observation should result in a requirement, prototype
experiment, monitored risk, or documented rejected choice.

The [2026-10-31 review](reviews/2026-10-31_DESIGN_REVIEW.md) reopens feeder selection,
adds capacity/operator workload to the gates, and separates name recognition from
exact-printing correctness. Mathematical simulation is not physical validation.

This process connects the dated research in `docs/hobbyist` to the S4 design and
helps prevent attractive mechanisms from advancing without evidence.

## Standard evidence record

For every useful external observation, record:

- Source and revision or review date
- Mechanism being discussed
- Observed failure or claimed benefit
- Card, stack, calibration, and environmental conditions
- Builder's stated or inferred cause
- Workaround or design revision
- Evidence quality
- Possible S4 manifestation
- Proposed design control
- Experiment and acceptance criterion
- Result and resulting decision

### Evidence levels

1. Published measurements, logs, or independently repeatable results
2. Working source, CAD, and reproducible build instructions
3. Detailed first-person build report
4. Short demonstration or community anecdote
5. Promotional or unsupported claim

Lower-quality evidence can identify a risk, but it cannot close that risk.

## Initial evidence-to-design map

| Hobbyist lesson | S4 risk | Current response | Required proof |
|---|---|---|---|
| Friction gaps alternate between no-feed and doubles | Silent two-card feed | Compare tuned friction/retard against vacuum; independent double detection | Controlled comparison and mixed-stack endurance |
| Cards can stick on broad gravity platforms | Chute stalls or irregular settling | Narrow ribs, air channels, steeper paths, replaceable strips | Gravity-surface coupons |
| Singulators require many iterations | First geometry is unlikely to be universal | Interchangeable shoe, roller, and retard coupons | Comparative singulation fixture |
| Separate presentation and metering improve control | Stack pressure disrupts separation | Cassette presents, selected separator isolates, roller meters | Empty-to-full stack matrix and pickup disengagement |
| One light rotary chute can serve many bins | Multiple gates inflate cost and calibration | One S4 selector | Randomized route endurance |
| Timed rotary motion drifts | Card enters the wrong known bin | Independent route-position evidence | Confirm-before-release test |
| Similar printings and foils confuse recognition | Confident incorrect identity | Stationary capture, two light states, thresholds, reject | Held-out recognition evaluation |
| Multipass handling invites stack reversal | Physically correct passes produce wrong final order | Keyed cassettes, identity tags, persistent run state | Deliberate-error workflow test |
| Public projects use mixed licenses | Accidental contamination of original work | Provenance ledger and original implementation | License review before reuse |
| Recursive sorting creates many group feeds | Excessive operator attention | Scan-first stable planning, capacity-aware chunks | Model plus timed cassette workflow |
| Same-art printing can be consistently misidentified | Silently incorrect set/number order | Identity-specific evidence, ambiguity and review | Independent printing ground truth |

## Safety invariants

The design must maintain these rules across normal operation and faults:

1. Exactly one physical card may be active in the controlled feed cycle.
2. A new cycle cannot begin until the previous card is accounted for.
3. A card cannot leave the imaging nip without confirmed routing.
4. Unknown or conflicting identity goes to reject; the software never guesses a
   normal destination.
5. Contradictory sensors stop the machine.
6. A full, absent, or incompatible cassette stops feeding.
7. Jam recovery cannot require bending or dragging a trapped card.
8. Power loss leaves every card retained or visibly recoverable.
9. Input, normal outputs, reject, and cards still inside reconcile with the run
   manifest.

## Failure-mode register

Score each failure for severity, occurrence, and detectability. High-severity
failures with poor detection require redundant evidence or a mechanical change,
not merely a warning.

Initial critical or high-priority cases are:

- Two aligned cards pass as one
- Correct identification followed by an incorrect selector position
- Card released before recognition completes
- Warped card bridges a chute or cassette mouth
- Output cassette is full, absent, or displaced
- Operator reloads the wrong cassette or orientation
- Dust gradually reduces vacuum performance
- Roller traction or diameter changes with wear
- Lighting, focus, or camera registration drifts
- Power fails while a card spans two modules
- A delayed recognition response is applied to a later physical card
- A confidently incorrect printing survives every recognition pass
- A full output or out-of-order spill chunk invalidates the logical pass
- Shared transport motion inadvertently picks up the next card
- Frequent cassette service erases the intended savings in human attention
- Recognition noise on verification passes stops the job too often
- Verification accepts a confusable printing as the expected card

Each entry should identify the initiating cause, local effect, final effect,
existing detection, proposed control, owner, test, and status.

## Prototype ladder

1. **Singulation comparison:** friction/retard baseline and vacuum challenger on
   one fixture; compare Hall and suitable ultrasonic double detection.
2. **Gravity coupon fixture:** angle, material, ribs, vents, print direction, and
   low-friction insert.
3. **Dual-nip imaging bench:** registration, drive synchronization, lighting,
   camera distance, and stop accuracy.
4. **Router fixture:** selector, independent position sensing, output geometry,
   cassette mouth, and reject.
5. **Cassette workflow simulation:** gates, orientation, identity, overflow, and
   multipass instructions.
6. **Integrated endurance machine:** only after the preceding fixtures meet their
   exit criteria.

Use shared mechanical interfaces so validated components transfer into integration
without being redesigned.

## Boundary-condition matrix

Tests must include more than clean average cards:

- New, worn, matte, glossy, foil, curled, dirty, and slightly damaged cards
- Minimum and maximum expected thickness
- Deliberately aligned doubles
- One-card, half-full, and maximum hopper loads
- Common sleeves after unsleeved reliability is established
- Dust, static, temperature, and humidity variation
- Printer calibration, filament, layer direction, and tolerance variation
- Low supply voltage and interrupted host communication
- Every selector transition, especially the longest move
- Empty, nearly full, full, missing, and incorrectly installed cassettes
- Long dwell times that allow a card to settle or adhere to a surface

Use sacrificial cards until the damage risk has been retired with evidence.

## Required measurements

Record at least:

- Acquisition success and retries
- Vacuum peak, decay, and release behavior
- Upper/lower nip timing and motor position
- Thickness measurement
- Image quality and recognition confidence
- Selector command and independently observed position
- Requested and actual destination
- Cassette identity and count
- Detected fault and recovery action
- Jam location and cause
- Card type and post-test damage inspection
- Input loads, output chunk removals, required visits, active human minutes, and
  elapsed time; measure manual sorting on the same jobs for comparison
- Name and printing confusion separately, with false acceptance and reject rate

Detected interruptions and silent failures must be reported separately. A detected
no-feed affects convenience; an undetected double or wrong route corrupts the sort.

## Reliability interpretation

A zero-failure run is evidence, not proof. With zero observed failures, the rough
95% upper failure-rate bound is `3 / cycles` under independent, comparable Bernoulli
trials and complete detection of the failure being measured. Cycling the same stock
or sharing one calibration creates dependence and does not establish performance
on unseen cards or environments:

| Zero-failure run | Approximate upper bound |
|---:|---:|
| 10,000 cycles | 0.03% |
| 100,000 cycles | 0.003% |
| 300,000 cycles | 0.001% |

The initial 10,000-cycle feeder milestone is an engineering gate. Longer release
testing will be required for strong claims about valuable-card safety.

## Adversarial design review

Before detailed enclosure CAD, answer these questions with either analysis or a
test:

- What happens if every card selects the same output?
- What happens if recognition takes ten seconds or returns late?
- Can two perfectly aligned cards defeat every detector?
- What happens when the selector is between routes?
- What happens if a cassette is removed during a cycle?
- How is a wrong cassette or orientation prevented?
- Where is a card after power loss at every point in the cycle?
- Can a curled foil remain bridged after a long dwell?
- Which parts require replacement after extended use?
- Can the design tolerate a poorly calibrated printer?

## Decision rule

A mechanism advances only when its requirement, evidence, failure modes, test
conditions, raw results, and resulting decision are recorded. Failed ideas remain
in the record with the conditions that invalidated them; they should not be silently
deleted and later rediscovered.
