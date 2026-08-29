# Handoff: writing-th v6.0 — Execution Architecture Complete, Ready to Build

**Date**: 2026-08-29 15:05
**Context**: Long session, multi-agent (Claude + Antigravity/Gemini working the same thread in parallel)

## What We Did

Started from a concrete symptom: the CRDB Exec Summary §1.1 review produced 14
correction points, most of them repeats — typos, dropped scope, floaty
UX findings with no application, and (twice in one file) the same
negation-contrast AI-tell Boss has flagged before. Traced this all the way to
an architecture-level diagnosis and a build-ready fix:

- **Audited the 14-point editing log** against the writing-th harness stages —
  `ψ/memory/logs/info/2026-08-29_12-46_crdb-exec-summary-editing-points-audit.md`
- **Corrected two stale claims** carried forward from the published 2026-08-25
  artifact into a fresh `/fyi --important` log (`miss_register.db` is actually
  built and populated — 48 candidates, 6 promotions — not "proposed"; and
  `style-capture` does capture structural/rhetorical patterns in prose, it just
  never promotes them into the binding lexicon)
- **Did real research** on how writing decomposes into steps — Flower & Hayes,
  Bereiter & Scardamalia (knowledge-telling vs. knowledge-transforming — this
  is the name for what's wrong), Toulmin, Minto's Pyramid Principle, Kellogg —
  and confirmed the current `writing-th` v5.0 schema has no argument-
  construction artifact at all, just a metadata contract → one-shot prose pass
- **Reviewed and corrected a v6.0 proposal** (co-authored with Antigravity/
  Gemini in the same document): kept `kind: structural` in the lexicon (a
  proposed removal would have inverted the actual Tranche-1 fix history), added
  ordering + a `supports` field to argument units so MECE is actually checkable,
  flagged a `paragraph_job` enum mismatch
- **Wrote the execution architecture** the science-grounded proposal was
  missing — who runs each stage, in what context, what enforces the gates —
  framed around one thesis: `argument-map.json` is a **token compression
  boundary**, not just an added artifact. Argument construction needs sources
  and no style material; verbalization needs the approved map and a style
  kernel but never the raw sources. Splitting them as agent/context boundaries
  roughly halves total load instead of adding to it.
- **Published a design-reviewed HTML explainer** for Boss —
  https://claude.ai/code/artifact/43043f5c-b791-4164-a214-f1985dfa2bd0 — bar-
  height pipeline diagram makes the compression-boundary thesis visible in one
  image (Stage 1 tallest, sources never re-enter after the Stage 2 gate,
  Stages 4/6 flat because they're pure CLI).

All of it is cross-linked with Obsidian `[[wiki-links]]` per Boss's preference,
mid-thread.

## Pending

- [ ] Antigravity/Gemini has since added a fourth doc,
      `ψ/inbox/2026-08-29_writing-th-v6-antigravity-adaptation.md` (AGY-specific
      adaptation of the same v6.0 design) — **not yet reviewed by this session**.
      Read it before building; it may duplicate or conflict with the build
      blueprint below.
- [ ] Nothing in the v6.0 design has been implemented. All four inbox docs are
      design/analysis only.
- [ ] Section 1.1 of the CRDB exec summary (`ψ/incubate/drafts/crdb-exec-
      summary-1.1/`) is still an isolated draft, not merged, and the 14-point
      audit's fixes are not yet applied to it.
- [ ] The negation-contrast lexicon promotion recommended twice in this thread
      (`kind: regex` for `ไม่ได้...แต่...` / `ไม่ควรถูกมองเป็น...แต่ควรถูกมองเป็น...`)
      has not been done — `register.py ready` was never actually run this
      session to check the gap between 48 logged candidates and 6 promotions.

## Next Session

- [ ] Read `ψ/inbox/2026-08-29_writing-th-v6-antigravity-adaptation.md` first —
      reconcile against the build blueprint before starting any implementation.
- [ ] Build order from the blueprint (§12), cheapest/highest-leverage first:
      1. Two hooks in `.claude/settings.local.json` (PreToolUse block on
         drafts without an approved `argument-map.json`; PostToolUse auto-lint)
      2. Three subagent definitions in `.claude/agents/` — `th-argument-mapper`,
         `th-verbalizer`, `th-editorial-reviewer` — following the
         `wp2-demand-scorer.md` pattern
      3. `argument_gate.py` (validate + prepare)
      4. Split `references/` by consumer, extract prose kernel, archive
         `STYLE_PACK_TH.md` §9's capture log
      5. `SKILL.md` v6.0 rewrite (Stage 0 must ask whether a writing plan
         exists, never assume; Stage 3 needs the bounded amendment path back
         to the Stage 2 gate)
      6. `warrant_trace.py` (optional, last)
      7. Blind forward test, then `tests/run_tests.py`
- [ ] Separately, and lower priority: run `register.py ready` against the live
      register and promote the negation-contrast pattern into `LEXICON_TH.json`
      as `kind: regex` — this doesn't require v6.0, fixes a known recurring
      correction today.
- [ ] Decide whether to continue section 1.1 under v5.0 now, or wait for v6.0's
      argument-map gate before touching it again — Boss hasn't said.

## Key Files

- `ψ/inbox/2026-08-29_writing-harness-skill-architecture-analysis.md` — full
  multi-author record, §1–9, signed sections throughout
- `ψ/inbox/2026-08-29_writing-th-v6-build-blueprint.md` — the build sheet
  (this session's, Claude-authored)
- `ψ/inbox/2026-08-29_writing-th-v6-antigravity-adaptation.md` — unreviewed,
  Antigravity/Gemini-authored, AGY-specific
- `ψ/memory/logs/info/2026-08-29_12-46_crdb-exec-summary-editing-points-audit.md`
  — the 14-point audit that started this
- `ψ/memory/logs/info/2026-08-29_13-00_writing-th-harness-architecture.md` —
  v5.0 architecture of record (has a known-stale claim about `miss_register.db`
  — see §5 of the analysis doc for the correction)
- `.agents/skills/writing-th/SKILL.md`, `.agents/skills/style-capture/SKILL.md`
  — the v5.0 skills to be superseded
- `ψ/memory/style/STYLE_PACK_TH.md`, `LEXICON_TH.json`, `miss_register.db` —
  live style state
- Artifact: https://claude.ai/code/artifact/43043f5c-b791-4164-a214-f1985dfa2bd0
  — HTML explainer for Boss's review
