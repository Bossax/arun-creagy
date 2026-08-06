# Lesson Learned: A scoring rubric built from one source's own metadata isn't evidence

**Context**: CRDB WP2 needed to rank 260 catalog rows by business criticality. First attempt used 5 criteria (sector tags, hazard-count, geographic coverage, data maturity, service linkage) — all derived from the same CSV being scored, or from a service report (D-043) that turned out to name no datasets at all.

**What went wrong**: Structure disguised the absence of grounding. Five weighted criteria felt like a defensible method, but every one of them was the catalog re-describing itself. "Cross-sector = important" was just reading the `Sectors` tag back. "National coverage = important" was actively backwards — the real demand (per D-043) was for finer sub-district granularity, not coarser national data.

**The fix**: found actual independent evidence — 34 concrete use cases in D-043 that name specific data/variable needs in prose, each traceable to a direct quote. Scoring against explicitly-stated demand (not proxy metadata) is a fundamentally different, defensible method.

**Generalizable rule**: before proposing a scoring/ranking method, ask "does any criterion here just restate the thing I'm trying to score, using different words?" If yes, it's not evidence, no matter how many criteria are stacked together. Independent grounding must come from a source separate from the object being evaluated.

**Secondary lesson**: when a domain expert asks "how do you know" about each of several criteria in a row, don't defend them one at a time — treat it as a signal the whole approach needs re-grounding.

**Tags**: evidence-grounding, scoring-methodology, crdb, wp2, data-inventory, rubric-design
