---
installer: local
name: recap
description: Local recap for this repo (uses project-local script).
trigger: /recap
---

# /recap — Fresh Start Context (Local)

**Goal**: Orient quickly using the project-local recap script.

This local override runs project-local scripts (Windows-safe) and avoids unix-only shell utilities.

## Usage

```
/recap           # Rich recap (project-local script)
/recap --quick   # Fast recap (git + focus only)
```

---

## DEFAULT MODE (Local)

Run the local rich recap script:

```bash
bun .roo/skills/recap/recap-rich.ts
```

Then add 2–3 “What’s next?” options based on the output.

---

## QUICK MODE (`/recap --quick`)

Use the fast local script:

```bash
bun .roo/skills/recap/recap.ts
```

---

## "What's next?" Rules

| If you see... | Suggest... |
|---------------|------------|
| Handoff exists | Continue from handoff |
| Untracked files | Commit them |
| Focus = completed | Pick from tracks or start fresh |
| Branch ahead | Push or create PR |
| Streak active | Keep momentum going |

---

## Hard Rules

1. **ONE bash call** — never multiple parallel calls (adds latency)
2. **No subagents** — everything in main agent
3. **Ask, don't suggest** — "What next?" not "You should..."

---

**Philosophy**: Detect reality. Surface blockers. Offer direction.

