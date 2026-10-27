from glyphs import Glyph
from glyphs.special.quotation_mark import QuotationMarkGlyph
from draw.polygon import draw_polygon


class QuoteGlyph(Glyph):
    """Base shape of the curly quotes: a wedge hanging from the ascent.

    Centered in the cell on its bounding box, so `offset` only nudges it
    away from the center. `turned` rotates it 180° for the opening quotes,
    `double` draws it twice, spaced like the bars of `"`. `low` drops it so
    the head sits on the baseline, with the tail below like a comma.

    Leaves `unicode` undefined so it stays abstract and isn't exported;
    each quote subclass sets its own.
    """

    name = "quote"
    offset = 0
    width_ratio = 1
    # Length of the tail below the head, relative to the x-height
    tail_ratio = 0.27
    foot_offset = 0.15
    taper = 0.3
    stroke_ratio = 1
    # Side of the square head, relative to stroke_x
    head_ratio = 1.5
    gap = QuotationMarkGlyph.gap
    turned = False
    double = False
    low = False

    def points(self, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx = self.stroke_ratio * dc.stroke_x
        fx = self.foot_offset * b.width
        hs = self.head_ratio * dc.stroke_x
        top = hs if self.low else dc.ascent
        bottom = top - hs - self.tail_ratio * b.height
        xl, xr = b.xmid - hs / 2, b.xmid + hs / 2

        # Square head, with the tail hanging from its right part
        pts = [
            (xl, top),
            (xr, top),
            (xr, top - hs),
            (b.xmid + self.taper * sx / 2 - fx, bottom),
            (b.xmid - sx / 2 - fx, bottom),
            (xr - sx, top - hs),
            (xl, top - hs),
        ]
        xs = [x for x, _ in pts]
        cx, cy = (min(xs) + max(xs)) / 2, (top + bottom) / 2
        if self.turned:
            pts = [(2 * cx - x, 2 * cy - y) for x, y in pts]
        return [(x + b.xmid - cx, y) for x, y in pts]

    def draw(self, pen, dc):
        pts = self.points(dc)
        if not self.double:
            draw_polygon(pen, points=pts)
            return
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        d = (self.gap * b.width + self.stroke_ratio * dc.stroke_x) / 2
        for dx in (-d, d):
            draw_polygon(pen, points=[(x + dx, y) for x, y in pts])
