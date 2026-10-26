from glyphs.special.left_single_quotation_mark import LeftSingleQuotationMarkGlyph
from glyphs.special.right_double_quotation_mark import RightDoubleQuotationMarkGlyph


class LeftDoubleQuotationMarkGlyph(LeftSingleQuotationMarkGlyph):
    """Two `‘`, spaced like the bars of `"`."""

    name = "left_double_quotation_mark"
    unicode = "0x201C"
    gap = RightDoubleQuotationMarkGlyph.gap
    draw = RightDoubleQuotationMarkGlyph.draw
    offset = -10
