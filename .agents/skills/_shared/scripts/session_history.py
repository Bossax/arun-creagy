#!/usr/bin/env python3
"""Host-neutral session-history adapter for Antigravity and Codex.

The script only reads the explicitly selected host's known local session roots and
prints a normalized JSON document. It intentionally returns an unavailable result
for an unknown host instead of probing every provider directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


def repo_slug() -> str:
    root = os.environ.get("ORACLE_SKILL_REPO", Path.cwd().name)
    return re.sub(r"[_\\s]+", "-", Path(root).name).lower()


def host_roots(host: str) -> list[Path]:
    home = Path(os.environ.get("USERPROFILE") or Path.home())
    if host == "antigravity":
        return [
            home / ".gemini" / "tmp" / repo_slug() / "chats",
            home / ".gemini" / "antigravity-cli" / "brain",
        ]
    if host == "codex":
        return [home / ".codex" / "sessions"]
    return []


def value_at(data: Any, *paths: tuple[str, ...]) -> Any:
    for path in paths:
        current = data
        for key in path:
            if not isinstance(current, dict) or key not in current:
                current = None
                break
            current = current[key]
        if current not in (None, ""):
            return current
    return None


def as_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(as_text(item) for item in value if as_text(item))
    if isinstance(value, dict):
        return as_text(value.get("text") or value.get("content") or "")
    return ""


def is_user_message(record: dict[str, Any]) -> bool:
    kind = str(value_at(record, ("type",), ("role",), ("payload", "type")) or "").lower()
    role = str(value_at(record, ("payload", "role"), ("role",)) or "").lower()
    return kind in {"user", "user_message", "user_input", "user_explicit"} or role == "user"


def parse_file(path: Path) -> dict[str, Any] | None:
    started: str | None = None
    ended: str | None = None
    messages: list[dict[str, str]] = []
    try:
        with path.open(encoding="utf-8") as handle:
            for raw in handle:
                try:
                    record = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                timestamp = value_at(record, ("timestamp",), ("created_at",), ("payload", "timestamp"))
                if isinstance(timestamp, str):
                    started = started or timestamp
                    ended = timestamp
                if is_user_message(record):
                    content = as_text(value_at(record, ("content",), ("payload", "content"), ("message", "content")))
                    if content:
                        messages.append({"timestamp": timestamp or "", "content": content[:400]})
    except (OSError, UnicodeError):
        return None
    if not started and not messages:
        return None
    session_id = re.sub(r"^(session-|rollout-)", "", path.stem)
    return {
        "sessionId": session_id[:64],
        "startedAt": started,
        "endedAt": ended,
        "messages": messages,
        "source": str(path),
    }


def recent_jsonl(roots: list[Path], limit: int) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        if root.is_dir():
            try:
                files.extend(item for item in root.rglob("*.jsonl") if item.is_file())
            except OSError:
                continue

    def mtime(path: Path) -> float:
        try:
            return path.stat().st_mtime
        except OSError:
            return -1

    return sorted(files, key=mtime, reverse=True)[:limit]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", choices=["auto", "antigravity", "codex"], default="auto")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    host = os.environ.get("ORACLE_SKILL_HOST", "").lower() if args.host == "auto" else args.host
    if host not in {"antigravity", "codex"}:
        print(json.dumps({"available": False, "host": "unknown", "sessions": [], "reason": "unknown-host"}))
        return 0
    roots = host_roots(host)
    found_roots = [root for root in roots if root.is_dir()]
    if not found_roots:
        print(json.dumps({"available": False, "host": host, "sessions": [], "reason": "history-root-not-found"}))
        return 0
    sessions = [result for file in recent_jsonl(found_roots, max(1, args.limit)) if (result := parse_file(file))]
    print(json.dumps({"available": bool(sessions), "host": host, "sessions": sessions, "reason": None if sessions else "no-readable-sessions"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
