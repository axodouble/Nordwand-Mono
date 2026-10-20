from glyphs.ligatures.double_right_arrow import RightArrowGlyph as DoubleRightArrowGlyph
from glyphs.special.greater_than_sign_2 import GreaterThanSign2Glyph


class DoubleRightArrow2Glyph(DoubleRightArrowGlyph):
    """Ligature glyph for => with the wide `ss03` arrow head"""

    name = "double_right_arrow_liga_2"
    components = ["equals_sign", "greater_than_sign_2"]
    span = GreaterThanSign2Glyph.span
