# Project Structure

This file defines where new work belongs so the design record, implementation,
and third-party research do not become mixed together.

| Path | Contents |
|---|---|
| `/designs` | Product-level small and medium sorter specifications |
| `/docs/hobbyist` | Dated research, user needs, costs, conclusions, and sources |
| `/docs/DESIGN_ASSURANCE.md` | Evidence levels, failure modes, test matrix, and decision gates |
| `/hardware/cad` | Original editable CAD and exported printable models |
| `/hardware/electronics` | Schematics, wiring, boards, and bills of materials |
| `/hardware/prototypes` | Fixture notes, assembly records, and iteration measurements |
| `/firmware` | Microcontroller motion, sensing, interlocks, and protocol |
| `/software` | Local card recognition, database, sort planner, simulator, and UI |
| `/tests` | Automated tests, mechanical test data, and acceptance reports |
| `/references/hobbyist-projects` | Ignored local snapshots of outside projects |

Root design documents describe decisions shared by both physical designs. A design
decision should be documented before CAD or code silently depends on it. Prototype
measurements belong with the relevant fixture and should be summarized back into
the design document that they confirm or overturn.
