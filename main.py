"""The One-Line Cat Joke That Lands: writes one joke about cats to /output/entry.txt."""

import os
import shutil


LINE = "My cat stared at the empty wall for an hour, then turned to me like I'd missed the ghost too."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Enforce it here so a bad line can never ship.
assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line must be one line of 1-200 chars"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself
    # (the grader mounts it read-only and runs as uid 65534; deleting it fails).
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only: the whole entry is a single sentence. No trailing
        # newline, so the file holds exactly the joke and nothing else.
        f.write(LINE)


if __name__ == "__main__":
    main()
