from glyphs.special.comma import CommaGlyph


class RightSingleQuotationMarkGlyph(CommaGlyph):
    """The comma, raised so its head sits at the ascent like `"`."""

    name = "right_single_quotation_mark"
    unicode = "0x2019"
    taper = 0.3
    stroke_ratio = 1.3

    def points(self, dc):
        pts = super().points(dc)
        dy = dc.ascent - max(y for _, y in pts)
        return [(x, y + dy) for x, y in pts]
