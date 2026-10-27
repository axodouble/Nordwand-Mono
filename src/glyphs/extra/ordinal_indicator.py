import dataclasses

from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen

from glyphs import Glyph


class OrdinalIndicatorGlyph(Glyph):
    """A lowercase letter scaled down and raised so its top meets the cap.

    The letter is drawn with heavier strokes before scaling, so the final
    strokes are `stroke_ratio` of the regular ones instead of shrinking with
    the letter. Subclasses set `unicode` and the `source` glyph class.
    """

    offset = 0
    scale = 0.55
    stroke_ratio = 0.8

    def draw(self, pen, dc):
        k = self.stroke_ratio / self.scale
        heavy = dataclasses.replace(
            dc,
            stroke_x=dc.stroke_x * k,
            stroke_y=dc.stroke_y * k,
            stroke_alt=dc.stroke_alt * k,
        )
        rec = RecordingPen()
        self.source().draw(rec, heavy)

        bp = BoundsPen(None)
        rec.replay(bp)
        x_min, _, x_max, y_max = bp.bounds

        s = self.scale
        cx = dc.window_width / 2 + self.offset
        t = Transform(s, 0, 0, s, cx - s * (x_min + x_max) / 2, dc.cap - s * y_max)
        rec.replay(TransformPen(pen, t))
