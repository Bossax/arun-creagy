"""PostToolUse hook: auto-lint a Thai draft after Write/Edit. Advisory only.

Reads the hook JSON payload on stdin (tool_input.file_path). If the path is
under ψ/incubate/drafts/, runs lint_thai_writing.py against it and returns the
findings as additionalContext. Never denies -- a linter is not a gate; the gate
is merge_draft.py, which reruns this same check and can refuse to merge.

Usage (as a hook, not interactively):
    post_draft_lint.py < payload.json
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[3]  # scripts -> writing-th -> skills -> .agents -> repo root
LEXICON = REPO_ROOT / "ψ" / "memory" / "style" / "LEXICON_TH.json"
DRAFTS_MARKER = "ψ/incubate/drafts/"


def additional_context(text: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": text,
        }
    }


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except ValueError:
        return 0

    tool_input = payload.get("tool_input") or {}
    path_str = tool_input.get("file_path") or tool_input.get("path")
    if not path_str:
        return 0

    normalized = str(Path(path_str)).replace("\\", "/")
    if DRAFTS_MARKER not in normalized:
        return 0
    if not path_str.endswith(".md"):
        return 0
    if not LEXICON.exists():
        return 0

    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "lint_thai_writing.py"), path_str, str(LEXICON), "--scope", "report"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    if output.strip():
        print(json.dumps(additional_context(f"lint_thai_writing.py advisory:\n{output.strip()}")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
