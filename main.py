#!/usr/bin/env python3
"""Make the coolest art — make.fun bounty coolest-art-01.

Writes one piece of art, "Phoenix Rebirth", to /output/entry.png.

The artwork is bundled with this program as art.png.b64: the 1024x1024
PNG (910,391 bytes, under the 1 MiB limit) encoded as a single line of
base64 text, so the repository holds no binary files. This program
decodes it at runtime and writes the exact PNG bytes to the output
path, so both sandbox runs produce identical bytes.

No network access, no randomness, no third-party dependencies: only the
Python 3.13 standard library is used. Deterministic by construction.
"""

import base64
import os
import sys

# Artwork bundled in this repository, next to this file, as base64 text.
ART_B64_FILENAME = "art.png.b64"

# Required output path for the competition.
OUTPUT_PATH = "/output/entry.png"

# Hard limits from the competition brief (checked after the copy).
MAX_BYTES = 1_048_576  # 1 MiB
MAX_DIMENSION = 1024


def _repo_path(filename):
    """Resolve a file bundled next to this script, wherever it is run from."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, filename)


def _png_dimensions(path):
    """Read width/height from a PNG header (bytes 16..24), stdlib only."""
    with open(path, "rb") as f:
        header = f.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("artwork is not a PNG file")
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    return width, height


def write_entry():
    """Decode the bundled artwork and write the exact PNG bytes out."""
    source = _repo_path(ART_B64_FILENAME)
    if not os.path.isfile(source):
        raise FileNotFoundError("bundled artwork missing: %s" % source)

    with open(source, "r", encoding="ascii") as f:
        encoded = f.read().strip()
    try:
        png_bytes = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise ValueError("bundled artwork is not valid base64: %s" % exc)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(png_bytes)

    size = os.path.getsize(OUTPUT_PATH)
    if size > MAX_BYTES:
        raise ValueError(
            "output is %d bytes, over the 1 MiB limit" % size
        )
    width, height = _png_dimensions(OUTPUT_PATH)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            "output is %dx%d, over the 1024x1024 limit" % (width, height)
        )
    return OUTPUT_PATH, size, width, height


def main():
    """Entry point: write the art and report what was written."""
    try:
        path, size, width, height = write_entry()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, %dx%d PNG)" % (path, size, width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
