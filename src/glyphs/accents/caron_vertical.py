from draw.polygon import draw_polygon
from glyphs.accents import Accent


class CaronVertical(Accent):
    """Apostrophe-like caron placed beside an ascender, as in ď and ť.

    Unlike the other accents, `draw_at` anchors the mark by its top-left
    corner, since it sits to the right of a stem rather than above it.
    """

    name = "caron_vertical"
    unicode = None
    generated_only = True  # Only used inside composed glyphs
    stroke_ratio = 1.1  # Width at the top, relative to stroke_x
    taper = 0.7  # Width at the bottom, relative to the top
    height = 0.4  # Relative to the x-height
    lean = 0.35  # Bottom shift to the left, relative to the top width
    gap = 0.75  # Space left of the mark, relative to stroke_x

    def top_width(self, dc):
        return self.stroke_ratio * dc.stroke_x

    def width(self, dc):
        """Horizontal extent of the mark, including the gap before it."""
        return self.gap * dc.stroke_x + self.top_width(dc)

    def draw_at(self, pen, dc, x, y):
        w = self.top_width(dc)
        x1 = x + self.gap * dc.stroke_x
        y1 = y - self.height * dc.x_height
        lean = self.lean * w
        draw_polygon(
            pen,
            points=[
                (x1, y),
                (x1 + w, y),
                (x1 + w - lean - (1 - self.taper) * w / 2, y1),
                (x1 - lean + (1 - self.taper) * w / 2, y1),
            ],
        )

    def draw(self, pen, dc):
        self.draw_at(pen, dc, x=dc.window_width / 2 - self.width(dc) / 2, y=dc.ascent)
