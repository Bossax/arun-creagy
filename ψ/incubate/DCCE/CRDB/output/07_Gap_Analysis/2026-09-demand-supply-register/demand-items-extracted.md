# WP2 §5.1 Gap Analysis — Phase A: Demand Item Extraction

Source: `ψ/incubate/DCCE/CRDB/output/archive/consultation_workshop/user_use_case_raw.md` (83 use cases, 5 groups).
Scope: extraction and TOR 5.3.5 risk-component tagging only. No matching against the data catalog or product inventory has been done in this pass — that is a later step.

Every `risk_component` assignment below is this analyst's best-guess reading of the item text, not a value carried over from any catalog metadata. Items whose category assignment is genuinely uncertain are marked in the `flags` column; two-category items list both components joined by `/`.

## Summary counts (risk_component × item_type)

| risk_component | dataset | product | total |
|---|---|---|---|
| Climatic Driver | 6 | 1 | 7 |
| Hazard | 29 | 9 | 38 |
| Exposure | 12 | 4 | 16 |
| Sensitivity | 10 | 7 | 17 |
| Adaptive Capacity | 3 | 6 | 9 |
| Impact | 8 | 8 | 16 |
| Response | 7 | 118 | 125 |
| Loss and Damage | 5 | 5 | 10 |
| **Total** | **80** | **158** | **238** |

Two items are dual-tagged across categories (counted once above under their primary tag, flagged individually in the tables): D109 (Hazard/Sensitivity, กลุ่มที่ 3) and D141 (Sensitivity/Adaptive Capacity, กลุ่มที่ 4).

**Why "Response" dominates (125/238, all but 7 of them "product"):** the raw use-case set over-represents Group 5 (การตีความข้อมูลและพัฒนาระบบข้อมูล — data-system/governance interpretation), which is 32 of the 83 use cases (39%) and is almost entirely composed of catalog/portal/metadata/API/governance asks (e.g. D148–D238) rather than physical-risk data. These are legitimate WP2 demand items — DCCE agencies explicitly asked for them — but they describe *how information should be organized and delivered*, not *which of the 8 risk-chain components the underlying data measures*. Tagging them "Response" (the TOR category closest to "institutional/informational capacity to act") is a coarse fit, not a strong match; treat the Response bucket as a mixed bag requiring its own sub-typology in a later pass rather than as a peer of the other 7 categories. This is flagged as a structural ambiguity, not resolved here.

## Notes: Sensitivity vs Adaptive Capacity split (flag for later matching)

The TOR 5.3.5 gap-analysis scheme separates **Sensitivity** (who/what is inherently susceptible to harm) from **Adaptive Capacity** (the resources/institutions available to cope or adapt), but the existing 260-dataset catalog (`data_catalog_v4.csv`, `cdm_sub_domain` field) only tags a single merged "Vulnerability" category (72 datasets). This means every item below tagged Sensitivity or Adaptive Capacity will, in the next matching step, be checked against the *same* 72-dataset "Vulnerability" pool — the catalog cannot currently distinguish which of those 72 actually cover Sensitivity content versus Adaptive Capacity content. Items flagged below as touching this boundary:

