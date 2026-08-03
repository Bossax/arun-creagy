---
date: 2026-08-03
tags: [claude-code, skills, verification, harness-mechanics]
source: "rrr: Arun_Creagy"
---

# Verify harness mechanics before asserting them

**Pattern**: Claims about how the agent harness resolves things (skill precedence between project `.claude/skills/` and global `~/.claude/skills/`, tool discovery paths, config-file conventions) are empirical facts specific to that harness version/setup — not things to infer from plausible-sounding architecture or "how it should work." They need a live test before being stated as fact.

**Concrete instance**: After copying adapted skills into a repo's `.claude/skills/`, claimed "Claude Code will discover them here, project-scoped, taking priority over the global `~/.claude/skills/` versions" — stated with confidence, never tested. The next `/rrr` invocation loaded the global skill instead, directly contradicting the claim. This happened in the same session where an earlier unverified assumption (`.agents/skills/` being on Claude Code's discovery path) had already been caught and corrected — the lesson didn't transfer from one instance to the next within the same session.

**Why it matters**: An unverified harness-mechanics claim doesn't just risk being wrong once — it silently invalidates every downstream action taken on the assumption. In this case, an entire round of "project-scoped adaptation" work was built on top of an assumption about precedence that turned out false, discovered only because the user happened to invoke the skill directly.

**Fix going forward**: Any claim of the form "X will take priority" / "the harness resolves this as Y" gets phrased as a hypothesis and tested with the cheapest available real invocation *before* being reported as settled — not after, and not "probably" stated as certain in the meantime.
