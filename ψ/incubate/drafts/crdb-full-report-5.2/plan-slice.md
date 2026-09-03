# Plan slice — CRDB full report §5.2 (ข้อเสนอแนะ)

Extracted from the chapter spine (`00-โครงเรื่องและแผนการเขียนรายงานฉบับสมบูรณ์.md`) and this session's interactive Stage 0 walkthrough, 2026-09-03.

## 1. Outline

Section job (from spine, row บท 5 / 5.2): answers project questions 3 ("อะไรที่ต้องพัฒนาใหม่") and 4 ("จะรักษาไว้อย่างไร"), jointly with §5.1 — §5.1 states the gap, §5.2 proposes the response. The chapter's key argument is that closing the gap requires two things together: a blueprint for the next phase of digital system development, and a governance structure that keeps the system working long-term.

Chapter-level rule (spine §1, "ลำดับการส่งต่อระหว่างบท"): Chapter 5 must reference Chapter 2's results (what is needed) and Chapter 3's results (what exists), and §5.1's gap findings — not re-derive any of them.

Boss-approved 3-unit split (this session), one unit per exec-summary source:

1. **พิมพ์เขียวสำหรับการพัฒนาระบบข้อมูลในระยะถัดไป** (from EX 4.3) — the 6-phase Data and Web Platform SDLC frame, the coverage claim (~70% of phase 1, ~80% of phase 2), the 8 handover components, the Content Writer / Software Developer role split, and the iterative-design-loop caveat.

   **Depth limit on the 8 components (Boss, 2026-09-03):** the main text states each component's *objective* only — what it is for, and why it matters to the next phase. The components' actual content goes to the appendix, which **Boss is authoring separately**. This unit must not reproduce or summarize that content. "Objective only" still has to clear the report's minimum-substance floor (style rule §4: enumerated lists carry evidence-backed substance, not bare names), so each of the 8 gets a sentence or two of purpose — not a one-line label, and not a content dump.
2. **ข้อเสนอแนะเชิงนโยบายด้านธรรมาภิบาลและการบริหารจัดการแพลตฟอร์ม** (from EX 4.4) — **4 recommendations**, ordered by how much decision authority กรม สส. holds:
   1. การวางโครงสร้างธรรมาภิบาลข้อมูลภายใน (4 tiers: คณะกรรมการ / Data Owner / Data Steward / Data Custodian)
   2. **กำลังคนด้านข้อมูลภายในองค์กร** — NEW, see §4 below
   3. การออกแบบขอบเขตงานจ้างโดยใช้ผลิตภัณฑ์นำและกรอบการพัฒนาแบบ Agile (5 services in 2 groups; MVP sequencing for the loss-and-damage statistics service; NESDC as methodology partner; ≥2 build cycles with a mid-contract beta milestone)
   4. การจัดทำข้อตกลงแลกเปลี่ยนข้อมูลกับหน่วยงานภายนอก (5 agencies, 97 datasets, ร้อยละ 37 of 260)
3. **แผนที่นำทางสำหรับการพัฒนาระบบและธรรมาภิบาลข้อมูล** (from EX 4.5) — 2 parallel work groups: the next build contract's TOR, and 8 institutional governance tasks (4 short-term ≤6 months, 4 medium-term 1–3 years).

**Boundary rule for the unit 2 ↔ unit 3 overlap.** EX 4.5's own argument map flags one deliberate overlap point with 4.4, and 4.5's prose cross-references 4.4 for the Agile rationale. Unit 2 owns the *rationale and substance* of each recommendation; unit 3 owns *sequencing and timeframe only*, pointing back to unit 2 rather than re-arguing it.

## 2. Evidence base (macro grounding)

**Primary — the three exec-summary drafts this section revises from.** All three were updated 2026-09-03 (10:03–10:04). Their existing `argument-map.json` files (4.3: 4 units; 4.5: 7 units; 4.4: none) are **stale against the updated prose** — 4.3 moved from "5 ผลผลิต" to "8 องค์ประกอบ" and from 13 to 14 deliverables, 4.4 gained explicit 3-item numbering, 4.5 gained timeframe labels and an eighth task. Boss's ruling (2026-09-03): **Stage 1 re-derives all three fresh from the current prose; the old argument maps are not the recovery base.**

