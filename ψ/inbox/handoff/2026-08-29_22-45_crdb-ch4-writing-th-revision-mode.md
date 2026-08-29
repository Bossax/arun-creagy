# Handoff: CRDB Chapter 4 revision-mode upgrade + writing-th cost architecture

**Date**: 2026-08-29 22:45
**Context**: Long session, single continuous thread, hit the account 5-hour usage limit mid-pipeline (reset 22:30 Bangkok — has now passed as of this handoff)

## What We Did

Upgraded CRDB executive-summary Chapter 4 (§4.1–4.4), drafted under writing-th v5 with no argument-map artifact, through the v6 pipeline via a new **revision mode** built specifically for this: recover the argument a finished draft already makes, repair what it left implicit, verbalize fresh from the repaired map.

**Harness changes (durable, committed to disk but not yet git-committed):**
- New `.agents/skills/writing-th/references/revision-mode.md` — the map-recovery doctrine: `recovered` / `repaired` / `new` provenance tags per argument unit, read-prior-draft-before-sources ordering, what recovery must and must not do.
- `SKILL.md` Stage 1 gained a revision branch; `artifact-schemas.md` gained `prior_draft`, `prior_approval`, unit-level `provenance`; `subagent-prompts.md` and `.claude/agents/th-argument-mapper.md` wired to match.
- Fixed the `.claude/skills/writing-th` vs `.agents/skills/writing-th` drift — the `.claude` copy was missing the entire v6.1 Stage 0/3 patch and had no `subagent-prompts.md` at all, which `check_skill_drift.py`'s `PAIRS` list never even checked for. Added that pair, ran `--sync`. `run_tests.py`: 44/44 passing.

**Pipeline run, all four sections (§4.1–4.4):**
- **Stage 0**: contracts amended — `report_specific_rules` backfilled (12 rules) from the writing plan's format block plus standing project rules and the committee's academic-register demand; `prior_draft` set; prior approvals preserved as `prior_approval`; new approval recorded under Boss's standing bypass (quoted verbatim in each contract's `approval.basis`).
- **Stage 1**: 4 argument maps recovered via `th-argument-mapper` (revision mode), all passing `argument_gate.py validate`. 29 units total: 8 recovered, 18 repaired, 3 new. Caught and fixed three real problems: an unverifiable "Paris Agreement Article 13" citation in §4.1 (regrounded on the actual verified source), a plan self-contradiction on Sitemap v9's category count (plan says 4 in one place, 6 in another and in the source file — 6 confirmed correct), and a near-verbatim duplicated Agile argument across §4.3/§4.4 (now owned solely by §4.3, §4.4 keeps only the sequencing consequence). Independently verified the 5-agency/97-dataset/37% figures in §4.3 against `data_catalog_v4.csv` — exact.
- **Chapter-spine check**: read all four maps together before verbalizing, caught an implicit 4.1→4.2 handoff, an apparent (but resolvable) sequencing-vs-concurrency tension between §4.3 and §4.4, and confirmed the 5-products duplication across 4.3/4.4 is deliberate (client-mandated) — passed explicit resolution instructions into each verbalizer prompt.
- **Stage 2**: self-approved under Boss's explicit standing bypass ("I allow you to bypass mu approval on argument map..I will wait to review the final drafts you produce"). Human review point moved to Stage 6.
- **Stage 3**: all four sections verbalized via `th-verbalizer`. Three of four subagent calls returned `status: failed` (HTTP 429, session usage limit) but **all four writes had already completed** before the error hit during the agent's final report-back — verified by reading each file directly.
- **Stage 4**: `lint_thai_writing.py` returns `MECHANICAL GATE PASSED` on all four sections (§4.1 failed this before the rewrite, on the `กรม สส.` vs lexicon-mandated `กรมฯ`/`DCCE` conflict — resolved by never emitting the bare roman token `DCCE`, decided by Boss as a contract-level exception rather than a lexicon change).

**Separately**: had a direct exchange with Boss about why this session's token cost was so much higher than a same-day Antigravity session that elevated Chapter 3 (`ψ/memory/retrospectives/2026-08/29/20.42_chapter_3_draft_elevation_and_staging.md`). Root cause identified precisely: Antigravity ran Stage 1/3/5 **in-line** in one continuous context instead of spawning fresh subagents, which avoided the repeated cold-start context tax **but also broke genuine Stage 5 reviewer independence** (self-graded within the same context, "mitigated" only by hash verification, which the harness's own SKILL.md explicitly says should be unreachable). This session ran every stage as a genuinely fresh, independent subagent — correct per the harness's own invariants, but far more expensive, and it's what let Stage 1 actually catch the three real problems above. Filed as product feedback (queued, not sent) on the lack of usage-quota visibility during subagent orchestration.

## Pending

- [ ] **Stage 5 — editorial review**, all four sections. Not run; this is what the rate limit interrupted. Independent `th-editorial-reviewer` per section, Tier 1 before Tier 2, `warrant_trace.py` first (every `recovered`/`repaired` unit's claim must trace). A review returning zero findings on sections this heavily reworked should be treated as a signal to re-run, not a result to accept — flagged explicitly because a same-day Chapter 3 run showed exactly this rubber-stamp pattern (five straight `findings: []` verdicts ~70s apart).
- [ ] **Stage 6 — human review and merge**. Present all four finished drafts together with the per-section provenance/change summary above. Merge via `merge_draft.py` only on explicit approval.
- [ ] Nothing has been git-committed this session (working tree only). Untracked: the four new `argument-map.json` files. Modified: the four section drafts and contracts, plus the new `revision-mode.md` and related skill files under `.agents/skills/writing-th/` and `.claude/skills/writing-th/` (not shown in the porcelain status above since they weren't captured in this snippet — verify with a fresh `git status` before committing).
- [ ] A parallel/earlier session today also touched `ψ/incubate/drafts/crdb-exec-summary-2.1..2.4` and style-capture files (`miss_register.db`, capture log, an evidence file at `22-27`) — untouched by this session, leave alone, but note them before any broad `git add`.

## Next Session

- [ ] Run Stage 5 for §4.1–4.4 (`th-editorial-reviewer`, independent clean context, rubric v6.0.0).
- [ ] Present the four finished, reviewed drafts to Boss for Stage 6 approval.
- [ ] On approval, merge via `merge_draft.py` for each section.
- [ ] The user has asked for a **separate plan** (this session, via `/forward`) on revising the writing-th workflow itself for lower Claude Code orchestration cost, without sacrificing the Stage 5 independence that Antigravity's approach gave up. See the plan file this handoff points to.

## Key Files

- Plan for this run: `C:\Users\sitth\.claude\plans\in-this-session-i-witty-whisper.md`
- Chapter 4 drafts: `ψ/incubate/drafts/crdb-exec-summary-4.{1,2,3,4}/`
- New harness reference: `.agents/skills/writing-th/references/revision-mode.md`
- Comparison retrospective (Antigravity, Chapter 3): `ψ/memory/retrospectives/2026-08/29/20.42_chapter_3_draft_elevation_and_staging.md`
- Writing plan (source of truth for §4.1–4.4 requirements): `ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่ 4 รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md`
