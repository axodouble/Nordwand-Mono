"""Accented / composed glyphs.

Each class pairs a base glyph with an accent mark. The accent_y controls
the vertical anchor. For lowercase letters with ascenders or dots (i, j),
draw_base is called to omit the dot.
"""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph

from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.dotted.i_2 import LowercaseI2Glyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.lowercase.z import LowercaseZGlyph

from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.g import UppercaseGGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.z import UppercaseZGlyph

from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.tilde import Tilde
from glyphs.accents.caron import Caron
from glyphs.accents.ring import Ring
from glyphs.accents.cedilla import Cedilla
from glyphs.accents.macron import Macron
from glyphs.accents.breve import Breve
from glyphs.accents.dot import DotAbove
from glyphs.accents.ogonek import Ogonek
from glyphs.accents.stroke import Stroke, UppercaseStroke
import pathops
from draw.rect import draw_rect

# Heights for accent positioning
_lc_accent = fc.accent
_uc_accent = fc.accent_cap
_cedilla_y = 0


# ── Lowercase with acute ─────────────────────────────────────────────


class LowercaseAAcuteGlyph(ComposedGlyph):
    name = "lowercase_aacute"
    unicode = "0xE1"
    base_glyph_class = LowercaseAGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseEAcuteGlyph(ComposedGlyph):
    name = "lowercase_eacute"
    unicode = "0xE9"
    base_glyph_class = LowercaseEGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseIAcuteGlyph(ComposedGlyph):
    name = "lowercase_iacute"
    unicode = "0xED"
    base_glyph_class = LowercaseIGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseOAcuteGlyph(ComposedGlyph):
    name = "lowercase_oacute"
    unicode = "0xF3"
    base_glyph_class = LowercaseOGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseUAcuteGlyph(ComposedGlyph):
    name = "lowercase_uacute"
    unicode = "0xFA"
    base_glyph_class = LowercaseUGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseYAcuteGlyph(ComposedGlyph):
    name = "lowercase_yacute"
    unicode = "0xFD"
    base_glyph_class = LowercaseYGlyph
    accent_class = Acute
    accent_y = _lc_accent


# ── Lowercase with grave ─────────────────────────────────────────────


class LowercaseAGraveGlyph(ComposedGlyph):
    name = "lowercase_agrave"
    unicode = "0xE0"
    base_glyph_class = LowercaseAGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseEGraveGlyph(ComposedGlyph):
    name = "lowercase_egrave"
    unicode = "0xE8"
    base_glyph_class = LowercaseEGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseIGraveGlyph(ComposedGlyph):
    name = "lowercase_igrave"
    unicode = "0xEC"
    base_glyph_class = LowercaseIGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseOGraveGlyph(ComposedGlyph):
    name = "lowercase_ograve"
    unicode = "0xF2"
    base_glyph_class = LowercaseOGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseUGraveGlyph(ComposedGlyph):
    name = "lowercase_ugrave"
    unicode = "0xF9"
    base_glyph_class = LowercaseUGlyph
    accent_class = Grave
    accent_y = _lc_accent


# ── Lowercase with circumflex ────────────────────────────────────────


class LowercaseACircumflexGlyph(ComposedGlyph):
    name = "lowercase_acircumflex"
    unicode = "0xE2"
    base_glyph_class = LowercaseAGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseECircumflexGlyph(ComposedGlyph):
    name = "lowercase_ecircumflex"
    unicode = "0xEA"
    base_glyph_class = LowercaseEGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseICircumflexGlyph(ComposedGlyph):
    name = "lowercase_icircumflex"
    unicode = "0xEE"
    base_glyph_class = LowercaseIGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseOCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ocircumflex"
    unicode = "0xF4"
    base_glyph_class = LowercaseOGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseUCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ucircumflex"
    unicode = "0xFB"
    base_glyph_class = LowercaseUGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


# ── Lowercase with dieresis ──────────────────────────────────────────


