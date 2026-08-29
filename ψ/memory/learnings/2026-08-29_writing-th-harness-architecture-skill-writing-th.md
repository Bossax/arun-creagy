---
id: learning_2026-08-29_writing-th-harness-architecture-skill-writing-th
type: learning
title: "Writing-TH Harness architecture (skill writing-th v5.0.0, created 2026-03-13, up"
concepts: [writing-th, style-capture, skill-architecture, thai-writing, editorial-gates]
tags: [writing-th, style-capture, skill-architecture, thai-writing, editorial-gates]
created: 2026-08-29
indexed_at: 2026-08-29T06:00:51.522Z
updated_at: 2026-08-29T06:00:51.522Z
hash: sha256:7f657d0880775fa73f60ef6bc68029b20d24a8ecdb010b42151dbc6174cf0ffa
source: "/fyi --important"
arra_id: learning_2026-08-29_writing-th-harness-architecture-skill-writing-th
arra_type: learning
arra_concepts: [writing-th, style-capture, skill-architecture, thai-writing, editorial-gates]
arra_created: 2026-08-29T06:00:51.522Z
---

# Writing-TH Harness architecture (skill writing-th v5.0.0, created 2026-03-13, up

Writing-TH Harness architecture (skill writing-th v5.0.0, created 2026-03-13, upgraded to current v5 form 2026-08-28; architecture doc published as an Artifact 2026-08-25). A closed loop between two skills sharing one style pack (ψ/memory/style/, STYLE_PACK_TH + LEXICON_TH v4.0, 48 rules).

FORWARD ARC — writing-th, 7 stages (0-6):
0 Calibration (loads style pack, jargon ban list, halts to confirm persona — STOP gate)
1 Strategy (victory condition, evidence→analysis→solution shape, no gate)
2 Density & Scope Validation (lists tables/equations/frameworks that must survive rewrite, halts for sign-off — STOP gate)
3 Payload Gate (4-Pillar Extraction: Claim, Concrete Example, Consequence, Mechanism, required before drafting; no gate)
4 Governed Execution (one subagent per subsection, writes only to ψ/incubate/drafts/, target file unreachable by construction; no gate)
5 Script Gates (lexicon lint + density check, exit code 1 = silent rejection, BINDING gate)
6 Merge (human approves, merge_draft.py copies draft over real file; BINDING + STOP gate)
Draft never touches destination until stage 6.

RETURN ARC — style-capture, 6 stages (A-F):
A Read the delta (git diff on hand-edited file, human-initiated)
B Materialize evidence (dated diff-evidence file of word-for-word changes + candidate rules)
C Validate before promoting (every rule declares kind: literal/regex/structural + scope; validate_lexicon.py rejects malformed rules — BINDING gate)
D Check the miss register (proposed, not built: SQLite append-only log, promotion fires once a pattern fails twice)
E Merge into the pack (appends examples/counter-examples to style pack + lexicon, no gate)
F Index to Oracle (calls oracle_learn so the round becomes searchable memory)

TRANCHE 1 (verified 2026-08-25, checks run not asserted): gates made binding not advisory; fixed 3 of 5 lexicon rules from 2026-08-05 round that were silently dead (prose descriptions compiled as regex); fixed a rule whose prescribed replacement contained its own banned string, which made the rerun-until-exit-0 loop non-terminating (now kind: structural); word/sentence boundaries now come from PyThaiNLP; merge_draft.py used to only check draft existed then copy without calling gates — now runs gates itself and exits 1 without touching destination if they fail. Regression suite: 20/20 fixtures pass, 11/20 disagree with the old linter including every defect case.

TRANCHE 2 (proposed, not built): move persona out of Stage 0 into a late voice pass; add missing structural-revision stage; move evidence gathering ahead of framing; fast/slow track split; restrict 4-pillar payload rule to argumentative paragraphs only; SQLite miss-register with fails-twice promotion trigger; density ceiling tied to Stage 2 preserve-list (density is currently a floor with no ceiling); subagent brief schema with non-removable clause; lint the scaffolding not just the draft; supersession marking so the pack can shrink (currently append-only, never retired); parenthetical allowlist for verbatim TOR titles.

Source: ψ/lab/writing-th-harness/ (Artifact "Writing-TH Harness", https://claude.ai/code/artifact/259a8a31-5d30-4e32-8bc5-bc7171b09cb3, updated 2026-08-25). Skill source: .agents/skills/writing-th/, .agents/skills/style-capture/, ψ/memory/style/ (pack v5.0, lexicon TH v4.0). Full detail: ψ/memory/logs/info/2026-08-29_13-00_writing-th-harness-architecture.md

---
*Added via Oracle Learn*
