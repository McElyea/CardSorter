"""Bench-starter printable parts: parametric source for STEP, IGES, STL, 3MF, OBJ,
and AMF exports.

These are first-print parts for the feeder comparison bench and capacity mockups
in hardware/prototypes/FEEDER_COMPARISON.md. They are not validated sorter parts.

Regenerate from the project root (CadQuery 2.x, Python 3.10-3.13):

    python hardware/cad/bench-starter/bench_starter.py

All dimensions are millimetres. Replace CARD_T with measured stock thickness and
rerun before trusting the stack gauges for capacity decisions.
"""

from pathlib import Path

import cadquery as cq
from OCP.IGESControl import IGESControl_Writer

OUT = Path(__file__).resolve().parent
REVISION = "r1"

# Card stack gauges (cards stand on their 63 mm edge, stacked along X)
CARD_W = 63.0          # nominal standard trading card width
CARD_T = 0.305         # assumed unsleeved thickness; replace with measured value
SIDE_CLEAR = 0.5       # per side across the card width
STACK_ALLOW = 4.0      # follower travel, curl, and removal allowance
WALL = 2.4
FLOOR = 2.0
WALL_H = 45.0
CAPACITIES = (150, 200, 250)
TICK_EVERY = 25        # rim tick spacing in cards; every fourth tick is deeper

# Fit coupon
COUPON = (96.0, 36.0, 8.0)
HOLES = (2.9, 3.2, 3.4, 4.0, 4.2)   # M3 self-tap, M3 clearance, heat-set pilots
SLOTS = (0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2)
SLOT_DEPTH = 6.0
ENGRAVE = 0.4


def engraving(text, size, plane, origin, depth):
    """Text solid that starts `depth` below the face and rises 0.1 mm above it."""
    return (cq.Workplane(plane, origin=origin)
            .workplane(offset=-depth)
            .text(text, size, depth + 0.1, combine=False))


def stack_gauge(cards):
    inner_l = cards * CARD_T + STACK_ALLOW
    inner_w = CARD_W + 2 * SIDE_CLEAR
    outer_l, outer_w, height = inner_l + 2 * WALL, inner_w + 2 * WALL, WALL_H + FLOOR

    body = (cq.Workplane("XY")
            .box(outer_l, outer_w, height, centered=(True, True, False))
            .edges("|Z").fillet(3.0)
            .faces("<Z").edges().chamfer(0.6))
    pocket = (cq.Workplane("XY").workplane(offset=FLOOR)
              .rect(inner_l, inner_w).extrude(height))
    body = body.cut(pocket)

    # Finger notch in the +Y wall for lifting the stack out
    notch = cq.Solid.makeCylinder(16.0, WALL + 2, cq.Vector(0, inner_w / 2 - 1, height),
                                  cq.Vector(0, 1, 0))
    body = body.cut(cq.Workplane().add(notch))

    # Fill-level ticks on the -Y rim, measured from the -X inner end wall
    for count in range(TICK_EVERY, cards + 1, TICK_EVERY):
        depth = 3.0 if count % (4 * TICK_EVERY) == 0 else 1.5
        x = -inner_l / 2 + count * CARD_T
        tick = (cq.Workplane("XY")
                .box(0.8, WALL + 2, depth + 1, centered=(True, True, False))
                .translate((x, -inner_w / 2 - WALL / 2, height - depth)))
        body = body.cut(tick)

    # Capacity label on the +X end wall, readable from that side
    label_origin = (outer_l / 2, 0, height / 2)
    body = body.cut(engraving(str(cards), 12, "YZ", label_origin, ENGRAVE + 0.2))
    return body


def fit_coupon():
    length, width, thick = COUPON
    body = (cq.Workplane("XY")
            .box(length, width, thick, centered=(True, True, False))
            .edges("|Z").fillet(2.0)
            .faces("<Z").edges().chamfer(0.4))

    # Front row: through holes for M3 screws and heat-set inserts
    for i, diameter in enumerate(HOLES):
        x = -30 + 15 * i
        hole = cq.Solid.makeCylinder(diameter / 2, thick + 2, cq.Vector(x, -7, -1))
        body = body.cut(cq.Workplane().add(hole))
        body = body.cut(engraving(f"{diameter:.1f}", 3.5, "XY", (x, -14, thick), ENGRAVE))

    # Back row: card slots open at the back edge, cut down from the top
    for i, slot in enumerate(SLOTS):
        x = -33 + 11 * i
        cut = (cq.Workplane("XY")
               .box(slot, 14, SLOT_DEPTH + 1, centered=(True, False, False))
               .translate((x, 6, thick - SLOT_DEPTH)))
        body = body.cut(cut)
        body = body.cut(engraving(f"{slot:.1f}", 3.5, "XY", (x, 1.0, thick), ENGRAVE))
    return body


MESH_TOL = (0.02, 0.1)   # linear (mm) and angular (rad) tessellation tolerance


def export_iges(part, target):
    """IGES in millimetres, written as trimmed surfaces (BRep mode)."""
    writer = IGESControl_Writer("MM", 1)
    writer.AddShape(part.val().wrapped)
    writer.ComputeModel()
    if not writer.Write(str(target)):
        raise RuntimeError(f"IGES export failed: {target}")


def export_obj(part, target):
    """OBJ mesh with shared vertices so it stays watertight. OBJ has no unit field;
    slicers read the values as millimetres."""
    vertices, triangles = part.val().tessellate(*MESH_TOL)
    index, points, faces = {}, [], []
    for tri in triangles:
        face = []
        for i in tri:
            v = vertices[i]
            key = (round(v.x, 6), round(v.y, 6), round(v.z, 6))
            if key not in index:
                index[key] = len(points) + 1
                points.append(key)
            face.append(index[key])
        if len(set(face)) == 3:
            faces.append(face)
    with open(target, "w", encoding="ascii", newline="\n") as f:
        f.write(f"# {target.stem} - CardSorter bench starter, units mm\n")
        f.writelines(f"v {x:.6f} {y:.6f} {z:.6f}\n" for x, y, z in points)
        f.writelines(f"f {a} {b} {c}\n" for a, b, c in faces)


def export(name, part):
    stem = f"cs_{name}_{REVISION}"
    for suffix in ("step", "iges", "stl", "3mf", "obj", "amf"):
        (OUT / suffix).mkdir(exist_ok=True)
        target = OUT / suffix / f"{stem}.{suffix}"
        if suffix == "step":
            cq.exporters.export(part, str(target))
        elif suffix == "iges":
            export_iges(part, target)
        elif suffix == "obj":
            export_obj(part, target)
        else:
            cq.exporters.export(part, str(target), tolerance=MESH_TOL[0],
                                angularTolerance=MESH_TOL[1])
    box = part.val().BoundingBox()
    print(f"{stem}: {box.xlen:.1f} x {box.ylen:.1f} x {box.zlen:.1f} mm, "
          f"{part.val().Volume() / 1000:.1f} cm^3")


def main():
    export("fit_coupon", fit_coupon())
    for cards in CAPACITIES:
        export(f"stack_gauge_{cards}", stack_gauge(cards))


if __name__ == "__main__":
    main()
