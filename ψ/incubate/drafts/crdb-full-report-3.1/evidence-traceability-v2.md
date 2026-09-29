# Evidence traceability v2 — 3.1 ทบทวนและสังเคราะห์ข้อมูลพื้นฐานและผลิตภัณฑ์ข้อมูลสารสนเทศ ณ ปัจจุบัน (Full Report)

เหตุที่จัดทำ: ความเห็นคณะกรรมการต่อเล่มร่างรายงานฉบับสมบูรณ์ งวดที่ 4 ข้อ 5.3.1 ให้เพิ่มรายละเอียดที่มาของข้อมูลและระบุแหล่งอ้างอิงให้ตรวจสอบได้ (`ψ/incubate/DCCE/CRDB/inbox_note/2026-09-23-Checklist...md`, §2). This file backs `polished-5.3.1-v2.md`. Reader-facing text names sources by their real names only; the locators below (sections, interview IDs, dataset IDs, CSV fields) stay here.

Supersedes `evidence-traceability.md` for the v2 text. The v1 file is unmodified.

## Evidence sets used

| Evidence set | Name used in reader text | What it backs |
|---|---|---|
| First interim-report submission (`inbox_source/2026-03-23_interim-report-1st-submission.md`, บทที่ 2 §2.2–2.7; บทที่ 1 §1.6) | รายงานฉบับกลาง | Product-landscape narrative, agency roles, DCCE risk-map structure and limits, DCCE website findings, reporting-chain description, survey/update-cycle limits, use cases |
| Stakeholder interview coverage table (`output/archive/archived_interim_report/2026-03-25-5.3.2-Interview-Coverage-Table.md`, INT-01–INT-11; detail in interim-report appendix ง) | การสัมภาษณ์หน่วยงานผู้มีส่วนเกี่ยวข้อง / การสัมภาษณ์ [หน่วยงาน] | Interview count (11), dates, interviewed units, topics covered |
| Data catalog (`output/02_Data_Inventory/data_catalog_v4.csv`, 260 rows) | บัญชีรายการชุดข้อมูลของโครงการ | Per-agency dataset counts, titles, spatial resolution, temporal resolution, access, time period, use limitations, provenance route (`data_source`) |
| WP7 gap-analysis report (`output/07_Gap_Analysis/2026-08-16-WP7-Gap-Analysis-Report.md`) | รายงานการวิเคราะห์ช่องว่างข้อมูล / การวิเคราะห์ช่องว่างข้อมูล | Catalog-wide statistics and ownership concentration (§3), 5 km downscaling (§3), risk-index mechanics (§5 Service 2), DDPM record limits (§5 Service 4), NESDC methodology (Gap 10), view-only products (Gap 6), grid vs admin units (Gap 3), lineage (Gap 5), connected access (§2), web-content check (§6), PDPA aggregation point (Gap 4) |
| IPCC AR6 WGII (2022), Chapter 1 "Point of Departure and Key Concepts", https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-1/ | กรอบความเสี่ยงของ IPCC ในรายงานการประเมินครั้งที่ 6 ของคณะทำงานที่ 2 (พ.ศ. 2565) | The framework definition: risk arises from the interaction of hazard, exposure and vulnerability, and responses modulate each. The explicit risk framing began with SREX and AR5. Verified by Boss's web search, 2026-09-29 (relayed by coordinator); not re-fetched in this pass |
| Boss decision, 2026-09-29 (relayed by coordinator) | stated as a consultant action | NESDC L&D project is closed; the consultants adopted its framework into the MVD |
| MVD name: `output/…` draft-final-report and exec-summary texts, e.g. "(ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ (Minimum Viable Dataset: MVD) สำหรับเหตุการณ์ด้านสภาพภูมิอากาศ" (found by grep across `ψ/incubate/DCCE/CRDB/output/**` and `ψ/incubate/drafts/crdb-exec-summary-3.4/02_th_draft.md`) | (ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ (Minimum Viable Dataset: MVD) | Full name of MVD at first mention |

Catalog provenance, computed from `data_source`: 140 rows from "Report รายงานฉบับสมบูรณ์โครงการปรับปรุงระบบฐานข้อมูลความเสี่ยงเชิงพื้นที่จากการเปลี่ยนแปลงสภาพภูมิอากาศ"; 31 rows "ข้อมูลจากการสัมภาษณ์"; 1 row another report (industrial-estate map); 6 rows blank; the other 82 are agency websites or data services. That supports "รายการที่เหลือส่วนใหญ่จากเว็บไซต์และบริการข้อมูล".

## Claim-by-claim

Status key: **S** = supported as stated · **P** = partly supported / inferred from adjacent evidence · **U** = not supported by the named sources (retained from v1 per Boss, marked `[ต้องตรวจแหล่ง]` in the text) · **C** = consultant inference/implication (analysis, not a sourced fact) · **B** = Boss decision/statement, no document source · **FLAG** = needs Boss decision

### Evidence-base block (new)

| Claim | Source | Status |
|---|---|---|
| หลักฐานสี่ชุด: รายงานฉบับกลาง, การสัมภาษณ์, บัญชีรายการชุดข้อมูล, รายงานการวิเคราะห์ช่องว่าง | Brief; the four files above | S |
| สัมภาษณ์ 11 หน่วยงาน ระหว่าง 17 ก.พ.–5 มี.ค. 2569 | Coverage table (INT-04 17 Feb earliest; INT-03, INT-10 5 Mar latest); Summary "Total interviews … 11" | S |
| Sector list of the 11 agencies | Coverage table `agency_or_institution` / `sector_or_domain` (DGA, DLA, FTI, MSDHS, NESDC, NSO, NXPO, OTP, TBA/banks, UDDC, DDPM) | S |
| หน่วยงานภายนอกที่กล่าวถึงผ่านการสัมภาษณ์โดยตรง ยกเว้น TMD และ GISTDA | DDPM INT-11, DGA INT-01, NSO INT-06, DLA INT-02, MSDHS INT-04, NESDC INT-05; TMD and GISTDA absent from the coverage table | S |
| สรุปผลการสัมภาษณ์รายหน่วยงานอยู่ในภาคผนวกของรายงานฉบับกลาง | Coverage table header: Appendix ง of interim-report appendix | S |
| บัญชีรายการ 260 ชุด บันทึกเจ้าของ ระดับพื้นที่ รอบการปรับปรุง การเข้าถึง ข้อจำกัด | CSV fields `owner_org`, `spatial_resolution`, `update_frequency_unit`, `access_rights_dataset`, `use_limitations` | S |
| 140 รายการจากรายงานโครงการปรับปรุงระบบฐานข้อมูลความเสี่ยงฯ, 31 จากการสัมภาษณ์ | CSV `data_source` counts | S |
| ทั้ง 260 รายการอยู่ในสถานะร่าง ยังไม่ผ่านการตรวจสอบรับรอง เพราะยังไม่มีขั้นตอนนี้ | CSV `endorsement_status` = Baseline-Draft ×260, `validation_flag` = Unverified-Baseline ×260; WP7 §3, Gap 9 | S |
| ยังไม่มีรายการใดระบุสัญญาอนุญาต | CSV `license_id` = "License not specified" ×260 | S |
| รายการจากรายงานโครงการปรับปรุงฯ เป็นตัวชี้วัดนำเข้า; หน่วยงานต้นทางระบุเบื้องต้น | CSV `notes` on these rows read "อาจมาจาก: …" (e.g., DDPM_3_2, NSO_2_2, NESDC_2_5, MSDHS_2_1) | S |
| ข้อมูลต้นทางจำนวนมากมีคุณภาพดี | WP7 §3 "much of which is sound" | S |

### Table 3 and landscape paragraphs (carried from v1)

| Claim | Source | Status |
|---|---|---|
| Table 3 rows (all cells unchanged from v1) | As in v1 sidecar | as v1 |
| Table 3 cell "ใช้กรอบความเสี่ยงของ IPCC จากรายงานการประเมินครั้งที่ 6 ของคณะทำงานที่ 2 ตามที่รายงานฉบับกลางระบุ" | **Framework:** verified, IPCC AR6 WGII (2022) Ch.1 (URL above). **That DCCE's index follows it:** interim report §2.2 ("พัฒนาขึ้นตามกรอบของ IPCC AR6"), attributed in the text to the interim report; catalog DCCE_3_1 "ดัชนีรวมจาก Hazard × Exposure × Vulnerability" corroborates the structure. This supersedes the 2026-08-29 citation-gap audit GAP for this claim only | S (framework) / S-attributed (DCCE's use) |
| Table 3 cell "ดัชนีชี้วัดที่ได้รับการยอมรับ" | Same claim as the "accepted in discussions" row below | **U** — marked `[ต้องตรวจแหล่ง]` |
| Table source line "คณะที่ปรึกษาสังเคราะห์จาก…" | Table content traces to interim ch.2 + catalog fields (v1 sidecar) | S |
| Landscape list of agency products (¶ "ภาพรวมของภูมิทัศน์…") | Interim §2.2 | S |
| Table 3 external row: TMD (forecasts, climate-extreme indices) and GISTDA (satellite data, open data services) | Data catalog TMD_x, GISTDA_x | S |
| Landscape list additions for TMD and GISTDA | Data catalog | S |
| ได้รับการยอมรับในวงสนทนาระดับจังหวัดและระดับนโยบาย | Interim §2.2 says the system is the most advanced product and "มีความพร้อมเชิงการสื่อสารต่อสาธารณะมากกว่า"; "accepted in provincial/policy discussions" is not stated | **U** — marked `[ต้องตรวจแหล่ง]` |
| ผู้ใช้ต้องใช้เวลามากในการค้นหาว่าข้อมูลอยู่ที่ใด ใครเป็นเจ้าของ เงื่อนไขการใช้ | Interim §2.4 ("หน่วยงานหลายแห่งยังสะท้อนตรงกันว่า…") | S |
| ระบบนิเวศข้อมูลมีความสมบูรณ์เชิงทรัพยากร แต่ขาดการจัดระเบียบเชิงความหมาย | Interim §2.7 ข้อสังเกตประการแรก | S |

