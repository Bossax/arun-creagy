# Evidence traceability — 3.1 ทบทวนและสังเคราะห์ข้อมูลพื้นฐานและผลิตภัณฑ์ข้อมูลสารสนเทศ ณ ปัจจุบัน (Full Report)

เหตุที่จัดทำ: ความเห็นคณะกรรมการต่อเล่มร่างรายงานฉบับสมบูรณ์ งวดที่ 4 ข้อ 5.3.1 ให้เพิ่มรายละเอียดที่มาของข้อมูลและระบุแหล่งอ้างอิงให้ตรวจสอบได้ (`ψ/incubate/DCCE/CRDB/inbox_note/2026-09-23-Checklist...md`, §2). `polished-5.3.1.md` names sources directly in prose per the format rule (no internal locators); this file carries the page/section/interview detail behind each name.

## Evidence sets used

| Evidence set | What it backs |
|---|---|
| First interim-report submission (`inbox_source/2026-03-23_interim-report-1st-submission.md`, บทที่ 2 §2.2–2.4) | Product-landscape narrative, agency names, IPCC AR6 attribution, the 25×25 km grid claim |
| Stakeholder interview coverage (`output/archive/archived_interim_report/2026-03-25-5.3.2-Interview-Coverage-Table.md`, INT-01–INT-11) | Confirms each named agency was directly interviewed, not inferred |
| Data catalog (`output/02_Data_Inventory/data_catalog_v4.csv`, 260 rows) | Per-dataset owner, spatial resolution, update frequency, access condition |
| WP7 gap-analysis report (`output/07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md`, §3) | Current catalog-wide statistics; supersedes the older 5.3.8 evidence note's figures |

## Claim-by-claim

| Claim | Source |
|---|---|
| กรมป้องกันและบรรเทาสาธารณภัยมีพอร์ทัลและคลังข้อมูลเหตุการณ์ภัยพิบัติและความเสียหายเชิงปฏิบัติการ | Interim report บทที่ 2 §2.2–2.3; interview INT (DDPM), Interview Coverage Table |
| สำนักงานพัฒนารัฐบาลดิจิทัลมีพอร์ทัลข้อมูลเปิดและระบบแลกเปลี่ยนข้อมูลระหว่างหน่วยงานภาครัฐ | Interim report บทที่ 2 §2.2–2.3; interview INT-01 (DGA), Interview Coverage Table |
| สำนักงานสถิติแห่งชาติมีศูนย์ข้อมูลสถิติด้านทรัพยากรธรรมชาติและสิ่งแวดล้อม | Interim report บทที่ 2 §2.2–2.3; Interview Coverage Table (NSO) |
| กรมส่งเสริมการปกครองท้องถิ่นมีระบบข้อมูลและระบบประเมินผลขององค์กรปกครองส่วนท้องถิ่น | Interim report บทที่ 2 §2.2; Interview Coverage Table (DLA) |
| กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์มีระบบข้อมูลกลุ่มเปราะบางและแดชบอร์ดเชิงพื้นที่ | Interim report บทที่ 2 §2.2–2.3; Interview Coverage Table (MSDHS) |
| สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติมีโครงการประเมินความสูญเสียและความเสียหาย อยู่ระหว่างพัฒนา | Interim report บทที่ 2 §2.2, §2.7; Interview Coverage Table (NESDC) |
| ระบบแผนที่ความเสี่ยงของกรม สส. แสดงผลหลักที่ระดับจังหวัดโดยใช้กริด 25×25 กม. ผลลัพธ์เป็นดัชนีเชิงสัมพัทธ์ ไม่ใช่ค่าความเสี่ยงสัมบูรณ์ | Interim report บทที่ 2 §2.2 |
| "กรอบการประเมินความเสี่ยงสากล" ที่ตัวแบบดัชนีอ้างอิง | Interim report names IPCC AR6 explicitly. **Not independently verified** — the project's own 2026-08-29 citation-gap audit flagged this identical claim (hazard×exposure×vulnerability, IPCC framework) as GAP elsewhere in the report: no primary IPCC document recoverable in-project. Left un-named in `polished-5.3.1.md` pending Boss's decision (see `gap-log-ch3.md`) |
| แต่ละระบบภายนอกทำงานภายใต้รอบอัปเดต ขอบเขตพื้นที่ และเงื่อนไขการเข้าถึงที่ต่างกัน | `data_catalog_v4.csv` fields `owner_org`, `spatial_resolution`, `update_frequency`, `access_rights_dataset`, across 260 rows |

## Note on figures not used

The 5.3.8 evidence note's "ร้อยละ 20 พร้อมใช้ / ร้อยละ 80 ติดข้อจำกัด" figure is computed from catalog v3 under a superseded domain taxonomy. WP7's own traceability appendix states its numbers replace that figure. `polished-5.3.1.md` does not currently state a readiness percentage in prose; if one is added later, it should come from WP7 §3 (260 datasets, ~17% openly published, 122 province-level / 41 local-grain / 36 gridded / 59 unrecorded), not from the 5.3.8 note.

## Downstream registration

This file's contents are candidate inputs for the full-report references chapter (session J, not yet started per `00-โครงเรื่อง...md` §5) and for `E-xxx` evidence-registry rows once sealed via `/seal`. Not registered in `CRDB-Evidence-Registry.md` yet — that ledger is only written through the seal skill.
