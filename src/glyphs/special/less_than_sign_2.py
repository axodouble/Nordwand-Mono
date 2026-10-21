from glyphs.special.greater_than_sign_2 import GreaterThenSign2Glyph
from glyphs.special.less_than_sign import LessThenSignGlyph


class LessThenSign2Glyph(LessThenSignGlyph):
    name = "less_than_sign_2"
    font_feature = {"ss03": 1}
    span = GreaterThenSign2Glyph.span
