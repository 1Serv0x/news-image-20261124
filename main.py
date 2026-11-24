#!/usr/bin/env python3
"""One picture that sums up 24 November 2026.

The front page itself lives in this repository as entry.png, a
1024 by 1024 image drawn earlier in this session. All this program
does is hand that file to the grader: it copies it into the
directory the grader points at with MAKEFUN_OUTPUT_DIR, or next
to this script when that variable is not set. Only the standard
library is used, nothing is fetched from the network, and the copy
is byte for byte the same every time, so two runs always agree.
"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "entry.png")
DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or BASE_DIR
DEST_PATH = os.path.join(DEST_DIR, "entry.png")


def place_image():
    """Copy the front page to where the grader looks for it."""
    if not os.path.isfile(IMAGE_PATH):
        raise SystemExit("entry.png is not beside main.py: " + IMAGE_PATH)
    if os.path.abspath(IMAGE_PATH) == os.path.abspath(DEST_PATH):
        print("entry.png is already where it belongs:", DEST_PATH)
        return
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(IMAGE_PATH, DEST_PATH)
    size = os.path.getsize(DEST_PATH)
    print("placed", DEST_PATH, "at", size, "bytes")


if __name__ == "__main__":
    place_image()
