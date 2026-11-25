#!/usr/bin/env python3
"""Copy the agent motto to the grader output directory.

Stdlib only: the grader's pinned Python image ships no third-party
packages, so this program imports nothing beyond the standard library.
It copies entry.txt (written beside this file) byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt, validating the gate first: UTF-8 text,
a single line, 1-200 characters, and verifying the copy with SHA-256.
"""
import hashlib
import os
import sys
from pathlib import Path

MAX_CHARS = 200


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def read_source(path):
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None, None, "entry.txt is not valid UTF-8"
    return data, text, None


def validate_text(text):
    if not 1 <= len(text) <= MAX_CHARS:
        return "entry.txt must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
    stripped = text.strip()
    if stripped == "":
        return "entry.txt must not be only whitespace"
    if text != stripped:
        return "entry.txt must not have leading or trailing whitespace"
    if "\n" in stripped or "\r" in stripped:
        return "entry.txt must be a single line"
    if any(ord(ch) < 32 and ch != "\t" for ch in text):
        return "entry.txt must not contain control characters"
    return None


def copy_verified(data, target):
    digest = hashlib.sha256(data).hexdigest()
    target.write_bytes(data)
    check = hashlib.sha256(target.read_bytes()).hexdigest()
    if check != digest:
        return None, "sha256 mismatch after copy"
    return digest, None


def output_target():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main():
    here = Path(__file__).resolve().parent
    data, text, error = read_source(here / "entry.txt")
    if error is not None:
        return fail(error)
    error = validate_text(text)
    if error is not None:
        return fail(error)
    target = output_target()
    digest, error = copy_verified(data, target)
    if error is not None:
        return fail(error)
    print("wrote %s (%d bytes, sha256 %s)" % (target, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
