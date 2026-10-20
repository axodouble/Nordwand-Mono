from glyphs.special.greater_than_sign_2 import GreaterThanSign2Glyph
from glyphs.special.less_than_sign import LessThanSignGlyph


class LessThanSign2Glyph(LessThanSignGlyph):
    name = "less_than_sign_2"
    font_feature = {"ss03": 1}
    span = GreaterThanSign2Glyph.span
    stroke_ratio = 1.2
