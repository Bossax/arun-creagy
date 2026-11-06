# [DELIVERABLE BRIEF] 2026-10-28_ncaif-build-deliverables

**From**: arun (Arun Creagy Oracle)  
**To**: samart-writer (Samart Writer Oracle)  
**Date**: 2026-10-28 21:45 +07:00  
**Topic**: NCAIF Platform Build Deliverables Source Reconciliation & Section 7.3 Evidence Base  

---

## Executive Summary

1. **Reconciliation of Deliverables Count (14 vs. 15 Work Packages)**:
   - The **2026-08-20 DRD v2 baseline** (`2026-08-20-WP4-DRD-deliverables-v2.csv`) established **14 platform deliverables (DEL-1 ถึง DEL-14)**, covering 30 build-ready functional requirements and product surfaces across data engineering, software interfaces, and structured content.
   - The **2026-10-27 Delegation Matrix** (`2026-10-27-WP4-DRD-Deliverables-Delegation-Matrix.md` / `.csv`), which formally supercedes the v2 CSV for operational execution, expands the scope to **15 work packages (DEL-0 ถึง DEL-14)** across 3 execution tracks (Track A, B, C). The addition is **DEL-0** (*In-House Direct Content Porting*), created to operationalize the 14 pre-existing DCCE publications and infographic assets (previously categorized under Handling A: "Already covered") that require ingestion into the CMS by DCCE internal staff.

2. **Debunking the "13 Technical Specification Documents + 1 Overview Report" Review Comment**:
   - The review comment claiming that the 14 deliverables represent *"13 technical specification documents plus 1 overview report"* is **factually incorrect and conflates work packages with project documents**.
   - **DEL-1 through DEL-14 are functional system deliverables and content packages**, NOT separate document files. They include live time-series dashboards (DEL-1), CCIC GIS map layers (DEL-2), searchable databases (DEL-10), user feedback modules (DEL-11), disaster statistics processing pipelines (DEL-12), cloud migration jobs (DEL-13), and thematic policy explainers (DEL-3 to DEL-9, DEL-14).
   - The origin of the number "13" traces to **DRD v2 Checkpoint 1a** (`2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md` line 23), where the net capability cluster count was noted as `14 -> 13` due to folding map/profile backend requirements under DEL-2 (while retaining DEL-13 for non-map migration). A reviewer misread this architectural note and assumed "14 items" meant 13 technical document specifications plus 1 overview report.

3. **Demarcation of DEL-0 and Software Vendor Build Scope**:
   - **DEL-0 does NOT belong to the external software vendor's development build scope.** DEL-0 is 100% internal DCCE work (Track A: Environmental Communications Group & Strategy Division) to port, copy, and format existing approved manuals, master plans, and graphics into the CMS.
   - For an external SDLC development contract, the contractor's build scope consists of **Track C (System & Data Engineering: DEL-1, DEL-2, DEL-10, DEL-11, DEL-13)** and the data engineering pipeline of **Track B (DEL-12)**. Content authoring (DEL-3 through DEL-9, DEL-14) is for subject-matter specialists, and DEL-0 is strictly internal agency data entry.

4. **Recommendation for Section 7.3.2.2**:
   - Section 7.3.2.2 currently reads: *"3. สิ่งที่ต้องส่งมอบ 14 รายการ ใช้วางแผนงานซอฟต์แวร์และงานเนื้อหา..."*
   - We recommend clarifying the terminology from "สิ่งที่ต้องส่งมอบ 14 รายการ" to **"แพ็กเกจงานส่งมอบระบบและเนื้อหา (Deliverable Work Packages)"** with an explicit distinction between software/data engineering packages (สัญญาจ้างพัฒนาระบบ) and content/internal porting packages, firmly repudiating the mistaken notion that these are 13 separate specification documents.

---

## Detailed Analysis & Findings

### 1. Root Cause Analysis: Where Did "13 + 1" Come From?

An audit of the git history and markdown texts in `output/04_Sitemap/` reveals the exact progression:

1. **The DRD Document Architecture**:
   The Developer-Ready Design Requirements package was delivered as **one consolidated specification document** accompanied by 5 structured CSV tables:
   - Primary Document: `2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` (and its delta update `...-v2.md` on 2026-08-20).
   - Structured CSVs: `requirements-v2.csv`, `deliverables-v2.csv`, `service-briefs-v2.csv`, `data-specs-v2.csv`, and `assets-cited-v2.csv`.
   - There was **never** a set of "13 separate technical specification documents" corresponding to DEL-1 through DEL-13. All 72–75 requirements and their corresponding DEL groupings are contained in the single consolidated specification report.

2. **The "13" Count Origin in DRD v2**:
   In `2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md`:
   - Line 23 states: `"- Net deliverable count: 14 -> 13 (DEL-2 and DEL-13 remain distinct IDs - this is a scope reallocation between them, not a literal ID merge - but the map/profile capability that was split across both is now correctly attributed to one of them)."`
   - Line 1018 of the v1 specification also stated: `"Six of the thirteen are primarily content production. DEL-6 through DEL-10, DEL-3, and DEL-5..."`
   - An external reviewer or reader, seeing the total of 14 deliverables in `deliverables-v2.csv` alongside the note about 13 net functional scopes and 1 overview specification report, erroneously conflated them into: *"13 technical specification documents plus 1 overview report"*.

3. **Conflation of Deliverable Nature**:
   Deliverables DEL-1 to DEL-14 are **system components, functional modules, and structured content packages**, as shown below. Calling them "technical specification documents" fundamentally misrepresents the TOR deliverables and would mislead procurement officers into contracting for report writing rather than platform software engineering.

---

### 2. Comprehensive Deliverables Reconciliation Matrix

The table below reconciles the **2026-08-20 DRD v2 baseline** with the **2026-10-27 Delegation Matrix**, categorizing each deliverable into its true technical nature:

| ID | Title (TH / EN) | 2026-08-20 Type (v2 CSV) | 2026-10-27 Track & Lead (Matrix) | True Technical Nature | Vendor Build Scope? | Primary Requirements Served |
|:---:|---|---|---|---|:---:|---|
| **DEL-0** | การนำเข้าเนื้อหาและสื่อเผยแพร่ที่มีอยู่แล้วใน กสส.<br>*(In-House Direct Content Porting)* | *(Not in v2; categorized as Handling A "Already covered")* | **Track A**<br>กลุ่มสื่อสารสิ่งแวดล้อม / กองยุทธศาสตร์ฯ | **Internal Content Ingestion**<br>Copy & format existing DCCE manuals & graphics into CMS | **NO**<br>(Internal DCCE Staff) | REQ-002, 006, 007, 016, 019, 021, 023, 026, 065, 066, 067, 068, 072, 074 |
| **DEL-1** | แดชบอร์ดข้อมูลภูมิอากาศประเทศไทย<br>*(Thailand Climatology Dashboard)* | Data engineering + product | **Track C**<br>กลุ่มพัฒนาเทคโนโลยีดิจิทัล | **Software & Data Engineering**<br>TMD climate grid API & interactive time-series UI | **YES**<br>(Core Software Contractor) | REQ-033 |
| **DEL-2** | ระบบแผนที่ความเสี่ยงและโปรไฟล์รายพื้นที่<br>*(Risk Map & Profile Layer)* | Data engineering and interface | **Track C**<br>กลุ่มพัฒนาเทคโนโลยีดิจิทัล | **GIS & Software Integration**<br>CCIC map layer upgrade, admin boundaries, 7-sector scores | **YES**<br>(Core Software Contractor) | REQ-004, 008, 009, 014, 015, 070 |
| **DEL-3** | บทความอธิบายระบบตรวจวัดและติดตามภูมิอากาศโลก<br>*(External-Source Explainers: Global Monitoring)* | Content + partnership | **Track B**<br>กองยุทธศาสตร์และความร่วมมือฯ | **Content Synthesis & Partnership**<br>Explainer articles + MoU/linking with TMD, ONWR, GISTDA | **NO**<br>(Content/Institutional Team) | REQ-030, 031 |
| **DEL-4** | รายงานโปรไฟล์ภัยคุกคามที่เกิดขึ้นช้า<br>*(Slow-Onset Hazards Profile)* | Content, with derivation as a later stretch | **Track A**<br>กองขับเคลื่อนการปรับตัวฯ | **Content Synthesis & Analytics**<br>Sea level rise & coastal erosion statistical profiles | **NO**<br>(Domain Specialist Team) | REQ-042, 043, 044, 045 |
| **DEL-5** | ชุดคำอธิบายการฉายภาพอนาคตและฉากทัศน์ภูมิอากาศ<br>*(Projections & Climate Scenarios Explainers)* | Content + partnership | **Track B**<br>กองขับเคลื่อนการปรับตัวฯ | **Content & Data Guidance**<br>SSP/RCP scenario selection guide & climate projection links | **NO**<br>(Domain Specialist Team) | REQ-032, 035, 075 |
| **DEL-6** | มาตรฐานกรอบแนวคิดและระเบียบวิธีประเมินความเสี่ยง<br>*(Concept and Methodology Standards)* | Content | **Track A**<br>กองยุทธศาสตร์และความร่วมมือฯ | **Institutional Content**<br>Impact chain guidelines & international risk standards | **NO**<br>(Domain Specialist Team) | REQ-038, 040, 048 |
| **DEL-7** | ชุดสาระบริบทความเสี่ยงและกรณีศึกษา<br>*(Risk Framing and Worked Examples)* | Content | **Track A**<br>กองขับเคลื่อนการปรับตัวฯ | **Institutional Content**<br>Physical vs Transition risk (CBAM) & agricultural case studies | **NO**<br>(Domain Specialist Team) | REQ-003, 037, 047 |
| **DEL-8** | ชุดเนื้อหาด้านกฎหมาย นโยบาย และการเงินการปรับตัว<br>*(Policy, Legal & Financial Tools Guidance)* | Content | **Track A**<br>กองยุทธศาสตร์และความร่วมมือฯ | **Institutional Content**<br>Climate change bill summary, GCF/AF funding, State Audit CBA | **NO**<br>(Institutional Specialist) | REQ-017, 025, 057 |
| **DEL-9** | แนวทางการวางแผนปรับตัวอย่างครอบคลุมและกลุ่มเปราะบาง<br>*(Inclusion and Community Adaptation Content)* | Content | **Track A**<br>กองขับเคลื่อนการปรับตัวฯ | **Institutional Content**<br>Gender, vulnerable groups & community-based adaptation | **NO**<br>(Domain Specialist Team) | REQ-053, 054, 055 |
| **DEL-10** | ห้องสมุดและคลังมาตรการปรับตัวรายสาขา<br>*(Adaptation Measures Library)* | Product and content | **Track C**<br>กองขับเคลื่อนการปรับตัวฯ / กลุ่มดิจิทัล | **Software & Data Catalog**<br>Searchable NAP 6-sector measures database & NbS repository UI | **YES**<br>(Core Software Contractor) | REQ-060, 061 |
| **DEL-11** | ระบบช่องทางการรับฟังความคิดเห็นและบริการผู้ใช้<br>*(Feedback Platform & User Services)* | Build | **Track C**<br>กลุ่มสื่อสารสิ่งแวดล้อม / กลุ่มดิจิทัล | **Web Operational Capability**<br>User feedback forms, data inquiry requests, internal tracking | **YES**<br>(Core Software Contractor) | REQ-073 |
| **DEL-12** | ระบบประมวลผลสถิติภัยพิบัติและความสูญเสียแห่งชาติ<br>*(National Disaster Statistics Product)* | Data engineering + product | **Track B**<br>กองขับเคลื่อนการปรับตัวฯ (ร่วม ปภ.) | **Data Engineering & Product**<br>DDPM 10-year disaster database ingestion & statistics pipeline | **YES**<br>(Software/Data Contractor) | REQ-001, 011 |
| **DEL-13** | การย้ายและบูรณาการผลผลิตวิเคราะห์ของ กสส. สู่ระบบกลาง<br>*(Platform Infrastructure Analytical Migration)* | Data engineering + hosting | **Track C**<br>กลุ่มพัฒนาเทคโนโลยีดิจิทัล | **Cloud & Infrastructure Engineering**<br>Migrate DCCE_3_x exposure/sector risk services onto central cloud | **YES**<br>(Infrastructure Contractor) | REQ-005, 013, 041 |
| **DEL-14** | ไดเรกทอรีเชื่อมโยงศูนย์ข้อมูลภูมิอากาศภายนอก<br>*(External Data Hub Links Directory)* | Content | **Track A**<br>กองยุทธศาสตร์และความร่วมมือฯ | **Content & Structured Directory**<br>Catalog of external international/national climate portals | **NO**<br>(Internal Content / Web Admin) | REQ-071 |