class LowercaseADieresisGlyph(ComposedGlyph):
    name = "lowercase_adieresis"
    unicode = "0xE4"
    base_glyph_class = LowercaseAGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseEDieresisGlyph(ComposedGlyph):
    name = "lowercase_edieresis"
    unicode = "0xEB"
    base_glyph_class = LowercaseEGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseIDieresisGlyph(ComposedGlyph):
    name = "lowercase_idieresis"
    unicode = "0xEF"
    base_glyph_class = LowercaseIGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseODieresisGlyph(ComposedGlyph):
    name = "lowercase_odieresis"
    unicode = "0xF6"
    base_glyph_class = LowercaseOGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseUDieresisGlyph(ComposedGlyph):
    name = "lowercase_udieresis"
    unicode = "0xFC"
    base_glyph_class = LowercaseUGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseYDieresisGlyph(ComposedGlyph):
    name = "lowercase_ydieresis"
    unicode = "0xFF"
    base_glyph_class = LowercaseYGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


# ── Lowercase with macron (romaji long vowels) ───────────────────────


class LowercaseAMacronGlyph(ComposedGlyph):
    name = "lowercase_amacron"
    unicode = "0x101"
    base_glyph_class = LowercaseAGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseEMacronGlyph(ComposedGlyph):
    name = "lowercase_emacron"
    unicode = "0x113"
    base_glyph_class = LowercaseEGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseIMacronGlyph(ComposedGlyph):
    name = "lowercase_imacron"
    unicode = "0x12B"
    base_glyph_class = LowercaseIGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseOMacronGlyph(ComposedGlyph):
    name = "lowercase_omacron"
    unicode = "0x14D"
    base_glyph_class = LowercaseOGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseUMacronGlyph(ComposedGlyph):
    name = "lowercase_umacron"
    unicode = "0x16B"
    base_glyph_class = LowercaseUGlyph
    accent_class = Macron
    accent_y = _lc_accent


# ── Lowercase with tilde ─────────────────────────────────────────────


class LowercaseATildeGlyph(ComposedGlyph):
    name = "lowercase_atilde"
    unicode = "0xE3"
    base_glyph_class = LowercaseAGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseNTildeGlyph(ComposedGlyph):
    name = "lowercase_ntilde"
    unicode = "0xF1"
    base_glyph_class = LowercaseNGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseOTildeGlyph(ComposedGlyph):
    name = "lowercase_otilde"
    unicode = "0xF5"
    base_glyph_class = LowercaseOGlyph
    accent_class = Tilde
    accent_y = _lc_accent


# ── Lowercase with ring ──────────────────────────────────────────────


class LowercaseARingGlyph(ComposedGlyph):
    name = "lowercase_aring"
    unicode = "0xE5"
    base_glyph_class = LowercaseAGlyph
    accent_class = Ring
    accent_y = _lc_accent


# ── Lowercase with cedilla ───────────────────────────────────────────


class LowercaseCCedillaGlyph(ComposedGlyph):
    name = "lowercase_ccedilla"
    unicode = "0xE7"
    base_glyph_class = LowercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class LowercaseSCedillaGlyph(ComposedGlyph):
    name = "lowercase_scedilla"
    unicode = "0x15F"
    base_glyph_class = LowercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Lowercase with caron ─────────────────────────────────────────────


class LowercaseSCaronGlyph(ComposedGlyph):
    name = "lowercase_scaron"
    unicode = "0x161"
    base_glyph_class = LowercaseSGlyph
    accent_class = Caron
    accent_y = _lc_accent


# ── Lowercase with breve ─────────────────────────────────────────────


class LowercaseGBreveGlyph(ComposedGlyph):
    name = "lowercase_gbreve"
    unicode = "0x11F"
    base_glyph_class = LowercaseGGlyph
    accent_class = Breve
    accent_y = _lc_accent


# ── Dotless i ────────────────────────────────────────────────────────


class LowercaseDotlessIGlyph(LowercaseIGlyph):
    name = "lowercase_dotlessi"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)


class LowercaseDotlessI2Glyph(LowercaseI2Glyph):
    name = "lowercase_dotlessi_2"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)


# ── Uppercase with acute ─────────────────────────────────────────────


