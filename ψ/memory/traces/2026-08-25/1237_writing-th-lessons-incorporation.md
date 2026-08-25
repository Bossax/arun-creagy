---
query: "writing-th learned lessons from past editing loops → what to improve"
target: "Arun_Creagy"
mode: smart (oracle → direct corpus read)
timestamp: 2026-08-25 12:37
---

# Trace: writing-th learned lessons → improvement backlog

**Target**: Arun_Creagy
**Mode**: smart, escalated to direct corpus read (Oracle vector index degraded, FTS5-only)
**Time**: 2026-08-25 12:37 SEAST

## Oracle Results
Hybrid search returned 12 hits but `vectorAvailable: false` — embedder unreachable, probe timed out at 2000ms.
Ranking was pointer-index only and surfaced unrelated course material. Escalated to direct read of
`ψ/memory/learnings/` and `ψ/memory/retrospectives/`.

## Files Found

### Learnings (high confidence)
- `ψ/memory/learnings/2026-04-02_writing-th-foresight-style-pack-governance.md`
- `ψ/memory/learnings/2026-04-05_foresight-v4-edit-discipline-and-style-pack-enforcement.md`
- `ψ/memory/learnings/2026-04-10_thai-strategic-writing-style.md`
- `ψ/memory/learnings/2026-06-10_analytical-integrity-over-strategic-style.md`
- `ψ/memory/learnings/2026-06-23_style-calibration-loop-and-pre-scaffolding-boundaries.md`
- `ψ/memory/learnings/2026-06-24_crdb-5.2-naturalization-style-lessons.md`
- `ψ/memory/learnings/2026-06-24_phase3-phase4-integrated-execution-and-delta-only-retrieval.md`
- `ψ/memory/learnings/2026-06-27_crdb-writing-workflow-best-practice.md`
- `ψ/memory/learnings/2026-07-01_style-pack-compliance-workflow-running-drafts-t.md`
- `ψ/memory/learnings/2026-07-02_captured-style-rules-from-in-place-edits-in-fullr.md`
- `ψ/memory/learnings/2026-07-03_rrr_preservation-first-thai-editing.md`
- `ψ/memory/learnings/2026-08-05_ncaif-institutional-thai-style-pack-v32-added-5.md`

### Retrospectives (high confidence)
- `ψ/memory/retrospectives/2026-04/02/17.03_writing-th-foresight-style-pack-frustration.md`
- `ψ/memory/retrospectives/2026-06/09/21.30_ncaif-style-hardening.md`
- `ψ/memory/retrospectives/2026-06/23/11.03_style_calibration_and_scaffold_realignment.md`

### System under evaluation
- `.agents/skills/writing-th/SKILL.md` (v4.0.0, 70 lines)
- `.agents/skills/writing-th/scripts/{lint_thai_writing,check_density,merge_draft}.py`
- `.agents/skills/style-capture/SKILL.md`
- `ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md` (38KB, 9 sections, 8 capture rounds)
- `ψ/memory/style/LEXICON_NCAIF-Institutional.json` (44 entries)

## Git History
Not searched — the corpus read was decisive.

## GitHub Issues/PRs
None searched.

## Cross-Repo Matches
None.

## Oracle Memory

Fourteen recurring lessons, grouped:

**Trust and over-claiming**
- 2026-04-02: never claim style is "fully materialized" unless upstream rules were actually
  condensed into the file. Over-claiming caused the highest recorded user frustration in the corpus.
- 2026-04-02: keep exactly one authoritative style artifact per project; duplicates cause split-brain.

**Rule form**
- 2026-04-05: principles alone do not enforce. Concrete "do not use" examples drawn from real
  rejected phrases are what make checking reliable.
- 2026-06-09: purging jargon creates a vacuum the model fills with empty placeholders
  ("สถานะความพร้อม"). A ban needs a paired emptiness check.

**Promotion loop**
- 2026-04-05: human comments are global signals, not local annotations — fix locally AND promote.
- 2026-06-27: explicit threshold — promote to the style pack when the same pattern fails twice.

**Contamination**
- 2026-04-05: internal scaffolding (spines, outlines) acts as a generative anchor. Metaphorical
  scaffolding language produces metaphorical final prose.

**Mechanical enforcement**
- 2026-07-01: hybrid works — scripted bulk replacement for 100% lexical coverage, then a manual
  polish pass because replacement wrecks Thai grammar and spacing. QC with a residual `[a-zA-Z]+` scan.
- 2026-07-01: LLM recency bias reintroduces banned terms (DCCE, CRDB, API, use case) whenever new
  content is merged. The gate must sit at merge time, not only at draft time.

**Fidelity**
- 2026-07-03: no-compression is a hard fidelity boundary, not a style preference. Subagent briefs
  must state that scope, examples, and qualifiers are non-removable.
- 2026-06-24: when a section is already substantively complete, the high-value edit is
  sentence-level naturalization, not structural redesign.

**Sequencing**
- 2026-06-10: evidence before persona. A strategic persona adopted before the gap matrix produces
  hollow drafts. Run the evidence pass BEFORE Stage 0.
- 2026-06-10: delegate high-volume data work to subagents early, to keep hallucinated summaries out
  of the main agent's history.
- 2026-06-24: workflow ambiguity causes repeated friction even when writing quality is strong.
  The fix is explicit deliverable definitions per phase, not more explanation.

## Summary

v4.0.0 already absorbed five of these — draft isolation, anti-compression, anti-batching,
4-Pillar Extraction, and the two STOP gates.

Eight remain unincorporated, and they change the improvement backlog from the earlier
static evaluation:

1. Stage 5 is named "Deterministic Validation" but enforces roughly 10% of the style pack, with
   3 dead lexicon rules and 1 infinite-loop trap. This repeats the 2026-04-02 over-claiming failure.
2. No miss-register, so the known "fails twice → promote" threshold has nothing tracking it.
3. Lint detects but never fixes; the 2026-07-01 lesson prescribes bulk-replace plus polish.
4. No residual-English QC scan.
5. Stages 1–3 scaffolding outputs are unlinted despite being generative anchors.
6. Stage 4 subagent briefs omit the non-removable clause.
7. No polish-vs-rewrite mode, so the 0.8 density gate is inert on naturalization passes.
8. Stage 0 confirms persona before evidence, which 2026-06-10 identifies as the hollow-draft cause.

**Next steps**: fold items 1–8 into the writing-th v5 revision alongside the four defects verified
by execution in this session (merge ungated, density one-sided, dead lexicon rules, over-broad regexes).
