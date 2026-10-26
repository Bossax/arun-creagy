# Evidence Map: CRDB Full Report Chapter 6 (Draft Version)
**Title**: (ร่าง) ข้อมูลเสนอแนะเชิงนโยบายและเชิงเทคนิคในการพัฒนารายการชุดข้อมูลพื้นฐาน รายการผลิตภัณฑ์ข้อมูลและสารสนเทศและการบริหารจัดการข้อมูลในระยะยาว  
**Mandate**: TOR Scope Clause 5.3.9 & Installment 3 Deliverable (Draft Final Report)  
**Analytical Posture**: Analytical Capability Framework (Grounding from Interviews, Workshop, and Gap Analysis)

---

## 1. Usable Source Documents

| Source File | Description & Relevant Content | Direct Quotation / Key Grounding |
|---|---|---|
| [`2026-06-25_draft_section-5.3.9.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/2026-06-25_draft_section-5.3.9.md) | Original drafted text for TOR 5.3.9 created on 2026-06-25 (`CH-029`). | Contains the 6 thematic pillars: 1) Internal Governance (6 elements), 2) Service Portfolio (4 categories), 3) 5-layer Technical Standards, 4) Technical Partnerships, 5) Positioning (Certifier, Translator, Integrator, Shield), 6) Resources/IT/Manpower. |
| [`analysis-piece-for-5.3.9.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/analysis-piece-for-5.3.9.md) | Analytical bridge connecting Gap Analysis to 5.3.9 sequencing. | *"ปัญหาใหญ่ที่สุดไม่ใช่ตัวข้อมูลดิบ แต่เป็นกลไกการนำข้อมูลไปใช้งาน... กรมฯ ไม่ควรเริ่มต้นจากการลงทุนผลิตหรือจัดหาข้อมูลใหม่... ระยะเร่งด่วน: ปิดช่องว่างมาตรฐาน Metadata และบัญชีระเบียบวิธีความเสี่ยง..."* |
| [`2026-06-25_evidence-note_5.3.3_5.3.8_5.3.9.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/2026-06-25_evidence-note_5.3.3_5.3.8_5.3.9.md) | Cross-cutting evidence notes linking FGDs, workshop, and gap findings. | Documents that 80% of data requests were manual/paper-based, and that users lack trust in uncertified datasets. |
| [`2026-06-25_draft_section-5.3.8.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/2026-06-25_draft_section-5.3.8.md) | Gap Analysis Draft (Section 5.3.8). | The 5 core findings: 1) Need for official baseline values, 2) Sub-provincial spatial resolution, 3) Need for science-to-decision translation, 4) Ad-hoc coordination, 5) Lack of uncertainty communication standards. |
| [`2026-03-05-Feature-Driven Data Governance Strategy v3.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/2026-03-05-Feature-Driven%20Data%20Governance%20Strategy%20v3.md) | Early Phase 1 governance framework (`D-011`). | Defined governance gates G1–G5 and publishing rails for data certification. |

---

## 2. Ledger Anchors & Decision History

- **`T-036` / `CH-029` (2026-06-25)**: Upgraded report sections 5.3.8 (Gap Analysis) and 5.3.9 (Policy & Technical Recommendations) to resolve 5 key user-feedback gaps.
- **`D-048`**: Hardened Service Package Specs v2 to serve as zero-discovery inputs.
- **`CH-016` (2026-05-27)**: Consolidated 26 workshop concepts into 10 Canonical Use Cases (UC-01 to UC-10).
- **`CH-022` (2026-06-05)**: Consolidated NCAIF to 7 User-Centric Intelligence Services.

---

## 3. Allocation Matrix to TOR Frame

| TOR Component | TOR Axis: Policy (ข้อเสนอแนะเชิงนโยบาย) | TOR Axis: Technical (ข้อเสนอแนะเชิงเทคนิค) |
|---|---|---|
| **1. รายการชุดข้อมูลพื้นฐาน** *(Baseline Data Inventory)* | • นโยบายการเปิดเผยข้อมูลสาธารณะ (Open Data Policy) เพื่อแก้ปัญหาข้อมูล 51% ที่จำกัดการเข้าถึง<br>• นโยบายการสร้างความร่วมมือเชิงสถาบันกับหน่วยงานต้นทาง (Pillar 4: Partnerships) | • มาตรฐานคำอธิบายข้อมูล (Metadata Standard 12 ฟิลด์ตาม DGA/ISO 19115)<br>• พจนานุกรมข้อมูลกลาง (Data Dictionary)<br>• แบบจำลองข้อมูลเชิงแนวคิด (CDM 8 โดเมน) |
| **2. รายการผลิตภัณฑ์ข้อมูลและสารสนเทศ** *(Information Product Inventory)* | • นโยบายการบริหารระบบข้อมูลในฐานะ Service Portfolio (4 กลุ่มบริการหลัก)<br>• การวางตำแหน่งเชิงยุทธศาสตร์: National Certifier และ Translator (Pillar 5) | • ระบบสารบัญระเบียบวิธีวิเคราะห์ความเสี่ยง (Risk Methodology Catalog)<br>• มาตรฐานการแปลงวิทยาศาสตร์สู่การตัดสินใจ (Science-to-Decision)<br>• มาตรฐานการสื่อสารความไม่แน่นอน (Uncertainty Communication) |
| **3. การบริหารจัดการข้อมูลในระยะยาว** *(Long-Term Data Management)* | • การสถาปนากรอบธรรมาภิบาลข้อมูลภายใน 6 องค์ประกอบ (Pillar 1)<br>• บทบาท Institutional Shield Provider คุ้มครองเจ้าหน้าที่<br>• นโยบายทรัพยากร โครงสร้างพื้นฐาน และกำลังคนเฉพาะทางรายสาขา (Pillar 6) | • มาตรฐานการเชื่อมต่อข้อมูล Interoperability และ API Web Services<br>• การฝังกฎตรวจสอบอัตโนมัติในระบบจัดการข้อมูล (Automated CMS Rules)<br>• กรอบลำดับการดำเนินงานเชิงวิเคราะห์ 3 ขอบฟ้า (3 Horizons) |