- `ψ/incubate/drafts/crdb-exec-summary-4.3/section-4.3-draft.md`
- `ψ/incubate/drafts/crdb-exec-summary-4.4/section-4.4-draft.md`
- `ψ/incubate/drafts/crdb-exec-summary-4.5/section-4.5-draft.md`

**Full-report-depth technical detail (exceeds what exec altitude carried):**

Unit 1:
- `output/00_Strategy_Reports/2026-05-21_CRDB-Technical-SDLC-and-Role-Accountability-Framework.md` — source of the 6-phase lifecycle frame and the role-accountability split
- `output/04_Sitemap/2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md` + the DRD v2 CSVs (`-requirements-`, `-deliverables-`, `-service-briefs-`, `-data-specs-`, `-assets-cited-`)
- `output/04_Sitemap/2026-08-20-WP4-Node-Content-Storyboard-and-Synthesis-Guide-v2.md`
- `output/06_Use_Case_Demand_Analysis/2026-08-15-WP4-Non-Catalog-Deliverable-Business-Narratives.md`

Unit 2:
- `output/08_Recommendations/2026-08-16-WP8-Recommendations-Report.md` (§§1, 2, 4 — governance and accountability, technical standards, data exchange agreements)
- `output/05_Data_Management_Framework/Governance_RACI/Pillar_07_Governance_Operating_Model_Technical_Specification.md`
- `output/05_Data_Management_Framework/Governance_RACI/คู่มือ แนวทางปฏิบัติการจัดทำธรรมาภิบาลข้อมูล  Data Governance User Manual.md`
- `output/06_Use_Case_Demand_Analysis/2026-08-14-WP6-Business-NFR-Thresholds-Table.md`
- `output/02_Data_Inventory/data_catalog_v4.csv` — the 260-dataset base and the 97/5-agency figures

Unit 3:
- `output/08_Recommendations/2026-08-16-WP8-Recommendations-Report.md` (§3 — what comes next, per body of work)

