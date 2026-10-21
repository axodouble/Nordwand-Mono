from math import atan2, cos, pi, sin, sqrt, tan
from config import FontConfig as fc
from draw.rect import draw_rect
from glyphs.numbers.zero import ZeroGlyph


def _draw_rounded_polygon(pen, points, radius):
    """Draw a convex polygon whose corners are circular arcs of `radius`,
    tangent to both adjacent edges."""
    n = len(points)
    for i, (vx, vy) in enumerate(points):
        (px, py), (nx, ny) = points[i - 1], points[(i + 1) % n]
        to_prev = (px - vx, py - vy)
        to_next = (nx - vx, ny - vy)
        angle = abs(
            atan2(
                to_prev[0] * to_next[1] - to_prev[1] * to_next[0],
                to_prev[0] * to_next[0] + to_prev[1] * to_next[1],
            )
        )
        cut = radius / tan(angle / 2)
        # Bezier handle length for a circular arc turning by (pi - angle).
        handle = 4 / 3 * tan((pi - angle) / 4) * radius

        ends = []
        for dx, dy in (to_prev, to_next):
            length = sqrt(dx**2 + dy**2)
            ux, uy = dx / length, dy / length
            ends.append(
                (
                    (vx + ux * cut, vy + uy * cut),
                    (vx + ux * (cut - handle), vy + uy * (cut - handle)),
                )
            )
        (start, start_handle), (end, end_handle) = ends
        if i == 0:
            pen.moveTo(start)
        else:
            pen.lineTo(start)
        pen.curveTo(start_handle, end_handle, end)
    pen.closePath()


def _offset_polygon(points, distances):
    """Move each edge of a counter-clockwise convex polygon inward by its
    own distance and return the new vertices."""
    n = len(points)
    lines = []
    for i in range(n):
        (x1, y1), (x2, y2) = points[i], points[(i + 1) % n]
        length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        nx, ny = -(y2 - y1) / length, (x2 - x1) / length  # Inward normal
        d = distances[i]
        lines.append(((x1 + nx * d, y1 + ny * d), (x2 - x1, y2 - y1)))

    inner = []
    for i in range(n):
        (ax, ay), (adx, ady) = lines[i - 1]
        (bx, by), (bdx, bdy) = lines[i]
        t = ((bx - ax) * bdy - (by - ay) * bdx) / (adx * bdy - ady * bdx)
        inner.append((ax + adx * t, ay + ady * t))
    return inner


class ZeroHexagonGlyph(ZeroGlyph):
    name = "zero_hexagon"
    font_feature = {"cv01": 2}
    width_ratio = 1.2
    flat_ratio = 0.4  # Half-length of the flat top / bottom, relative to half-width
    corner_radius = 1.0  # Outer corner radius, in stroke widths
    dot_stroke_ratio = 1.1
    dot_fill = 0.6  # Max dot side, as a fraction of the counter's half-width

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_left=True,
            overshoot_right=True,
            number=True,
            min_margin=fc.min_margin_uppercase,
        )
        sx = dc.stroke_x * self.stroke_x_ratio
        sy = dc.stroke_y * self.stroke_y_ratio
        radius = self.corner_radius * dc.stroke_x
        cx, cy = b.xmid, b.ymid
        f = self.flat_ratio * b.width / 2

        outer = [
            (b.x2, cy),
            (cx + f, b.y2),
            (cx - f, b.y2),
            (b.x1, cy),
            (cx - f, b.y1),
            (cx + f, b.y1),
        ]

        # Each edge's stroke blends the vertical (stroke_x) and horizontal
        # (stroke_y) weights by its slope, so the flat edges get stroke_y.
        thickness = []
        for i in range(len(outer)):
            (x1, y1), (x2, y2) = outer[i], outer[(i + 1) % len(outer)]
            phi = atan2(abs(y2 - y1), abs(x2 - x1))
            thickness.append(sqrt((sx * sin(phi)) ** 2 + (sy * cos(phi)) ** 2))
        inner = _offset_polygon(outer, thickness)
        inner_radius = max(radius - min(thickness), 0.15 * radius)

        _draw_rounded_polygon(pen, outer, radius)
        _draw_rounded_polygon(pen, inner[::-1], inner_radius)

        # Cap the dot to the counter's width so it keeps some air around it
        # at heavy weights, where the counter gets small.
        inner_half_width = inner[0][0] - cx
        d = min(
            dc.stroke_x * self.dot_stroke_ratio, 140, self.dot_fill * inner_half_width
        )
        draw_rect(pen, cx - d / 2, cy - d / 2, cx + d / 2, cy + d / 2)