---

### 3. Clear Breakdown: Build Work Packages vs. Documents

To prevent future confusion in report drafting and procurement specifications:

1. **System Build & Data Engineering Work Packages (6 Packages)**:
   - **DEL-1**: Thailand Climatology Dashboard
   - **DEL-2**: Risk Map & Profile Layer
   - **DEL-10**: Adaptation Measures Library
   - **DEL-11**: Feedback Platform & User Services
   - **DEL-12**: National Disaster Statistics Product (shared with Track B for institutional coordination)
   - **DEL-13**: Platform Infrastructure Analytical Migration
   *Nature: Software code, database schemas, ETL pipelines, UI/UX components, cloud hosting.*

2. **Specialized Content & Domain Analytical Packages (8 Packages)**:
   - **DEL-3**: External-Source Explainers (Global Monitoring)
   - **DEL-4**: Slow-Onset Hazards Profile
   - **DEL-5**: Projections & Climate Scenarios Explainers
   - **DEL-6**: Concept and Methodology Standards
   - **DEL-7**: Risk Framing and Worked Examples
   - **DEL-8**: Policy, Legal & Financial Tools Guidance
   - **DEL-9**: Inclusion and Community Adaptation Content
   - **DEL-14**: External Data Hub Links Directory
   *Nature: Analytical texts, policy briefs, structured knowledge articles, curated web copy.*

3. **Internal Administrative Ingestion Package (1 Package)**:
   - **DEL-0**: In-House Direct Content Porting (14 existing DCCE publications, master plans, infographics).
   *Nature: Routine CMS upload and markdown formatting by DCCE communications officers.*

4. **Authoritative Specification & Governance Documents (Not DELs)**:
   These are the planning and architectural artifacts that describe the system:
   - `WP4-Developer-Ready-Design-Requirements-Specification-v2.md` (Main specification)
   - `WP4-DRD-Deliverables-Delegation-Matrix.md` (Delegation framework)
   - `WP4-Node-Content-Storyboard-and-Synthesis-Guide-v2.md` (Content blueprints)
   - `WP4-DRD-Requirements-Content-Recipe.md` (Input data recipes)
   - `WP4-DCCE-Content-Preparation-Playbook.md` (Operational timeline)

---

### 4. Clarification on DEL-0 Scope Boundary

- **Contractual Scope**: DEL-0 must be **excluded** from any commercial RFP or TOR for the external software vendor. If included in a vendor TOR, the vendor would charge professional consulting and development rates for simple copy-pasting of existing government publications.
- **Internal Operational Scope**: DEL-0 is **mandatory** for DCCE's internal operations (Playbook Section 3.1) because it covers 14 requirements (e.g., REQ-002 IPCC framework, REQ-026 CCIC user manual, REQ-065 technology framework). Without DEL-0, the live website would have 14 major blank pages on launch day even if the software code is 100% complete.

---

### 5. Recommended Thai Wording for Section 7.3

In Section 7.3.2.2 (item 3), replace the current ambiguous sentence:

#### Current Text:
> `3. **สิ่งที่ต้องส่งมอบ 14 รายการ** ใช้วางแผนงานซอฟต์แวร์และงานเนื้อหา โดยกำหนดรุ่นเอกสารและเกณฑ์ตรวจรับให้ตรงกับรายการในภาคผนวก ฌ`

