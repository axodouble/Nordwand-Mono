from glyphs.special.comma import CommaGlyph


class RightSingleQuotationMarkGlyph(CommaGlyph):
    """The comma, raised so its head sits at the ascent like `"`.

    Unlike the comma, it is centered in the cell on its bounding box, so
    `offset` only nudges it away from the center.
    """

    name = "right_single_quotation_mark"
    unicode = "0x2019"
    taper = 0.3
    stroke_ratio = 1.3

    def points(self, dc):
        pts = super().points(dc)
        xs = [x for x, _ in pts]
        dx = dc.window_width / 2 + self.offset - (min(xs) + max(xs)) / 2
        dy = dc.ascent - max(y for _, y in pts)
        return [(x + dx, y + dy) for x, y in pts]
