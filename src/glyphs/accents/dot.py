from glyphs.accents import Accent
from draw.rect import draw_rect


class DotAbove(Accent):
    name = "dotaccent"
    unicode = "0x2D9"
    stroke_width = 1.5

    def draw_at(self, pen, dc, x, y):
        dw = self.stroke_width * dc.stroke_x / 2
        draw_rect(pen, x - dw, y - dw, x + dw, y + dw)
