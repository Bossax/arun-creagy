"""Merge a validated draft over its real target file.

The gates run HERE, not somewhere upstream that a caller has to remember.
If either gate fails, the destination is never touched.

Usage:
    merge_draft.py <draft> <dest> --lexicon <path> [--source <path>]
    merge_draft.py <draft> <dest> --skip-gates
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from _venv import child_python


def run_gate(name, args):
    """Run a gate script. Returns True on exit 0."""
    proc = subprocess.run(
        [child_python(), str(SCRIPTS / name)] + [str(a) for a in args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    for line in out.rstrip().splitlines():
        print(f"    {line}")
    return proc.returncode == 0


def merge(draft_path, dest_path, lexicon_path=None, source_path=None, skip_gates=False):
    draft = Path(draft_path)
    dest = Path(dest_path)

    if not draft.exists():
        print(f"MERGE REFUSED: draft not found at {draft_path}")
        sys.exit(1)

    if skip_gates:
        print("!" * 66)
        print("!!  WARNING: --skip-gates -- merging WITHOUT validation.")
        print("!!  The draft has not been linted and its density is unchecked.")
        print("!" * 66)
    else:
        if not lexicon_path:
            print("MERGE REFUSED: --lexicon is required (or pass --skip-gates deliberately)")
            sys.exit(1)

        print(f"Gate 1/2  lint_thai_writing.py  {draft.name}")
        if not run_gate("lint_thai_writing.py", [draft, lexicon_path]):
            print(f"\nMERGE REFUSED: lint failed. {dest_path} was NOT modified.")
            sys.exit(1)

        if source_path:
            print(f"Gate 2/2  check_density.py  {draft.name}")
            if not run_gate("check_density.py", [source_path, draft]):
                print(f"\nMERGE REFUSED: density failed. {dest_path} was NOT modified.")
                sys.exit(1)
        else:
            print("Gate 2/2  check_density.py  skipped (no --source given)")

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(draft, dest)

    print("\nMERGE SUCCESSFUL")
    print(f"  source: {draft_path}")
    print(f"  target: {dest_path}")
    print(f"\nThe scratch directory may now be archived: {draft.parent}")
    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge a gated draft over its target file.")
    parser.add_argument("draft", help="path to the draft in the isolation directory")
    parser.add_argument("dest", help="path to the real target file")
    parser.add_argument("--lexicon", help="lexicon JSON the linter validates against")
    parser.add_argument("--source", help="original source doc, enables the density gate")
    parser.add_argument("--skip-gates", action="store_true",
                        help="merge without validating -- deliberate override only")
    ns = parser.parse_args()

    merge(ns.draft, ns.dest, ns.lexicon, ns.source, ns.skip_gates)