class UppercaseAAcuteGlyph(ComposedGlyph):
    name = "uppercase_aacute"
    unicode = "0xC1"
    base_glyph_class = UppercaseAGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseEAcuteGlyph(ComposedGlyph):
    name = "uppercase_eacute"
    unicode = "0xC9"
    base_glyph_class = UppercaseEGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseIAcuteGlyph(ComposedGlyph):
    name = "uppercase_iacute"
    unicode = "0xCD"
    base_glyph_class = UppercaseIGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseOAcuteGlyph(ComposedGlyph):
    name = "uppercase_oacute"
    unicode = "0xD3"
    base_glyph_class = UppercaseOGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseUAcuteGlyph(ComposedGlyph):
    name = "uppercase_uacute"
    unicode = "0xDA"
    base_glyph_class = UppercaseUGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseYAcuteGlyph(ComposedGlyph):
    name = "uppercase_yacute"
    unicode = "0xDD"
    base_glyph_class = UppercaseYGlyph
    accent_class = Acute
    accent_y = _uc_accent


# ── Uppercase with grave ─────────────────────────────────────────────


class UppercaseAGraveGlyph(ComposedGlyph):
    name = "uppercase_agrave"
    unicode = "0xC0"
    base_glyph_class = UppercaseAGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseEGraveGlyph(ComposedGlyph):
    name = "uppercase_egrave"
    unicode = "0xC8"
    base_glyph_class = UppercaseEGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseIGraveGlyph(ComposedGlyph):
    name = "uppercase_igrave"
    unicode = "0xCC"
    base_glyph_class = UppercaseIGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseOGraveGlyph(ComposedGlyph):
    name = "uppercase_ograve"
    unicode = "0xD2"
    base_glyph_class = UppercaseOGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseUGraveGlyph(ComposedGlyph):
    name = "uppercase_ugrave"
    unicode = "0xD9"
    base_glyph_class = UppercaseUGlyph
    accent_class = Grave
    accent_y = _uc_accent


# ── Uppercase with circumflex ────────────────────────────────────────


class UppercaseACircumflexGlyph(ComposedGlyph):
    name = "uppercase_acircumflex"
    unicode = "0xC2"
    base_glyph_class = UppercaseAGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseECircumflexGlyph(ComposedGlyph):
    name = "uppercase_ecircumflex"
    unicode = "0xCA"
    base_glyph_class = UppercaseEGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseICircumflexGlyph(ComposedGlyph):
    name = "uppercase_icircumflex"
    unicode = "0xCE"
    base_glyph_class = UppercaseIGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseOCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ocircumflex"
    unicode = "0xD4"
    base_glyph_class = UppercaseOGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseUCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ucircumflex"
    unicode = "0xDB"
    base_glyph_class = UppercaseUGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


# ── Uppercase with dieresis ──────────────────────────────────────────


class UppercaseADieresisGlyph(ComposedGlyph):
    name = "uppercase_adieresis"
    unicode = "0xC4"
    base_glyph_class = UppercaseAGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseEDieresisGlyph(ComposedGlyph):
    name = "uppercase_edieresis"
    unicode = "0xCB"
    base_glyph_class = UppercaseEGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseIDieresisGlyph(ComposedGlyph):
    name = "uppercase_idieresis"
    unicode = "0xCF"
    base_glyph_class = UppercaseIGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseODieresisGlyph(ComposedGlyph):
    name = "uppercase_odieresis"
    unicode = "0xD6"
    base_glyph_class = UppercaseOGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseUDieresisGlyph(ComposedGlyph):
    name = "uppercase_udieresis"
    unicode = "0xDC"
    base_glyph_class = UppercaseUGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


# ── Uppercase with tilde ─────────────────────────────────────────────


class UppercaseATildeGlyph(ComposedGlyph):
    name = "uppercase_atilde"
    unicode = "0xC3"
    base_glyph_class = UppercaseAGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseNTildeGlyph(ComposedGlyph):
    name = "uppercase_ntilde"
    unicode = "0xD1"
    base_glyph_class = UppercaseNGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseOTildeGlyph(ComposedGlyph):
    name = "uppercase_otilde"
    unicode = "0xD5"
    base_glyph_class = UppercaseOGlyph
    accent_class = Tilde
    accent_y = _uc_accent


