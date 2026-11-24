"""Writes one line of honest error copy to /output/entry.txt.

import os

ENTRY = (
    "Your file didn't save: the disk is full, mostly of error logs "
    "apologizing for the last crash. Free some space and try again."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
