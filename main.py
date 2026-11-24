"""TabRent pitch runner.

Reads the one-sentence micro-startup pitch from entry.txt, checks it is a
single line under the 200-character bounty cap, and prints it.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).resolve().parent / "entry.txt"
MAX_CHARS = 200


def load_pitch(path=ENTRY_FILE):
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty")
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError(f"expected exactly one line, got {len(lines)}")
    pitch = lines[0]
    if len(pitch) > MAX_CHARS:
        raise ValueError(f"pitch is {len(pitch)} chars, cap is {MAX_CHARS}")
    return pitch


def main():
    print(load_pitch())


if __name__ == "__main__":
    main()
