#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261119.

Writes the finished image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR
when set, for local testing). Standard library only, no network, fully
deterministic: it decodes the finished image from entry.png.b64, the
single-line base64 of entry.png shipped in this repository (the PNG
itself cannot be pushed through the GitHub App's text-only snapshot
push, so it travels as text). The image was drawn by draw_entry.py
from the 19 November 2026 news; decoding the same bytes gives the
same output on every run.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(SRC, "r", encoding="ascii") as f:
        raw = base64.b64decode(f.read().strip())
    # Write the decoded bytes verbatim: same bytes in, same bytes out.
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(raw)


if __name__ == "__main__":
    main()