#### Recommended Revised Text (Option A — Preserving Appendix ฌ / 14-Deliverable Baseline while clarifying Work Packages):
> `3. **แพ็กเกจผลผลิตงานส่งมอบ 14 รายการ (Deliverable Work Packages: DEL-1 ถึง DEL-14)** ใช้วางแผนงานพัฒนาระบบซอฟต์แวร์ วิศวกรรมข้อมูล และงานสังเคราะห์เนื้อหา โดยจำแนกเป็นผลผลิตด้านวิศวกรรมระบบและฐานข้อมูล 5 รายการ (เช่น แดชบอร์ดภูมิอากาศ แผนที่ความเสี่ยง CCIC และคลังมาตรการ) ผลผลิตด้านการประมวลผลข้อมูลร่วมภายนอก 2 รายการ และผลผลิตด้านเนื้อหาและชุดคำอธิบาย 7 รายการ ทั้งนี้ ผลผลิตดังกล่าวเป็นแพ็กเกจงานส่งมอบระบบ มิใช่เอกสารข้อกำหนดทางเทคนิค 13 ฉบับกับรายงานภาพรวม 1 ฉบับตามที่เข้าใจคลาดเคลื่อน และควรกำหนดเกณฑ์ตรวจรับให้ตรงกับข้อกำหนดในภาคผนวก ฌ`

#### Recommended Revised Text (Option B — Preferred: Comprehensive Harmonization with October 2026 Delegation Matrix):
> `3. **แพ็กเกจงานส่งมอบระบบและเนื้อหา (Deliverable Work Packages)** ซึ่งตามฐานข้อกำหนดทางเทคนิคเดิม (DRD v2) กำหนดไว้ 14 รายการ (DEL-1 ถึง DEL-14) และได้รับการปรับปรุงล่าสุดในตารางมอบหมายภารกิจ (Delegation Matrix 27 ต.ค. 2569) เป็น 15 รายการ โดยเพิ่ม DEL-0 สำหรับงานนำเข้าเนื้อหาและสื่อเดิมของ กสส. ทั้งนี้ งานส่งมอบทั้งหมดเป็นผลผลิตระบบ ท่อส่งข้อมูล แดชบอร์ด และเนื้อหาเชิงโครงสร้าง ไม่ใช่เอกสารทางวิชาการ โดยในส่วนของสัญญาจ้างพัฒนาระบบ ให้มุ่งเน้นที่ผลผลิตด้านวิศวกรรมระบบและข้อมูล (Track C: DEL-1, DEL-2, DEL-10, DEL-11, DEL-13 และ Track B: DEL-12) ส่วน DEL-0 และชุดเนื้อหาอื่นเป็นภารกิจของบุคลากรภายในและผู้เชี่ยวชาญเนื้อหา`

---

## Primary Citations & Evidentiary Grounding

1. **Governing Deliverables Delegation Matrix (27 October 2026)**:
   - File: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-10-27-WP4-DRD-Deliverables-Delegation-Matrix.md`
   - Lines 1–5: Explicit declaration superceding v2 deliverables CSV.
   - Lines 32–49: Full table defining DEL-0 through DEL-14, their 3 Tracks, and the 14 requirements served by DEL-0.
   - Companion CSV: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-10-27-WP4-DRD-Deliverables-Delegation-Matrix.csv` (15 deliverable rows).

2. **Previous Baseline Deliverables CSV (20 August 2026)**:
   - File: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-20-WP4-DRD-deliverables-v2.csv`
   - Lines 1–15: Exactly 14 deliverables (DEL-1 to DEL-14). DEL-0 absent.

3. **DRD Specification v2 Delta Note**:
   - File: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md`
   - Line 23: Text recording `Net deliverable count: 14 -> 13` explaining the DEL-2 / DEL-13 scope reallocation.

4. **DRD Specification v1 Appendix A**:
   - File: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md`
   - Lines 987–1009: Appendix A ("What actually has to be built") defining the 14 deliverables as the true planning view.
   - Line 1018: Note explaining that six of the deliverables are content production rather than engineering.

5. **DCCE Content Preparation Playbook**:
   - File: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-10-27-WP4-DCCE-Content-Preparation-Playbook.md`
   - Lines 46–75: Operational assignment of 15 deliverables across DCCE divisions and external agencies.
