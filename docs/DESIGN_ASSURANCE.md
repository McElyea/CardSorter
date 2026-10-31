# Design Assurance and Evidence-to-Test Process

## Purpose

Hobbyist research should become a verification program rather than an inspiration
board. Every material observation should result in a requirement, prototype
experiment, monitored risk, or documented rejected choice.

The [2026-10-31 review](reviews/2026-10-31_DESIGN_REVIEW.md) added capacity and
operator workload to the gates and separated name recognition from exact-printing
correctness. The [reliability rework](reviews/2026-10-31_RELIABILITY_REWORK.md) made
predictable throughput and positive control gates as well. Mathematical simulation
is not physical validation.

This process connects the dated research in `docs/hobbyist` to the
[R8 design](../designs/R8_RELIABLE_SORTER.md) and helps prevent attractive mechanisms
from advancing without evidence.

## Standard evidence record

For every useful external observation, record:

- Source and revision or review date
- Mechanism being discussed
- Observed failure or claimed benefit
- Card, stack, calibration, and environmental conditions
- Builder's stated or inferred cause
- Workaround or design revision
- Evidence quality
- Possible R8 manifestation
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

## Evidence-to-design map

| Lesson | Design risk | Current response | Required proof |
|---|---|---|---|
| Friction gaps alternate between no-feed and doubles | Silent two-card feed | Torque-limited brake roller; Hall double detection; retard pad and vacuum as comparisons | Controlled comparison and mixed-stack endurance |
| Cards can stick on broad gravity platforms | Irregular timing and landing | Positive control: driven nips to the pocket, no gravity platforms | Continuous transport bench |
| Free-fall routing timing depends on card condition | Unpredictable throughput, bounce | Driven router entry, fixed cadence | Cadence adherence over 10,000 cycles |
| Stop-for-capture ties cycle time to recognition | Throughput varies with host latency | Capture in motion; pipelined recognition with a deadline; late answer goes to reject | Injected-latency test; latency distribution on real hosts |
| Singulators require many iterations | First geometry is unlikely to be universal | Interchangeable roller, brake, pad, and shoe coupons | Comparative feeder bench |
| Separate presentation and metering improve control | Stack force changes as the hopper empties | Constant-force follower; pick roller on its own drive | Empty-to-full force and pick-time matrix |
| One light rotary chute can serve many bins | Multiple gates inflate cost and calibration | One indexed router (R-A) or fail-safe gates (R-B) by bend test | Randomized route endurance |
| Timed rotary motion drifts | Card enters the wrong known pocket | Independent router position evidence before entry | Confirm-before-entry test |
| Bending can curl or whiten cards | Damage from curved paths | Straight path where possible; minimum radius from the bend test | Card bend test |
| Roller traction changes with wear | Slower or slipping cards, missed slots | Purchased urethane rollers; slip encoder; maintenance threshold | Slip trend over endurance run |
| Similar printings and foils confuse recognition | Confident incorrect identity | Two strobed captures, thresholds, reject | Held-out recognition evaluation |
| Multipass handling invites stack reversal | Physically correct passes produce wrong final order | Keyed pockets, persistent run state, sequence verification | Deliberate-error workflow test |
| Public projects use mixed licenses | Accidental contamination of original work | Provenance ledger and original implementation | License review before reuse |
| Recursive sorting creates many group feeds | Excessive operator attention | Scan-first stable planning, capacity-aware chunks | Model plus timed pocket workflow |
| Same-art printing can be consistently misidentified | Silently incorrect set/number order | Identity-specific evidence, ambiguity and review | Independent printing ground truth |

## Safety invariants

The design must maintain these rules across normal operation and faults:

1. Exactly one physical card is picked per cadence slot.
2. A new pick cannot begin until the previous card is accounted for.
3. A card enters the router only when its route is confirmed and the router's
   position is independently verified; otherwise it takes the default reject
   route or the transport stops.
4. Unknown or conflicting identity goes to reject; the software never guesses a
   normal destination.
5. Contradictory sensors stop the machine.
6. A full, absent, or incompatible pocket stops picking.
7. Jam recovery cannot require bending or dragging a trapped card.
8. Power loss leaves every card held or visibly recoverable.
9. Input, normal outputs, reject, and cards still inside reconcile with the run
   manifest.
