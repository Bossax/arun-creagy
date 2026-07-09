# A-BTR Themes & Sitemap Gap Analysis Report

**Date**: 2026-07-09  
**Database**: [`a_btr_dissection.db`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/a_btr_dissection.db)  
**Sitemap Source**: [`NCAIF_Detailed_Sitemap_v6.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/NCAIF_Detailed_Sitemap_v6.md)  

## 1. Compliance Metrics & Summary

- **Total BTR Requirements**: 379
- **Successfully Mapped Requirements**: 379 (100.0% coverage)
- **Orphaned (Unmapped) Requirements**: 0
- **Total Sitemap Nodes**: 38
- **Sitemap Nodes with BTR Content**: 16 (42.1% of sitemap)
- **Sitemap Nodes without BTR Content (Content Gaps)**: 22 (57.9% of sitemap)

---

## 2. Orphaned BTR Requirements Diagnostics

> [!NOTE]
> **SUCCESS**: All dissected BTR requirements are successfully mapped to at least one sitemap landing zone. No orphaned requirements found.

---

## 3. Sitemap Content Gaps (Empty Nodes)

The following sitemap nodes currently have **zero** matching A-BTR requirements mapped to them. These represent content gaps where the website structure expects data, but the BTR adaptation report does not provide supporting material. These must be filled by other national plans, weather datasets, or departmental announcements:

| Node ID | Code | Level | Title (TH) | Title (EN) | Brief Content / Action Item |
|---|---|---|---|---|---|
| SIT-1 | 1 | 1 | หน้าแรก | Home: National Climate Adaptation Portal | Section header node. No direct requirements needed. |
| SIT-1.1 | 1.1 | 2 | สรุปสำหรับผู้บริหาร | Executive Overview | Section header node. No direct requirements needed. |
| SIT-1.2 | 1.2 | 2 | สืบค้นข้อมูลรายพื้นที่ |  | Requires supplemental inputs from other agency portals. |
| SIT-2 | 2 | 1 | ศูนย์ข้อมูลสำหรับผู้กำหนดนโยบายและแผน | Policy Maker Information Center | Section header node. No direct requirements needed. |
| SIT-2.4 | 2.4 | 2 | บริการข้อมูลสำหรับการวางแผน |  | Requires supplemental inputs from other agency portals. |
| SIT-3 | 3 | 1 | วงจรขับเคลื่อนการปรับตัว | Adaptation Knowledge Cycle | Section header node. No direct requirements needed. |
| SIT-3.1 | 3.1 | 2 | วิทยาศาสตร์ของสภาพภูมิอากาศ | Climate Science | Section header node. No direct requirements needed. |
| SIT-3.1.3 | 3.1.3 | 3 | ฉากทัศน์ภูมิอากาศในอนาคต |  | Requires CMIP6 downscaling instructions and user tutorials. |
| SIT-3.2 | 3.2 | 2 | การวิเคราะห์ผลกระทบ ความเสี่ยง และความเปราะบาง | Risk Analysis | Section header node. No direct requirements needed. |
| SIT-3.2.1 | 3.2.1 | 3 | การวิเคราะห์ความเปราะบางและการเปิดรับภัย |  | Requires theoretical background text on climate sensitivity and vulnerability. |
| SIT-3.2.3 | 3.2.3 | 3 | ผลกระทบลูกโซ่ |  | Requires impact chain templates (e.g. from GIZ or DCCE projects). |
| SIT-3.2.5 | 3.2.5 | 3 | กรอบทฤษฎีและเอกสารคู่มือ |  | Requires standard risk assessment manuals and PDF guides. |
| SIT-3.3.3 | 3.3.3 | 3 | ห้องสมุดมาตรการปรับตัวตามสาขา |  | Requires sector-specific adaptation measure database entry forms. |
| SIT-3.3.4 | 3.3.4 | 3 | กรณีศึกษาการวางแผนการปรับตัว |  | Requires planning templates from actual pilot project budgets. |
| SIT-3.4 | 3.4 | 2 | การติดตาม ประเมินผล และถอดบทเรียน | M&E and Learning | Section header node. No direct requirements needed. |
| SIT-3.4.1 | 3.4.1 | 3 | แนวทางการติดตามและประเมินผลการปรับตัว |  | Requires GGA/M&E baseline guidelines and theoretical indicators. |
| SIT-4 | 4 | 1 | เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ | Tools & Services | Section header node. No direct requirements needed. |
| SIT-4.2 | 4.2 | 3 | Visualization and Analytics Application |  | Requires development of interactive GIS web maps (Climate Risk Map Apps). |
| SIT-4.3 | 4.3 | 3 | ศูนย์รวมเครื่องมือและแหล่งข้อมูลภายนอก |  | Requires external hyperlinks to international databases (TMD, GISTDA, Copernicus). |
| SIT-5 | 5 | 1 | ข่าว ประกาศ และช่องทางการติดต่อ | News and Contact | Section header node. No direct requirements needed. |
| SIT-5.1 | 5.1 | 3 | ประกาศกิจกรรมของศูนย์ การอัพเดทชุดข้อมูล การเผยแพร่ชุดข้อมูล ความร่วมมือกับหน่วยงาน กิจกรรม workshop งานอบรมที่เกี่ยวกับข้อมูลสภาพภูมิอากาศ |  | Requires CMS setup for ongoing workshop, training, and activity posts. |
| SIT-5.2 | 5.2 | 3 | ช่องทางการรับ feedback ที่เป็นระบบเพื่อการปรับปรุงผลิตภัณฑ์ข้อมูล ชุดข้อมูล บริการสารสนเทศ การสื่อสาร |  | Requires system feedback forms and database logger setup. |

---

## 4. Node Mapping Density Distribution

The distribution of mapped requirements shows where the portal content is concentrated:

| Node ID | Code | Level | Title (TH) | Requirements Mapped | Mapped Share (%) |
|---|---|---|---|---|---|
| SIT-3.3 | 3.3 | 2 | การวางแผนการปรับตัวและการปฏิบัติ | 77 | 20.3% |
| SIT-2.1 | 2.1 | 2 | สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ | 58 | 15.3% |
| SIT-3.2.4 | 3.2.4 | 3 | ความสูญเสียและความเสียหาย | 53 | 14.0% |
| SIT-2.3 | 2.3 | 2 | เครื่องมือทางนโยบาย กฎหมาย และการเงิน | 53 | 14.0% |
| SIT-3.2.2 | 3.2.2 | 3 | การวิเคราะห์ความเสี่ยง | 51 | 13.5% |
| SIT-3.1.2 | 3.1.2 | 3 | ปัจจัยขับเคลื่อนทางภูมิอากาศ | 50 | 13.2% |
| SIT-3.1.1 | 3.1.1 | 3 | ข้อมูลสังเกตุการณ์ | 46 | 12.1% |
| SIT-2.2 | 2.2 | 2 | สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน | 41 | 10.8% |
| SIT-3.4.3 | 3.4.3 | 3 | กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ การคัดสรรและถอดบทเรียนโครงการเด่น | 40 | 10.6% |
| SIT-1.1.2 | 1.1.2 | 3 | ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย | 32 | 8.4% |
| SIT-3.4.2 | 3.4.2 | 3 | ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย | 31 | 8.2% |
| SIT-3.3.5 | 3.3.5 | 3 | โครงการที่กำลังดำเนินการ | 31 | 8.2% |
| SIT-1.1.1 | 1.1.1 | 3 | ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย | 10 | 2.6% |
| SIT-3.3.1 | 3.3.1 | 3 | แนวทางการวางแผนการปรับตัว | 5 | 1.3% |
| SIT-4.1 | 4.1 | 3 | บัญชีข้อมูล | 4 | 1.1% |
| SIT-3.3.2 | 3.3.2 | 3 | เส้นทางกลยุทธ์การปรับตัวของประเทศ | 4 | 1.1% |