**Narrative texture only, NOT figures or structure (Boss's ruling, 2026-09-03):**
- `output/draft_final_report/5.3/2026-06-25_draft_section-5.3.9.md` — its 6-category recommendation taxonomy (internal governance / service portfolio / 5-layer technical standards / technical partnerships / competitive positioning / resources) never went through exec-summary approval and conflicts with the approved 4-recommendation + 5-service + 8-task structure. Usable for phrasing and framing only. The "National Certifier / Translator / Integrator / Institutional Shield Provider" role vocabulary in its §5 is **not** to be imported.

Trace logs (from spine §3, TR ของบท 5): tor70-previous-criticism-and-dcce-recommendations, crdb-final-sprint-precode-dcce-approval-gates, director-toey-persona-and-tor70-briefing-critique, tor70_content_gap_analysis, tor70-analysis-timeline-reconstruction, a-btr-requirement-analysis, crdb-btr-me-integration-trace, adaptation-me-evidence-base-trace, thai-line-agencies-institutional-mental-model, crdb-evidence-merl-platform-feasibility.

## 3. Session-specific rules

- Active actor: คณะที่ปรึกษา (per report-wide rule §3 of `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md`).
- Target altitude: full-report level, "inverted detail" — restore technical detail the exec summary compressed; long lists and large tables to appendix only.
- This section **proposes**; it does not restate the gap. Reference §5.1's findings rather than re-deriving them, and reference Chapter 2 (framework results) and Chapter 3 (the 9 information services) rather than reproducing them.
- **Keep the two "what we hand over" lists visibly distinct.** Unit 1's 8 components are the handover package produced by this project. Units 2 and 3's 5 services are the targets proposed for the *next* contract's scope. They are different lists and the committee must not read them as one.
- Numbers trace to the DRD v2 set (75 requirements / 14 deliverables / 7 service briefs / 11 data specs — the spine's confirmed figures) and `data_catalog_v4.csv` (260 datasets; 97 held by 5 agencies). The older "13 deliverables / 9 service briefs / 12 data specs" figures are superseded and must not be used.
- Full report-wide style rules (§1 name/abbreviation use, §2 no internal document positions, §4 numbered lists for enumerable parallels, §5 Why/What/So-What minimum per subsection, §6 register and banned words, §8 พ.ศ. dating, §9 table naming, §10 figures) apply per `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md`, copied into `report_specific_rules` of the writing contract.

## 4. New content: unit 2 recommendation 2 — กำลังคนด้านข้อมูลภายในองค์กร

Boss-directed addition (2026-09-03), replacing the framing of DFR 5.3.9 §6. That section's original content (domain/sectoral experts, IT infrastructure investment, climate finance access) is **not** what this recommendation argues.

**Claim:** กรม สส. should build in-house data capability — data engineers, data analysts, and data management staff — as a function distinct from the department's existing IT unit.

**The distinction that carries it:** IT keeps systems, networks, and availability running. Data professionals work on the content itself — pipelines, quality, models, analysis. A department can have a fully staffed IT unit and still have nobody able to judge whether a dataset is fit to publish.

**Grounds:** the department currently has no staff proficient in data management or data engineering. The platform's value depends on work that never ends — updating datasets, curating quality, running analysis. The catalog holds 260 entries all awaiting certification review, and that review is continuous work, not a one-off task.

**Warrant:** contract-based delivery can *build* a platform; it cannot *keep one alive*. Without in-house capability, every update, maintenance task, and analysis has to route through a contractor — through a procurement cycle, and through whichever vendor holds the contract at the time.

**Application to design:** sustainability (the platform keeps working after the contract closes), flexibility (the department can change and extend without waiting to procure), usability (someone in-house understands the data well enough to keep it useful to real users).

**Why it sits at position 2 in unit 2:** EX 4.4 is ordered by decision authority — internal governance (full control) → own contract terms (full control) → external negotiation (dependent) — and closes deliberately on the dependent item. Building in-house capacity is full control, and it pairs directly with recommendation 1: recommendation 1 names Data Steward and Data Custodian, recommendation 2 says the department must build the skill to actually fill them, or the structure is names on paper.

**Links into the approved chain (use these as grounds, not the 5.3.9 role taxonomy):**
- Recommendation 1's 4-tier structure assigns data responsibilities that require data proficiency to discharge.
- Recommendation 3's product-owner argument already warns that without a data strategy, digital projects get bounded by whatever the contractor happens to understand — and that understanding changes with each new vendor. This is the same argument at the staffing level.
- Recommendation 3's Agile two-cycle beta milestone assumes departmental staff can review work in progress and give substantive feedback, which requires people who can read the data.
- Unit 3's group-2 tasks (build the catalog, certify domain by domain, develop analytical methodology continuously) are standing internal work, not contract deliverables.

**Evidence gap to close at Stage 1:** this recommendation's grounds are thinner than the other three — it currently rests on institutional logic plus Boss's direct knowledge of the department's staffing. Before verbalization, run a targeted evidence search (`/trace`) on DCCE's current data/IT staffing structure to see whether anything in the WP record substantiates the "no proficient staff today" claim. If nothing does, the claim must be written as the consultant's assessment rather than as a documented finding.

## 5. Open items carried into Stage 1

1. **The "บทที่ 5.3" pointer.** EX 4.4 cross-references "บทที่ 5.3" for the 5 services, but the full report's Chapter 5 has only §5.1 and §5.2. The 9 services are established in Chapter 3 §3.3; the 5 selected for the next contract are named inside §5.2 itself. Default handling unless Boss rules otherwise: name the 5 in place and reference Chapter 3 §3.3 for where the demand analysis established them.
2. **Appendix scope — resolved (Boss, 2026-09-03).** The 8 handover components' content goes to **ภาคผนวก ฌ**, which Boss is authoring. This section neither drafts nor summarizes that content. **Boss also inserts the appendix cross-reference himself** — unit 1 must not name a specific appendix letter. A generic mention that details sit in the report's appendix is acceptable (EX 4.3's own prose already carries one); naming "ภาคผนวก ฌ" or any other letter is Boss's to place.

## Stage 0 approval

Approved by Boss, 2026-09-03. The 3-unit split, the fresh re-derivation of all three exec-summary sources, the narrative-texture-only treatment of DFR 5.3.9, and the placement and framing of the new กำลังคนด้านข้อมูล recommendation were each confirmed in session. No Stage 2 bypass carried over from the exec-summary Chapter 4 precedent (treated as open per spine §7 until Boss says otherwise).
