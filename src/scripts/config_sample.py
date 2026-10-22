#!/usr/bin/env python3
"""Build the Regular OTF of a custom config and render a code sample with it.

Usage: python -m scripts.config_sample nordley
  reads configs/nordley/config.yml, writes configs/nordley/sample.png
"""

import argparse
import os

from config import FontConfig as fc, load_config
from generate_font import build_font
from scripts.samples import SAMPLE_1, _lexer, _target_image_width, render_sample
from pygments.lexers import PythonLexer


def main(name):
    config_dir = os.path.join("configs", name)
    load_config(os.path.join(config_dir, "config.yml"))

    family = fc.family_name.replace(" ", "")
    out_root = f"custom-fonts/{family}"
    os.makedirs(f"{out_root}/otf", exist_ok=True)
    font_path = f"{out_root}/otf/{family}-Regular.otf"
    build_font(output_path=font_path, ttf=False, out_root=out_root)

    render_sample(
        os.path.join(config_dir, "sample.png"),
        _lexer(PythonLexer),
        SAMPLE_1,
        font_path,
        _target_image_width(font_path),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("name", help="Folder name under configs/")
    main(parser.parse_args().name)