# ── Uppercase with ring ──────────────────────────────────────────────


class UppercaseARingGlyph(ComposedGlyph):
    name = "uppercase_aring"
    unicode = "0xC5"
    base_glyph_class = UppercaseAGlyph
    accent_class = Ring
    accent_y = _uc_accent


# ── Uppercase with cedilla ───────────────────────────────────────────


class UppercaseCCedillaGlyph(ComposedGlyph):
    name = "uppercase_ccedilla"
    unicode = "0xC7"
    base_glyph_class = UppercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class UppercaseSCedillaGlyph(ComposedGlyph):
    name = "uppercase_scedilla"
    unicode = "0x15E"
    base_glyph_class = UppercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Uppercase with caron ─────────────────────────────────────────────


class UppercaseSCaronGlyph(ComposedGlyph):
    name = "uppercase_scaron"
    unicode = "0x160"
    base_glyph_class = UppercaseSGlyph
    accent_class = Caron
    accent_y = _uc_accent


# ── Uppercase with breve ─────────────────────────────────────────────


class UppercaseGBreveGlyph(ComposedGlyph):
    name = "uppercase_gbreve"
    unicode = "0x11E"
    base_glyph_class = UppercaseGGlyph
    accent_class = Breve
    accent_y = _uc_accent


# ── Uppercase with dot above ─────────────────────────────────────────


class UppercaseIDotGlyph(ComposedGlyph):
    name = "uppercase_idotaccent"
    unicode = "0x130"
    base_glyph_class = UppercaseIGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


# ── Uppercase with macron (romaji long vowels) ───────────────────────


class UppercaseAMacronGlyph(ComposedGlyph):
    name = "uppercase_amacron"
    unicode = "0x100"
    base_glyph_class = UppercaseAGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseEMacronGlyph(ComposedGlyph):
    name = "uppercase_emacron"
    unicode = "0x112"
    base_glyph_class = UppercaseEGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseIMacronGlyph(ComposedGlyph):
    name = "uppercase_imacron"
    unicode = "0x12A"
    base_glyph_class = UppercaseIGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseOMacronGlyph(ComposedGlyph):
    name = "uppercase_omacron"
    unicode = "0x14C"
    base_glyph_class = UppercaseOGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseUMacronGlyph(ComposedGlyph):
    name = "uppercase_umacron"
    unicode = "0x16A"
    base_glyph_class = UppercaseUGlyph
    accent_class = Macron
    accent_y = _uc_accent


# ── Polish: acute ────────────────────────────────────────────────────


class LowercaseCAcuteGlyph(ComposedGlyph):
    name = "lowercase_cacute"
    unicode = "0x107"
    base_glyph_class = LowercaseCGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseNAcuteGlyph(ComposedGlyph):
    name = "lowercase_nacute"
    unicode = "0x144"
    base_glyph_class = LowercaseNGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseSAcuteGlyph(ComposedGlyph):
    name = "lowercase_sacute"
    unicode = "0x15B"
    base_glyph_class = LowercaseSGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseZAcuteGlyph(ComposedGlyph):
    name = "lowercase_zacute"
    unicode = "0x17A"
    base_glyph_class = LowercaseZGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseCAcuteGlyph(ComposedGlyph):
    name = "uppercase_cacute"
    unicode = "0x106"
    base_glyph_class = UppercaseCGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseNAcuteGlyph(ComposedGlyph):
    name = "uppercase_nacute"
    unicode = "0x143"
    base_glyph_class = UppercaseNGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseSAcuteGlyph(ComposedGlyph):
    name = "uppercase_sacute"
    unicode = "0x15A"
    base_glyph_class = UppercaseSGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseZAcuteGlyph(ComposedGlyph):
    name = "uppercase_zacute"
    unicode = "0x179"
    base_glyph_class = UppercaseZGlyph
    accent_class = Acute
    accent_y = _uc_accent