10. The transport can stop at any moment with every card in the path held by a
    nip; no card is ever in free fall.

## Failure-mode register

Score each failure for severity, occurrence, and detectability. High-severity
failures with poor detection require redundant evidence or a mechanical change,
not merely a warning.

Initial critical or high-priority cases are:

- Two aligned cards pass as one
- Correct identification followed by an incorrect router position
- Card enters the router before its route is confirmed
- Warped card bridges a guide or pocket mouth
- Output pocket is full, absent, or displaced
- Operator reloads the wrong stack or orientation
- Roller traction or diameter changes with wear
- Brake roller limiter torque drifts
- Constant-force follower friction rises and changes stack force
- Pick roller pulls the next card before its slot
- Head exit nip speed mismatch buckles or drags a card
- Pocket stacking scuffs card faces
- Lighting, strobe timing, focus, or camera registration drifts
- Recognition latency often exceeds the deadline, raising the reject rate
- Power fails while a card spans two modules
- A delayed recognition response is applied to a later physical card
- A confidently incorrect printing survives every recognition pass
- A full output or out-of-order spill chunk invalidates the logical pass
- Frequent pocket service erases the intended savings in human attention
- Recognition noise on verification passes stops the job too often
- Verification accepts a confusable printing as the expected card
- Dust gradually reduces vacuum performance (vacuum comparison only)

Each entry should identify the initiating cause, local effect, final effect,
existing detection, proposed control, owner, test, and status.

## Card bend test

Bend representative cards (new, worn, foil, each game's stock) around printed
mandrels of decreasing radius, for example 300, 200, 150, 100, and 75 mm, for
repeated cycles at the transport speed. Measure residual curl with a feeler gauge
on a flat plate and inspect edges and faces under magnification. The smallest
radius with no measurable residual curl and no whitening, with margin, becomes the
minimum path radius. This decides between router R-A and R-B.

## Prototype ladder

1. **Feeder bench:** brake roller expected, retard pad and vacuum comparisons;
   constant-force presentation; Hall and slip sensing.
2. **Card bend test:** minimum path radius.
3. **Continuous transport and imaging bench:** belt-synchronized nips, two-strobe
   capture in motion, buffer and deadline with mocked recognition.
4. **Router and pocket bench:** R-A or R-B, independent position sensing, default
   reject, head-nip speed matching, stacking candidates.
5. **Pocket workflow simulation:** keyed pockets, orientation, overflow, and
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
- Every router transition, especially the longest move
- Empty, nearly full, full, missing, and incorrectly installed pockets
- Long dwell times that allow a card to settle or adhere to a surface
- Host latency spikes and a host that stops answering mid-job

Use sacrificial cards until the damage risk has been retired with evidence.

## Required measurements

Record at least:

- Pick success, retries, and pick time per cycle
- Skipped cadence slots and their reasons
- Transport slip from the idler encoder
- Thickness measurement
- Image quality and recognition confidence
- Route latency from capture to answer
- Router command and independently observed position
- Requested and actual destination
- Pocket identity and count
- Detected fault and recovery action
- Jam location and cause
- Card type and post-test damage inspection
- Vacuum peak, decay, and release behavior (vacuum comparison only)
- Input loads, output chunk removals, required visits, active human minutes, and
  elapsed time; measure manual sorting on the same jobs for comparison
- Estimated versus actual job time
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
- What happens when the router is between positions?
- What happens if a pocket is removed during a cycle?
- How is a wrong pocket or orientation prevented?
- Where is a card after power loss at every point in the cycle?
- Can a curled foil remain bridged after a long dwell?
- Which parts require replacement after extended use, and at what cycle count?
- Can the design tolerate a poorly calibrated printer?
- What does the machine do when slip or pick time drifts out of range?

## Decision rule

A mechanism advances only when its requirement, evidence, failure modes, test
conditions, raw results, and resulting decision are recorded. Failed ideas remain
in the record with the conditions that invalidated them; they should not be silently
deleted and later rediscovered.
