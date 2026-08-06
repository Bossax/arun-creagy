# WP2 Demand Signals — Stage A Extraction (Draft)

**Purpose**: This is Stage A of a two-stage WP2 (Data Inventory) scoring pipeline for identifying the 10 most business-critical datasets in the 260-row `data_catalog_v3.csv`. An earlier attempt scored datasets using proxy metadata (sector tags, hazard-count tags, national-vs-local coverage) and was rejected by the project lead as ungrounded guesswork. This corrected approach grounds the scoring in what stakeholders have *explicitly and concretely asked for*, as documented in the D-043 NCAIF Service Intelligence Report (`output/06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`), which the project lead has already reviewed and accepted.

**Scope of this document**: extraction only. Every explicitly-named concrete data/variable/spatial-resolution need mentioned across the 8 services and 34 use cases is listed below, grouped by service, with a direct Thai quote + English gloss and a source citation (service number, use-case number or "narrative" if drawn from the service's framing prose rather than the numbered use-case list). No mapping to the data catalog happens here — that is Stage B, out of scope for this document. Nothing below is inferred beyond what the source text states; where a reading is ambiguous, that is flagged explicitly rather than resolved.

Source document: `output/06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (v6.0).

---

## Service 1 — คลังข้อมูลภูมิอากาศและบริการรับรองข้อมูลทางการ (Climate Data Repository & Official Certification Service)

No numbered "กรณีการใช้งานที่เกี่ยวข้อง" list is present for this service in the source document — it is described only in narrative form. Signals below are drawn from that narrative.

1. **Signal**: Demand for a certified/quality-assured, standardized single-source-of-truth metadata catalog (rather than a specific variable) — i.e., the *service itself* is the demand, not a named dataset.
   - Source: บริการ 1, narrative (paragraph 2)
   - Quote (TH): "บริการนี้จึงทำหน้าที่เป็นแพลตฟอร์มกลางสำหรับการค้นหาและเข้าถึงชุดข้อมูลที่ได้รับการรับรองมาตรฐานและคุณภาพจากกรมการเปลี่ยนแปลงสภาพภูมิอากาศ โดยทำหน้าที่เป็นแหล่งข้อมูลความจริงเพียงหนึ่งเดียว (Single Source of Truth) ที่มีการจัดการชุดอธิบายข้อมูล (metadata) ตามมาตรฐานของประเทศไทย"
   - Gloss (EN): "This service acts as a central platform for discovering and accessing datasets that have been certified to standard and quality by the Department of Climate Change and Environment, serving as a Single Source of Truth with metadata management per Thailand's national standard."
   - Ambiguity flag: **Yes.** This is a meta-level demand for a certification/discovery *service*, not a named data variable or dataset. It does not point to any specific dataset in the catalog and cannot itself be used to rank individual catalog rows — it is structural/process demand, distinct from the concrete variable-level signals in Services 2–8. Included for completeness but flagged as out-of-shape for Stage B's dataset-matching purpose.

---

## Service 2 — การวิเคราะห์ความเสี่ยงในระดับพื้นที่ที่มีความละเอียดสูง (High-Resolution Spatial Risk Analysis)

### Narrative-level signals

2. **Signal**: Risk data at sub-district (ตำบล), municipal (เทศบาล), household, real-estate/property, and agricultural-parcel (แปลงเพาะปลูก) spatial resolution, finer than current province-level risk data.
   - Source: บริการ 2, narrative (paragraph 1)
   - Quote (TH): "ผู้ใช้ข้อมูลมีความต้องการข้อมูลความเสี่ยงในระดับตำบล เทศบาล ครัวเรือน อสังหาริมทรัพย์ แปลงเพาะปลูก และทรัพย์สินรูปแบบอื่นๆ ตามรูปแบบของหน่วยย่อยของการวิเคราะห์ที่แต่ล่ะภาคส่วนต้องจัดการ"
   - Gloss (EN): "Data users need risk data at sub-district, municipal, household, real-estate, agricultural-parcel, and other property levels, matching the analysis sub-unit each sector must manage."

3. **Signal**: Risk analysis at Enumeration Area (EA) level, per the National Statistical Office's census sub-unit definition.
   - Source: บริการ 2, narrative (paragraph 2)
   - Quote (TH): "บริการนี้จึงยกระดับการวิเคราะห์ความเสี่ยงจากภัยที่เกิดจากการเปลี่ยนแปลงสภาพภูมิอากาศในอนาคตมาสู่ระดับตำบล หรือระดับหน่วยย่อยของการทำสำมะโนประชากร (Enumeration Area, อ้างอิง สำนักงานสถิติแห่งชาติ) หรือหน่วยพื้นที่อื่นๆ ที่เจาะจงมากขึ้น"
   - Gloss (EN): "This service elevates future climate-hazard risk analysis to sub-district level, or the census Enumeration Area sub-unit (per the National Statistical Office), or other more specific spatial units."

### Use-case-level signals

4. **Signal**: Urban-zone risk analysis (no named variable beyond "risk in urban areas").
   - Source: บริการ 2, use case 1
   - Quote (TH): "การวิเคราะห์ความเสี่ยงในเขตเมือง"
   - Gloss (EN): "Risk analysis in urban zones."
   - Ambiguity flag: Vague — no specific hazard or variable named; could span flood, heat, or multi-hazard risk.

5. **Signal**: Biodiversity risk analysis / biodiversity data.
   - Source: บริการ 2, use case 2
   - Quote (TH): "การวิเคราะห์ความเสี่ยงต่อความหลากหลายทางชีวภาพ"
   - Gloss (EN): "Risk analysis for biodiversity."

6. **Signal**: Household economic resilience assessment for households dependent on agriculture and manufacturing income, tied to disaster-damage scenarios.
   - Source: บริการ 2, use case 3
   - Quote (TH): "การประเมินภูมิคุ้มกันทางเศรษฐกิจของครัวเรือนที่พึ่งพารายได้ในภาคส่วนต่างๆ เช่นเกษตรกรรมและอุตสาหกรรมการผลิต หากเกิดภัยพิบัติที่สร้างความเสียหายขึ้น"
   - Gloss (EN): "Assessment of the economic resilience of households dependent on income from sectors such as agriculture and manufacturing, in the event of damaging disasters."

7. **Signal**: Identification of intra-urban livability tipping points/critical points, to support long-term relocation planning.
   - Source: บริการ 2, use case 4
   - Quote (TH): "การระบุจุดวิกฤติและจุดเปลี่ยนผ่านของความสามารถในการอยู่อาศัยของพื้นที่ภายในเมือง เพื่อทำแผนการอพยพคนออกจากพื้นที่ในระยะยาว"
   - Gloss (EN): "Identifying critical points and tipping points of intra-urban livability, to plan long-term population relocation."

8. **Signal**: Proactive welfare-program design for people with disabilities, tied to pre-hazard evacuation planning (e.g., bedridden patients before flooding).
   - Source: บริการ 2, use case 5
   - Quote (TH): "การออกแบบโปรแกรมสนับสนุนสวัสดิการสังคมแก่ผู้พิการประเภทต่างๆ แบบเชิงรุก เพื่อป้องกันและลดผลกระทบของภัย ล่วงหน้าก่อนการเกิดภัย เช่นการอพยพผู้ป่วยติดเตียงก่อนเหตุการณ์น้ำท่วม"
   - Gloss (EN): "Proactive design of social welfare support programs for people with various disabilities, to prevent/mitigate hazard impacts in advance — e.g., evacuating bedridden patients before a flood event."

9. **Signal**: Matching of risk areas, at-risk groups, and municipal administrative boundaries, for resource/budget-source allocation.
   - Source: บริการ 2, use case 6
   - Quote (TH): "การจับคู่พื้นที่เสี่ยง กลุ่มเสี่ยง และขอบเขตการปกครองระดับเทศบาล เพื่อรวบรวมทรัพยากรที่ต้องใช้และแหล่งที่มาของงบประมาณในการสนับสนุน"
   - Gloss (EN): "Matching at-risk areas, at-risk groups, and municipal administrative boundaries, to compile needed resources and funding sources."

10. **Signal**: Heat-hazard vulnerability mapping for the urban poor, at neighborhood-level resolution.
    - Source: บริการ 2, use case 7
    - Quote (TH): "ทำแผนที่ความเปราะบางต่อภัยความร้อนของกลุ่มคนยากจนในเขตเมืองเพื่อระบุมาตรการแทรกแซงในระดับย่านและมาตราการปรับตัว"
    - Gloss (EN): "Mapping heat-hazard vulnerability of the urban poor to identify neighborhood-level intervention and adaptation measures."

11. **Signal**: Agricultural-parcel-level (แปลงเกษตร) monitoring of climate-variability impacts, to support recovery policy and carbon-credit project development.
    - Source: บริการ 2, use case 8
    - Quote (TH): "การติดตามผลกระทบจากความแปรปรวนของสภาพภูมิอากาศระดับแปลงเกษตร เพื่อวางนโยบายในการฟื้นฟูแปลงเกษตรจากความเสียหายและสนับสนุนการพัฒนาโครงการคาร์บอนเครดิต"
    - Gloss (EN): "Monitoring climate-variability impacts at agricultural-parcel level, to inform recovery policy for damaged plots and support carbon-credit project development."

---

## Service 3 — หลักฐานสนับสนุนการตัดสินใจด้านการเงินและงบประมาณ (Financial/Budget Decision-Support Evidence)

### Narrative-level signals

12. **Signal**: Methodology/data for calculating "Avoided Losses" value, Cost-Benefit Analysis, and other economic-benefit metrics for climate-resilient infrastructure investment.
    - Source: บริการ 3, narrative (paragraph 2)
    - Quote (TH): "บริการนี้จึงทำหน้าที่เป็นกลไกสร้างความชอบธรรมผ่านระเบียบวิธีการคำนวณมูลค่าของความเสียหายที่หลีกเลี่ยงได้ (Avoided Losses) การวิเคราะห์ต้นทุนและผลประโยชน์ของโครงการ (Cost Benefit Analysis) และผลประโยชน์ทางเศรษฐกิจอื่นๆ"
    - Gloss (EN): "This service functions as a legitimacy mechanism via a methodology for calculating Avoided Losses value, Cost-Benefit Analysis, and other economic benefits."

### Use-case-level signals

13. **Signal**: Economic damage calculation using a "damage function" for financial risk modeling.
    - Source: บริการ 3, use case 1
    - Quote (TH): "การคำนวณมูลค่าเสียหายเชิงเศรษฐกิจโดยใช้ damage function ของภาคการเงิน (Financial Risk Modeling)"
    - Gloss (EN): "Calculating economic damage value using the financial sector's damage function (Financial Risk Modeling)."

14. **Signal**: Real economic damage/loss estimation from disaster events, for emergency-fund allocation assessment.
    - Source: บริการ 3, use case 2
    - Quote (TH): "การประมาณความเสียหายและความสูญเสียทางทางเศรษฐกิจที่แท้จริงจากเหตุการณ์ภัยพิบัติเพื่อประเมินการจัดสรรเงินฉุกเฉิน"
    - Gloss (EN): "Estimating true economic damage and loss from disaster events, to assess emergency-fund allocation."

15. **Signal**: Climate-risk-adjusted Return on Investment (ROI) certification for large infrastructure project loans.
    - Source: บริการ 3, use case 3
    - Quote (TH): "การออกใบรับรองอัตราผลตอบแทนจากการลงทุน (Return On Investment) ที่ปรับตามความเสี่ยงของผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศแล้ว ให้แก่เงินกู้ของโครงการโครงสร้างพื้นฐานขนาดใหญ่"
    - Gloss (EN): "Issuing climate-risk-adjusted ROI certificates for loans to large infrastructure projects."

16. **Signal**: Financial-justification communication data for climate-resilient transport infrastructure projects that cost more than historical baseline pricing.
    - Source: บริการ 3, use case 4
    - Quote (TH): "การสื่อสารเหตุผลสนับสนุนทางการเงินแก่โครงการก่อสร้างโครงสร้างพื้นฐานคมนาคมที่ออกแบบให้มีภูมิคุ้มกันต่อการเปลี่ยนแปลงสภาพภูมิอากาศในอนาคต ซึ่งใช้งบประมาณมากกว่าราคากลางในอดีต"
    - Gloss (EN): "Communicating financial justification for climate-resilient transport infrastructure construction projects that cost more than the historical baseline budget."

17. **Signal**: ROI calculation for Nature-based Solutions, for comparison against Gray Infrastructure design.
    - Source: บริการ 3, use case 5
    - Quote (TH): "การคำนวณอัตราผลตอบแทนจากการลงทุนของโครงการที่ใช้ธรรมชาติเป็นฐาน (Nature-based solution) เพื่อเปรียบเทียบกับการออกแบบโดยโครงสร้างสีเทา (Gray infrastructure)"
    - Gloss (EN): "Calculating ROI for Nature-based Solution projects to compare against Gray Infrastructure design."

18. **Signal**: Evidence documentation set for local government (อปท.) annual budget ordinance or reserve-fund use requests.
    - Source: บริการ 3, use case 6
    - Quote (TH): "ชุดเอกสารหลักฐานสนับสนุนสำหรับองค์การปกครองส่วนท้องถิ่นในการใช้ประกอบการจัดทำเทศบัญญัติงบประมาณรายจ่ายประจำปี หรือการทำเรื่องขอใช้เงินสะสม"
    - Gloss (EN): "A supporting evidence document set for local administrative organizations to use in preparing their annual expenditure budget ordinance, or in requesting use of reserve funds."

---

## Service 4 — การประเมินความสูญเสียและความเสียหายจากการเปลี่ยนแปลงสภาพภูมิอากาศในอดีต (Historical Loss & Damage Assessment)

### Narrative-level signals

19. **Signal**: Statistics on Economic Loss and Non-economic Loss from past-to-present disaster impacts, compiled comprehensively with a transparent methodology.
    - Source: บริการ 4, narrative (paragraph 2)
    - Quote (TH): "บริการนี้จึงทำหน้าที่สร้างฐานข้อมูลของหลักฐานเชิงประจักษ์ของผลกระทบจากภัยพิบัติในอดีตถึงปัจจุบัน เพื่อรวบรวมสถิติความเสียหายทางเศรษฐกิจ (Economic Loss) และความสูญเสียด้านอื่นๆ (Non-economic Loss) อย่างรอบด้านและใช้ระเบียบวิธีที่โปร่งใส"
    - Gloss (EN): "This service builds an empirical-evidence database of disaster impacts from the past to the present, compiling Economic Loss and Non-economic Loss statistics comprehensively and with a transparent methodology."

### Use-case-level signals

20. **Signal**: Improved accuracy of the country's disaster loss & damage assessment.
    - Source: บริการ 4, use case 1
    - Quote (TH): "การพัฒนาความแม่นยำของการประเมินความสูญเสียและความเสียหายจากภัยพิบัติของประเทศ"
    - Gloss (EN): "Improving the accuracy of the country's disaster loss and damage assessment."

21. **Signal**: Macro-level economic loss reporting, broken down by sector.
    - Source: บริการ 4, use case 2
    - Quote (TH): "การจัดทำรายงานความสูญเสียทางเศรษฐกิจในระดับมหภาค แยกตามภาคส่วน"
    - Gloss (EN): "Preparing macro-level economic loss reports, broken down by sector."

22. **Signal**: Loss & damage assessment for disclosure under the Sendai Framework reporting.
    - Source: บริการ 4, use case 3
    - Quote (TH): "การจัดทำการประเมินความสูญเสียและความเสียหายเพื่อเปิดเผยในรายงานตามกรอบ Sendai"
    - Gloss (EN): "Preparing loss and damage assessment for disclosure in Sendai Framework reporting."

23. **Signal**: Loss & damage assessment methodology for financial-sector stress testing.
    - Source: บริการ 4, use case 4
    - Quote (TH): "ระเบียบวิธีในการประเมินความสูญเสียและความเสียหายเพื่อการทำ stress testing ของภาคการเงิน"
    - Gloss (EN): "Methodology for loss and damage assessment to support financial-sector stress testing."

24. **Signal**: Tourism-sector loss assessment (Tourism Impact), to identify vulnerability of tourist destinations and prioritize recovery.
    - Source: บริการ 4, use case 5
    - Quote (TH): "การประเมินความสูญเสียของภาคการท่องเที่ยว (Tourism Impact) เพื่อระบุความเปราะบางของแหล่งท่องเที่ยวและจัดลำดับความสำคัญในการฟื้นฟู"
    - Gloss (EN): "Assessing tourism-sector loss (Tourism Impact) to identify vulnerability of tourist destinations and prioritize recovery."

---

## Service 5 — ตัวแปรทางวิศวกรรมเพื่อการออกแบบโครงสร้างพื้นฐาน (Engineering Variables for Climate-Resilient Infrastructure Design)

### Use-case-level signals

25. **Signal**: Rainfall Intensity, Peak Flow, and Temperature Extremes data, converted at an appropriate spatial/temporal resolution into Design Runoff figures and flood-level scenarios, for road-network design.
    - Source: บริการ 5, use case 1
    - Quote (TH): "สนับสนุนการดำเนินงานด้านการคำนวณตัวแปรทางวิศวกรรมที่ใช้ในการออกแบบเพื่อรองรับการเปลี่ยนแปลงสภาพภูมิอากาศ เช่น การแปลง Rainfall Intensity, Peak Flow, Temperature Extremes ในระดับความละเอียดที่เหมาะสม ให้เป็นตัวเลข Design Runoff และระดับน้ำท่วมในฉากทัศน์ต่างๆ เพื่อออกแบบโครงข่ายถนน"
    - Gloss (EN): "Supporting the calculation of engineering design variables for climate-resilient design, such as converting Rainfall Intensity, Peak Flow, and Temperature Extremes — at appropriate resolution — into Design Runoff figures and flood levels under various scenarios, to design road networks."

26. **Signal**: Datasets on risk, hazard maps, land-suitability, and ecosystem services, under multiple scenarios, for sustainable urban planning.
    - Source: บริการ 5, use case 2
    - Quote (TH): "การพัฒนาแนวทางการวางผังเมืองที่ยั่งยืน โดยต้องการชุดข้อมูลที่เกี่ยวข้องกับความเสี่ยง แผนที่ภัย ความเหมาะสมในการใช้ที่ดิน บริการทางนิเวศวิทยา ภายใต้ฉากทัศน์ต่างๆ"
    - Gloss (EN): "Developing sustainable urban planning approaches, requiring datasets on risk, hazard maps, land-use suitability, and ecosystem services, under various scenarios."

27. **Signal**: Rainfall Intensity-Duration-Frequency (IDF) curve, shifting from a 30-year historical average basis to future-projection data, for urban drainage-system design.
    - Source: บริการ 5, use case 3
    - Quote (TH): "การปรับปรุงกราฟ Intensity-Duration-Frequency ของน้ำฝนจากการใช้ค่าเฉลี่ยย้อนหลัง 30 ปี ไปสู่การใช้ข้อมูลคาดการณ์ในอนาคตเพื่อการออกแบบระบบระบายน้ำในเมือง"
    - Gloss (EN): "Updating the rainfall Intensity-Duration-Frequency curve from a 30-year historical average basis to future-projection data, for urban drainage-system design."

28. **Signal**: Landslide risk and soil/slope stability models, integrated into the building-permit issuance process.
    - Source: บริการ 5, use case 4
    - Quote (TH): "การผนวกรวมแบบจำลองวิเคราะห์ความเสี่ยงในการเกิดดินถล่มและความมั่นคงของชั้นดินไปในกระบวนการออกใบอนุญาตสร้างอาคาร"
    - Gloss (EN): "Integrating landslide-risk analysis models and soil-layer stability into the building-permit issuance process."

29. **Signal**: Marine infrastructure risk assessment (storm exposure and sea-level rise), for port maintenance/upgrade planning.
    - Source: บริการ 5, use case 5
    - Quote (TH): "การประเมินความเสี่ยงต่อโครงสร้างพื้นฐานทางทะเล (Marine Infrastructure) เพื่อวางแผนบำรุงรักษาและปรับปรุงท่าเรือให้รองรับพายุและระดับน้ำทะเลที่สูงขึ้น"
    - Gloss (EN): "Assessing risk to marine infrastructure, to plan port maintenance and upgrades to withstand storms and rising sea levels."

---

## Service 6 — ระบบเฝ้าระวังและเตือนผลกระทบของภัยล่วงหน้าแบบพหุภัย (Multi-Hazard Impact Early Warning System)

### Narrative-level signals

30. **Signal**: Soil water-absorption capacity data, at sub-district (ตำบล) resolution, as a vulnerability input for multi-hazard impact forecasting/warning.
    - Source: บริการ 6, narrative (paragraph 2)
    - Quote (TH): "บริการนี้จะพัฒนาระบบที่สามารถแปลงข้อมูลสภาพอากาศให้เป็นผลกระทบต่อชีวิตและทรัพย์สิน โดยคาดการณ์ผลกระทบลูกโซ่ที่เกิดจากภัยหลายแหล่ง (Multi-hazard) และแจ้งเตือนโดยผนวกเอาความเปราะบางของพื้นที่ (เช่น ขีดความสามารถในการดูดซับน้ำของดินในแต่ละตำบล) เข้ามาร่วมพิจารณา"
    - Gloss (EN): "This service will develop a system that converts weather data into impacts on life and property, forecasting chain impacts from multi-hazard sources, and issuing alerts that incorporate area vulnerability (e.g., soil water-absorption capacity in each sub-district)."

### Use-case-level signals

31. **Signal**: Drought management in the industrial sector and its downstream production-process impacts.
    - Source: บริการ 6, use case 1
    - Quote (TH): "การจัดการภัยแล้งในภาคอุตสาหกรรมและผลกระทบที่ตามมาในกระบวนการผลิต"
    - Gloss (EN): "Drought management in the industrial sector and its resulting impacts on production processes."

32. **Signal**: Heat-impact and health-impact forecasting for outdoor workers and elderly community members, to trigger response measures and cooling-shelter setup.
    - Source: บริการ 6, use case 2
    - Quote (TH): "การคาดการณ์ผลกระทบจากอากาศร้อนและผลกระทบด้านสุขภาพต่อผู้ทำงานกลางแจ้งและผู้สูงอายุในชุมชน เพื่อสั่งการมาตรการรับมือ และการจัดทำห้องหลบร้อน"
    - Gloss (EN): "Forecasting heat impacts and health impacts on outdoor workers and elderly community members, to trigger response measures and set up cooling shelters."

33. **Signal**: Financial-value estimation of business-disruption impact for SMEs.
    - Source: บริการ 6, use case 3
    - Quote (TH): "การพัฒนาแนวทางในการประมาณมูลค่าทางการเงินของการชะงักของการดำเนินธุรกิจแก่ SME"
    - Gloss (EN): "Developing an approach to estimate the financial value of business-operation disruption for SMEs."

34. **Signal**: Marine-ecosystem monitoring, specifically advance coral-bleaching early warning, to trigger conservation-area closure.
    - Source: บริการ 6, use case 4
    - Quote (TH): "การเฝ้าระวังระบบนิเวศทางทะเล เช่น การเตือนภัยปะการังฟอกขาวล่วงหน้าเพื่อสั่งการปิดพื้นที่อนุรักษ์"
    - Gloss (EN): "Marine ecosystem monitoring, such as advance coral-bleaching warnings to trigger conservation-area closure."

35. **Signal**: Localized flash-flood thresholds, set using per-sub-district soil water-absorption capacity as the determining factor for warning trigger points.
    - Source: บริการ 6, use case 5
    - Quote (TH): "การตั้งค่าเกณฑ์น้ำท่วมฉับพลันระดับพื้นที่ (Localized Flood Thresholds) โดยใช้ขีดความสามารถในการดูดซับน้ำของดินในแต่ละตำบลเป็นตัวกำหนดจุดเตือนภัย"
    - Gloss (EN): "Setting localized flash-flood thresholds, using each sub-district's soil water-absorption capacity as the determinant of the warning trigger point."
    - Note: This duplicates/reinforces signal #30 (soil water-absorption capacity per sub-district) — same concrete data need appears in both the service narrative and this use case.

---

## Service 7 — การติดตามและประเมินผลการดำเนินนโยบายด้านการปรับตัวของประเทศ (National Adaptation Policy Monitoring & Evaluation)

### Narrative-level signals

36. **Signal**: Technology Readiness status/gap tracking, linking national and local adaptation targets.
    - Source: บริการ 7, narrative (paragraph 2)
    - Quote (TH): "ช่วยให้เข้าใจสถานะความก้าวหน้าและช่องว่างทางเทคโนโลยี (Technology Readiness) ที่ยังขาด"
    - Gloss (EN): "Helps understand the status of progress and the remaining Technology Readiness gaps."

### Use-case-level signals

37. **Signal**: Tracking of national Technology Readiness Levels (TRL), to manage funding to research institutions closing technology gaps needed for adaptation.
    - Source: บริการ 7, use case 1
    - Quote (TH): "การติดตาม Technology Readiness Levels ของประเทศเพื่อจัดการการให้ทุนแก่หน่วยงานวิจัยปิดช่องว่างทางเทคโนโลยีที่จำเป็นในการปรับตัว"
    - Gloss (EN): "Tracking the country's Technology Readiness Levels, to manage funding to research institutions to close technology gaps needed for adaptation."

38. **Signal**: Local-government performance indicator adaptation, aligned to national adaptation targets.
    - Source: บริการ 7, use case 2
    - Quote (TH): "แนวทางในการปรับตัวชี้วัดประสิทธิภาพการทำงานขององค์กรปกครองส่วนท้องถิ่นให้สอดคล้องกับเป้าหมายการปรับตัวของประเทศ"
    - Gloss (EN): "An approach for adapting local-government performance indicators to align with the country's adaptation targets."
    - Ambiguity flag: No specific named dataset — this is a process/indicator-alignment need rather than a data variable per se.

39. **Signal**: Area-based funding for spatial/area-based hazard-prevention planning.
    - Source: บริการ 7, use case 3
    - Quote (TH): "หน่วยงานให้ทุนเชิงพื้นที่ต้องการให้ทุนในการวางแผนเชิงพื้นที่ เพื่อป้องกันภัยที่อาจเกิดขึ้นในอนาคต"
    - Gloss (EN): "Area-based funding agencies want to fund spatial/area-based planning, to prevent hazards that may occur in the future."
    - Ambiguity flag: This reads as a funding-mechanism need, not a specific data-variable ask; no named dataset.

40. **Signal**: Data collection to support Global Goal on Adaptation (GGA) reporting.
    - Source: บริการ 7, use case 4
    - Quote (TH): "การรวบรวมข้อมูลสนับสนุนรายงานเป้าหมายการปรับตัวระดับโลก (Global Goal on Adaptation)"
    - Gloss (EN): "Compiling data to support Global Goal on Adaptation reporting."

---

## Service 8 — มาตรฐานการจัดการความไม่แน่นอนและเกราะป้องกันการตัดสินใจทางการ (National Climate Uncertainty Governance & Institutional Shield)

### Narrative-level signals

41. **Signal**: Assessment of "readiness status" (สถานะความพร้อม) and "appropriate use" (การใช้งานที่เหมาะสม) of climate data products/datasets, in the context of climate risk management.
    - Source: บริการ 8, narrative (paragraph 2)
    - Quote (TH): "โดยบริการนี้ควรมีองค์ประกอบหลักที่สามารถประเมิน สถานะความพร้อม และการใช้งานที่เหมาะสม ของผลิตภัณฑ์ข้อมูลและชุดข้อมูลต่างๆ ในบริบทของการจัดการความเสี่ยงจากการเปลี่ยนแปลวสภาพภูมิอากาศ"
    - Gloss (EN): "This service should have core components able to assess the readiness status and appropriate use of data products and datasets, in the context of climate-change risk management."
    - Ambiguity flag: This is a meta-level (data-quality/fitness-for-use assessment capability) demand, not a request for a specific dataset or variable — similar in kind to Service 1's signal.

### Use-case-level signals

42. **Signal**: Scenario-analysis planning capability for organizations.
    - Source: บริการ 8, use case 1
    - Quote (TH): "การวางแผนแบบวิเคราะห์ฉากทัศน์ของหน่วยงาน"
    - Gloss (EN): "Scenario-analysis-based planning for organizations."
    - Ambiguity flag: No named variable or dataset — implies scenario/projection data generally (climate scenarios), but does not specify which.

43. **Signal**: Flexible/robust adaptation policy and strategy planning under uncertain conditions.
    - Source: บริการ 8, use case 2
    - Quote (TH): "การวางนโยบายและกลยุทธ์การปรับตัวที่ยืดหยุ่นและทนทานต่อสถานการณ์"
    - Gloss (EN): "Formulating adaptation policy and strategy that is flexible and robust to conditions."
    - Ambiguity flag: No specific data variable named.

44. **Signal**: Communication of risk-data uncertainty.
    - Source: บริการ 8, use case 3
    - Quote (TH): "การสื่อสารความไม่แน่นอนของข้อมูลความเสี่ยง"
    - Gloss (EN): "Communicating the uncertainty of risk data."
    - Ambiguity flag: Refers to uncertainty *metadata/handling* of risk data generally, not a named dataset or variable.

---

## Summary

- **Total demand signals extracted: 44** (across 8 services; Service 1 contributes 1 narrative-level signal with no numbered use cases in the source; Services 2–8 contribute narrative + numbered use-case signals as itemized above).
- **Signals flagged as ambiguous / not directly variable-specific: 9** — signals #1 (Service 1 narrative), #4 (Service 2 UC1, vague hazard scope), #38, #39 (Service 7 UC2–3, process/funding-mechanism asks), #41 (Service 8 narrative, meta-level fitness-for-use), #42, #43, #44 (Service 8 UC1–3, general scenario/policy/uncertainty-communication asks without a named variable), plus #35 flagged as a duplicate/reinforcement rather than a distinct new signal.
- Recurring concrete named-variable/resolution asks that appear more than once across services (useful signal strength for Stage B): **soil water-absorption capacity at sub-district level** (Service 6 narrative + UC5); **sub-district/ตำบล-level spatial resolution generally** (Service 2 narrative, Service 2 narrative EA reference, Service 6); **Rainfall Intensity / IDF curves** (Service 5 UC1 and UC3); **economic loss / non-economic loss statistics** (Service 3 UC1–2, Service 4 narrative + UC1–5).
- No signal in this document has been matched against `data_catalog_v3.csv`. That matching is explicitly Stage B and out of scope here.
