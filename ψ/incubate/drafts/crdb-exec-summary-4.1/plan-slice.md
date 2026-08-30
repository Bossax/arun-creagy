# Plan slice — Executive Summary §4.1 สรุปช่องว่างและอุปสรรคของข้อมูล

Source: `ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่ 4 รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md`,
Executive Summary Chapter 4 plan (§4, lines 477–501).

## Section brief (verbatim scope)

> ### 4.1 สรุปช่องว่างและอุปสรรคของข้อมูล
> [[2026-08-16-WP7-Gap-Analysis-Report]]
> - สรุปช่องว่างและอุปสรรคในระบบนิเวศข้อมูล
> - อุปสรรคของการพัฒนาบริการแต่ล่ะข้อโดยย่อ
> - ช่องว่างเนื้อหาเว็บไซต์

This is a brief, front-loaded gap/obstacle summary — the reader's first exposure
to the chapter's problem statement. It sets up (but does not itself resolve)
the A-BTR-specific argument that §4.2 carries.

**Stays technical-only**: this section's closing/transition argument must not invoke
WP7's institutional-gap synthesis (the "absence of a coordinating role across
agencies" framing) -- that belongs to §4.4, which owns the institutional/
governance conclusion. §4.1 closes purely on the technical gap inventory
(structural gaps, per-service blockers, content gap) and transitions to A-BTR
as the sharpest technical case, nothing more (Boss correction, 2026-08-30).

**Owns the general website content-gap figure**: the 75-topic readiness split
(16 full / 26 partial / 33 gap → 79% needs fresh research/synthesis) against
the 391-item digital asset inventory is a whole-website statistic, not
A-BTR-specific (confirmed against the Full Report's own argument map, arg-03).
Boss corrected this scoping directly on 2026-08-30: this figure belongs here,
under "ช่องว่างเนื้อหาเว็บไซต์," not in §4.2. §4.2 references it only in
passing, if at all, before narrowing to the A-BTR-linked subset.

## Storyline position (§2 of the plan, shared by both reports)

- Point 1 of the shared storyline: open with why A-BTR forces the frame (กรม สส. is
  Thailand's national focal point for adaptation under Paris Agreement Art. 13),
  then show that existing data/content is not yet organized enough to support
  policy decisions or operations with confidence.
- Content gap: 44% of website content entirely missing, 35% partial → 79% needs
  fresh synthesis; only 21% (16/75) is publication-ready.
- Demand gap: 9 climate information services user agencies actually want
  (distilled from WP6 Service Intelligence) do not yet match the current data
  state.
- Both supply-side and demand-side gaps must be shown together before rolling up
  into the 11-dimension supply gap (WP7).
- Also covers national/international reporting obligations, especially A-BTR
  under UNFCCC — named here as context, developed fully in §4.2.

## Evidence base (§9.1, §9.2 of the plan)

- WP7 Gap Analysis Report (2026-08-16) — 11-dimension supply gap, extends
  demand-supply analysis, impact on 9 services (adds BTR and Loss Database).
  `07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md`
- WP4 Content-Source Gap Analysis v2 (E-093) — 75-topic readiness split
  (16 full / 26 partial / 33 gap). `04_Sitemap/2026-08-20-WP4-Content-Source-Gap-Analysis-v2.md`
- DCCE Unified Digital Asset Database (E-080) — 391-item digital asset registry.
  `04_Sitemap/DCCE_Unified_Digital_Asset_Database.csv`
- WP6 Service Intelligence v6.0 — demand definition for the 9 climate
  information services, distilled from direct user-agency interviews/workshops.
  `06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`
- WP8 Recommendations Report (D-074) — institutional role structure background.

## Global writing-format rules (§ "ข้อกำหนดรูปแบบการเขียน", lines 14–38)

1. **Agency naming**: full Thai+English name at first mention
   ("กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม"), then only "กรม สส." —
   never bare "สส." without "กรม" leading it.
2. **NCAIF**: never bare English acronym without the Thai full name at first
   mention ("โครงสร้างข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ
   (National Climate Adaptation Information Framework: NCAIF)"), then
   "โครงสร้างข้อมูลด้านการปรับตัวฯ" or "โครงสร้างข้อมูล NCAIF".
3. **No internal jargon abbreviations** (TOR70, CRDB) without spelling out at
   first use. CRDB = "โครงการจ้างที่ปรึกษาพัฒนาชุดข้อมูลองค์ความรู้ความเสี่ยงและ
   ผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ".
4. **No internal document locators** in main narrative prose (working-deck slide
   numbers, page numbers, superseded internal section references). Cite by
   document name, E-xxx evidence code, or named standard/framework; keep
   locators in the evidence-traceability sidecar only.
5. **Sentence subject = "คณะที่ปรึกษา"** for study/survey/interview/workshop/
   analysis/synthesis/design-decision sentences. Avoid passive voice or
   "โครงการ" as actor, except when stating the project's contractual
   objective/scope.
6. **Parallel-item formatting**: countable parallel items (11 gap dimensions,
   9 services, etc.) as numbered/bulleted lists with substantive descriptions —
   not run-on prose.
7. **Executive-summary substance retention**: cut operational detail/deep
   stats/technical detail, but never reduce a point to one floating sentence.
   Every subsection needs Why / What / So-What in at least 1–2 paragraphs.
8. **Formal vocabulary**: official terms ("ข้อมูลอภิพันธ์"/"ข้อมูลกำกับ",
   "สถาปัตยกรรมสารสนเทศ", "ธรรมาภิบาลข้อมูล"); avoid colloquial phrasing.
9. **[Skill-level, prose-kernel.md] No contrastive/justify-by-flaw scaffolding**:
   do not justify a recommendation by first negating a bad alternative
   ("แทนที่จะ...", "เพื่อป้องกัน...", "เพื่อลดความเสี่ยง...", "หลีกเลี่ยง...").
   State what should be done directly.

## Exclusions (this section)

- Per-field metadata technical statistics
- Full enumerated table of the 260 datasets
