# Plan: Skills path compatibility + upstream follow-up

**Date**: 2026-03-09 17:38

## What we accomplished

- Confirmed root cause: skill docs hardcode Claude skill home (`~/.claude/skills/...`) while Roo installs to `~/.roo/skills/...`.
- Implemented a local compatibility setup so `bun ~/.claude/skills/...` works.
- Opened upstream issue: https://github.com/Soul-Brews-Studio/oracle-v2/issues/344
- Opened local tracking issue: https://github.com/Bossax/arun_creagy/issues/1

## Current state (important)

- `bun ~/.claude/skills/recap/recap.ts` now works.
- Evidence suggests `~/.claude/skills` is currently a **mirrored directory** (hashes match) rather than a proven link to `~/.roo/skills` (`samefile=False`) → risk of drift.

Details captured in:
- [ψ/memory/learnings/2026-03-09_skill-path-compat-link.md](ψ/memory/learnings/2026-03-09_skill-path-compat-link.md:1)

## Pending

- [ ] Decide whether to convert mirror → junction/symlink (reduces drift, increases coupling).
- [ ] Monitor `oracle-v2#344` for upstream fix and remove/adjust local workaround when available.

## Next Session: Pick Your Path

| Option | Command | What It Does |
|---|---|---|
| **Continue** | `/recap` | Re-orient, then continue upstream follow-up |
| **Clean up first** | Review untracked vault files, then `/recap` | Decide whether to commit/ignore untracked ψ changes |
| **Fresh start** | `/recap --quick` | Minimal context, start a different thread |

### Cleanup Checklist (if any)

- [ ] Review `git status --short` (untracked vault files may be expected; decide on policy)
- [ ] Optionally: add a note to [`README.md`](README.md:1) about skill path assumptions (if you want future-you to remember quickly)

