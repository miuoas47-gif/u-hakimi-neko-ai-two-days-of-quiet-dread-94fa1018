"""Two Days of Quiet Dread — a one-line approving review with quiet dread.

Runs with no arguments and exits 0. Writes a single line of at most
140 characters to entry.txt inside $MAKEFUN_OUTPUT_DIR (falling back
to ./output when that variable is not set), exactly as the grader
expects: the repository is read-only, only the output dir is writable.
The line is a fixed constant, so two runs are byte-identical.
"""

import os
from pathlib import Path

COMMENT = "Approved. The tests pass, the sun will expand, and neither fact really changes the other, so ship it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Single line, no trailing newline: the gate counts characters,
    # and one clean line is what a tired reviewer would paste.
    (out_dir / "entry.txt").write_text(COMMENT, encoding="utf-8")


if __name__ == "__main__":
    main()
