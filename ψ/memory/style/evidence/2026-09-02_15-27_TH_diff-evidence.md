# TH Style Diff Evidence — 2026-09-02 15:27

**Source mode**: In-Place / Single File (Smart Diff Resolver), working-copy `git diff`, run on two files in one capture pass.
**Files**:
- `ψ/incubate/drafts/crdb-full-report-2.3/draft.md`
- `ψ/incubate/drafts/crdb-full-report-2.6/draft.md`

**Context**: TH (Thai institutional writing, repo-wide). Triggered because Boss reported qwen-verbalized drafts still show dropped subjects/objects and cut-out clarifying nouns despite the existing Core Kernel rule #11 ("Elaborate, Don't Drop, Clarifying Nouns"). Instead, the actual working-copy edits on 2.3/2.6 turned out to be dominated by content restructuring (a whole subsection deleted in 2.3, large new evidence paragraphs added in 2.6) rather than the flagged noun/subject-drop pattern — captured here is only what genuinely disposed as lexical/structural.

## Word-diff table output

Computed via `diff_word_table.py --git`, per-file: 49 rows (2.3), 75 rows (2.6). Full raw tables not reproduced here (see git history of this file's originating session); every row was reviewed and dispositioned below.

## Disposition summary

| Pattern | Category | Status | Notes |
|---|---|---|---|
| `ระดับภาค` / `ระดับสาขา` → `รายภาค` / `รายสาขา` | lexical (regex) | **confirmed_generalizable — PROMOTED** | Repeated 3x across both files. Boss: tone/register fix, meaning unchanged. Category noun, not geographic level. |
| `การนำทาง` → `เส้นทางการใช้งาน` | lexical (literal) | **confirmed_generalizable — PROMOTED** | Repeated 5+ times in 2.6 (2 distinct sightings registered). Boss: tone/register fix, literal UX jargon. |
| `โครงสร้างสารสนเทศของเว็บไซต์` → `ผังเว็บไซต์` (sitemap sense) | lexical (literal) | **confirmed_generalizable — PROMOTED** | Boss: "it is sitemap originally, the draft drifted." Restoring established project term. |
| `ประตูทางเข้า` / `ประตู` (role-based entry point) → `จุดเริ่มต้นของเส้นทางการใช้งาน` | lexical (literal) | **mechanical — PROMOTED** | Extension of pre-existing `ประตูหลัก` rule (same front-door/gateway metaphor). Bypassed 2x threshold as a mechanical reapplication. **Caveat**: does not apply to `ประตูระบายน้ำ` (floodgate) — real engineering term, not a metaphor. Flagged separately as a possible mis-edit in the source draft (2 instances of `ประตูระบายน้ำเค็ม` → `หน้าระบายน้ำเค็ม`), pending Boss's answer. |
| `คณะที่ปรึกษา` dropped from repeated sentence-openers within one paragraph run | structural (Core Kernel #8 nuance) | **confirmed_generalizable — PROMOTED** | Boss: "reduce robotic repetition across a paragraph run." Refines, does not reverse, the active-institutional-agency rule. Name actor once per topic/run, not every sentence. |
| §2.3.4 "การประเมินความพร้อมของโครงสร้างข้อมูลฯ" (whole subsection, 4 paragraphs, named benchmarks ADB/Copernicus) | content | **not lexical — content_correction, log only** | Entire subsection deleted from the draft. Scope/content decision, not a style pattern. Not promoted. |
| Large new paragraph in 2.3 (line 11: DCCE vision, governance sub-committee, PDF/website/infographic scope) | content | **not lexical — content_correction, log only** | New factual content inserted, not present in AI draft. Not promoted. |
| Large new paragraphs in 2.6 (1.1/1.2 subsections: IPCC AR6 risk equation, named historical disasters, loss figures, ECA/Adaptation Finance Tracker detail) | content | **not lexical — content_correction, log only** | Boss filling in real data/evidence the draft lacked, and removing a literal duplicate paragraph (2.6.2's old prose repeated content already present at the top of the section). Not promoted. |
| "3 ประเด็น" prose list → "ประการแรก / ที่สอง / ที่สาม" enumeration (2.3); "หน่วยเนื้อหาแรก/ที่สอง" prose → "1.1 / 1.2" numbered subheadings (2.6) | structural | **not novel — already covered** | Matches existing §3 Secondary Pass Rule "Structured Breakdowns for Complex Lists." Reapplication, not a new rule. |
| `ประตูระบายน้ำเค็ม` → `หน้าระบายน้ำเค็ม` (2.6, 2 instances) | **flagged, not captured** | **possible error — pending Boss answer** | Looks like the anti-metaphor "ประตู" instinct misapplied to a genuine technical term (floodgate/sluice gate). Not promoted either direction; needs Boss's confirmation before either reverting or accepting. |

## Stale-usage sweep (`check_term_propagation.py`)

Both newly-canonical terms have older usages elsewhere in the project that were not part of this capture's scope and are NOT auto-fixed:

- `โครงสร้างสารสนเทศของเว็บไซต์`: 5 lines across `crdb-exec-summary-1.4/section-1.4-draft.md`, `crdb-full-report-2.6/draft.md` (own heading, untouched by this edit), `crdb-full-report-2.6/writing-contract.json` (×3).
- `การนำทาง`: 10 lines across `crdb-exec-summary-1.1/02b_1.1_th.md`, `crdb-exec-summary-1.1/02_th_draft.pre-1.1-revision.md`, `crdb-exec-summary-1.4/writing-contract.json`, `crdb-full-report-2.2/draft-1.md`, `crdb-full-report-2.2/lane-a-polished-5.2.2.md`, `crdb-full-report-2.3/draft.md` (×3, remaining after this edit).

These are reported, not modified — cleanup is a separate decision for whoever next touches those files/sections.

## Candidate rules by layer

- **lexical**: 4 promoted (see table above; now in `LEXICON_TH.json` v4.6, entries 81–84).
- **structural**: 1 promoted (Core Kernel rule 8 nuance, `STYLE_PACK_TH.md`).
- **content** (out of scope for promotion, logged only): 3 items — whole-subsection deletion, two large evidence insertions.
