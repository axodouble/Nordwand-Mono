from math import atan2, cos, pi, sin, sqrt, tan
from config import FontConfig as fc
from draw.rect import draw_rect
from glyphs.numbers.zero import ZeroGlyph


def _draw_rounded_diamond(pen, cx, cy, a, c, radius, reverse=False):
    """Draw a diamond with half-width `a` and half-height `c` whose corners
    are circular arcs of `radius`, tangent to both adjacent edges."""
    half_tip = atan2(a, c)  # Half interior angle at the top / bottom tips
    half_side = pi / 2 - half_tip  # Half interior angle at the side tips
    vertices = [
        ((cx, cy + c), half_tip),
        ((cx + a, cy), half_side),
        ((cx, cy - c), half_tip),
        ((cx - a, cy), half_side),
    ]
    if reverse:
        vertices = vertices[::-1]

    n = len(vertices)
    for i, ((vx, vy), half) in enumerate(vertices):
        cut = radius / tan(half)
        # Bezier handle length for a circular arc turning by (pi - 2 * half).
        handle = 4 / 3 * tan((pi - 2 * half) / 4) * radius
        points = []
        for (nx, ny), _ in (vertices[i - 1], vertices[(i + 1) % n]):
            length = sqrt((nx - vx) ** 2 + (ny - vy) ** 2)
            ux, uy = (nx - vx) / length, (ny - vy) / length
            points.append(
                (
                    (vx + ux * cut, vy + uy * cut),
                    (vx + ux * (cut - handle), vy + uy * (cut - handle)),
                )
            )
        (start, start_handle), (end, end_handle) = points
        if i == 0:
            pen.moveTo(start)
        else:
            pen.lineTo(start)
        pen.curveTo(start_handle, end_handle, end)
    pen.closePath()


class ZeroDiamondGlyph(ZeroGlyph):
    name = "zero_diamond"
    font_feature = {"cv01": 2}
    width_ratio = 1.3
    corner_radius = 1.0  # Outer corner radius, in stroke widths
    dot_stroke_ratio = 1.1
    dot_fill = 0.6  # Max dot side, as a fraction of the counter's half-width

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            number=True,
            min_margin=fc.min_margin_uppercase,
        )
        sx = dc.stroke_x * self.stroke_x_ratio
        sy = dc.stroke_y * self.stroke_y_ratio
        radius = self.corner_radius * dc.stroke_x
        cx, cy = b.xmid, b.ymid

        # Push the top and bottom vertices outward so the rounded tips still
        # reach the baseline and cap height; a few passes converge on the
        # angle. The side tips stay inside the body so the glyph fits its cell.
        a, c = b.width / 2, b.height / 2
        for _ in range(5):
            c = b.height / 2 + radius * (1 / sin(atan2(a, c)) - 1)

        # Perpendicular stroke thickness of the slanted edges, blending the
        # vertical (stroke_x) and horizontal (stroke_y) stroke weights.
        phi = atan2(c, a)
        s = sqrt((sx * sin(phi)) ** 2 + (sy * cos(phi)) ** 2)
        # Offsetting each edge inward by `s` is a uniform scale about the center.
        scale = 1 - s * sqrt(1 / a**2 + 1 / c**2)
        inner_radius = max(radius - s, 0.15 * radius)

        _draw_rounded_diamond(pen, cx, cy, a, c, radius)
        _draw_rounded_diamond(
            pen, cx, cy, a * scale, c * scale, inner_radius, reverse=True
        )

        # Cap the dot to the counter's width so it keeps some air around it
        # at heavy weights, where the counter gets small.
        d = min(dc.stroke_x * self.dot_stroke_ratio, 140, self.dot_fill * a * scale)
        draw_rect(pen, cx - d / 2, cy - d / 2, cx + d / 2, cy + d / 2)
