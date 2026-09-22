# Handoff: Sub-law TOR §1 Intent Section — Stage 2/3 revision in progress

**Date**: 2026-09-22 13:46
**Context**: mid-session, Boss said "I will revise both the argument .json and the first draft you make and I will come back" — handed off with his own edits pending.

## What We Did

- **Verification criteria** built and saved to `ψ/lab/Sub-law_TOR/verification-criteria.md`, grounded in World Bank/ADB QCBS, ILO's real scored evaluation annex, and a GSA framework — 8 dimensions (responsiveness/traceability, understanding of context, methodology soundness, scope coverage, work-plan feasibility, deliverables clarity, internal coherence, value-add).
- **Ran verification against `Draft-Proposal_Sub-Law.md`**: strong within หมวด ๑๒ scope, two real gaps found — missing ๔.๓.๖ hybrid-meeting deliverable, and no milestone alignment to the TOR's day-210 Draft Final Report deadline.
- **Read `CC-Act-Section12.md`**: surfaced a real institutional-boundary issue — กรมอุตุนิยมวิทยา (not DCCE) holds primary climate-database authority under the Act; DCCE's SOP #1 needs to be scoped as "receive & publish," not "produce," data.
- **`/style-capture` round**: promoted 10 mechanical lexical rules to `LEXICON_TH.json` v4.7 (banning untranslated English consulting-methodology brand names: Step-by-step, Process Flow, RACI Matrix, Process Architecture, Legal Obligation Mapping, Institutional Mapping, Gap Analysis, Readiness Assessment, Target Operating Model, Regulatory Roadmap). Flagged the "Gap Analysis" proper-noun collision with real CRDB document titles (WP7 Gap Analysis Report etc.) — added an explicit exception, did not touch those files. 5 structural/regex candidates confirmed generalizable but correctly held in the miss-register (need a 2nd sighting before promotion).
- **Created `ψ/incubate/drafts/Sub-law_TOR-annotated-notes.md`**: an annotated copy of the original draft with inline `[หมายเหตุที่ปรึกษา]` notes covering the 3 gaps found (meeting deliverable, milestone alignment, SOP #1 institutional boundary). Boss has since edited this file directly (3 commits: a7ff306, 0be8399, 8e22be1) — restructured §1 per his own instructions (background/intent before methodology-framework naming; the data→risk→plan cycle diagram moved out of §2).
- **Built a full writing-th v6.0 Stage 0→5 pipeline for a new §1 intent section** at `ψ/incubate/drafts/sub-law-tor-section1-intent/` (writing-contract.json, argument-map.json, draft.md, editorial-review.json):
  - Numbering resolved: `Chapter12-CC-Act-Original.md`'s ๑๕๖–๑๗๒ numbering confirmed authoritative over the ๑๕๘–๑๗๔ numbering used elsewhere (Boss decision, 2026-09-22).
  - Grounded the "institutional gap" claim via `/trace` against `WP7-Gap-Analysis-Report.md` §7 (real stakeholder-sourced finding: no coordinating/standard-setting role, no recourse when an agency refuses to share data) — stronger than pure inference from the statute's novelty.
  - Grounded the "Part 1 + Part 2 are one mechanism" claim via web search: **UNFCCC Decision 3/CMA.4** defines a 4-stage iterative adaptation cycle (risk assessment → planning → implementation → M&E) that maps directly onto Chapter 12's two parts. This is a permitted citation distinct from the banned NFCS/WMO framing.
  - **Stage 5 editorial review ran and FAILED** — 2 major findings: (F1) arg-04's grounds incorrectly cited "มาตรา ๑๕๘–๑๕๙" for the risk-assessment-approval content, which is มาตรา ๑๕๙ alone (๑๕๘ is Met Dept's separate database duty); (F2) draft paragraph 2's three institutional-role claims (Met Dept/Committee/Cabinet) had no มาตรา citations at all, violating the contract's evidence_policy.
  - Fixed both in `argument-map.json` (reset `approval.status` to `pending` per the bounded-amendment protocol), but did **not** yet re-apply the citation fixes to `draft.md` — Boss interrupted to take over editing both files himself.
  - Also fixed, mid-session, per Boss's direct feedback: arg-06's claim went through two more style corrections — first the banned negation-contrast pattern (`ไม่ใช่...แต่...`), then a second pass removing an abstract spatial metaphor ("เส้นแบ่งเดียว" / "single dividing line") that Boss flagged as the same category of translated-scaffolding language as the already-banned "จุดยืน/จุดตัด" rule. Current claim text: "สองส่วนของหมวด ๑๒ เป็นกลไกเดียวกัน โดยส่วนที่ ๑ กำหนดผู้เป็นเจ้าของหลักฐาน และส่วนที่ ๒ กำหนดผู้รับผิดชอบการนำหลักฐานไปปฏิบัติ"
  - **Mid-session file-sync issue observed**: at one point the argument-map.json on disk reverted several already-applied fixes (Boss's own concurrent edits, now explained by the commit history above) — resolved by reapplying against the live disk state rather than assuming my last in-memory version was current. Worth remembering for next session: always re-read before editing this file, don't trust turn-to-turn memory of its content.

## Pending

- [ ] Boss is revising `argument-map.json` and `draft.md` directly — his changes are NOT YET SEEN by this session.
- [ ] `editorial-review.json` still has the FAILED verdict from the last run (2 major, unresolved) — needs a fresh Stage 5 review once Boss's revision + the F1/F2 fixes are reconciled.
- [ ] Once map is re-approved and draft is corrected: re-run Stage 4 mechanical lint (venv path note below), re-run Stage 5 (fresh subagent, never fork/inline), then Stage 6 merge into the real draft.
- [ ] The original draft still has TWO other Boss-flagged annotation notes not yet resolved: the ๔.๓.๖ meeting-deliverable gap and the milestone-alignment gap (in `Sub-law_TOR-annotated-notes.md`, separate from the §1 intent work).
- [ ] `writing-th`'s own venv is missing at the expected path (`.agents/skills/writing-th/.venv`) — all lint/gate scripts this session were run via `.oracle-shared-skills/skills/writing-th/.venv/Scripts/python.exe` instead. Someone should either create the local venv or symlink/junction it properly; flagged but not fixed.

## Next Session

- [ ] Read `ψ/incubate/drafts/sub-law-tor-section1-intent/argument-map.json` and `draft.md` fresh — do not assume this session's last-known content; Boss said he'd revise both directly.
- [ ] Confirm whether Boss's revision already addresses F1/F2, or whether they still need fixing.
- [ ] Get `approval.status` back to `approved` only after Boss confirms the map is final.
- [ ] Re-run Stage 4 (`lint_thai_writing.py`) and Stage 5 (fresh `th-editorial-reviewer` Agent) before treating the §1 section as ready to merge.
- [ ] Once §1 is settled, the two remaining annotation-note gaps (meeting plan, milestone table) in `Sub-law_TOR-annotated-notes.md` still need the same argument-map → draft → review treatment, or a lighter-weight direct fix if Boss prefers.

## Key Files

- `ψ/lab/Sub-law_TOR/Draft-Proposal_Sub-Law.md` — original proposal (untouched)
- `ψ/lab/Sub-law_TOR/verification-criteria.md` — the 8-dimension checklist
- `ψ/incubate/drafts/Sub-law_TOR-annotated-notes.md` — annotated copy, Boss-edited (3 commits)
- `ψ/incubate/drafts/sub-law-tor-section1-intent/` — full writing-th pipeline for the new §1 intent section (contract, map, draft, review receipt)
- `ψ/lab/Sub-law_TOR/Chapter12-CC-Act-Original.md` — authoritative Act text, ๑๕๖–๑๗๒ numbering
- `ψ/incubate/DCCE/CRDB/output/07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md` — grounds the institutional-gap claim
- `ψ/memory/traces/2026-09-22/1309_chapter12-pre-law-problem-framing.md` — trace log
- `ψ/memory/style/LEXICON_TH.json` (v4.7), `ψ/memory/style/STYLE_PACK_TH.md` — updated this session
