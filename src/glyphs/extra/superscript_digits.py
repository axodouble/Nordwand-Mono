from glyphs.extra.ordinal_indicator import OrdinalIndicatorGlyph
from glyphs.numbers.one import OneGlyph
from glyphs.numbers.two import TwoGlyph
from glyphs.numbers.three import ThreeGlyph


class SuperscriptDigitGlyph(OrdinalIndicatorGlyph):
    """A digit scaled down with its top at the cap height."""

    scale = 0.5
    # Lighter than the ordinals: digits have tighter counters at this size
    stroke_ratio = 0.65


class SuperscriptOneGlyph(SuperscriptDigitGlyph):
    name = "superscript_one"
    unicode = "0xB9"
    source = OneGlyph


class SuperscriptTwoGlyph(SuperscriptDigitGlyph):
    name = "superscript_two"
    unicode = "0xB2"
    source = TwoGlyph


class SuperscriptThreeGlyph(SuperscriptDigitGlyph):
    name = "superscript_three"
    unicode = "0xB3"
    source = ThreeGlyph
