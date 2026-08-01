# Content Plan: DCCE Climate Adaptation Platform Budget Defense Widescreen Deck

## 1. Insight Card

*   **Reader Question**: How can DCCE justify a 25M THB budget envelope for the National Climate Adaptation Platform, proving it will build a sustainable, DGA-compliant, and technically ready data system instead of a legacy static portal?
*   **Source-Specific Finding**: Thailand currently holds 391 fragmented climate digital assets (80.6% are static PDFs/knowledge documents) that are locked in manual coordination processes and low resolution (25-100km). DCCE has created a pre-validated, build-ready logical blueprint (CDM v3.0, Sitemap v8.0, and DGA-aligned quality gates G1-G5) that directly maps to TOR70, allowing procurement to bypass the discovery/alpha phases and begin development immediately.
*   **Mechanism**:
    1.  *Data Pipeline*: Automated 3-layer data engine (Bronze raw, Silver standardized via DOPA codes, Gold CDM-aggregated).
    2.  *Governance & Compliance*: DGA-aligned roles (Data Owner, Data Steward, Technical Custodian) and OpenLineage audit traces mapping local M&E activity data to international BTR reports.
    3.  *Application Layer*: PostGIS spatial core running high-resolution (township level) risk mappers and economic loss-avoided calculations.
*   **Consequence**: Approving the budget envelope immediately launches construction, bypassing 10-16 weeks of standard discovery delay, establishing DCCE's national authority, and protecting high-risk economic zones (e.g. Chao Phraya Basin which drives 66% of GDP).
*   **Visual Proof**: Comparison graphs (Legacy fragmentation vs. Target platform), Dual-Architecture flowcharts (Data engine to Portal), Governance lifecycle structures, and a 4-module build roadmap.
*   **Evidence Anchors**:
    *   [DCCE_Unified_Digital_Asset_Database_Summary.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/DCCE_Unified_Digital_Asset_Database_Summary.md#L11-L18)
    *   [รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md#L23-L36)
    *   [บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md#L120-L128)
    *   [2026-07-06_btr-me-reporting-pipeline-use-case.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-07-06_btr-me-reporting-pipeline-use-case.md#L84-L94)
    *   [5.2.9 สรุปผลการพัฒนาโครงสร้างข้อมูล...](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/final_report/5.2/5.2.9%20สรุปผลการพัฒนาโครงสร้างข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ%20และ%20(ร่าง)%20โครงสร้างการบริหารจัดการข้อมูลการเปลี่ยนแปลงสภาพภูมิอากาศ.md#L144-L159)
    *   [TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026.md#L150-L200)

---

## 2. Module Mapping (Slide Structure)

### Slide 1: Climate Economic Threat, Data Gaps & Digital Infrastructure
*   **Claim ID**: C-001 (Climate Threat, Gaps & Digital Infrastructure)
*   **Evidence Anchor**: `DCCE_Unified_Digital_Asset_Database_Summary.md#L11-L18` & `รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md#L23-L36`
*   **Mechanism**: Emphasizing that climate change threat to economy (World Bank CCDR) requires dynamic data to manage future risk under uncertainty, which highlights existing data gaps (PDF lock, low resolution) and makes the national digital infrastructure (DGA standard integration) crucial for adaptation planning.
*   **Reader Job**: Understand the economic threat, see the current data gaps, and recognize digital infrastructure as the key adaptation capability.
*   **Visual Role**: Three-column dashboard structure: (1) Climate Threat to Economy, (2) Existing Data Gaps, (3) Digital Infrastructure for Adaptation.


### Slide 2: User Demands & Frontend Sitemap Architecture
*   **Claim ID**: C-002 (Stakeholder Demand & Sitemap Architecture)
*   **Evidence Anchor**: `บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md#L120-L128` & `2026-07-06_btr-me-reporting-pipeline-use-case.md#L84-L94`
*   **Mechanism**: Justifying the frontend sitemap information architecture (Home/Area Search, Policy Maker Center, Knowledge Cycle, Tools & Services, News & Contact) for tool/information dissemination per user needs, backed by the backend data management foundation.
*   **Reader Job**: Validate how surveyed stakeholder demands shape the sitemap structure and backend data foundation.
*   **Visual Role**: Two-column layout: (1) 50% width on Surveyed Demands, (2) 50% width on Frontend Sitemap Tree linked to Backend Data Foundation.

### Slide 3: Climate Data System Conceptual Design & A-BTR Showcase
*   **Claim ID**: C-003 (Conceptual Design & A-BTR Pipeline)
*   **Evidence Anchor**: `2026-07-06_btr-me-reporting-pipeline-use-case.md#L33-L42` & `5.2.9 สรุปผลการพัฒนาโครงสร้างข้อมูล...#L144-L159`
*   **Mechanism**: Conceptual design of the data system building on country DGA infrastructure and industry-best practice to allow data discovery and sharing in climate risk/adaptation domains, highlighting the A-BTR reporting pipeline as the comprehensive strategic starting usecase.
*   **Reader Job**: Confirm data system viability, DGA integration, and the A-BTR strategic pipeline alignment.
*   **Visual Role**: Federated Pipeline Flow Diagram (Local inputs ➔ DGA-aligned standard validation ➔ Discovery & Sharing Database ➔ A-BTR & GDX outputs).

### Slide 4: FY2027 Key Platform Deliverables
*   **Claim ID**: C-004 (FY2027 Build Components & Technical Readiness)
*   **Evidence Anchor**: `TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026.md#L150-L200`
*   **Mechanism**: 4 concrete deliverables ready for immediate implementation (Data Pipeline, Metadata & Governance, Risk Search & GIS, BTR Analysis & Reporting) backed by a pre-validated logical blueprint (frozen requirements).
*   **Reader Job**: Assess procurement integrity, build readiness, and zero discovery-phase delays under the 25M THB envelope.
*   **Visual Role**: Horizontal roadmap milestone grid detailing core functional modules.

---

## 3. Excluded Claims (Prohibited Content)
*   Do not include itemized hardware/software licensing fees or server hosting cost sheets.
*   Do not visualize abstract or decorative icons (e.g. lightbulbs, generic gears, gears turning together) that have no semantic relationship to data architecture.
