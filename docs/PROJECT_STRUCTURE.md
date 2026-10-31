# Project Structure

This file defines where new work belongs so the design record, implementation,
and third-party research do not become mixed together.

| Path | Contents |
|---|---|
| `/designs` | Primary R8 specification and superseded alternatives |
| `/docs/hobbyist` | Dated research, user needs, costs, conclusions, and sources |
| `/docs/reviews` | Dated design reviews and decision records |
| `/docs/DESIGN_ASSURANCE.md` | Evidence levels, failure modes, test matrix, and decision gates |
| `/docs/BOM_PRICING.md` | Dated purchased-parts price estimate with sources |
| `/hardware/cad` | Original editable CAD and exported printable models |
| `/hardware/electronics` | Schematics, wiring, boards, and bills of materials |
| `/hardware/prototypes` | Fixture notes, assembly records, and iteration measurements |
| `/firmware` | Microcontroller motion, sensing, interlocks, and protocol |
| `/software` | Local card recognition, database, sort planner, simulator, and UI |
| `/tests` | Automated tests, mechanical test data, and acceptance reports |
| `/references/hobbyist-projects` | Ignored local snapshots of outside projects |

Root design documents describe decisions that apply to the primary design. A design
decision should be documented before CAD or code silently depends on it. Prototype
measurements belong with the relevant fixture and should be summarized back into
the design document that they confirm or overturn.
