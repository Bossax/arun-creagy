# Evidence Map: CRDB Full Report Chapter 7 (Section 7.3 Final Recommendations)
**Title**: 7.3 ข้อมูลเสนอแนะเชิงนโยบายและเชิงเทคนิคในการพัฒนารายการชุดข้อมูลพื้นฐาน รายการผลิตภัณฑ์ข้อมูลและสารสนเทศและการบริหารจัดการข้อมูลในระยะยาว (ฉบับสมบูรณ์)  
**Mandate**: TOR Installment 4 Deliverable 4 (Final Policy and Technical Recommendations)  
**Analytical Posture**: Operational Procurement & Implementation Blueprint (Hardened for Downstream Contracting)

---

## 1. Usable Source Documents

| Source File | Description & Relevant Content | Direct Quotation / Key Grounding |
|---|---|---|
| [`Chapter 6-report-first-submission.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-full-report-6/Chapter%206-report-first-submission.md) | First submission text containing the hardened blueprint, 4 decision-authority recommendations, and 2-track roadmap. | Primary source text for migration and restructuring into Section 7.3 under the TOR dual-axis $\times$ 3-component structure. |
| [`2026-08-16-WP8-Recommendations-Report.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/08_Recommendations/2026-08-16-WP8-Recommendations-Report.md) | WP8 final recommendations deliverable (`D-074`, `CH-044`). | Establishes DCCE ownership across contracts, the UK GDS agile delivery precedent (`E-088`), the 4 governance roles, the 5 priority services, and the 6-month roadmap. |
| [`plan-slice.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-full-report-6/plan-slice.md) | Strategic design slice approved by Boss on 2026-09-03. | Section 4 articulates the in-house data talent rationale: *"IT keeps systems, networks, and availability running. Data professionals work on the content itself — pipelines, quality, models, analysis... Contract-based delivery can build a platform; it cannot keep one alive."* |
| [`crdb-exec-summary-4.3`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-exec-summary-4.3/section-4.3-draft.md), [`4.4`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-exec-summary-4.4/section-4.4-draft.md), [`4.5`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-exec-summary-4.5/section-4.5-draft.md) | Approved executive summary drafts. | Source of the approved 4 recommendations ordered by decision authority, the 6-phase SDLC coverage figures (70%/80%), the 8 handover components, and the 8 governance tasks. |
| [`data_catalog_v4.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/data_catalog_v4.csv) | Master catalog of 260 baseline datasets. | Confirms exact empirical figures: 260 datasets; 97 datasets (37.3%) held by 5 core agencies (TMD, GISTDA, DDPM, NSO, NESDC); over 51% restricted. |
| [`2026-05-21_CRDB-Technical-SDLC-and-Role-Accountability-Framework.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-21_CRDB-Technical-SDLC-and-Role-Accountability-Framework.md) | Technical SDLC & Role Accountability Framework (`D-031`). | Source of the 6-phase SDLC framework and the strict Content Writer vs. System Developer role separation. |
| [`2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md) | DRD v2 Specifications (`D-077`, `CH-046`). | Reconciles the 75 requirement items, 14 deliverables, 38 sitemap nodes, and companion data specs. |

---

## 2. Ledger Anchors & Decision History

- **`T-043` / `CH-044` / `D-074` (2026-08-16)**: Sealed the WP8 Recommendations Report, introducing the UK GDS Agile delivery model (`E-088`), 4 governance tiers, and line agency agreements.
- **`CH-030` / `CH-034` / `CH-036` (July–August 2026)**: Shifted project focus to TOR70 alignment, establishing the "Blueprint as a Shield" to provide zero-discovery handoff specifications.
- **`CH-046` (2026-08-20)**: Finalized DRD v2 specifications (75 requirements, 14 deliverables, 38 nodes).
- **`plan-slice.md` §4 (2026-09-03)**: Boss's explicit mandate establishing Recommendation 2 (In-House Data Talent).

---

## 3. Dissected Allocation Matrix to TOR Frame

| TOR Component | TOR Axis: Policy (ข้อเสนอแนะเชิงนโยบาย) | TOR Axis: Technical (ข้อเสนอแนะเชิงเทคนิค) |
|---|---|---|
| **1. รายการชุดข้อมูลพื้นฐาน** *(Baseline Data Inventory)* | • **นโยบายข้อตกลงแลกเปลี่ยนข้อมูล 5 หน่วยงานหลัก**: ทำข้อตกลงทวิภาคีกับ อม., GISTDA, ปภ., สสช., สศช. ที่ถือครอง 97 ชุดข้อมูล (37%) โดยยึดความต้องการของ กรม สส. เป็นตัวตั้ง และดำเนินงานคู่ขนาน (`REC-BASE-POL-01`) | • **การบังคับใช้แบบจำลองข้อมูล CDM 8 โดเมนและ Metadata**: กำหนดให้เป็นเกณฑ์เทคนิคของสัญญาจ้าง และการจัดทำทะเบียนทรัพย์สินดิจิทัลรายกลุ่มงาน (`REC-BASE-TECH-01`) |
| **2. รายการผลิตภัณฑ์ข้อมูลและสารสนเทศ** *(Information Product Inventory)* | • **ยุทธศาสตร์ผลิตภัณฑ์นำและการจัดลำดับ 5 บริการสำคัญ**: กรม สส. ถือบทบาท Product Owner; โฟกัส 3 บริการเดิม (ความเสี่ยงเชิงพื้นที่, แผนที่ภัย, ดัชนีความเสี่ยง) + 2 บริการใหม่ (A-BTR และ Loss & Damage MVP ร่วมกับ สศช.) (`REC-PROD-POL-01`) | • **พิมพ์เขียวสถาปัตยกรรมระบบ SDLC 6 ระยะ & ข้อมูลสนับสนุน 8 รายการ**: ส่งมอบระยะ 1 (~70%) และ 2 (~80%), ข้อกำหนด 8 องค์ประกอบในภาคผนวก ฌ, การแยกบทบาท Content Writer vs System Developer (`REC-PROD-TECH-01`) |
| **3. การบริหารจัดการข้อมูลในระยะยาว** *(Long-Term Data Management)* | • **โครงสร้างธรรมาภิบาลข้อมูลภายใน 4 ระดับ**: คณะกรรมการกองฯ, Data Owner, Data Steward, Data Custodian เพื่อรับรอง 260 ชุดข้อมูล (`REC-MGMT-POL-01`)<br>• **นโยบายสร้างกำลังคนด้านข้อมูลในองค์กร**: Data Engineers, Analysts, Managers แยกขาดจากฝ่ายไอทีเดิม (`REC-MGMT-POL-02`)<br>• **กรอบสัญญาจ้างพัฒนาระบบแบบ Agile**: อย่างน้อย 2 รอบพร้อมหมุดหมาย Beta กลางสัญญา (`REC-MGMT-POL-03`) | • **แผนที่นำทางแบบ 2 กลุ่มงานคู่ขนาน**: กลุ่มสัญญาจ้างพัฒนาระบบ + ภารกิจธรรมาภิบาล 8 งาน (ระยะสั้น 4 งาน 6 เดือน, ระยะกลาง 4 งาน 1-3 ปี) พร้อมระบุจุดบรรจบของสัญญา (`REC-MGMT-TECH-01`) |
