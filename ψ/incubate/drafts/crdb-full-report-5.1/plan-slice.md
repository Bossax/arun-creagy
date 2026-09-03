# Plan slice — CRDB full report §5.1 (วิเคราะห์ช่องว่างอุปทาน–อุปสงค์)

Extracted from the chapter spine (`00-โครงเรื่องและแผนการเขียนรายงานฉบับสมบูรณ์.md`) and this session's interactive Stage 0 walkthrough, 2026-09-02.

## 1. Outline

Section job (from spine, row บท 5 / 5.1): answers project question 3 ("อะไรที่ต้องพัฒนาใหม่") jointly with §5.2's question 4 — §5.1 states the gap, §5.2 proposes the response. §5.1 does not itself propose solutions.

Chapter-level rule (spine §1, "ลำดับการส่งต่อระหว่างบท"): Chapter 5 must reference Chapter 2's results (what's needed) and Chapter 3's results (what exists) and subtract them — not re-derive either.

Boss-approved 3-unit split (this session):

1. **Supply-demand structural gap analysis** — the 11 named structural gaps (WP7 §4) and the per-service blocking table (9 services, WP7 §5).
2. **Website content readiness gap** — 79% figure, 16 FULL / 26 PARTIAL / 33 GAP breakdown out of 75 sitemap-mandated topics.
3. **A-BTR case study** — institutional mandate, BTR2's 5 self-reported knowledge gaps, CRDB's independent pipeline-process diagnosis, strategic complexity (4 adaptation-cycle stages), platform response.

Closes with a transition to §5.2 (no policy content in this section).

## 2. Evidence base (macro grounding)

Primary — the two approved exec-summary argument maps this section revises from:
- `ψ/incubate/drafts/crdb-exec-summary-4.1/argument-map.json` (units 1 and 2 recover from here — arg-01 the 11 gaps, arg-02 the 9-service table, arg-03 the website content split, arg-04 the transition logic)
- `ψ/incubate/drafts/crdb-exec-summary-4.2/argument-map.json` (unit 3 recovers from here in full — all 5 argument units)

Full-report-depth technical detail (exceeds what exec altitude carried):
- `output/07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md` — source of the 11-gap/9-service framework itself
- `output/07_Gap_Analysis/รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md`
- `output/04_Sitemap/2026-08-20-WP4-Content-Source-Gap-Analysis-v2.md`
- `output/02_Data_Inventory/2026-03-12-DCCE_Website_Content_Gap_*.md` (Inventory, Matrix, Report_Insert, Summary)
- `output/06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/section_A_institutional_baseline.md`, `section_C_priorities_barriers_and_strategy.md`, `a_btr_dissection_master_joined.csv`, `a_btr_to_sitemap_gap_analysis.md`

Narrative texture only, NOT figures (old framework superseded):
- `output/draft_final_report/5.3/2026-06-25_draft_section-5.3.8.md` — usable for the quantitative/qualitative/institutional gap-dimension framing and the closing DCCE-role argument (§5.3.8 final paragraph: DCCE as standard-setter/certifier rather than sole data producer), but its own gap count (8 services), aggregate readiness split (~20%/80%), and dataset count framing are stale relative to WP7's 11-gap/9-service taxonomy and must not be carried into the draft.

Trace logs (from spine §3, TR ของบท 5): tor70-previous-criticism-and-dcce-recommendations, crdb-final-sprint-precode-dcce-approval-gates, director-toey-persona-and-tor70-briefing-critique, tor70_content_gap_analysis, tor70-analysis-timeline-reconstruction, a-btr-requirement-analysis, crdb-btr-me-integration-trace, adaptation-me-evidence-base-trace, thai-line-agencies-institutional-mental-model, crdb-evidence-merl-platform-feasibility.

## 3. Session-specific rules

- Active actor: คณะที่ปรึกษา (per report-wide rule §3 of `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md`).
- Target altitude: full-report level, "inverted detail" — restore technical detail the exec summary compressed; long lists/tables to appendix only if truly long.
- A-BTR is written out in full on first mention: "รายงานความโปร่งใสรายสองปีด้านการปรับตัว (Adaptation Biennial Transparency Report: A-BTR)" — this is a real external report name, not an internal project abbreviation, so it is exempt from the internal-abbreviation ban.
- No policy/solution content — every gap statement closes toward §5.2, not toward a fix.
- Numbers must trace to WP7 (11 gaps/9 services) or WP4/2026-03-12 files (content gap), never to 5.3.8's superseded 8-service/20-80 framing.
- Full report-wide style rules (§1 name/abbreviation use, §2 no internal document positions, §4 numbered lists for enumerable parallels, §6 register/banned words, §8 พ.ศ. dating, §9 table naming) apply per `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md`, copied into `report_specific_rules` of the writing contract.

## Stage 0 approval

Approved by Boss, 2026-09-02, "Approve as-is" — contract as summarized, no Stage 2 bypass carried over from the exec-summary Chapter 4 precedent (treated as open per spine §7 until Boss says otherwise).
