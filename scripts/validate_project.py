#!/usr/bin/env python3
"""Perform structural checks for the DOS assembly project."""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    required = [ROOT / "src/main.asm", ROOT / "src/file.txt", ROOT / "src/Score.txt"]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing runtime files: {', '.join(missing)}")

    source = (ROOT / "src/main.asm").read_text(encoding="utf-8", errors="replace").lower()
    markers = [".model small", ".stack", ".data", ".code", "int 21h"]
    absent = [marker for marker in markers if marker not in source]
    if absent:
        raise SystemExit(f"Missing assembly sections/instructions: {', '.join(absent)}")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    generated = [path for path in tracked if Path(path).suffix.lower() in {".exe", ".obj"}]
    if generated:
        raise SystemExit("Generated DOS binaries are tracked: " + ", ".join(generated))

    print(f"Validated {len(source.splitlines())} lines of MASM source and required data files.")


if __name__ == "__main__":
    main()
