from glyphs.special.right_single_quotation_mark import RightSingleQuotationMarkGlyph


class LeftSingleQuotationMarkGlyph(RightSingleQuotationMarkGlyph):
    """`’` turned 180° within its own bounding box."""

    name = "left_single_quotation_mark"
    unicode = "0x2018"

    def points(self, dc):
        pts = super().points(dc)
        xs, ys = [x for x, _ in pts], [y for _, y in pts]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        return [(2 * cx - x, 2 * cy - y) for x, y in pts]
