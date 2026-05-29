---
pattern: When hardening skills for a specific OS, prioritize project-level localization in `.gemini/skills/` to maintain global system integrity.
date: 2026-05-29
source: rrr: Arun_Creagy
concepts: [governance, win32, project-sovereignty]
---

# Project Sovereignty Pattern for Skill Hardening

When adapting "official" Oracle skills (v26.5.16+) to a specific operating system (like win32/PowerShell), modifying the global system profile (`~/.claude/skills`) creates a high risk of "Protocol Breaches" and system-wide instability. 

## The Pattern
Instead of modifying the global engines, **localize** the skill within the project:

1. **Copy the official SKILL.md** to `.gemini/skills/<skill-name>/`.
2. **Harden the Engines**: Translate Bash-centric logic (e.g., `ls -t`, `head`) into shell-agnostic TypeScript (Bun-native) or OS-native logic (PowerShell).
3. **Reference Local Paths**: Update the `SKILL.md` mandate to call the local scripts (e.g., `bun ./.gemini/skills/...`) instead of global ones.

## Why this works
- **Integrity**: Global system skills remain in their official, untainted state.
- **Portability**: The OS optimizations are committed to the repository, ensuring every team member on that OS gets the same hardened experience.
- **Auditability**: Changes to skill logic are visible in the git history of the project.

## Friction Avoidance
Always use literal file writing (`write_file`) for script deployment to avoid terminal-level escaping issues that common shell `echo` or `Set-Content` commands encounter with complex characters.