# ── Polish: dot above ────────────────────────────────────────────────


class LowercaseZDotGlyph(ComposedGlyph):
    name = "lowercase_zdotaccent"
    unicode = "0x17C"
    base_glyph_class = LowercaseZGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseZDotGlyph(ComposedGlyph):
    name = "uppercase_zdotaccent"
    unicode = "0x17B"
    base_glyph_class = UppercaseZGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


# ── Polish: ogonek ───────────────────────────────────────────────────


class OgonekComposedGlyph(ComposedGlyph):
    """Hangs the ogonek from the base glyph's measured outline, so it follows
    the real shape of each base (including italic variants)."""

    accent_class = Ogonek
    accent_y = 0
    # Hang from the rightmost stem, spanning it from its inner to its outer
    # edge. Otherwise the hook is a stem wide and placed by `ogonek_inset`.
    from_stem = False
    # Hook center, measured from the base's right edge as a fraction of its
    # width (0 = flush with the right edge).
    ogonek_inset = 0.0
    ogonek_width = Ogonek.stem_ratio  # Start width, relative to stroke_x
    ogonek_start = 0.0
    stem_probe = 0.25  # Height where the stem is measured, relative to x-height

    def _base_path(self, base, dc):
        path = pathops.Path()
        pen = pathops.PathPen(path)
        base.draw_base(pen, dc) if hasattr(base, "draw_base") else base.draw(pen, dc)
        return pathops.simplify(path)

    def _rightmost_stem(self, path, dc):
        """Horizontal span of the rightmost piece of the outline crossing a
        thin band just above the baseline."""
        y = self.stem_probe * dc.x_height
        band = pathops.Path()
        draw_rect(pathops.PathPen(band), -1000, y, 2000, y + 1)
        section = pathops.op(path, band, pathops.PathOp.INTERSECTION)
        pieces = []
        for contour in section.contours:
            xs = [x for _, points in contour for x, _ in points]
            pieces.append((min(xs), max(xs)))
        return max(pieces, key=lambda piece: piece[1])

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        base.draw_base(pen, dc) if hasattr(base, "draw_base") else base.draw(pen, dc)

        path = self._base_path(base, dc)
        start = self.ogonek_start * dc.x_height
        if self.from_stem:
            x1, x2 = self._rightmost_stem(path, dc)
            Ogonek().draw_at(
                pen,
                dc,
                x=(x1 + x2) / 2,
                y=self.accent_y,
                width=x2 - x1,
                start=start,
            )
        else:
            x1, _, x2, _ = path.bounds
            width = self.ogonek_width * dc.stroke_x
            x = x2 - self.ogonek_inset * (x2 - x1) - width / 2
            Ogonek().draw_at(
                pen, dc, x=x, y=self.accent_y, width=width, start=start
            )


class LowercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_aogonek"
    unicode = "0x105"
    base_glyph_class = LowercaseAGlyph
    from_stem = True


class LowercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_eogonek"
    unicode = "0x119"
    base_glyph_class = LowercaseEGlyph
    ogonek_inset = 0.3


class UppercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_aogonek"
    unicode = "0x104"
    base_glyph_class = UppercaseAGlyph
    ogonek_width = 0.85
    ogonek_inset = 0.05


class UppercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_eogonek"
    unicode = "0x118"
    base_glyph_class = UppercaseEGlyph
    ogonek_inset = 0.2


# ── Polish: stroke ───────────────────────────────────────────────────


class LowercaseLStrokeGlyph(ComposedGlyph):
    name = "lowercase_lslash"
    unicode = "0x142"
    base_glyph_class = LowercaseLGlyph
    accent_class = Stroke
    accent_y = 0.55 * fc.ascent

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)


class UppercaseLStrokeGlyph(ComposedGlyph):
    name = "uppercase_lslash"
    unicode = "0x141"
    base_glyph_class = UppercaseLGlyph
    accent_class = UppercaseStroke
    accent_y = 0.45 * fc.cap

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)
