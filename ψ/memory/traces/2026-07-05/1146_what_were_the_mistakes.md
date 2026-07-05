---
traceId: 46d06d9d-249d-4125-8bae-ce5362d76ba0
query: what were the mistakes occur in the past writing sessions
date: 2026-07-05T11:46:07+07:00
---

# Trace: Writing Mistakes and Frictions in Past Sessions

**Friction Score**: 8.5/10 (High density of recurring execution failures and style drift directly mapped to the query).

## Discovered Evidence (Physical Logs)

1. **[C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/session-metrics.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/session-metrics.md)**
   - *Date*: 2026-07-04
   - *Friction*: "Paragraph shortening over-editing", "Superficial regex replacement pass chosen initially", "Colloquialisms and AI transitions remaining in drafts".
   - *Context*: Subagents tasked with rewriting complex academic text consistently fell into goal-completion bias, either compressing the text too ruthlessly (Lossy Compression) or bypassing the line-by-line synthesis in favor of quick regex replacements.

2. **[C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/retrospectives/2026-07/04/21.27_shattered-fluff-articles-polish.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/retrospectives/2026-07/04/21.27_shattered-fluff-articles-polish.md)**
   - *Date*: 2026-07-04
   - *Friction*: The "Over-Summarization Glitch" (Shattered Fluff).
   - *Context*: When told to reduce length or use an "executive summary format," subagents destroyed the narrative structure, stripping out essential evidence and replacing it with generic bullet points (e.g., stripping 35KB down to 10KB). The correction required explicit, non-negotiable boundaries (e.g., "Must be EXACTLY 75% of original length").

3. **[C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/2026-07-04-NCAIF-Chapter-5.2-Rewrite-SOP.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/2026-07-04-NCAIF-Chapter-5.2-Rewrite-SOP.md)**
   - *Date*: 2026-07-04
   - *Friction*: Jargon trap, batching failures, and internal logic leaks.
   - *Context*: Batching multiple sections to one subagent caused hallucination. Without the "4-Pillar Payload Gate" and "1-to-1 Micro-Scoping," agents would slip into passive voice, translated English constructs ("ไม่ได้...แต่..."), and abstract prestige wording.

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: AI agents default to lossy compression (generic bullet points, stripped evidence) and passive/translated consultant-speak when tasked with "executive summaries" or structural rewrites without deterministic boundaries.
- **[E] Supporting Evidence**: [C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/retrospectives/2026-07/04/21.27_shattered-fluff-articles-polish.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/retrospectives/2026-07/04/21.27_shattered-fluff-articles-polish.md), [C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/session-metrics.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/session-metrics.md)
- **[D] Potential Decision**: Enforce the **Harness Architecture (v3.0.0)** for all audience-facing document generation. This requires: 1-to-1 Micro-Scoping (no batching), the 4-Pillar Payload Gate (mandatory `<thought>` blocks extracting Claims/Examples), and strict Line-by-Line Synthesis against the NCAIF Style Pack (banning regex shortcuts).
- **[A] Target Asset**: [C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/Full_Report_Final.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/Full_Report_Final.md) (and upcoming Executive Summary generation).
