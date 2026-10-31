# CAD

Place original parametric CAD here. Every released printable mesh should identify
its editable source, units, revision, print orientation, material, and required
tolerances. Routine parts must fit a 220 × 220 mm FDM bed.

## Release file formats

Every released part ships in these formats, exported from the same source revision:

| Format | Role | Requirement |
|---|---|---|
| Native source | Original parametric model | Required. The tool is not yet chosen; prefer one usable without an account or subscription, such as FreeCAD. |
| STEP (`.step`) | Editable exchange | Required for every part, so builders can modify geometry in any CAD tool. |
| STL (`.stl`) | Universal printable mesh | Required for every part, in millimetres, already in its intended print orientation. |
| 3MF (`.3mf`) | Print-ready plate | Required for each release plate set. Carries units, orientation, and recommended print settings. |

STL carries no units or settings, so its accompanying notes must state units,
orientation, material, and tolerances. A 3MF must not contain settings that only
one slicer can read; keep the essentials in the notes too. Interchangeable test
coupons follow the same rule so fixture iterations stay reproducible.
