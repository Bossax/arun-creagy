# A-BTR Themes & Sitemap Structural Gap Analysis Report (De-escalated Edition)

**Date**: 2026-07-10  
**Database**: [`a_btr_dissection.db`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/a_btr_dissection.db)  
**Target Sitemap Baseline**: [`NCAIF_Detailed_Sitemap_v8.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/NCAIF_Detailed_Sitemap_v8.md)  

## 1. Compliance Metrics & Summary

- **Total BTR Requirements**: 379
- **Successfully Mapped Requirements**: 379 (100.0% coverage)
- **Orphaned (Unmapped) Requirements**: 0
- **Total Sitemap Nodes (Sitemap v8.0)**: 41 (De-bloated: standalone pages converted to logical sub-nodes and merged where possible)
- **Sitemap Nodes with BTR Content**: 19 (46.3% of sitemap)
- **Sitemap Nodes without BTR Content (Category Headers / Systems only)**: 22 (53.7% of sitemap)

> [!NOTE]
> **UX Realignment & De-escalation**: Based on human design feedback, bureaucratic/academic reporting sections required by A-BTR were **de-escalated** to avoid cluttering the front-end user experience (อปท., วิศวกร, นักวางแผน):
> 1. **Slow-Onset Hazards Profile** (`3.2.2.1`) is nested under **Risk Analysis** (`3.2.2`).
> 2. **Adaptation Finance Directory & Support Tracking** (`2.3.1`) and **Institutional Arrangements** (`2.3.2`) are nested under the **Policy Hub (2.3)**.
> 3. **GESI (Inclusive Adaptation)** and **Barriers/Challenges** are merged directly into **Planning Guidelines** (`3.3.1`) and **Roadmap** (`3.3.2`) respectively.

---

## 2. Realigned Compliance Sub-Nodes

Below are the newly registered compliance sub-nodes that hold A-BTR requirement linkages without cluttering the main navigation hierarchy:

| Node ID         | Code    | Node Title (TH)                     | Parent Node                     | Added BTR Requirements | Topic Focus / Reporting Context                         |
| --------------- | ------- | ----------------------------------- | ------------------------------- | ---------------------- | ------------------------------------------------------- |
| **SIT-2.3.1**   | 2.3.1   | แหล่งทุนและการติดตามงบประมาณปรับตัว | SIT-2.3 (นโยบาย การเงิน)        | **7**                  | Climate budget tagging and support tracking (Section 4) |
| **SIT-2.3.2**   | 2.3.2   | กลไกเชิงสถาบันและการประสานงาน       | SIT-2.3 (นโยบาย การเงิน)        | **16**                 | Inter-agency committees and roles (Section 1)           |
| **SIT-3.2.2.1** | 3.2.2.1 | การติดตามภัยคุกคามที่เกิดขึ้นช้า    | SIT-3.2.2 (วิเคราะห์ความเสี่ยง) | **17**                 | SLR, land subsidence, and salinity (Section 5)          |
|                 |         |                                     |                                 |                        |                                                         |

---

## 3. Revised Mapping Density Distribution

| Node ID | Code | Node Title (TH) | Mapped BTR Requirements Count | Status |
|---|---|---|---|---|
| SIT-3.3 | 3.3 | การวางแผนการปรับตัวและการปฏิบัติ | **62** | 🟢 Fully Supported |
| SIT-2.1 | 2.1 | สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ | **58** | 🟢 Fully Supported |
| SIT-3.2.2 | 3.2.2 | การวิเคราะห์ความเสี่ยง | **51** | 🟢 Fully Supported |
| SIT-3.1.2 | 3.1.2 | ปัจจัยขับเคลื่อนทางภูมิอากาศ | **50** | 🟢 Fully Supported |
| SIT-3.1.1 | 3.1.1 | ข้อมูลสังเกตุการณ์ | **46** | 🟢 Fully Supported |
| SIT-3.2.4 | 3.2.4 | ความสูญเสียและความเสียหาย | **44** | 🟢 Fully Supported |
| SIT-2.2 | 2.2 | สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน | **41** | 🟢 Fully Supported |
| SIT-2.3 | 2.3 | เครื่องมือทางนโยบาย กฎหมาย และการเงิน | **41** | 🟢 Fully Supported |
| SIT-3.4.3 | 3.4.3 | กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ การคัดสรรและถอดบทเรียนโครงการเด่น | **40** | 🟢 Fully Supported |
| SIT-1.1.2 | 1.1.2 | ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย | **32** | 🟢 Fully Supported |
| SIT-3.3.5 | 3.3.5 | โครงการที่กำลังดำเนินการ | **31** | 🟢 Fully Supported |
| SIT-3.4.2 | 3.4.2 | ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย | **31** | 🟢 Fully Supported |
| SIT-3.2.2.1 | 3.2.2.1 | การติดตามภัยคุกคามที่เกิดขึ้นช้า | **17** | 🟢 Fully Supported |
| SIT-2.3.2 | 2.3.2 | กลไกเชิงสถาบันและการประสานงาน | **16** | 🟢 Fully Supported |
| SIT-3.3.1 | 3.3.1 | แนวทางการวางแผนการปรับตัว | **16** | 🟢 Fully Supported |
| SIT-1.1.1 | 1.1.1 | ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย | **10** | 🟢 Fully Supported |
| SIT-3.3.2 | 3.3.2 | เส้นทางกลยุทธ์การปรับตัวของประเทศ | **10** | 🟢 Fully Supported |
| SIT-2.3.1 | 2.3.1 | แหล่งทุนและการติดตามงบประมาณปรับตัว | **7** | 🟢 Fully Supported |
| SIT-4.1 | 4.1 | บัญชีข้อมูล | **4** | 🟢 Fully Supported |

