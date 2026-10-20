.PHONY: install build build-otf install-mac

install:
	uv sync

build:
	uv run python -m generate_font --web-font
	uv run python -m scripts.banner
	uv run python -m scripts.specimen_pdf
	uv run python -m scripts.samples
	uv run python -m scripts.alternatives_markdown

build-font:
	uv run python -m generate_font --web-font

build-otf:
	uv run python -m generate_font --otf

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts

visualize:
	open -n -a /Library/Frameworks/Python.framework/Versions/3.12/Resources/Python.app \
    --env "__PYVENV_LAUNCHER__=$PWD/.venv/bin/python" \
    --args -m visualize lowercase_a
