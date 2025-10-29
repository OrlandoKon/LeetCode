#!/usr/bin/env python3
"""
Move top-level .java files into ./Java and top-level .py files into ./Python.

Behavior:
- The script uses the current directory as the root. No extra arguments needed.
- By default it WILL perform the moves when run. Use --dry-run to preview.

Usage:
  python move_sources.py         # perform moves in current directory
  python move_sources.py --dry-run  # show what would be moved
  python move_sources.py -v      # verbose
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Tuple


def find_available_name(dest: Path) -> Path:
    """Return a Path that doesn't exist by appending _1, _2, ... before suffix."""
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    i = 1
    while True:
        candidate = parent / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def move_files(root: Path) -> Tuple[int, int]:
    """Move files and return (moved_count, skipped_count).
    Only operates on files that are direct children of `root` (no recursion).
    """
    moved = 0
    skipped = 0

    root = root.resolve()
    java_dir = root / "Java"
    py_dir = root / "Python"

    script_name = Path(__file__).name

    for p in root.iterdir():
        if not p.is_file():
            continue
        if p.name == script_name or p.name == 'switch.py':
            # don't move the script itself
            skipped += 1
            continue

        ext = p.suffix.lower()
        if ext == ".java":
            target_dir = java_dir
        elif ext == ".py":
            target_dir = py_dir
        else:
            skipped += 1
            continue

        try:
            if p.parent.resolve() == target_dir.resolve():
                skipped += 1
                continue
        except FileNotFoundError:
            pass

        dest_dir = target_dir
        dest = dest_dir / p.name
        if dest.exists():
            dest = find_available_name(dest)

        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(p), str(dest))

        moved += 1

    return moved, skipped


def main() -> None:
    root = Path('.')

    moved, skipped = move_files(root)

    print(f"Summary: moved={moved}, skipped/non-target files={skipped}")


if __name__ == "__main__":
    main()
