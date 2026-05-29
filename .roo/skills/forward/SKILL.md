---
installer: local
name: forward
description: Local /forward for Roo (no plan mode). Writes handoff (ψ), plan (plans/), and outbox pending (ψ).
trigger: /forward
---

# /forward — Handoff + Plan (Local, Roo)

This repo uses **plan artifacts** under [`plans/`](plans:1) instead of any “plan mode UI”.

**Default contract**

- Write **handoff** to [`ψ/inbox/handoff/`](ψ/inbox/handoff:1) (vault; do **not** commit)
- Write **plan** to [`plans/`](plans:1) (repo; may be committed)
- Write/update **outbox pending** at [`ψ/outbox/`](ψ/outbox:1) (vault; do **not** commit)
- **Never** create GitHub issues unless explicitly requested via `--issues`

## Usage

```bash
/forward "tor section 11 redlines"
/forward --only "wrap up"
/forward --plan-only "next session plan"
/forward --no-outbox "handoff + plan only"
/forward --issues "offer issue creation"
```

## Action (Windows-safe, no bash)

Run the local script:

```bash
bun .roo/skills/forward/forward.ts -- "<optional focus/slug>"
```

### Script outputs

The script prints:

- Handoff path (ψ)
- Plan path (plans)
- Outbox path (ψ)

## Hard Rules

1. **Never `git add` files under `ψ/`**.
2. If `--issues` is used, you must ask for explicit confirmation before running any `gh issue create`.
3. If ψ is a symlink, always write to the resolved real path.