- **D048, D051** (MSDHS welfare-registry/individual vulnerable-population data) — squarely Sensitivity (who is exposed and inherently susceptible), but the phrase "ฐานข้อมูลกลุ่มเปราะบาง" ("vulnerable-group database") is exactly the kind of item that gets filed under the catalog's merged "Vulnerability" tag without distinguishing this from capacity data.
- **D055, D056, D058** (DDPM's "ชุดดัชนีความเปราะบางมาตรฐาน" — standard vulnerability index set) — the use case's own wording is "vulnerability index," which in DDPM's usage appears to bundle sensitivity and capacity dimensions together; cannot cleanly split without seeing the actual 10–20 indicators.
- **D094, D095** (NSO Common Frame → Human Settlement vulnerability mapping) — Sensitivity as stated, but same merged-tag risk.
- **D132, D133** (UDDC "double vulnerability" overlay) — Sensitivity as stated (socioeconomic susceptibility), explicitly UDDC's own vulnerability framing.
- **D134, D135, D136** (MSDHS hazard×subgroup granular impact data, gender/equality data) — Sensitivity (who is disproportionately susceptible by subgroup), not Adaptive Capacity.
- **D141 (dual-tagged)** — NSO's Agricultural Census indicators (household debt, debt repayment status, asset ownership, land tenure: owner vs. renter) is the clearest case of genuine ambiguity in this whole set: debt/asset-ownership data is arguably a direct measure of *coping resources* (Adaptive Capacity), not just inherent susceptibility (Sensitivity). Quote: "หนี้ครัวเรือน สถานะการชำระหนี้ ความเป็นเจ้าของสินทรัพย์เกษตร ... สถานะการถือครองที่ดิน" (Interview Summary - NSO.md:93). Flagged as genuinely ambiguous rather than force-resolved.
- **D144, D146** (NXPO Institutional Resilience Index) — Adaptive Capacity as stated (explicitly an institutional-capacity index), the cleanest non-ambiguous Adaptive Capacity item in the set.
- **D168–D170** (NESDC Milestone 11 "ภูมิคุ้มกันของสังคมต่อการเปลี่ยนแปลงสภาพภูมิอากาศ" — societal immunity/resilience) — tagged Adaptive Capacity on the reading that "ภูมิคุ้มกัน" (immunity/resilience) is a capacity concept, but the NESDC use case does not define the indicator set, so this is a judgment call, not a directly quoted category label.

Recommendation for the next phase: when matching demand to supply, treat every Sensitivity/Adaptive-Capacity-tagged demand item as matched only against the catalog's 72-dataset "Vulnerability" pool as a *whole*, and flag in the gap report that the catalog's own taxonomy cannot currently confirm whether the Adaptive-Capacity side of demand is actually covered — this is a supply-side taxonomy gap, not just a matching exercise.

---

## กลุ่มที่ 1: เศรษฐศาสตร์และการเงิน (15 use cases, 39 items)

| item_id | item_text_th | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| D001 | แผนที่น้ำท่วมแบบความน่าจะเป็นระดับตำแหน่ง/สินทรัพย์ (ระบุชนิดน้ำท่วม pluvial/riverine/coastal) | dataset | Hazard | TBA / Commercial Banks | TBA.md:48 | |
| D002 | เมตริกความลึกและระยะเวลาน้ำท่วม (depth/duration) | dataset | Hazard | TBA / Commercial Banks | TBA.md:26 | |
| D003 | damage functions ที่ใช้ได้กับการประเมินเชิงการเงินระดับสินทรัพย์ | product | Impact | TBA / Commercial Banks | TBA.md:28 | |
| D004 | ข้อมูล/กรอบสำหรับเชื่อม "ความเสี่ยงกายภาพ → ผลกระทบลูกโซ่/ซัพพลายเชน" | product | Impact | TBA / Commercial Banks | TBA.md:33 | |
| D005 | ข้อมูล/แผนที่น้ำท่วมระดับตำแหน่งที่ให้ความน่าจะเป็นของการเกิดน้ำท่วม ณ จุด (probability at specific locations) | dataset | Hazard | TBA / Commercial Banks | TBA.md:17 | |
| D006 | แผนที่/ข้อมูลติดตามน้ำท่วมหลายรูปแบบ (pluvial/riverine/coastal) | dataset | Hazard | TBA / Commercial Banks | TBA.md:26 | |
| D007 | สเปกความละเอียด/การใช้งานที่ชัดเจนเพื่อหลีกเลี่ยงการสรุปแบบระดับจังหวัด | product | Hazard | TBA / Commercial Banks | TBA.md:26 | vague — this is a metadata/spec requirement, not a dataset itself |
| D008 | เส้นทาง LT-LEDS เชิงตัวเลขที่แตกย่อยถึงระดับ sub-sector | dataset | Climatic Driver | TBA / Commercial Banks | TBA.md:35 | ambiguous — LT-LEDS is a mitigation/transition-pathway scenario, not a physical climate driver in the TOR 5.3.5 sense; nearest fit is Climatic Driver as scenario input, but arguably sits outside the 8-category scheme entirely (transition risk, not physical risk) |
| D009 | ตาราง mapping ISIC → กิจการ/การดำเนินงานจริงในประเทศ (domestic operations) | product | Exposure | TBA / Commercial Banks | TBA.md:35 | borderline — this is a sector-classification reference table, not exposure data per se |
| D010 | แนวทางการใช้งานสำหรับการจัดกลุ่มพอร์ตและการประเมินความเสี่ยง | product | Response | TBA / Commercial Banks | TBA.md:35 | |
| D011 | ระบบ/กรอบวิธีการมาตรฐานสำหรับคำนวณ Loss and Damage ทางเศรษฐกิจ | product | Loss and Damage | NESDC | NESDC.md:45 | |
| D012 | ชุดข้อมูลความสูญเสียจากภัยพิบัติที่มากกว่า "ยอดเงินชดเชย" (ความเสียหายโดยตรง + ความสูญเสียทางอ้อม/การหยุดชะงักทางธุรกิจ/ต้นทุนโอกาส + ผลกระทบลูกโซ่ด้านโลจิสติกส์) | dataset | Loss and Damage | NESDC | NESDC.md:56 | |
| D013 | ข้อมูลผลกระทบน้ำท่วมระดับเหตุการณ์ (event-level) สำหรับพื้นที่เศรษฐกิจสำคัญ | dataset | Impact | NESDC | NESDC.md:58 | |
| D014 | ค่าประมาณความเสียหายสินทรัพย์โดยตรง | dataset | Loss and Damage | NESDC | NESDC.md:58 | |
| D015 | ค่าประมาณความสูญเสียจากการหยุดชะงักทางธุรกิจ/ต้นทุนโอกาส | dataset | Loss and Damage | NESDC | NESDC.md:58 | |
| D016 | สมมติฐาน/การเชื่อมโยงตัวแปรที่นำไปใช้ในแบบจำลองเศรษฐกิจมหภาคได้ | product | Loss and Damage | NESDC | NESDC.md:58 | borderline — this is a methodology/parameter set, not itself a loss figure |
| D017 | ข้อมูลฐานจากกระทรวงเกษตรฯ (ผลผลิตพืชผล การใช้น้ำ) | dataset | Sensitivity | NESDC | NESDC.md:36 | ambiguous — could equally be read as Exposure (agricultural assets) depending on downstream use |
| D018 | ข้อมูลฐานจากกระทรวงทรัพยากรธรรมชาติฯ (ระดับน้ำในอ่างเก็บน้ำ) | dataset | Hazard | NESDC | NESDC.md:36 | reservoir level as a drought-hazard indicator |
| D019 | ข้อมูล/ตัวแปรความเสี่ยงสภาพภูมิอากาศที่นำไปใช้ในการประเมินเศรษฐศาสตร์โครงการโครงสร้างพื้นฐานได้ | dataset | Impact | NESDC | NESDC.md:29 | vague — "climate risk variable" as stated could be Hazard or Impact |
| D020 | สมมติฐาน/พารามิเตอร์สำหรับการคิดลด (รวมความเสี่ยงโรคระบาดและความไม่แน่นอนในอนาคต) | product | Response | NESDC | NESDC.md:29 | this is an economic-appraisal discount-rate parameter, not a physical risk-chain category — flagged as poor fit for any of the 8 |
| D021 | ตาราง proxy value/ต้นทุนมาตรฐานรายประเภทสินทรัพย์ (เช่น ถนน อาคาร ปศุสัตว์) | dataset | Loss and Damage | DDPM | DDPM.md:56 | |
| D022 | ข้อมูลความเสียหายเชิงกายภาพรายเหตุการณ์/รายพื้นที่ | dataset | Impact | DDPM | DDPM.md:56 | |
| D023 | แนวทางคำนวณที่ระบุข้อจำกัดของการประเมิน (โดยเฉพาะความสูญเสียทางอ้อม) | product | Loss and Damage | DDPM | DDPM.md:56 | |
| D024 | กลไกเชื่อมโยง/แลกเปลี่ยนข้อมูลข้ามหน่วยงาน (multi-agency data) | product | Response | DDPM | DDPM.md:56 | |
| D025 | ชุดข้อมูลเศรษฐกิจ/ภาคส่วนที่ใช้ประเมินความสูญเสียทางอ้อม | dataset | Loss and Damage | DDPM | DDPM.md:56 | |
| D026 | ระเบียบวิธีคำนวณที่รองรับ indirect loss | product | Loss and Damage | DDPM | DDPM.md:56 | |
| D027 | ชั้นข้อมูล/ตัวชี้วัดความเสี่ยงเชิงพื้นที่ระดับเทศบาล/ตำบล | dataset | Hazard | DLA | DLA.md:52 | vague — "composite risk indicator" as stated could span multiple components |
| D028 | กลไกเชื่อมโยงความเสี่ยง→รายการโครงการ/กิจกรรม→งบประมาณ | product | Response | DLA | DLA.md:52 | |
| D029 | ตัวอย่างแม่แบบ/แนวทางการเขียนคำชี้แจงงบประมาณที่อ้างอิงข้อมูลความเสี่ยง | product | Response | DLA | DLA.md:68 | |
| D030 | ตัวชี้วัด/เครื่องมือคำนวณต้นทุน-ประโยชน์/ROI ของมาตรการ (ลดความเสี่ยง/ลด GHG) | product | Response | DLA | DLA.md:57 | |
| D031 | ข้อมูลฐานความเสียหาย/ความเสี่ยง (baseline) และผลลัพธ์ที่คาดว่าจะลดลง | dataset | Impact | DLA | DLA.md:57 | |
| D032 | แบบฟอร์มสรุปผลที่ "เข้าใจง่าย" สำหรับประกอบการอนุมัติงบ | product | Response | DLA | DLA.md:59 | |
| D033 | ข้อมูล/ผลการประเมินการปล่อยคาร์บอนของ SMEs (Scope 1 และ 2) ก่อนและหลังได้รับเงินกู้ | dataset | Response | FTI | FTI.md:18 | GHG-emissions data is mitigation-side, not physical-risk data — genuinely outside the 8 TOR categories; tagged Response only as nearest institutional-process fit |
| D034 | วิธีการ/มาตรฐานการคำนวณที่ยอมรับร่วมกันสำหรับการเปรียบเทียบก่อน–หลัง | product | Response | FTI | FTI.md:18 | same caveat as D033 |
| D035 | คู่มือ/Manual และตัวอย่างวิธีคำนวณที่ชัดเจนสำหรับการประเมินผลกระทบทางการเงินจากภัยสภาพภูมิอากาศ (เช่น business interruption costs) | product | Impact | FTI | FTI.md:52 | |
| D036 | ผลคาดการณ์คลื่นความร้อนระดับ 10 ตารางกม. | dataset | Hazard | FTI | FTI.md:63 | |
| D037 | วิธี/โมเดลการแปลงผลคาดการณ์เป็นต้นทุนการหยุดชะงักทางธุรกิจและการสูญเสียผลิตภาพแรงงาน | product | Impact | FTI | FTI.md:63 | |
| D038 | ข้อมูลบัญชีการท่องเที่ยว (tourism accounts) | dataset | Exposure | NSO | NSO.md:110 | ambiguous — could be read as Sensitivity (economic dependency on the tourism sector) |
| D039 | วิธี/กรอบการนำข้อมูลบัญชีการท่องเที่ยวไปใช้ในแบบจำลองความสูญเสียทางเศรษฐกิจ/ความเปราะบางทางเศรษฐกิจ | product | Loss and Damage | NSO | NSO.md:110 | use case's own wording names both "loss" and "economic vulnerability" — dual relevance to L&D and Sensitivity |

---

## กลุ่มที่ 2: วางแผนและนโยบายเชิงพื้นที่ (22 use cases, 68 items)

| item_id | item_text_th | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| D040 | ผลการ downscale ฉากทัศน์สภาพภูมิอากาศระดับเมือง (SSP3/SSP5) | dataset | Climatic Driver | UDDC | UDDC.md:20 | |
| D041 | DEM ความละเอียด 1 เมตร | dataset | Exposure | UDDC | UDDC.md:31 | ambiguous — terrain data underpins both hazard modeling and exposure mapping |
| D042 | แบบจำลอง/แผนที่น้ำท่วมในอนาคต (future flood inundation maps) | product | Hazard | UDDC | UDDC.md:33 | |
| D043 | ข้อมูลภาพถ่ายโดรนความละเอียด ~20 ซม. | dataset | Exposure | UDDC | UDDC.md:35 | |
| D044 | DSM/DTM ที่ระบุรายละเอียดพื้นที่ (เช่น canopy/ชั้นความหลากหลายทางชีวภาพ) | dataset | Exposure | UDDC | UDDC.md:37 | |
| D045 | อินพุต/พารามิเตอร์และผลลัพธ์จากแบบจำลอง Urban InVest เพื่อประเมิน retention/drainage | product | Adaptive Capacity | UDDC | UDDC.md:63 | borderline — ecosystem-service buffering capacity read as Adaptive Capacity; could also be argued as Response (intervention design output) |
| D046 | ชั้นข้อมูลเชิงพื้นที่ที่เชื่อมจากแบบจำลองไปสู่งานออกแบบ/วางแผน NbS ได้ | product | Response | UDDC | UDDC.md:63 | |
| D047 | แผนที่ภัย/ชั้นข้อมูลภัยที่ใช้งานได้ (เช่น floods, droughts, heatwaves, landslides, PM2.5) | dataset | Hazard | MSDHS | MSDHS.md:22 | |
| D048 | ฐานข้อมูลกลุ่มเปราะบางของ MSDHS (welfare registries/field surveys) ที่เชื่อมโยงเชิงพื้นที่ได้ | dataset | Sensitivity | MSDHS | MSDHS.md:23, MSDHS.md:25 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D049 | การสรุปผลระดับตำบลและเทศบาล (map/dashboard) เพื่อใช้งานเชิงแผนและการสื่อสารกับท้องถิ่น | product | Response | MSDHS | MSDHS.md:32 | |
| D050 | แผนที่/ชั้นข้อมูลความเสี่ยงน้ำท่วมระดับเทศบาล | dataset | Hazard | MSDHS | MSDHS.md:32 | |
| D051 | ข้อมูลกลุ่มเป้าหมาย/กลุ่มเปราะบางที่จำแนกตามประเภท (เช่น pregnant women, bedridden patients) | dataset | Sensitivity | MSDHS | MSDHS.md:32 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D052 | ผลการจับคู่พื้นที่เสี่ยง–กลุ่มเป้าหมาย–หน่วยงานท้องถิ่น (table/map/dashboard) ที่ใช้ประกอบการจัดสรรงบ | product | Response | MSDHS | MSDHS.md:53 | |
| D053 | ผลคาดการณ์/ฉากทัศน์ความเหมาะสมต่อการอยู่อาศัยช่วง 2–5 ปี (habitability forecasts) ระบุพื้นที่เสี่ยง "permanently flooded" หรือความเสี่ยงหลักอื่นๆ | product | Hazard | MSDHS | MSDHS.md:44 | forward-looking hazard projection with an implicit exposure/habitability judgment folded in |
| D054 | การสรุปผลระดับพื้นที่เพื่อใช้กำหนดแผนย้ายถิ่นและแผนฝึกอาชีพใหม่ | product | Response | MSDHS | MSDHS.md:51 | |
| D055 | ชุดดัชนีความเปราะบางมาตรฐาน (10–20 ดัชนี) | product | Sensitivity | DDPM | DDPM.md:23 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D056 | ข้อมูล/ตัวแปรนำเข้าที่ใช้คำนวณดัชนี | dataset | Sensitivity | DDPM | DDPM.md:23 | |
| D057 | คู่มือการเลือกใช้ดัชนีให้เหมาะกับบริบทพื้นที่ | product | Response | DDPM | DDPM.md:28 | |
| D058 | ผลลัพธ์เชิงพื้นที่ (เช่น คะแนน/ชั้นความเสี่ยงรายพื้นที่) | product | Sensitivity | DDPM | DDPM.md:28 | |
| D059 | ฐานข้อมูลเหตุการณ์ย้อนหลังที่มีพิกัด/ตำแหน่งเพียงพอสำหรับทำแผนที่ | dataset | Hazard | DDPM | DDPM.md:31 | |
| D060 | เครื่องมือทำแผนที่และการสรุปเชิงพื้นที่ | product | Response | DDPM | DDPM.md:31 | |
| D061 | แนวทางการเลือกช่วงเวลาย้อนหลัง (3–5 ปี) และข้อจำกัดของการใช้ข้อมูลอดีตแทนการคาดการณ์อนาคต | product | Hazard | DDPM | DDPM.md:31 | vague/methodological note |
| D062 | ชุดข้อมูล near real-time ของ BMA (ฝน/ระดับน้ำคลอง/สถานะการสูบ/เซนเซอร์น้ำท่วม) | dataset | Hazard | BMA | BMA.md:73 | |
| D063 | ชุดข้อมูลลุ่มน้ำต้นน้ำ (สภาพน้ำ/การระบาย/เงื่อนไขลุ่มน้ำ) | dataset | Hazard | BMA | BMA.md:73 | |
| D064 | ชุดข้อมูลน้ำขึ้นน้ำลง | dataset | Hazard | BMA | BMA.md:73 | |
| D065 | กลไกเชื่อมโยงข้อมูล/มาตรฐานแลกเปลี่ยน (เช่น API/metadata) | product | Response | BMA | BMA.md:73 | |
| D066 | ชุดข้อมูล/แผนที่คาดการณ์ความเสี่ยงภัย (เช่น น้ำท่วม ภัยแล้ง PM2.5) ระดับเทศบาล/ตำบล | dataset | Hazard | DLA | DLA.md:37 | |
| D067 | วิธีสรุปผลที่ "เข้าใจง่าย" (เช่น แผนที่/คะแนน/ชั้นความเสี่ยง) | product | Response | DLA | DLA.md:48 | |
| D068 | เมทาดาทาอธิบายสมมติฐาน/ข้อจำกัดของการคาดการณ์ | product | Response | DLA | DLA.md:49 | vague |
| D069 | รายการชุดข้อมูลภัย/ความเสี่ยงที่เป็นมาตรฐาน (catalog) พร้อมผู้ดูแลข้อมูล | product | Response | DLA | DLA.md:40 | infrastructure/catalog item, not a risk-component dataset itself |
| D070 | จุดเข้าถึงแบบรวมศูนย์ (single entry point) เพื่อค้นหา/ดาวน์โหลด/อ้างอิง | product | Response | DLA | DLA.md:55 | |
| D071 | เอกสารกำกับคุณภาพ/การแนะนำการเลือกใช้ข้อมูลตามประเภทภัยและบริบทพื้นที่ | product | Response | DLA | DLA.md:57 | |
| D072 | ข้อมูลคาดการณ์ปริมาณฝนที่ปรับตามสภาพภูมิอากาศ (พร้อมสมมติฐาน/ช่วงเวลา) | dataset | Climatic Driver | DPT | DPT.md:57 | |
| D073 | ข้อมูลอุทกวิทยาที่เกี่ยวข้องสำหรับงานระบายน้ำ | dataset | Hazard | DPT | DPT.md:63 | |
| D074 | แผนที่พื้นที่เสี่ยงน้ำท่วมที่ใช้เป็นฐานข้อมูลการวางผัง/ออกแบบ | dataset | Hazard | DPT | DPT.md:63 | |
| D075 | ข้อมูลเรขาคณิต/รายละเอียดโครงสร้างพื้นฐานระดับท้องถิ่น (เช่น ความสูงถนน รูปตัด/โครงข่ายระบายน้ำ ความหนาแน่นสถานี/จุดสำคัญ) | dataset | Exposure | DPT | DPT.md:75 | |
| D076 | ชั้นข้อมูล/แผนที่ภัยที่เกี่ยวข้อง (น้ำท่วม ภัยแล้ง กัดเซาะชายฝั่ง) ที่พร้อมใช้งานเชิงพื้นที่ | dataset | Hazard | DPT | DPT.md:43 | |
| D077 | ชั้นข้อมูลการใช้ประโยชน์ที่ดิน/การใช้ประโยชน์อาคาร | dataset | Exposure | DPT | DPT.md:45 | |
| D078 | ข้อมูลเศรษฐสังคมที่เชื่อมโยงเชิงพื้นที่ได้ | dataset | Sensitivity | DPT | DPT.md:49 | |
| D079 | รูปแบบข้อมูลเชิงพื้นที่ที่ "ดิจิทัลและอ้างอิงพิกัด" (GIS-ready) พร้อมเมทาดาทาเพื่อใช้ซ้ำในการวางแผน | product | Response | DPT | DPT.md:61, DPT.md:77 | data-format standard, not risk-component data |
| D080 | ข้อมูลความร้อนเมืองระดับละเอียดที่ใช้งานได้สำหรับผังเมืองต่ำกว่าระดับจังหวัด | dataset | Hazard | DPT | DPT.md:59 | |
| D081 | ตัวชี้วัด/แผนที่ความร้อนเชิงพื้นที่ | product | Hazard | DPT | DPT.md:59 | |
| D082 | เมทาดาทาอธิบายวิธีการ/ความละเอียด/ข้อจำกัด | product | Response | DPT | DPT.md:79 | vague |
| D083 | แผนที่ความเสี่ยงระดับ 10 ตารางกม. แบบ location-based และ sector-based | product | Hazard | FTI | FTI.md:52 | |
| D084 | ข้อมูลคาดการณ์น้ำต้นทุน/น้ำประปาหรืออุปทานน้ำระดับประเทศ | dataset | Hazard | FTI | FTI.md:28 | could also be read as Climatic Driver (water-supply projection) |
| D085 | ข้อมูลความต้องการใช้น้ำภาคอุตสาหกรรมย้อนหลังมากกว่า 10 ปี | dataset | Exposure | FTI | FTI.md:28 | |
| D086 | ผลการประเมินความเสี่ยงการขาดแคลนน้ำระยะ 20 ปี | product | Impact | FTI | FTI.md:28 | |
| D087 | ข้อมูลความต้องการใช้น้ำภาคอุตสาหกรรม | dataset | Exposure | FTI | FTI.md:61 | |
| D088 | ข้อมูลคาดการณ์อุปทานน้ำที่ปรับตามสภาพภูมิอากาศ | dataset | Hazard | FTI | FTI.md:61 | |
| D089 | ผลการซ้อนทับเพื่อประเมินความเสี่ยงการขาดแคลนน้ำระยะ 20 ปี (EEC) | product | Impact | FTI | FTI.md:61 | |
| D090 | คำอธิบาย/ตรรกะการแบ่งหน่วย EA และขอบเขตการใช้งาน | product | Exposure | NSO | NSO.md:63 | reference-geography definition, not risk data per se |
| D091 | ข้อมูล/ขอบเขตเชิงพื้นที่ของ EA ที่นำไปซ้อนทับในงานทำแผนที่ได้ | dataset | Exposure | NSO | NSO.md:106 | |
| D092 | แนวทางการเชื่อม EA กับชั้นข้อมูล exposure ของ risk map | product | Exposure | NSO | NSO.md:106 | |
| D093 | ฐานข้อมูล Common Frame (ระดับตำบล) | dataset | Exposure | NSO | NSO.md:49 | |
| D094 | การแม็ปตัวแปร/ดัชนีที่ใช้สะท้อนความเปราะบางด้าน Human Settlement | product | Sensitivity | NSO | NSO.md:108 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D095 | ผลสรุปเชิงพื้นที่ที่นำไปใช้ในงานประเมินความเสี่ยงได้ | product | Sensitivity | NSO | NSO.md:108 | |
| D096 | ชุดข้อมูล/ฐานข้อมูลระดับมหภาคที่ใช้สำหรับนโยบาย (macro-data) | dataset | Impact | NXPO | NXPO.md:40 | vague — "macro-data" is undefined in the source text |
| D097 | รายงาน/สรุปสาระจากแหล่งต่างประเทศ | product | Response | NXPO | NXPO.md:40 | not risk-component-specific |
| D098 | ชุดสรุป/รวบรวมข้อมูลจาก DCCE และรายงานที่ปรึกษาให้อยู่ในรูปแบบที่ใช้งานได้ในการออกแบบนโยบาย | product | Response | NXPO | NXPO.md:40 | |
| D099 | ชุดข้อมูล/ตัวแปรที่ผู้ใช้ปลายทางต้องใช้ในการตัดสินใจ (end-user decision data requirements) | dataset | Response | NXPO | NXPO.md:42 | this is a meta-requirement about data planning, not itself risk data |
| D100 | กรอบ/กระบวนการเชื่อม "ความต้องการผู้ใช้" กับการออกแบบแบบจำลอง/การเก็บข้อมูล | product | Response | NXPO | NXPO.md:42 | |
| D101 | สรุปช่องว่าง/รายการข้อมูลที่ถูกเก็บแต่ไม่ถูกใช้เพื่อปรับแผนการผลิตข้อมูล | product | Response | NXPO | NXPO.md:42 | |
| D102 | ชุดข้อมูล/ตัวชี้วัดความเสี่ยงและผลกระทบสำหรับ heatwaves, health crises (disease vectors), และ food degradation | dataset | Impact | NXPO | NXPO.md:44 | |
| D103 | สรุปความเชื่อมโยงผลกระทบลูกโซ่เพื่อใช้ประกอบนโยบาย (evidence package) | product | Impact | NXPO | NXPO.md:44 | |
| D104 | ข้อมูลน้ำย้อนหลัง 10 ปี | dataset | Hazard | OTP | OTP.md:18 | |
| D105 | จุดเสี่ยงใน GIS | dataset | Hazard | OTP | OTP.md:21 | |
| D106 | แบบจำลองปริมาณฝนช่วงกลับซ้ำ 50–100 ปี | dataset | Climatic Driver | OTP | OTP.md:54 | |
| D107 | แบบจำลองอุทกวิทยาความละเอียดสูงเพื่อทำแผนที่การไหลของภัย (hazard flows) ซ้อนทับบนเส้นทางคมนาคมถึงระดับจุดระบุสินทรัพย์/ตำแหน่งเฉพาะ (เช่น หลักกิโลเมตรทางหลวง, หมายเลขเสาไฟตามแนวรถไฟ) | product | Hazard | OTP | OTP.md:58 | |

---

## กลุ่มที่ 3: ปฏิบัติงานเชิงพื้นที่ (8 use cases, 23 items)

| item_id | item_text_th | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| D108 | แดชบอร์ดที่แปลงข้อมูลดิบเป็นภาพรวมเชิงพื้นที่ (โดย Technology Center เป็น data hub) | product | Response | MSDHS | MSDHS.md:25 | |
| D109 | ข้อมูล hazard + vulnerable populations ที่สรุประดับตำบลเพื่อสื่อสารและตัดสินใจภาคสนาม | dataset | Hazard / Sensitivity | MSDHS | MSDHS.md:27 | genuinely dual — the use case bundles hazard data and vulnerable-population data together as one requirement; not splittable from the source text as written |
| D110 | ข้อมูลกลุ่มเปราะบางระดับรายบุคคล/ครัวเรือน (เช่น ข้อมูลทะเบียนสวัสดิการ/สำรวจภาคสนาม) ที่สามารถแลกเปลี่ยนกับหน่วยงานท้องถิ่น/สาธารณสุขได้อย่างปลอดภัย | dataset | Sensitivity | MSDHS | MSDHS.md:27 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D111 | กลไกการแชร์ข้อมูลภายใต้ข้อกำกับ (เช่น สิทธิ์เข้าถึง/การบันทึกการใช้งาน) | product | Response | MSDHS | MSDHS.md:27 | |
| D112 | ข้อมูลเหตุการณ์และความเสียหายระดับหมู่บ้าน (10 ปี) | dataset | Impact | DDPM | DDPM.md:44 | |
| D113 | ตัวระบุพื้นที่มาตรฐาน (หมู่บ้าน/ตำบล/อำเภอ/จังหวัด) | product | Response | DDPM | DDPM.md:44 | reference geocoding standard, not risk data |
| D114 | เครื่องมือสรุป/รายงานสถานการณ์ตามพื้นที่ | product | Response | DDPM | DDPM.md:44 | |
| D115 | เครื่องมือรายงาน GIS | product | Response | DDPM | DDPM.md:44 | |
| D116 | มาตรฐานพิกัด/รูปแบบการบันทึกตำแหน่ง | product | Response | DDPM | DDPM.md:44 | |
| D117 | การฝึกอบรม/แนวทางใช้งานสำหรับผู้บันทึกข้อมูลระดับพื้นที่ | product | Response | DDPM | DDPM.md:44 | |
| D118 | ข้อมูลแจ้งเตือนจากหน่วยงานเทคนิคหลายหน่วยงาน | dataset | Hazard | DDPM | DDPM.md:33 | |
| D119 | กลไกการรวม/แสดงผลข้อมูลแบบ near real-time | product | Response | DDPM | DDPM.md:33 | |
| D120 | ช่องทางการเผยแพร่/แจ้งเตือนที่ใช้ได้จริงในภาคสนาม | product | Response | DDPM | DDPM.md:34 | |
| D121 | ขั้นตอน QC มาตรฐานสำหรับจังหวัด | product | Response | DDPM | DDPM.md:40 | |
| D122 | เกณฑ์/ตัวชี้วัดคุณภาพข้อมูล | product | Response | DDPM | DDPM.md:40 | |
| D123 | ระบบติดตามสถานะ/ความครบถ้วนของการรายงานตามสายงาน | product | Response | DDPM | DDPM.md:42 | |
| D124 | ข้อมูล heat index/ตัวชี้วัดความร้อนระดับเมืองและระดับพื้นที่ | dataset | Hazard | BMA | BMA.md:75 | |
| D125 | ฐานข้อมูลตำแหน่งและคุณลักษณะของ cooling points | dataset | Response | BMA | BMA.md:75 | adaptation-infrastructure inventory, tagged Response |
| D126 | ผลพยากรณ์ไมโครไคลเมต/ตัวแปรที่เกี่ยวข้องสำหรับการเตือนภัย/วางแผนระยะสั้น | dataset | Climatic Driver | BMA | BMA.md:75 | |
| D127 | เครื่องมือแผนที่/แดชบอร์ดเพื่อระบุกลุ่มเป้าหมายและติดตามการดำเนินการ | product | Response | BMA | BMA.md:75 | |
| D128 | ข้อมูลพื้นฐานจากสำมะโน/ฐานข้อมูลของ NSO (ประชากร เกษตร สถานประกอบการ) ที่ผูกเชิงพื้นที่ได้ | dataset | Exposure | NSO | NSO.md:59 | |
| D129 | ขอบเขตพื้นที่ภัยพิบัติที่ DDPM ประกาศ (ระดับตำบล) | dataset | Hazard | NSO | NSO.md:59 | |
| D130 | เครื่องมือ/กระบวนการซ้อนทับเชิงพื้นที่เพื่อสรุปผลกระทบ | product | Impact | NSO | NSO.md:59 | |

---

## กลุ่มที่ 4: กลุ่มเปราะบางและความสามารถในการรับมือปรับตัว (6 use cases, 17 items)

| item_id | item_text_th | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| D131 | แผนที่ภัยกายภาพ/ความเสี่ยงสภาพภูมิอากาศที่ลงถึงระดับพื้นที่ย่อย | dataset | Hazard | UDDC | UDDC.md:39 | |
| D132 | ข้อมูลเศรษฐสังคมที่เชื่อมโยงเชิงพื้นที่ได้ | dataset | Sensitivity | UDDC | UDDC.md:65 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D133 | ผลการซ้อนทับ/ตัวชี้วัด double vulnerability (เช่น แผนที่/ตารางสรุป) | product | Sensitivity | UDDC | UDDC.md:65 | |
| D134 | ข้อมูลผลกระทบจากภัยแยกตาม hazard × subgroup (children / elderly / ประเภทความพิการ 7 ประเภท ฯลฯ) | dataset | Sensitivity | MSDHS | MSDHS.md:42 | Sensitivity/Adaptive-Capacity split item — see Notes section |
| D135 | โครงสร้างข้อมูล/ตัวชี้วัดทางสังคมที่ทำให้จำแนก subgroup ได้อย่างสอดคล้อง | product | Sensitivity | MSDHS | MSDHS.md:40 | |
| D136 | ข้อมูล/ตัวชี้วัดที่จำแนกความต้องการด้านเพศและความเท่าเทียม (เช่น pregnant women, LGBTQ+ individuals) สำหรับการออกแบบศูนย์พักพิง | dataset | Sensitivity | MSDHS | MSDHS.md:43 | |
| D137 | แนวทาง/โปรโตคอลการปฏิบัติในศูนย์พักพิงที่อ้างอิงข้อมูล (protocols) | product | Response | MSDHS | MSDHS.md:43 | |
| D138 | ตัวชี้วัด/กรอบวิธีการวัด adaptive capacity หรือ management capacity | product | Adaptive Capacity | DDPM | DDPM.md:61 | |
| D139 | ข้อมูลปฏิบัติการ/ทรัพยากร/กระบวนการที่ใช้สร้างตัวชี้วัด | dataset | Adaptive Capacity | DDPM | DDPM.md:61 | |
| D140 | รูปแบบรายงาน/แดชบอร์ดสรุป bottlenecks และความสามารถในการจัดการ | product | Adaptive Capacity | DDPM | DDPM.md:63 | |
| D141 | ตัวชี้วัดจาก Agricultural Census (หนี้ครัวเรือน สถานะการชำระหนี้ ความเป็นเจ้าของสินทรัพย์เกษตร เช่น รถไถ สถานะการถือครองที่ดิน: เป็นเจ้าของ vs เช่า) | dataset | Sensitivity / Adaptive Capacity | NSO | NSO.md:93 | genuinely ambiguous — debt/asset-ownership/tenure data plausibly measures coping resources (Adaptive Capacity) as much as inherent susceptibility (Sensitivity); see Notes section, not force-resolved |
| D142 | โครงสร้างตัวแปร/นิยามและเมทาดาทาเพื่อใช้ในแบบจำลอง | product | Response | NSO | NSO.md:108 | |
| D143 | การเชื่อมโยงตัวชี้วัดเหล่านี้เข้ากับดัชนีความเปราะบาง/ความเสี่ยง | product | Sensitivity | NSO | NSO.md:108 | |
| D144 | ดัชนี Institutional Resilience Index (ประเมินความสามารถของ อปท./เทศบาล) | dataset | Adaptive Capacity | NXPO | NXPO.md:70 | |
| D145 | ผลคาดการณ์คลื่นความร้อนระดับพื้นที่ (localized heatwave projections) | dataset | Hazard | NXPO | NXPO.md:70 | |
| D146 | ผลการผสาน/จัดอันดับพื้นที่ "เสี่ยง × ขีดความสามารถ" (เช่น แผนที่/ตารางจัดลำดับ) | product | Adaptive Capacity | NXPO | NXPO.md:70 | |
| D147 | เกณฑ์คัดเลือกเทศบาลเป้าหมายเพื่อการแทรกแซง | product | Response | NXPO | NXPO.md:70 | |

---

## กลุ่มที่ 5: การตีความข้อมูลและพัฒนาระบบข้อมูล (32 use cases, 91 items)

Note: this group is dominated by data-governance/portal/metadata/catalog asks. Nearly all items here are tagged "Response" for lack of a better TOR 5.3.5 fit — see the summary-table note above. Where an item genuinely does carry physical-risk content (climate projections, hazard maps, socioeconomic exposure data), it is tagged accordingly.

| item_id | item_text_th | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| D148 | พอร์ทัลรวมศูนย์ข้อมูลน้ำ | product | Response | UDDC | UDDC.md:46 | |
| D149 | กลไกมาตรฐาน/การรับรองข้อมูลฐานและแบบจำลอง (รวมการ "ประกาศ" ชุดมาตรฐานที่ใช้ร่วมกัน) | product | Response | UDDC | UDDC.md:52 | |
| D150 | ช่องทางข้อมูลดิบที่ดาวน์โหลด/เรียกใช้ได้ (CSV/APIs) | product | Response | UDDC | UDDC.md:56 | |
| D151 | แดชบอร์ดสรุปสำหรับผู้บริหารท้องถิ่น | product | Response | UDDC | UDDC.md:61 | |
| D152 | ชุดแผนที่ความเสี่ยงจาก DCCE ที่มีสถานะเป็นทางการ/อ้างอิงได้ | product | Hazard | UDDC | UDDC.md:48 | |
| D153 | เอกสารกำกับ/เมทาดาทาเพื่อใช้เป็นหลักฐานประกอบการอนุมัติงบ | product | Response | UDDC | UDDC.md:54 | |
| D154 | รูปแบบการอ้างอิงที่นำไปใช้ในเอกสาร/กระบวนการงบประมาณของหน่วยงานท้องถิ่นได้ | product | Response | UDDC | UDDC.md:54 | |
| D155 | จุดเข้าถึงแบบรวมศูนย์สำหรับชุดข้อมูลพื้นฐาน (foundational datasets) และ risk maps | product | Response | TBA / Commercial Banks | TBA.md:41 | |
| D156 | รูปแบบการนำเสนอที่จัดหมวด/สรุปตามประเภทสินทรัพย์ (asset type-aggregates) | product | Exposure | TBA / Commercial Banks | TBA.md:41 | |
| D157 | เมทาดาทา/เงื่อนไขการใช้งานที่ชัดเจน | product | Response | TBA / Commercial Banks | TBA.md:41 | |
| D158 | แนวทาง/มาตรฐานการอ่านและใช้ probabilistic hazard maps (รวมตัวอย่างการตีความที่ถูกต้อง) | product | Hazard | TBA / Commercial Banks | TBA.md:39 | |
| D159 | เมทาดาทาอธิบายความหมายของช่วงกลับซ้ำ/ความน่าจะเป็นและข้อจำกัด | product | Response | TBA / Commercial Banks | TBA.md:39 | |
| D160 | สื่ออบรม/คู่มือเพื่อยกระดับความเข้าใจของนักวิเคราะห์ | product | Response | TBA / Commercial Banks | TBA.md:39 | |
| D161 | แค็ตตาล็อกข้อมูลแบบรวมศูนย์ (single entry point) | product | Response | MSDHS | MSDHS.md:34 | |
| D162 | เมทาดาทาทางเทคนิค (เช่น คำอธิบายตัวแปร ความละเอียด ช่วงเวลา หน่วยวัด) | product | Response | MSDHS | MSDHS.md:34 | |
| D163 | data dictionary/คู่มืออ่านข้อมูลสำหรับชุดข้อมูลภัยสำคัญ (เช่น DDPM historical disasters) | product | Response | MSDHS | MSDHS.md:49 | |
| D164 | ชุดข้อมูลคาดการณ์/forecast (predictive) และ baseline ที่สรุประดับตำบลและเทศบาล | dataset | Hazard | MSDHS | MSDHS.md:32 | vague — "forecast/baseline" unspecified content could also be Exposure or Sensitivity baselines |
| D165 | เมทาดาทาอธิบายสมมติฐาน/ข้อจำกัดของการคาดการณ์ | product | Response | MSDHS | MSDHS.md:32 | |
| D166 | ข้อมูลตัวชี้วัด SDGs ที่ผ่านการทำความสะอาด/มาตรฐานร่วมกันข้ามกระทรวง | dataset | Response | NESDC | NESDC.md:25 | general SDG indicator set, not risk-component specific |
| D167 | นิยาม baseline และตัวชี้วัดที่ทำให้เทียบเคียงได้ (เช่น การทำให้ตัวชี้วัดการเสียชีวิตบนท้องถนนสอดคล้องกันระหว่างกระทรวง) | product | Response | NESDC | NESDC.md:25 | |
| D168 | ตัวชี้วัดมาตรฐาน (Milestone 11) | product | Adaptive Capacity | NESDC | NESDC.md:51 | "ภูมิคุ้มกันของสังคมต่อการเปลี่ยนแปลงสภาพภูมิอากาศ" read as a capacity concept — judgment call, source text does not define the indicator set |
| D169 | ค่า baseline (Milestone 11) | dataset | Adaptive Capacity | NESDC | NESDC.md:51 | same caveat as D168 |
| D170 | ค่าเป้าหมายที่สอดคล้องกับ Milestone 11 (ภูมิคุ้มกันของสังคมต่อการเปลี่ยนแปลงสภาพภูมิอากาศ) | product | Adaptive Capacity | NESDC | NESDC.md:51 | same caveat as D168 |
| D171 | แค็ตตาล็อกชุดข้อมูลพร้อมเมทาดาทา | product | Response | DDPM | DDPM.md:34 | |
| D172 | API และมาตรฐานการเข้าถึง/สิทธิ์การใช้ข้อมูล | product | Response | DDPM | DDPM.md:34 | |
| D173 | รายการชุดข้อมูลที่แลกเปลี่ยนได้และคู่มือการใช้งาน | product | Response | DDPM | DDPM.md:34 | |
| D174 | taxonomy/กรอบจัดหมวดหมู่มาตรฐาน (เช่น UNDRR Exposure/Vulnerability sector groupings) | product | Response | DDPM | DDPM.md:52 | directly relevant to the catalog's own Exposure/Vulnerability categorization gap noted in the Notes section |
| D175 | mapping table ระหว่างหมวดหมู่ข้อมูลของ DDPM กับมาตรฐาน | product | Response | DDPM | DDPM.md:54 | |
| D176 | นิยามข้อมูล/รหัสหมวดหมู่ที่ใช้ร่วมกัน | product | Response | DDPM | DDPM.md:54 | |
| D177 | กฎ/โมเดลสำหรับตรวจจับความผิดปกติและการลงหมวดผิด | product | Response | DDPM | DDPM.md:58 | |
| D178 | ขั้นตอน data cleaning/standardization | product | Response | DDPM | DDPM.md:58 | |
| D179 | รายงานผลการคัดกรอง (เช่น flagged records) และวงจรการแก้ไขข้อมูล | product | Response | DDPM | DDPM.md:60 | |
| D180 | แนวทางสถาปัตยกรรมการเชื่อมต่อกับ GDX สำหรับข้อมูลไม่เปิดเผย | product | Response | DGA | DGA.md:82 | |
| D181 | แนวทางการเผยแพร่ Open Data ผ่าน data.go.th/CKAN | product | Response | DGA | DGA.md:87 | |
| D182 | ข้อเสนอแนะในรายงานสุดท้ายให้ใช้ GDX สำหรับข้อมูลไม่เปิดเผย และใช้ data.go.th สำหรับข้อมูลเปิด | product | Response | DGA | DGA.md:87 | |
| D183 | แนวปฏิบัติ/เกณฑ์การจัดชั้นข้อมูลตาม DGA (3 กลุ่ม: internal / share via GDX / open data) | product | Response | DGA | DGA.md:69 | |
| D184 | กระบวนการ/คู่มือการจัดชั้นข้อมูลสำหรับหน่วยงาน | product | Response | DGA | DGA.md:69 | |
| D185 | การอ้างอิงแนวทาง Data Classification ของ DGA ในงาน Data Governance Framework (WP3) | product | Response | DGA | DGA.md:87 | |
| D186 | แนวทาง/เทคนิค data masking และ anonymization สำหรับชุดข้อมูลภาครัฐ | product | Response | DGA | DGA.md:78 | governance/privacy mechanism protecting personal identifiers in sensitive-population data; tagged Response rather than Sensitivity since the item itself is a technique, not the underlying population data |
| D187 | หลักปฏิบัติในการแยก personal identifiers ออกจากข้อมูลแกนสำหรับการวิเคราะห์ก่อนเผยแพร่เป็น Open Data | product | Response | DGA | DGA.md:78 | |
| D188 | เกณฑ์/คำแนะนำจาก DGA สำหรับการเลือกสถาปัตยกรรมแค็ตตาล็อกข้อมูล (integrate vs separate platform) | product | Response | DGA | DGA.md:54 | |
| D189 | ข้อกำหนด/แนวทางการเลือก primary host ที่สอดคล้องกับ KPI Digital Government Readiness | product | Response | DGA | DGA.md:54 | |
| D190 | กลไกการปรึกษาหารือกับ DGA ระหว่างออกแบบระบบ | product | Response | DGA | DGA.md:54 | |
| D191 | รายการชุดข้อมูล GHG ที่ต้องใช้จากหน่วยงานเป้าหมาย (เช่น 3–4 หน่วยงาน) | dataset | Response | DGA | DGA.md:89 | GHG/mitigation data, outside the 8-category physical-risk scheme |
| D192 | การตรวจสอบว่ามี API ของชุดข้อมูลเหล่านี้อยู่บน GDX แล้วหรือไม่ | product | Response | DGA | DGA.md:89 | |
| D193 | แผนการประชุมเชิงเทคนิคเพื่อกำหนดชุดข้อมูลและแนวทางเชื่อมต่อผ่าน GDX | product | Response | DGA | DGA.md:89 | |
| D194 | จุดเข้าถึงข้อมูลกลาง (single source of truth) พร้อมวิธีสืบค้นและสรุปผลแบบเข้าใจง่าย | product | Response | DLA | DLA.md:57 | |
| D195 | ชุดข้อมูล/ตัวชี้วัดความเสี่ยงและผลกระทบที่ใช้เป็นหลักฐานเชิงนโยบาย | dataset | Impact | DLA | DLA.md:57 | |
| D196 | รูปแบบการอ้างอิง (citation/metadata) ที่หน่วยงานท้องถิ่นใช้ประกอบเอกสารอนุมัติงบได้ | product | Response | DLA | DLA.md:66 | |
| D197 | มาตรฐานการแม็ปข้อมูลความเสี่ยง/ตัวชี้วัดเข้ากับโครงสร้าง e-MENSCR | product | Response | DLA | DLA.md:61 | |
| D198 | กลไกเชื่อมต่อ/แลกเปลี่ยนข้อมูล (เช่น API หรือชุดข้อมูลที่อ้างอิงได้) ระหว่างคลังข้อมูลความเสี่ยงกับ e-MENSCR | product | Response | DLA | DLA.md:61 | |
| D199 | คู่มือการใช้งานสำหรับท้องถิ่นและจังหวัด | product | Response | DLA | DLA.md:61 | |
| D200 | ชุดข้อมูลเชิงพื้นที่ที่เป็นดิจิทัลและอ้างอิงพิกัด (แทนไฟล์กระดาษ/PDF) | dataset | Exposure | DPT | DPT.md:61 | generic spatial-data-format ask, cross-cutting rather than one risk component |
| D201 | เมทาดาทาที่ชัดเจน (ผู้ดูแลข้อมูล ความละเอียด ขอบเขตการใช้ ข้อจำกัด) | product | Response | DPT | DPT.md:65 | |
| D202 | มาตรฐาน/รูปแบบข้อมูลเชิงพื้นที่ที่อ่านได้ด้วยเครื่อง | product | Response | DPT | DPT.md:71 | |
| D203 | รายการชุดข้อมูลขั้นต่ำที่จำเป็นต่อการประเมินความเสี่ยง | product | Response | DPT | DPT.md:71 | |
| D204 | แนวทาง/บริการข้อมูลที่เชื่อม "การคาดการณ์สภาพภูมิอากาศ" เข้ากับ workflow การออกแบบเชิงวิศวกรรม/ภาคส่วน | product | Climatic Driver | DPT | DPT.md:81 | |
| D205 | กลไก/กระบวนการตรวจสอบและรับรองชุดข้อมูลภัย (รวมถึงข้อมูลน้ำ) และการประกาศชุดข้อมูลที่เป็น single source of truth | product | Response | FTI | FTI.md:46 | |
| D206 | พอร์ทัลแบบโต้ตอบ (interactive portal) พร้อม chatbot | product | Response | FTI | FTI.md:48 | |
| D207 | รายชื่อ/ช่องทางติดต่อที่อัปเดต | product | Response | FTI | FTI.md:48 | |
| D208 | กลไกดูแลความต่อเนื่องของความรู้/ข้อมูลผู้รับผิดชอบ | product | Response | FTI | FTI.md:48 | |
| D209 | แนวทาง/การสื่อสารคุณค่าทางธุรกิจของการแชร์ข้อมูล | product | Response | FTI | FTI.md:50 | |
| D210 | กลไก/โครงสร้างชุมชนผู้ใช้ข้อมูล (Data User Community) เพื่อแชร์การวิเคราะห์และสร้างความร่วมมือ | product | Response | FTI | FTI.md:50 | |
| D211 | baseline/ชุดข้อมูลอ้างอิงที่เป็นมาตรฐาน (unified baseline) | dataset | Response | NXPO | NXPO.md:49 | generic, not risk-component specific |
| D212 | กระบวนการตรวจสอบ/รับรองข้อมูล (verification) และกลไกประกาศ single source of truth | product | Response | NXPO | NXPO.md:49 | |
| D213 | แนวทาง/เอกสารกำกับเพื่อให้หน่วยงานต่าง ๆ ใช้ baseline เดียวกัน | product | Response | NXPO | NXPO.md:49 | |
| D214 | รายงาน Thailand Assessment Reports (ฉบับครอบคลุม) | product | Response | NXPO | NXPO.md:53 | |
| D215 | ชุดข้อมูล/สาระสรุประดับมหภาคสำหรับนโยบายที่อ้างอิงได้ | dataset | Response | NXPO | NXPO.md:53 | vague/generic |
| D216 | กลไกการอัปเดต/ทบทวนรายงานเป็นระยะ | product | Response | NXPO | NXPO.md:53 | |
| D217 | สถาปัตยกรรม/แนวทางการทำ Clearinghouse ที่เน้นการลิงก์ชุดข้อมูลภายนอก | product | Response | NXPO | NXPO.md:63 | |
| D218 | ฟังก์ชันค้นหาและลิงก์ไปยังแหล่งข้อมูลภายนอกพร้อมเมทาดาทา | product | Response | NXPO | NXPO.md:63 | |
| D219 | แนวทางอ้างอิง/เทียบเคียงกับ Climate-ADAPT (EU) | product | Response | NXPO | NXPO.md:63 | |
| D220 | รายการสถิติภายใต้ FDES (6 components / 21 sub-components) ที่แม็ปกับหน่วยงาน | product | Response | NSO | NSO.md:33 | |
| D221 | เกณฑ์การจัด tier และผลการจัด tier | product | Response | NSO | NSO.md:33 | |
| D222 | มติ/เอกสารมอบหมายหน่วยงานผู้รับผิดชอบการผลิตข้อมูล | product | Response | NSO | NSO.md:39 | |
| D223 | รายการชุดข้อมูลที่ดึงจาก GD Catalog | product | Response | NSO | NSO.md:41 | |
| D224 | กลไกการลิงก์ชุดข้อมูลที่อยู่บนเว็บไซต์หน่วยงาน (URL linking) | product | Response | NSO | NSO.md:41 | |
| D225 | แนวทาง/มาตรฐานการอ้างอิงแหล่งข้อมูลต้นทาง | product | Response | NSO | NSO.md:43 | |
| D226 | โครงสร้าง/มาตรฐาน tag กลาง | product | Response | NSO | NSO.md:44 | |
| D227 | mapping ระหว่าง tag กับกรอบมาตรฐาน (เช่น FDES) | product | Response | NSO | NSO.md:44 | |
| D228 | ฟังก์ชันค้นหาหลายมุมมองที่อิง tag | product | Response | NSO | NSO.md:44 | |
| D229 | มาตรฐานรูปแบบ/โครงสร้างข้อมูลสำหรับแลกเปลี่ยน | product | Response | NSO | NSO.md:71 | |
| D230 | ข้อกำหนดเมทาดาทาขั้นต่ำ (revision frequency, definitions, tags) | product | Response | NSO | NSO.md:71 | |
| D231 | คู่มือ/สื่ออบรมสำหรับหน่วยงานผู้ผลิตข้อมูล | product | Response | NSO | NSO.md:71 | |
| D232 | กลไกประสาน/ดึงข้อมูลจากหลายหน่วยงาน | product | Response | NSO | NSO.md:18 | |
| D233 | กระบวนการรวม/จัดรูปแบบให้เป็นชุดข้อมูลชาติชุดเดียว (single official national dataset) | product | Response | NSO | NSO.md:18 | |
| D234 | เอกสารกำกับนิยาม/เมทาดาทาเพื่อความสอดคล้อง | product | Response | NSO | NSO.md:18 | |
| D235 | ชุดข้อมูลคาดการณ์สภาพภูมิอากาศระยะยาวที่ได้รับการยอมรับ (โดยเฉพาะ hydrological projections) ที่หน่วยงานต่าง ๆ นำไปใช้ได้รายปี | dataset | Climatic Driver | OTP | OTP.md:73 | |
| D236 | รูปแบบการให้บริการ/การเผยแพร่ที่รองรับการนำไปใช้ซ้ำ | product | Response | OTP | OTP.md:73 | |
| D237 | แดชบอร์ดสาธารณะ | product | Response | OTP | OTP.md:33 | |
| D238 | ช่องทาง/กระบวนการเชื่อมระบบสำหรับหน่วยงานรัฐ (ผ่านหนังสือราชการ) เพื่อเข้าถึงและดาวน์โหลดข้อมูลดิบ (เช่น Shapefiles, Excel) | product | Response | OTP | OTP.md:37, OTP.md:39 | |

---

## Overall coverage check

83 of 83 use cases extracted (verified by grep count of `^- Agency:` lines in the source file = 83; group breakdown: กลุ่มที่ 1 = 15 use cases, กลุ่มที่ 2 = 22 use cases, กลุ่มที่ 3 = 8 use cases, กลุ่มที่ 4 = 6 use cases, กลุ่มที่ 5 = 32 use cases; 15+22+8+6+32 = 83). 238 atomic demand items extracted (D001–D238), none dropped.
