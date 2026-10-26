from glyphs.special.quotation_mark import QuotationMarkGlyph
from glyphs.special.right_single_quotation_mark import RightSingleQuotationMarkGlyph
from draw.polygon import draw_polygon


class RightDoubleQuotationMarkGlyph(RightSingleQuotationMarkGlyph):
    """Two `’`, spaced like the bars of `"`."""

    name = "right_double_quotation_mark"
    unicode = "0x201D"
    gap = QuotationMarkGlyph.gap
    offset = 20

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        d = (self.gap * b.width + self.stroke_ratio * dc.stroke_x) / 2
        pts = self.points(dc)
        for dx in (-d, d):
            draw_polygon(pen, points=[(x + dx, y) for x, y in pts])
