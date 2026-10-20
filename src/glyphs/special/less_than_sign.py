from glyphs import Glyph
from glyphs.special.greater_than_sign import GreaterThanSignGlyph
from draw.chevron import draw_chevron


class LessThanSignGlyph(Glyph):
    name = "less_than_sign"
    unicode = "0x3C"
    offset = 0
    width_ratio = 1
    overlap = 0.6
    span = GreaterThanSignGlyph.span
    stroke_ratio = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.stroke_ratio
        draw_chevron(pen, s, s, b.x1, b.x2, dc.math, h, delta=s)