### กรม สส. — risk map and climate data

| Claim | Source | Status |
|---|---|---|
| ระบบแผนที่ความเสี่ยงมีสามส่วน (แบบจำลองและดัชนี / แผนที่และภาพข้อมูล / ฐานข้อมูลและเครื่องมือ) | Interim §2.2 | S |
| ชั้นแบบจำลองและดัชนีพัฒนาตามกรอบความเสี่ยงของ IPCC AR6 WGII (2022), attributed "รายงานฉบับกลางระบุว่า" | Interim §2.2 | S-attributed |
| กรอบ IPCC: ความเสี่ยงเกิดจากปฏิสัมพันธ์ระหว่างภัย การเผชิญภัย ความเปราะบาง; การตอบสนองมีผลต่อแต่ละองค์ประกอบ | IPCC AR6 WGII Ch.1, https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-1/ (Boss-verified). The SREX/AR5 origin is kept here only, not in the text | S |
| ดัชนีรวมข้อมูลภัย การเผชิญภัย ความเปราะบาง ในหกสาขาการปรับตัว | Interim §2.2; CSV DCCE_3_1 notes | S |
| บัญชีรายการบันทึกผลลัพธ์ 7 ชุด (6 สาขา + ดัชนีภูมิอากาศ) | CSV DCCE_3_1 … DCCE_3_7 | S |
| ระดับจังหวัด รายปี CSV เปิดเผย ช่วง 1960–2100 | CSV DCCE_3_x `spatial_resolution`=Province, `update_frequency_unit`=ปี, `data_format`=CSV, `access_rights_dataset`=Public, DCCE_3_1 period 1960–2100. DCCE_3_2…3_7 carry `time_period_end` 2101–2106, which is a data-entry artifact; DCCE_3_1 used | S (artifact noted) |
| ภาพฉาย SSP2-4.5 และ SSP5-8.5 | CSV DCCE_3_1 `use_limitations` "มีเฉพาะ ssp585 และ ssp245". Later rows increment (ssp246…ssp251), same artifact | S |
| URL of risk database (sidecar only) | CSV `url` https://ccic.dcce.go.th/riskarea | — |
| ข้อมูลภูมิอากาศกริด 19 ชุด ผ่าน Climate Data Visualization | CSV DCCE_2_1 … DCCE_2_19, `data_source` "Website Climate Data Visualization", `url` https://clim-webbased.dcce.go.th/DataServices | S |
| ตัวแปร: ฝน, Tmax, Tmin, Tmean, ความชื้นสัมพัทธ์ | CSV titles DCCE_2_x | S |
| ย้อนหลัง 1981–2023; คาดการณ์ถึง 2099–2100; WRF-Chem, RegCM5, SD CMIP6 | CSV DCCE_2_x `time_period_*`, `notes` | S |
| ความละเอียดทางเวลารายวันและรายเดือน; เข้าถึงเมื่อยื่นขอ | CSV `temporal_resolution` "รายวัน; รายเดือน"; `access_rights_dataset`=Restricted | S |
| WRF-Chem มีเฉพาะ SSP5-8.5 | CSV DCCE_2_6 … 2_10 `use_limitations` | S |
| กรม สส. จัดทำข้อมูล SD 5 กม. สำหรับฝนและ Tmax/Tmin/Tmean ภายใต้ SSP2-4.5/5-8.5; ละเอียดกว่ากริด 25 กม.; เป็นจุดตั้งต้นของข้อมูลภัยและความเสี่ยงที่ละเอียดขึ้น | WP7 §3, stated as WP7 states it (WP7's own appendix traces the detail to the submitted 5.3.8 draft). The catalog's SD rows do not record 5 km | S (as WP7 states) |
| Producing unit name | WP7 writes "DCCE's Climate Change Research Center". The repo's Thai name for a DCCE centre is "ศูนย์วิจัยการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (Climate Change and Environment Research Center)" (`output/05_Data_Management_Framework/CDM_EARCatalog/DCCE Data Value Chain.md`; inception report). The English names differ, and no source links the 5 km data to that centre, so the text drops the unit name and uses "กรม สส." | Dropped — **FLAG** if Boss wants the unit named |
| ข้อจำกัด 1: ระดับจังหวัด กริด 25×25 กม. | Interim §2.2 | S |
| ข้อจำกัด 2: ดัชนีสัมพัทธ์ ไม่ใช่ค่าความเสียหายทางการเงิน/ความเสี่ยงสัมบูรณ์ | Interim §2.2 | S |
| ข้อจำกัด 3: การคาดประมาณอนาคตสมมติข้อมูลเศรษฐกิจสังคมบางส่วนคงที่ | Interim §2.2 | S (new in v2) |
| หน่วยวิเคราะห์กำหนดที่จังหวัดก่อนคำนวณ; คูณและปรับค่ามาตรฐานเป็นคะแนนเดียว ย้อนกลับไม่ได้ | WP7 §5 Service 2 | S |
| เหมาะกับภาพรวม จัดลำดับ สื่อสารนโยบาย มากกว่าระดับอำเภอ/ตำบล | Interim §2.2, §2.4 | S |
| ข้อมูลประชากร/ทรัพย์สินจำแนกกลุ่มสังคมเศรษฐกิจยังไม่มีที่ความละเอียดเดียวกัน | WP7 Gap 2 | S |
| Design implications (ยืนยันขอบเขต เสริมคำอธิบาย เชื่อมโยง พัฒนาข้อมูลการเผชิญภัยควบคู่) | Carried from v1 + consultant inference from WP7 Gap 2 | C |

### กรม สส. — website and subsystems

| Claim | Source | Status |
|---|---|---|
| เว็บไซต์รวบรวมรายงานนโยบาย รายงานวิชาการ ข่าว โครงการ ระบบย่อย ลิงก์เครื่องมือ | Interim §2.2 | S |
| ลักษณะเว็บไซต์ตามภารกิจ มีเว็บย่อยซ้อน ("เว็บซ้อนเว็บ") | Interim §2.2 | S |
| เส้นทางผ่านหน้าแรก → ข่าว/รายงาน/หน้าโครงการ → ระบบย่อย; เนื้อหาวงจรการปรับตัวกระจัดกระจาย | v1 text; interim §1.6, §2.2 | S |
| เนื้อหาสำหรับผู้กำหนดนโยบายอยู่ในรูปเอกสาร; ผู้ใช้เชิงพื้นที่ไม่มีเส้นทางที่เป็นรูปธรรม | Interim §2.2 | S |
| ตรวจหน้าเนื้อหาของแพลตฟอร์มใหม่กับทรัพย์สินดิจิทัลกรม สส. 391 รายการ (สิ่งพิมพ์ ชุดข้อมูล เครื่องมือ สื่อ) | WP7 §6 (from WP4 content-source gap report, D-061) | S |
| หน้าเชิงบรรยายมีแหล่งรองรับในเกณฑ์ใช้ได้; หน้าแดชบอร์ด/แผนที่/เครื่องคำนวณมีข้อมูลแบบมีโครงสร้างน้อย | WP7 §6 | S |
| สอดคล้องกับข้อค้นพบเรื่องสถานภาพการเผยแพร่ภายในกรม สส. | v1 (originally the TOR 5.2.2 finding) | as v1 |

### กรมอุตุนิยมวิทยา (TMD) — catalog only, not interviewed

| Claim | Source | Status |
|---|---|---|
| 37 ชุด มากที่สุดในบัญชีรายการ | CSV `owner_org`=TMD; WP7 §3 | S |
| หกหน่วยงาน (TMD, DCCE, GISTDA, DDPM, NSO, NESDC) ถือครองประมาณครึ่งหนึ่ง | WP7 §3 ("Roughly half the catalog sits with those six") | S (now used, since TMD and GISTDA have accounts) |
| ไม่ได้สัมภาษณ์; รายงานฉบับกลางไม่บรรยายผลิตภัณฑ์เป็นรายการ | Coverage table (absent); interim ch.2 (grep finds only generic "ข้อมูลอุตุนิยมวิทยา") | S |
| กลุ่มตัวขับเคลื่อนทางภูมิอากาศและข้อมูลภัย | CSV `cdm_sub_domain` CLIMATE_DRIVER / HAZARD / COMPOSITE_INDEX, plus 3 VULNERABILITY input indicators | P (the 3 input indicators are classed vulnerability) |
| WRF 6 ชุด (ฝน 1 ชม./24 ชม., ความกดอากาศ, RH, T2M, ลม 10 ม.), กริด ทั้งประเทศ, เปิดเผย, ภาพเท่านั้น; ส่วนพยากรณ์อากาศเชิงตัวเลข กองพยากรณ์อากาศ | CSV TMD_1_1 … TMD_1_6 (`use_limitations` "เผยแพร่เป็นภาพเท่านั้น"; `data_source`) | S |
| ดัชนีความร้อนรายวัน ระดับจังหวัด 2014–2019 ภาพ เปิดเผย; เส้นทางพายุตามเหตุการณ์ | CSV TMD_2_1, TMD_3_1 (TMD_3_1 access blank) | S |
| 2 ชุดที่ขอเพื่อ WebGIS กรม สส. อยู่ระหว่างขอ ยังไม่ได้รับ ณ เวลาจัดทำบัญชี | CSV TMD_4_1, TMD_5_1 (`use_limitations` "อยู่ระหว่างขอข้อมูล - ยังไม่ได้รับ"; notes "จากรายการขอข้อมูล WebGIS DCCE 19/01/2026") | S (dated to catalog time) |
| ดัชนีสุดขั้ว 24 ชุด (ตัวอย่าง TXx, WSDI, SU35, Rx1day, Rx5day, CDD, SPI-1, HI_Heat/Flood/Drought = เฉลี่ย intensity/duration/frequency) รายปี, SPI รายเดือน, Restricted | CSV TMD_6_1 … TMD_6_24 (titles, notes, `update_frequency_unit`) | S |
| รวบรวมจากรายงานโครงการปรับปรุงระบบฐานข้อมูลความเสี่ยง; เจ้าของบันทึกเป็น TMD แต่ "เป็นข้อมูลภายในจากโครงการของ DCCE" | CSV TMD_6_x `data_source`, `use_limitations` | S |
| ตัวชี้วัดจังหวัด 3 รายการ ที่มาเบื้องต้น | CSV TMD_6_25 … TMD_6_27 (notes "อาจมาจาก") | S |
| 7 เปิดเผย; 27 ไม่ระบุระดับพื้นที่ | CSV counts (Public 7, Restricted 29, blank 1; Unknown 27) | S |
| ผลิตภัณฑ์ที่ดูได้บนหน้าจอเท่านั้นใช้เป็นข้อมูลนำเข้าไม่ได้ | WP7 Gap 6 (general statement, applied to TMD image outputs) | S (general) / C (application) |
| Design implication (lineage แยกผู้ผลิตต้นทาง/ผู้คำนวณ; ระดับพื้นที่; รูปแบบไฟล์) | WP7 Gap 5 names lineage; application is consultant inference | C |

### สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ (GISTDA) — catalog only, not interviewed

| Claim | Source | Status |
|---|---|---|
| Thai name "สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ"; English name | Repo texts (e.g., `output/…` "สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ (GISTDA)"); WP7 §3 "Geo-Informatics and Space Technology Development Agency". The "(องค์การมหาชน)" suffix is not in the repo, so it is not used | S |
| 17 ชุด อันดับสาม รองจาก TMD และ DCCE | CSV; WP7 §3 | S |
| ไม่ได้สัมภาษณ์; รายงานฉบับกลางไม่บรรยายผลิตภัณฑ์ | Coverage table; interim ch.2 (no mention) | S |
| API gateway 10 ชุด (burnt area latest/365 days; crop suitability and crop check for 6 crops; palm, rubber annual; rice, maize, cassava, sugarcane biweekly; 40 m) 2025–2026 | CSV GISTDA_1_1 … GISTDA_1_10 (`data_source` "Website Gistda Gateway", url api-gateway, titles) | S. "ครอบคลุมช่วง 2568–2569": time periods 2025, with burnt-area-365 to 2026 |
| Disaster Platform 3 ชุด (flood extent from satellite, hotspots: event-based; soil moisture weekly; tambon; 2022/2023 → 2025/2026) | CSV GISTDA_3_1 … GISTDA_3_3; full system name from `data_source` | S |
| Marine GI Portal 2 ชุด (SST daily grid from VIIRS on Suomi-NPP/NOAA-20; nighttime light annual 2016–2025, proxy for economic activity) | CSV GISTDA_2_1, GISTDA_2_2 (`data_source`, notes) | S |
| Data Cube ภาพถ่ายดาวเทียม รายวัน/รายเดือน 2017–2025 | CSV GISTDA_4_1 | S |
| ตัวชี้วัดพื้นที่น้ำท่วมซ้ำซาก ระดับจังหวัด Restricted, ข้อมูลนำเข้า | CSV GISTDA_5_1 (`data_source` = risk-database project report) | S |
| 16/17 เปิดเผย; ส่วนใหญ่กริดหรือตำบล | CSV counts (Grid 9, Tambon 3, Unknown 4, Province 1) | S |
| การเข้าถึงหลายขั้นตอน (Disaster Platform) | CSV GISTDA_3_x `use_limitations` | S |
| มีการกำหนดรุ่นของบริการ | CSV titles/notes (v1.1, v1.2, v2.2) | S |
| ข้อมูลภัยเป็นกริด ข้อมูลประชากรเป็นเขตการปกครอง ยังไม่มีวิธีเชื่อมที่ตกลงร่วมกัน | WP7 Gap 3 | S |
| การเข้าถึงที่เชื่อมต่อกับระบบงานของผู้ใช้เป็นความต้องการ | WP7 §2 ("Access that connects to working systems") | S; calling GISTDA an example of it is C |
| Design implication (บันทึกช่องทาง รุ่น รอบการปรับปรุง; ขอบเขตน้ำท่วมอาจใช้ประกอบบันทึก DDPM) | Consultant inference (hedged "อาจ") | C |

### กรมป้องกันและบรรเทาสาธารณภัย (DDPM)

| Claim | Source | Status |
|---|---|---|
| ผู้ผลิตข้อมูลปฐมภูมิ; พอร์ทัลและคลังข้อมูลเชิงปฏิบัติการ | Interim §2.2, §2.3 | S |
| สายการรายงาน อปท. → อำเภอ → จังหวัด → ส่วนกลาง | Interim §2.3; INT-11 topic | S |
| หน่วยที่สัมภาษณ์และวันที่ 23 ก.พ. 2569 | INT-11 | S |
| 15 ชุด ทุกชุด Restricted | CSV `owner_org`=DDPM, `access_rights_dataset` | S |
| ข้อมูลเหตุการณ์ย้อนหลัง 10 ปี; ความเสียหายทรัพย์สิน (ถนน ปศุสัตว์ วัด) ระดับหมู่บ้าน ตามเหตุการณ์ | CSV DDPM_2_1, DDPM_2_3 (`spatial_resolution`=Mooban, `temporal_resolution`=ตามเหตุการณ์, `data_source`=interview) | S |
| ความเสียหายผูกกับการเบิกจ่ายเยียวยา | CSV DDPM_2_3 notes; INT-11 topic | S |
| เริ่มนำเครื่องมือรายงานผ่านระบบภูมิสารสนเทศมาใช้ | CSV DDPM_2_1 notes "เริ่ม rollout เครื่องมือ GIS reporting" | S |
| แผนที่ความเสี่ยงอุทกภัย 2016–2025 | CSV DDPM_1_1 | S |
| ประเมินความเสี่ยง 17 จังหวัดภาคเหนือ ระดับตำบล ดัชนี 10–20 ตัวชี้วัด | CSV DDPM_2_2 | S. The catalog's procurement status and expected Sep 2569 completion were **removed** per Boss (no status information) |
| ตัวชี้วัดระดับจังหวัด 11 รายการ เป็นข้อมูลนำเข้าของฐานข้อมูลความเสี่ยงกรม สส. ที่มาเบื้องต้น | CSV DDPM_3_1 … DDPM_3_11, `data_source`=risk-database project report, notes "อาจมาจาก" | S |
| ข้อมูลไหลทางเดียว; ส่วนกลางตรวจสอบภาคสนามไม่ได้; ขาดการจำแนกตาม UNDRR | CSV DDPM_2_1 `use_limitations` | S |
| อปท. บันทึกล่าช้า/ไม่ตรงประเภท | CSV DDPM_2_3 `use_limitations` | S |
| ข้อมูลตามเหตุการณ์มีคุณค่าต่อการประเมินหลังเหตุการณ์ แต่ล่าช้า คลาดเคลื่อน เปลี่ยนเมื่อตรวจย้อนหลัง | Interim §2.4 | S |
| บันทึกระบุผู้ได้รับผลกระทบและเงินเยียวยา ไม่มีมูลค่าเป็นตัวเงิน/จำแนกสาขาจังหวัด; ค่าศูนย์กำกวม; ข้อมูลระดับครัวเรือน | WP7 §5 Service 4 | S |
| Design implication (แหล่งอ้างอิงเหตุการณ์ + ข้อมูลอภิพันธ์; มูลค่าความสูญเสียต้องใช้ระเบียบวิธีเพิ่ม) | Consultant inference from the above + WP7 Service 4 | C |

Style-pack note: the DDPM paragraph frames the records by operational scope (event and relief reporting), not as a general failing, per STYLE_PACK §7 on institutional criticism.

### สำนักงานสถิติแห่งชาติ (NSO)

| Claim | Source | Status |
|---|---|---|
| ผลิตข้อมูลจากสำมะโนและสำรวจ รอบเวลาต่างกัน | Interim §2.3 | S |
| พัฒนาศูนย์ข้อมูลสถิติทรัพยากรธรรมชาติและสิ่งแวดล้อม; จัดกลุ่ม/แท็กตามกรอบสถิติสิ่งแวดล้อม | Interim §2.2, §2.3; INT-06 (FDES) | S |
| หน่วยที่สัมภาษณ์และวันที่ 23 ก.พ. 2569 | INT-06 | S |
| 14 ชุด; 6 Public ผ่านระบบคลังข้อมูลสถิติ | CSV NSO_1_1 … NSO_1_6 (`data_source` "Website ระบบคลังข้อมูลสถิติ", url nsodw.nso.go.th) | S |
| สำมะโนประชากรฯ ทุก 10 ปี นับผู้อยู่อาศัยจริง | CSV NSO_1_2 notes and `use_limitations` ("ทุก 10 ปี") | S |
| สำมะโนเกษตร ระดับตำบล | CSV NSO_1_3 | S |
| สำมะโนอุตสาหกรรม ข้อมูลการเงินถึงระดับจังหวัด | CSV NSO_1_4 `use_limitations` | S |
| LFS รายเดือน; SES รายปี ระดับจังหวัด ใช้คำถามทดแทน (เชื้อเพลิงแข็ง) | CSV NSO_1_5, NSO_1_6 | S. LFS `spatial_resolution` is Unknown, `geo_coverage` จังหวัด |
| 8 ชุด Restricted: Common Frame ระดับตำบล รวม >10 หน่วยงาน; FDES 6/21 รอ ครม.; ตัวชี้วัดประชากร 6 รายการเป็นข้อมูลนำเข้า | CSV NSO_1_8, NSO_1_7, NSO_2_1 … NSO_2_6 | S |
| วินัยทางสถิติเหมาะกับค่าฐานระดับประเทศ | Interim §2.3 (วิธีการได้มาของข้อมูล รูปแบบแรก) | S |
| ข้อจำกัดด้านขนาดตัวอย่างและความถี่ | INT-06 topic | S |
| สำรวจที่เผยแพร่ระดับจังหวัดอาจไม่พอ; สำรวจ/สำมะโนอาจไม่ทันสถานการณ์ | Interim §2.4 | S |
| Design implication (ค่าฐานการเผชิญภัย/ความเปราะบาง; FDES เป็นจุดอ้างอิงจัดหมวด) | Consultant inference (hedged "อาจ") | C |

### สำนักงานพัฒนารัฐบาลดิจิทัล (DGA)

| Claim | Source | Status |
|---|---|---|
| โครงสร้างพื้นฐานจัดเก็บ เชื่อมโยง เผยแพร่; พอร์ทัลข้อมูลเปิด; ระบบแลกเปลี่ยนข้อมูล; สนับสนุน metadata/data catalog | Interim §2.2, §2.3 | S |
| หน่วยที่สัมภาษณ์ (ผอ. และทีม Open Data / GDX) วันที่ 4 มี.ค. 2569; หัวข้อ catalog, GDX, ธรรมาภิบาล, การจัดชั้นเปิด/แลกเปลี่ยน/ภายใน | INT-01 | S |
| "ระบบแลกเปลี่ยนข้อมูลภาครัฐ (GDX)" pairs the interim report's description with the interview's acronym | Interim §2.2 + INT-01 | P (pairing is inferential) |
| บัญชีรายการไม่มีชุดข้อมูลที่ DGA เป็นเจ้าของ | CSV: no `owner_org`=DGA; no row mentions DGA/GDX | S |
| บทบาทผู้กำหนดกติกา การจัดหมวดหมู่ เส้นทางการเข้าถึง มากกว่าผู้ผลิตข้อมูลภูมิอากาศ | Interim §2.3 | S |
| การเชื่อมผ่านพอร์ทัลหรือ API ขึ้นกับกติกาการแลกเปลี่ยนและคุณภาพ metadata | Interim §2.3 (วิธีการได้มา รูปแบบที่สี่) | S |
| Design implication (ใช้เป็นกลไกเชื่อมโยง; การจัดชั้นสามระดับอาจเป็นฐานการจัดชั้นเผยแพร่) | Consultant inference (hedged "อาจ") | C |

### กรมส่งเสริมการปกครองท้องถิ่น (DLA)

| Claim | Source | Status |
|---|---|---|
| ระบบข้อมูลและระบบประเมินผลสนับสนุน อปท. | Interim §2.2 | S |
| หน่วยที่สัมภาษณ์ (กองสิ่งแวดล้อม; กองป้องกันฯ) วันที่ 20 ก.พ. 2569; หัวข้อระบบข้อมูลขยะ การประเมินผลท้องถิ่น บทบาท สถ.จังหวัด ความต้องการข้อมูลภัยระดับเทศบาล/ตำบล | INT-02 | S |
| อาศัยรอบการรายงานและการประเมินผลประจำปี | Not found in interim ch.2, INT-02 or the catalog. Interim §2.4 names annual reporting only for NSO "หรือหน่วยงานด้านเศรษฐกิจและสังคม" | **U** — kept per Boss, marked `[ต้องตรวจแหล่ง]` (DLA block and cross-agency paragraph) |
| บัญชีรายการไม่มีชุดข้อมูลที่ DLA เป็นเจ้าของ | CSV: no `owner_org`=DLA. The only mention is PWA_2_4 notes, as a possible co-source | S |
| ข้อมูลท้องถิ่นในบัญชีรายการมาจากสายการรายงานของ DDPM | CSV DDPM_2_1, DDPM_2_3 (LAO-reported) | S |
| อปท. สองบทบาท: ต้นทางข้อมูล และผู้ใช้เพื่อแผน/คำของบประมาณ | Interim §2.3 (reporting chain), §2.6 กลุ่มที่สอง | S |
| ข้อมูลระดับจังหวัดมักไม่พอสำหรับท้องถิ่น; ต้องการชุดสรุปอธิบายว่าพื้นที่ใดเสี่ยงอย่างไร ควรลงทุนก่อน | Interim §2.5 กลุ่มที่สี่, §2.6 กลุ่มที่สอง | S |
| Design implication (สองทิศทาง) | Consultant inference | C |

### กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์ (MSDHS)

| Claim | Source | Status |
|---|---|---|
| ข้อมูลกลุ่มเปราะบางจากระบบสวัสดิการ การสำรวจภาคสนาม ทะเบียนเชื่อมโยง | Interim §2.3 | S |
| กำลังพัฒนาแดชบอร์ดเชิงพื้นที่ | Interim §2.2 | S |
| หน่วยที่สัมภาษณ์และวันที่ 17 ก.พ. 2569 | INT-04 | S |
| 5 ชุด ทุกชุด Restricted | CSV `owner_org`=MSDHS | S |
| ทะเบียนระดับตำบล เชื่อมผ่านเลข 13 หลักของ มท. | CSV MSDHS_1_1 (`geo_coverage` ตำบล, notes) | S |
| ครู ก.: 43,000 คน (2568); 200 คน/จังหวัด (2569) | CSV MSDHS_1_2 notes | S |
| แผนที่ทับซ้อนกับธนาคารโลกและจุฬาฯ; 3 จังหวัดนำร่อง เชียงใหม่ นครราชสีมา ปัตตานี; 2024–2025 | CSV MSDHS_1_3 (title lists Chiang Mai, Korat, Pattani; notes "จุฬาฯ Demography") | S. Korat rendered as นครราชสีมา |
| ตัวชี้วัด 2 รายการ (ชุมชนแออัด, ผู้พิการ) เป็นข้อมูลนำเข้า | CSV MSDHS_2_1, MSDHS_2_2 | S |
| ขาด metadata/data dictionary; ขาดทีมข้อมูล/IT | CSV MSDHS_1_1 `use_limitations` | S |
| ต้องคำนึงการคุ้มครองข้อมูลส่วนบุคคลและการใช้ในภาวะวิกฤติ | v1; interim §2.4 (sensitive/personal data) | S |
| ต้องการข้อมูลกลุ่มย่อยระดับเทศบาล/ชุมชน; ระบุกลุ่มเปราะบางอยู่ที่ใด ภัยใด | Interim §2.4, §2.6 กลุ่มที่สาม | S |
| PDPA บางครั้งตีความว่าห้ามเปิดทั้งชุด ทั้งที่การรวมข้อมูลอาจแก้ได้ | WP7 Gap 4. General statement, not MSDHS-specific; the text phrases it generally | S |
| Design implication (แยกชั้นรายบุคคล/รวมระดับพื้นที่) | Consultant inference | C |

### สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติ (NESDC)

| Claim | Source | Status |
|---|---|---|
| ผู้ใช้เชิงนโยบาย ใช้ข้อมูลเศรษฐกิจและผลกระทบประเมินเศรษฐกิจมหภาค | Interim §2.3 | S |
| เป็นเจ้าของกรอบและโครงการประเมิน loss and damage | Interim §2.2 (project exists) | S |
| หน่วยที่สัมภาษณ์และวันที่ 2 มี.ค. 2569; หัวข้อ | INT-05 | S |
| 14 ชุด ทุกชุด Restricted | CSV `owner_org`=NESDC | S |
| ประเมินความเสี่ยงโครงการลงทุนโครงสร้างพื้นฐาน; ใช้กับโครงการกู้เงินขนาดใหญ่ เช่น เจ้าพระยา; อัตราคิดลด 7% เพราะขาดแบบจำลอง | CSV NESDC_1_1 notes and `use_limitations` | S |
| 13 ตัวชี้วัดเศรษฐกิจสังคมระดับจังหวัด เป็นข้อมูลนำเข้า (MPI, Gini, HDI, GPP ต่อหัว, ประชากรรวมแฝง) | CSV NESDC_2_1 … NESDC_2_13 | S |
| มอบหมายสถาบันการศึกษาพัฒนาระเบียบวิธี L&D ตามแนวปฏิบัติสากล เริ่มภาคเกษตร | WP7 Gap 10, §5 Service 4. WP7's "running through mid-2026" end date was **removed** per Boss | S |
| ในช่วงที่จัดทำรายงานฉบับกลาง โครงการยังอยู่ในช่วงพัฒนา | Interim §2.2 ("อยู่ในกระบวนการพัฒนา") | S |
| ปัจจุบันโครงการปิดลงแล้ว; คณะที่ปรึกษานำกรอบมาใช้ใน (ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ (MVD) | Boss decision 2026-09-29. Adjacent support: the LDM archive (`output/09_LDM_LossDamage_DataModel/archive/extracts/2026-06-25_DDPM-context-extraction_for_TOR_5.3.6.md` and others) records NESDC input to the draft MVD design | **B** |
| WP7's "strong candidate for official calculation manual, not confirmed" | Superseded by Boss's statement; removed from the text | — |
| Design implication (MVD gives a link between DDPM records and economic valuation; NESDC indicators need provenance metadata) | Consultant inference | C |
| Table 3 and cross-agency wording ("นำมาใช้ใน (ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ", "ผลผลิตของโครงการที่ปิดลงแล้ว") | Boss decision | **B** |

### Cross-agency synthesis and gap list

| Claim | Source | Status |
|---|---|---|
| DDPM บันทึกตามเหตุการณ์ | Interim §2.4 | S |
| ข้อมูลสถิติ NSO ปรับปรุงตามรอบสถิติ | Interim §2.4 | S |
| TMD forecasts hourly/daily, published as images; GISTDA cycles event/weekly/biweekly/annual, mostly open via services | Data catalog TMD_1_x, GISTDA_x | S |
| ชุดข้อมูลเปิดของ DGA ปรับปรุงตามรอบสถิติของแต่ละชุด | Carried from v1. No DGA-specific update-cycle evidence in the named sources. Sentence split so the marker sits on the DGA half only | **U** — marked `[ต้องตรวจแหล่ง]` |
| DLA รอบรายงานประจำปี | See DLA row above | **U** — marked `[ต้องตรวจแหล่ง]` |
| MSDHS คุ้มครองข้อมูลส่วนบุคคล/ภาวะวิกฤติ | As above | S |
| NESDC: ผลผลิตของโครงการที่ปิดลงแล้ว นำมาใช้ใน MVD | Boss decision | **B** |
| Gap 1 examples (ทะเบียนไม่มี metadata; การจำแนกภัยไม่มีแนวทางร่วม) | CSV MSDHS_1_1, DDPM_2_1 `use_limitations` | S |
| Gap 2 figures: 122 จังหวัด / 41 ท้องถิ่น / 36 กริด / 59 ไม่ระบุ (~1/4) | WP7 §3. The raw CSV shows Province 122, Grid 36, Unknown 59; local 41 = Point 21 + Tambon 9 + Local 6 + Mooban 5 | S |
| Gap 3 figure: ~ร้อยละ 17 เปิดเผย | WP7 §3; CSV Public 43/260 = 16.5% (3 rows have blank access) | S |
| Closing paragraphs (strategic role, design direction) | v1; interim §2.7 closing | S (the caveat "มิได้ประกาศว่า…บูรณาการสมบูรณ์" is kept, now as a trailing clause) |

## Figures deliberately not used

- **฿1.62 trillion cumulative L&D, 2006–2024** (WP7 §5 Service 4). Kept out, per Boss (2026-09-29).
- **Status and completion dates** for DDPM's northern assessment (catalog: procurement, due Sep 2569) and NESDC's method work (WP7: to mid-2026). Removed per Boss.
- **National adaptation monitoring platform** (18 agencies, six sectors, manual entry; WP7 §5 Service 7). WP7 does not name its owner, so it is not attributed to DCCE here.
- **The 5.3.8 "ร้อยละ 20 / 80" readiness split.** Superseded, as in v1.

## Downstream registration

Candidate inputs for the full-report references chapter and for `E-xxx` evidence-registry rows via `/seal`. Not registered in `CRDB-Evidence-Registry.md`.
