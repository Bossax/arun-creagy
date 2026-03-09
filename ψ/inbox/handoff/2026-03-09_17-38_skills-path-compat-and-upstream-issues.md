# Handoff: Skill path compatibility (Roo vs Claude) + upstream notifications

**Date**: 2026-03-09 17:38
**Context**: Resolved Oracle skill invocation failures caused by docs hardcoding Claude skill home in a Roo environment; informed upstream and tracked locally.

## What We Did
- Diagnosed that multiple skill docs hardcode  while Roo installs to .
- Implemented a local compatibility setup so Claude-path invocations work (validated with # RECAP

🕐 17:38 | Mar 09, 2026

---

## 🚧 FOCUS
`none` No active focus

## 📅 TODAY
No schedule

## 📊 GIT: main (+0 ahead)
Last: docs: rewrite README for Arun Creagy + refresh pulse identit

**Untracked** (2):
  ψ/inbox/handoff/2026-03-09_17-38_skills-path-compat-and-upstream-issues.md
  ψ/memory/learnings/2026-03-09_skill-path-compat-link.md

---

## 📝 LAST SESSION
Retro: ψ\memory\retrospectives\2026-03\09\11.45_awaken-arun-creagy-realignment.md
Handoff: none).
- Opened upstream issue in oracle-v2: https://github.com/Soul-Brews-Studio/oracle-v2/issues/344
- Opened local tracking issue in this repo: https://github.com/Bossax/arun_creagy/issues/1
- Wrote internal note with workaround + undo guidance: ψ/memory/learnings/2026-03-09_skill-path-compat-link.md

## Pending
- [ ] Confirm whether  is a real link (junction/symlink) vs a mirrored directory; current evidence shows same hashes but not samefile → drift risk.
- [ ] Monitor oracle-v2#344 for an upstream agent-agnostic fix (docs + runtime path resolution).

## Next Session
- [ ] Run  to re-orient.
- [ ] If upstream ships a fix: remove local workaround and standardize on the supported approach.

## Key Files
- [ψ/memory/learnings/2026-03-09_skill-path-compat-link.md](ψ/memory/learnings/2026-03-09_skill-path-compat-link.md:1)
- [ψ/memory/logs/info/2026-03-09_12-50_recap-skill-path-assumption.md](ψ/memory/logs/info/2026-03-09_12-50_recap-skill-path-assumption.md:1)
