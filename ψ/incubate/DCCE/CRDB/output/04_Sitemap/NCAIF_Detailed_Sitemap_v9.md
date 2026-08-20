# NCAIF Detailed Sitemap v9.0 (Practicality Baseline)

**Status**: DRAFT — Phase 2 of the v8→v9 practicality pass, pending Checkpoint 2 sign-off
**Supersedes**: `NCAIF_Detailed_Sitemap_v8.md` (D-050)
**Constraint**: Keep the service intelligence DNA. Speak the language of practical stakeholders (อปท., วิศวกร, นักวางแผน, สตง.) on the front end. No complex AI jargon.

> [!NOTE]
> **What changed from v8, and why.** v8's inline `[N, MUST/SHOULD]` UNFCCC A-BTR compliance tags are removed entirely — BTR traceability now lives only in the DRD's own tracking columns (Layer 3, not the reader-facing sitemap), since a full v6-vs-v8 diff this session showed the tags correlated almost exactly with sections that grew heavier than v6 without matching demand: 2.3/2.3.1 and 3.3.1 most of all. Two annotation conventions replace the tags where the information is still genuinely useful to a reader:
> - *(shared build — see DEL-N)* — this content is one deliverable serving multiple sections; don't build it twice.
> - *(pending DCCE decision — see Brief E-N)* — this content has no committed build behind it yet; show it as pending, not as a finished feature.
>
> Six items present in `NCAIF_Detailed_Sitemap_v6.md` (Boss's original intention) but missing from v8 have been restored, confirmed item-by-item this session. One (2.4) was deliberately kept collapsed rather than restored. See the per-node notes below for each.

---

## 1. หน้าแรก (Home: National Climate Adaptation Portal)

> [!NOTE]
> **Structure note (19 August 2026, carried from v8):** Per the Homepage Concept draft (`2026-08-19-WP4-Homepage-Concept.md`), Home is a router, not an info page. Its function: hero statement, area search (1.2 below), task-based routing into the site's sections, a thin national-context strip linking out to Country Overview (1B), latest updates, and help/feedback. Detailed page design is next-project scope.

### 1.2 สืบค้นข้อมูลรายพื้นที่ (Interactive Area Search)
* ระบบสืบค้นข้อมูลความเสี่ยงเชิงพื้นที่แบบโต้ตอบ (Interactive Search Engine) เพื่อนำทางผู้ใช้ไปสู่ผลวิเคราะห์เชิงปฏิบัติการ
    *   **Search Hierarchy**: รองรับการค้นหารายระดับการปกครอง (จังหวัด -> อำเภอ -> ตำบล)
    *   **Map Integration**: แสดงตำแหน่งและขอบเขตการปกครองซ้อนทับบนแผนที่ความเสี่ยงเชิงพื้นที่ (Spatial Risk Map) *(shared build — see DEL-2/DEL-13, also embedded at 2.2, 2.4-link, and 4.2)*
    *   **Quick-view Dashboard**: แสดงบัตรข้อมูลสรุปความเปราะบางเฉพาะจุด ภัยคุกคามหลัก และมาตรการที่แนะนำในเบื้องต้น

---

## 1B. ภาพรวมประเทศ (Country Overview)

> [!NOTE]
> **Structure note, carried from v8:** Formerly "1.1 สรุปสำหรับผู้บริหาร," re-parented to its own top-level section, sibling to Home. Node code "1B" is provisional pending final site renumbering.

*   **1.1.1 ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย** *(shared build — see DEL-7, also referenced from 3.1/3.2)*:
    *   ประวัติศาสตร์และแนวโน้มภัยธรรมชาติของประเทศ
    *   กรอบแนวคิดและนิยามความเสี่ยงตามมาตรฐาน IPCC (Hazard, Exposure, Vulnerability)
    *   ความเข้าใจความเสี่ยงทางกายภาพ (Physical Risk) และความเสี่ยงจากการเปลี่ยนผ่าน (Transition Risk)
    *   แผนภาพและบัตรข้อมูลสรุปความเสี่ยงระดับชาติ (National Risk Profile Summary Cards)
*   **1.1.2 ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย**:
    *   พื้นที่เสี่ยงสูง (Hotspots) รายสาขาและระดับภูมิภาค
    *   สรุปสาระสำคัญของแผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศระดับชาติ (NAP Summary)
    *   ตัวอย่างมาตรการปรับตัวที่มีความคุ้มค่าสูง พร้อมรายละเอียดเบื้องต้น

---

## 2. ศูนย์ข้อมูลสำหรับผู้กำหนดนโยบายและแผน (Policy Maker Information Center)

### 2.1 สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ
* ภาพรวม climatic zone ของประเทศไทยและ historical climatology (linked to 3.1.2)
* สรุปสถิติภัยพิบัติจากภูมิอากาศในอดีต *(shared build — see DEL-12, Service 4; a different view of the same data as the loss/damage summary below, not a separate compilation)*
* สรุปข้อมูลความสูญเสียและความเสียหายทางเศรษฐกิจจากภัยพิบัติจากภูมิอากาศ — บัตรสรุปพร้อมลิงก์ไปยังแดชบอร์ดฉบับเต็มที่ 3.2.4 *(shared build — see DEL-12/LD-1; the full dashboard is built once, at 3.2.4, not duplicated here)*
*   สรุปแนวโน้มการเปิดรับภัย (Exposure Trends) (data from existing products. different view is presented here with some analysis )

### 2.2 สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน
*   สรุปโปรไฟล์ความเสี่ยงและความเปราะบางรายพื้นที่ (รายภูมิภาค, 77 จังหวัด, และระดับท้องถิ่น/อปท.) *(shared build — see DEL-2, same profile layer as 1.2/2.4-link/4.2)*
*   สรุปโปรไฟล์ความเสี่ยงเฉพาะสาขาเป้าหมายหลัก 6 สาขา (เกษตรกรรม, น้ำ, สาธารณสุข, ท่องเที่ยว, ป่าไม้/ระบบนิเวศ, พลังงานและการตั้งถิ่นฐาน) — *confirmed: both items source from CCIC (`ccic.dcce.go.th/riskarea`) — same domain as SYS-003's map application, verified against the asset-citation registry this session*
*   สังเคราะห์แผนจังหวัด/อำเภอ และข้อมูลระดับ อปท. *(pending DCCE resourcing decision — see Briefs E-5/E-6; province/district plan synthesis and LAO-level disaggregation are both real needs with no committed build yet — flagged, not silently left blank)*

### 2.3 เครื่องมือทางนโยบาย กฎหมาย และการเงิน
*   → ลิงก์ไปยังสรุปสาระสำคัญของแผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศระดับชาติ (NAP Summary, full detail at 1.1.2) — *cross-referenced rather than re-authored, per Boss's decision this session*
*  สถานะการดำเนินการตามแผนการปรับตัวระดับชาติ (NAP Implementation Status) — *restored from v6; answers a different question than the Act's legal status below — this is progress-tracking, not the plan's content summary above*
*   สถานะการดำเนินการและแผนดำเนินงานภายใต้ พ.ร.บ. การเปลี่ยนแปลงสภาพภูมิอากาศ (พ.ร.บ. โลกร้อน)
*   สรุปมาตรการทางกฎหมายและนโยบายที่ส่งเสริมการปรับตัว (เช่น พ.ร.บ. ป้องกันและบรรเทาสาธารณภัย, กฎกระทรวงผังเมือง, กฎหมายและนโยบายด้านการจัดการน้ำ)
*   สรุปเครื่องมือทางการเงินและแหล่งทุนที่ใช้ในการลงทุนปรับตัว, รายการแหล่งทุน และ**กรณีศึกษาการเงินเพื่อการปรับตัว** — *restored from v6 (v8 had dropped the case-studies half); detail at 2.3.1*
*   เครื่องมือการประเมินทางเศรษฐศาสตร์ของการลงทุนด้านการปรับตัว (Economics of Climate Adaptation Tool - ECA) และระเบียบวิธีประเมินต้นทุนและผลประโยชน์ (Cost-Benefit / Avoided Losses) *(pending DCCE decision — see Brief E-1; the strongest single cluster of undecided demand in the whole platform, per the DRD — do not present as a finished tool until DCCE actually commits)*
*   → ลิงก์ไปยังกรอบการติดตามและประเมินผลโครงการปรับตัวของประเทศไทย (full detail at 3.4.1) — *restored from v6; a policy maker on this page can reach the M&E framework in one click again*

*   **2.3.1 แหล่งทุนและการติดตามงบประมาณปรับตัว (Adaptation Finance Directory & Support Tracking)**:
    *   รายการแหล่งทุนภาครัฐ/เอกชน/ต่างประเทศ (GCF, AF, GEF, คู่มือการให้ทุนของ DCCE) พร้อมกรณีศึกษาการใช้งานจริง — real material exists today, buildable now
    *   *(pending DCCE decision — see Brief E-1, remaining items below have no methodology or material behind them yet)*:
        *   รายงานสถิติการจัดสรรงบประมาณแผ่นดินสำหรับการปรับตัวและการจัดทำระบบงบประมาณจำแนกรายจ่ายภูมิอากาศ (Climate Budget Tagging)
        *   การติดตามการรับเงินช่วยเหลือ เทคโนโลยี และความช่วยเหลือด้านวิชาการจากต่างประเทศ (Adaptation Finance Tracker) — *confirmed same product as the Finance Tracker mention at 3.3.5, named explicitly here so the connection isn't left implicit*
        * การประเมินและการดึงดูดการมีส่วนร่วมของภาคการเงินและภาคเอกชนในการจัดหาทุนเพื่อการปรับตัว 

*   **2.3.2 กลไกเชิงสถาบันและการประสานงาน (Institutional Governance & Coordination)** *(shared build — see DEL-8, same deliverable as the systemic-barriers content at 3.3.2)*:
	* บทบาทและหน้าที่ของกรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (DCCE) ในฐานะจุดประสานงานกลางของประเทศ
    * โครงสร้างคณะกรรมการนโยบายการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ และคณะอนุกรรมการรายสาขา
    * กลไกการประสานงานและบูรณาการการดำเนินงานปรับตัวระหว่างหน่วยงานรัฐระดับชาติและระดับท้องถิ่น (อปท.)
    * ช่องทางและสถิติการมีส่วนร่วมของภาคประชาสังคม ภาคเอกชน และสถาบันวิชาการในวงจรการปรับตัว

### 2.4 บริการข้อมูลสำหรับการวางแผน
- Links to [[#4. เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ (Tools & Services)]] — *kept as a pure router, per Boss's decision this session; the map/profile content DEL-2/DEL-13 would have surfaced here is already reachable via 1.2, 2.2, and 4.2, so a dedicated hub page would be duplicating an entry point rather than adding one*

---

## 3. วงจรขับเคลื่อนการปรับตัว (Adaptation Knowledge Cycle)

### 3.1 วิทยาศาสตร์ของสภาพภูมิอากาศ (Climate Science)
*   **3.1.1 ข้อมูลสังเกตุการณ์**:
    * บทความและลิ้งค์ไปยัง ชุดข้อมูลสภาพอากาศรายสถานีสังเกตการณ์ระยะสั้นและระยะกลาง (ข้อมูลหลักจากกรมอุตุนิยมวิทยา) (data catalog)
    * บทความและลิ้งค์ไปยัง ชุดข้อมูลสังเกตการณ์ผ่านดาวเทียม (Satellite-based observation parameters: พื้นที่ป่าไม้, การใช้ประโยชน์ที่ดิน Land Cover, แหล่งน้ำ, แนวปะการังฟอกขาว) (ข้อมูลหลักจาก GISTDA) (data catalog)
    *  ข้อมูลการติดตามปรากฏการณ์สภาพภูมิอากาศที่มีนัยสำคัญระดับสากล (เช่น ดัชนี ENSO, การชะลอตัวของ AMOC)
*   **3.1.2 ปัจจัยขับเคลื่อนทางภูมิอากาศ**:
    * ข้อมูล Climatology และตัวแปรทางสภาพภูมิอากาศที่สำคัญ (Temperature trends, Rainfall intensity changes)
    * แนวคิด ตัวขับเคลื่อนผลกนะทบทางภูมิอากาศ Climate Impact Driver
    * บทความและลิ้งค์ไปยังคลังชุดข้อมูลคาดการณ์อนาคตความละเอียดสูงระดับประเทศ (Downscaled climate projections) (https://clim-webbased.dcce.go.th/)
*   **3.1.3 ฉากทัศน์ภูมิอากาศในอนาคต** (Climate Scenarios):
    *   คู่มือและบทอธิบายการใช้งานฉากทัศน์ภูมิอากาศ
    *   แหล่งข้อมูล climate scenario — *restored from v6; a distinct "where do I actually get this data" pointer, separate from the usage explainer*
    *   มาตรฐานการบริหารจัดการความไม่แน่นอนและแนวทางการเลือกชุดข้อมูลคาดการณ์อนาคต (National Climate Uncertainty Governance Standard) *(pending DCCE decision — see Brief E-2)*
    *   ตัวอย่างกรณีศึกษาการประยุกต์ใช้แบบจำลองคาดการณ์สภาพภูมิอากาศในการวางแผนกลยุทธ์ระยะยาว

### 3.2 การวิเคราะห์ผลกระทบ ความเสี่ยง และความเปราะบางเสี่ยง (Impact, Vulnerability, and Risk Assessment)
*   **3.2.1 การวิเคราะห์ความเปราะบางและการเปิดรับภัย** (Exposure and Vulnerability Analysis):
    *  บทนิยามและแนวคิดเชิงทฤษฎี (Exposure, Sensitivity, Adaptive Capacity, Resilience)
    *  คลังแบบจำลองฟังก์ชันความเสียหาย (Damage Functions) รายภาคส่วนสำหรับการประเมินภัย *(pending DCCE decision — see Brief E-1; no v6 precedent, purely a forward-looking note until the wider finance-evidence service is commissioned)*
*   **3.2.2 การวิเคราะห์ความเสี่ยง** (Risk Analysis):
    * กรอบแนวทางและขั้นตอนการประเมินความเสี่ยงที่เป็นมาตรฐานเดียวกันของประเทศ
    * ผลวิเคราะห์ความเสี่ยงรายสาขา (เช่น ความมั่นคงทางอาหาร, ความมั่นคงด้านน้ำ, ผลกระทบต่อสุขภาพจากภัยความร้อน, ความเสี่ยงต่อการชะงักทางธุรกิจของ SME)
    * แหล่งข้อมูลผลการประเมินความเสี่ยงอื่นๆ — *restored from v6; pointers to other risk-assessment sources/references*
    *   **3.2.2.1 การติดตามภัยคุกคามที่เกิดขึ้นช้า (Slow-Onset Hazards Profile)**:
        * รายงานสถิติและการประเมินภัยคุกคามระยะยาวที่เกิดขึ้นอย่างช้าๆ (Slow-Onset Events) เช่น การเพิ่มขึ้นของอุณหภูมิเฉลี่ย และการเปลี่ยนแปลงคาบการกระจายน้ำฝน
        * ข้อมูลอัตราการเพิ่มขึ้นของระดับน้ำทะเล (Sea-Level Rise) ตลอดแนวชายฝั่งไทยและบริเวณอ่าวไทย
        * ข้อมูลการทรุดตัวของแผ่นดิน (Land Subsidence) ในเขตกรุงเทพมหานครและปริมณฑล และการหนุนของน้ำเค็ม (Salinity Intrusion)
        * สถิติการกัดเซาะชายฝั่งและการสูญเสียพื้นที่ชายหาด
*   **3.2.3 ผลกระทบลูกโซ่ (Impact Chain)**:
    * แผนภูมิแสดงแนวคิดผลกระทบเชื่อมโยงแบบลูกโซ่ (Multi-hazard Impact Chain Analysis)
    * กรณีศึกษาแบบจำลอง Impact Chain ในภาคส่วนเกษตรกรรมและการตั้งถิ่นฐานเมือง
*   **3.2.4 ความสูญเสียและความเสียหาย (Loss and Damage)** *(shared build — see DEL-12/LD-1; the same DDPM-sourced dataset backs 2.1's summary card and 1.1.1's disaster history)*:
    *  กรอบทฤษฎี Loss and Damage ภายใต้กรอบอนุสัญญา UNFCCC
    *   แดชบอร์ดสรุปสถิติภัยพิบัติจากภูมิอากาศและความสูญเสียทางเศรษฐกิจ (Economic Losses) และทางกายภาพจากภัยสภาพอากาศในอดีต — full build lives here; 2.1 links to this, does not duplicate it
    * การบันทึกสถิติความสูญเสียที่ไม่ใช่เศรษฐกิจ (Non-economic Losses: เช่น ผลกระทบด้านสุขภาพจิต ความหลากหลายทางชีวภาพ มรดกวัฒนธรรมที่สูญหาย)
*   **3.2.5 กรอบทฤษฎีและเอกสารคู่มือ**:
    * ระเบียบวิธีและเอกสารมาตรฐาน (Manuals) การประเมินความเสี่ยง ผลกระทบ และการคำนวณ Loss and Damage ของหน่วยงานรัฐ

### 3.3 การวางแผนการปรับตัวและการปฏิบัติ (Planning and Implementation)
*   **3.3.1 แนวทางการวางแผนและการออกแบบโครงการแบบมีส่วนร่วม (Planning Guidelines & Participatory Project Design)**:
    *   กรอบกฎหมายและระเบียบที่ต้องปฏิบัติตามในการออกแบบโครงการ (พ.ร.บ. การเปลี่ยนแปลงสภาพภูมิอากาศ, พ.ร.บ. ป้องกันและบรรเทาสาธารณภัย, กฎกระทรวงผังเมือง ฯลฯ) *(shared build — see DEL-8; same underlying legal/policy content as 2.3, reframed here as project-design compliance guidance for planners — closes the gap Boss flagged this session: 2.3's legal summary previously had no home in Section 3)*
    *   ระเบียบวิธีประเมินต้นทุนและผลประโยชน์ (Cost-Benefit Analysis) และเครื่องมือ ECA — *(pending DCCE decision — see Brief E-1; same undecided service as 2.3, see that page rather than re-describing it here)*
    *   แนวปฏิบัติการบูรณาการมิติด้านเพศวิถี ความเท่าเทียมทางเพศ และสิทธิมนุษยชนในมาตรการปรับตัว (Gender & Social Inclusion Integration) — genuinely new since v6, but real, ready-to-build content, kept as committed
    *   ข้อมูลมาตรการคุ้มครองและช่วยเหลือกลุ่มเปราะบาง (เด็ก ผู้สูงอายุ ผู้พิการ และชุมชนชายแดน/ชายฝั่ง)
    *   การประยุกต์ใช้ภูมิปัญญาท้องถิ่น องค์ความรู้ดั้งเดิม และมรดกทางวัฒนธรรมในการปรับตัวของชุมชน

*   **3.3.2 เส้นทางกลยุทธ์การปรับตัวของประเทศ (Adaptation Roadmap & Planning)**:
    *   แผนภาพและเส้นทางกลยุทธ์การดำเนินงาน (NAP Roadmap Execution Staging)
    *   ฉากทัศน์การวางแผนมาตรการปรับตัว (Adaptation Scenarios)

*   **3.3.3 ห้องสมุดมาตรการปรับตัวตามสาขา**:
    * ระบบสืบค้นและคัดกรองมาตรการเชิงเทคนิคและนโยบาย (Searchable Database) จำแนกตามภัย ภาคส่วน และงบประมาณ
    * รายการมาตรการแบบผสมผสานระหว่างมาตรการวิศวกรรมโครงสร้าง (Grey Infrastructure) และการปรับตัวโดยใช้ธรรมชาติเป็นฐาน (Nature-based Solutions - NBS)
*   **3.3.4 กรณีศึกษาการวางแผนการปรับตัว**:
    *  คลังข้อมูลแนวทางการทำแผนจัดการความเสี่ยงสภาพภูมิอากาศ ของหน่วยงานราชการและภาคเอกชน *(distinct from 3.4.3, confirmed by Boss: this is case studies of the planning process itself — how organizations built their risk-management plans — not the implemented result)*
*   **3.3.5 โครงการที่กำลังดำเนินการ (Project Tracking Status)**:
    *   → ลิงก์ไปยังระบบติดตามความก้าวหน้าโครงการปรับตัว (full detail at 3.4.2's Adaptation M&E Platform) — *merged per Boss's decision this session: project-tracking status was being claimed as a function of the M&E Platform, which itself doesn't exist yet (Brief E-3) — one pending capability described once, not two separately-worded pending items*
    * การติดตามการเงินเพื่อการปรับตัว (Adaptation Finance Tracker) — *(pending DCCE decision — see Brief E-1, same undecided finance-tracking service as 2.3.1; see that page's pending items rather than a separate build here — the v8 mockups had built this twice, once here as a Sankey diagram and once at 2.3.1, with conflicting figures)*

### 3.4 การติดตาม ประเมินผล และถอดบทเรียน (Monitoring, Evaluation, and Learning)
*   **3.4.1 แนวทางการติดตามและประเมินผลการปรับตัว**:
    *  กรอบการติดตามและประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศไทย (info page) — *now also linked from 2.3, restored*
    * กรอบการวิเคราะห์ระดับความก้าวหน้าทางเทคโนโลยีและนวัตกรรมปรับตัว (Technology Readiness Levels - TRL in Adaptation)
    *   ความเชื่อมโยงกับตัวชี้วัดเป้าหมายการปรับตัวระดับโลก (Global Goal on Adaptation - GGA Indicators)
*   **3.4.2 ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย (Adaptation M&E Platform)** *(pending DCCE resourcing decision — see Brief E-3; nothing built yet, per the DRD — now also the claimed home for 3.3.5's project-tracking function, merged here this session)*:
    * ระบบติดตามความก้าวหน้าและระดับการลดความเปราะบางรายภาคส่วนและรายจังหวัด (National M&E Tracker)
    * สถานะและการดำเนินงานโครงการปรับตัวรายโครงการ (Project Tracking Status — เช่น โครงการประกันภัยพืชผล, การใช้งานระบบฐานข้อมูล Agri-Map, การปรับปรุงโครงสร้างควบคุมน้ำ) — *moved here from 3.3.5*
*   **3.4.3 กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ** *(distinct from 3.3.4, confirmed by Boss: this is case studies of implemented results — flagship projects that came out of the planning process, not the planning process itself)*:
    *  คลังบทเรียนโครงการเด่น (Flagship Projects Case Studies) ถอดบทเรียนความสำเร็จ อุปสรรค และแนวทางปฏิบัติที่เป็นเลิศ (Best Practices)

---

## 4. เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ (Tools & Services)

> [!NOTE]
> **Structure note, decided this session:** No 4.1/4.2/4.3 category split — the mockup (`11_tools_and_services_hub_4.html`) already proved the flat, tag-filterable model works better than a forced hierarchy: one searchable grid of tools, filtered by category tags. Data Catalog is one tool among several, not a separate top-level category.

**Search + category filter**: ค้นหาเครื่องมือ/ชุดข้อมูล พร้อม filter pills (ทั้งหมด, บัญชีข้อมูล, แผนที่เสี่ยงภัย, ผลกระทบ, เศรษฐศาสตร์/เงิน, มาตรการ)

Tools in the grid, each tagged by category:
*   **บัญชีข้อมูล (Data Catalog)** `[บัญชีข้อมูล]`: ระบบสืบค้นชุดข้อมูลดิบ (Raw Datasets) ผลิตภัณฑ์วิเคราะห์ข้อมูล และข้อมูลอธิบาย (Metadata Directory) ตามเกณฑ์มาตรฐานความมั่นคงปลอดภัย
*   **แผนที่ความเสี่ยงภูมิอากาศ (Climate Risk Map)** `[แผนที่เสี่ยงภัย]` *(shared build — see DEL-13; the canonical hosting point for the map/analytical infrastructure also embedded at 1.2 and 2.2)*: ระบบโปรแกรมประยุกต์แสดงแผนที่ภัยและวิเคราะห์ความเสี่ยงเชิงโต้ตอบ สำหรับดึงตัวแปรไปใช้งานวิศวกรรมโยธา (เช่น ค่าคาดการณ์ปริมาณฝนและอุณหภูมิในระดับแปลงที่แปลงเป็นเกณฑ์ออกแบบ Design Curves/IDF Curves)
*   **ตัวสำรวจผลกระทบภูมิอากาศ (Climate Impact Explorer)** `[ผลกระทบ]` *(mockup-sourced — not yet cross-checked against a DRD deliverable; flag for Phase 3's DRD update rather than treating as committed)*
*   **เครื่องมือการประเมินทางเศรษฐศาสตร์ของการลงทุนด้านการปรับตัว (ECA)** `[เศรษฐศาสตร์/เงิน]` *(pending DCCE decision — see Brief E-1, same as 2.3/3.3.1 — do not present as a finished tool here either)*
*   **ตัวสำรวจมาตรการปรับตัว (Adaptation Options Explorer)** `[มาตรการ]` *(mockup-sourced — not yet cross-checked against a DRD deliverable; flag for Phase 3's DRD update rather than treating as committed)*
*   **ระบบติดตามการเงินเพื่อการปรับตัว (Adaptation Finance Tracker)** `[เศรษฐศาสตร์/เงิน]` *(pending DCCE decision — see Brief E-1, same as 2.3.1/3.3.5 — the mockup built this a third time here with yet another figure; do not build as a finished dashboard until decided)*

**ศูนย์รวมเครื่องมือและแหล่งข้อมูลภายนอก** (external hub, not natively built): จุดเชื่อมต่อไปยังพอร์ทัลข้อมูลระดับสากลและพอร์ทัลเฉพาะทาง (เช่น TMD Weather API, GISTDA Geo-Informatics Portal, Copernicus Climate Data Store)

---

## 5. ข่าว ประกาศ และช่องทางการติดต่อ (News and Contact)
*   **5.1 ประกาศและกิจกรรมการมีส่วนร่วม**: ระบบกระจายข่าวสารการอัปเดตข้อมูล กิจกรรมอบรมเชิงปฏิบัติการ (Workshops) ในการวิเคราะห์และตีความข้อมูลสภาพภูมิอากาศเพื่อการวางแผนเชิงพื้นที่
*   **5.2 ช่องทางการรับฟังข้อคิดเห็นและบริการผู้ใช้ (Feedback & Helpdesk)**: แพลตฟอร์มรับเสียงสะท้อนจากหน่วยงานผู้ใช้งานในแบบที่เป็นระบบเพื่อปรับปรุงคุณภาพชุดข้อมูล ขยายขอบเขตการบริการ และทวนสอบการตอบสนองความต้องการเชิงสถาบัน

---

## Summary of changes from v8

**Structural sharing confirmed (no new builds needed where already shared):**
- Risk map & profile: DEL-2/DEL-13, one capability across 1.2, 2.2, 2.4-link, 4 — confirmed to literally share a backend domain (`ccic.dcce.go.th`), not just conceptually related
- Risk framing & worked examples: DEL-7, one explainer set across 1.1.1, 3.1, 3.2
- Policy & institutional content: DEL-8, one deliverable across 2.3/2.3.2 (policy summary) and 3.3.1/3.3.2 (project-design compliance framing + systemic-barriers report) — 3.3.1 gained a legal-framework bullet this round specifically to give 2.3's law/Act content a home in Section 3, per Boss's review
- Disaster stats & Loss and Damage: DEL-12/LD-1, one DDPM-sourced build across 1.1.1, 2.1, 3.2.4 (resolves the D-068/D-069 disagreement found this session — DRD's framing confirmed correct)
- Project tracking: merged 3.3.5 into 3.4.2 — both were describing the same not-yet-built M&E Platform function; 3.3.5 is now a pointer, not a second description

**Marked pending DCCE decision (was presented as finished in v8/mockups; now honestly flagged instead):**
- ECA / Cost-Benefit / Avoided Losses (2.3, 3.3.1, and Tools & Services) — Brief E-1
- Budget tagging, aid/tech-transfer tracking (named "Adaptation Finance Tracker" explicitly, per Boss's review), private-sector finance engagement (2.3.1) — Brief E-1
- Damage function library (3.2.1) — Brief E-1
- Uncertainty governance standard (3.1.3) — Brief E-2
- Project Tracking Status (moved to 3.4.2) — Brief E-3
- Adaptation Finance Tracker (3.3.5, 2.3.1, and Tools & Services) — Brief E-1; the mockups had built this three times (Sankey at 3.3.5, directory at 2.3.1, progress bar at Tools & Services) with conflicting figures (฿100M vs. ฿42,500M) — now one pending item named consistently in all three places
- Provincial/district plan synthesis, LAO-level disaggregation (2.2) — Briefs E-5/E-6

**Restored from v6 (confirmed by Boss this session):**
- 2.3: NAP implementation status; finance case studies at 2.3.1; M&E framework link
- 3.1.3: climate scenario data sources
- 3.2.2: other risk assessment result sources

**Deliberately kept as-is (not restored):**
- 2.4: kept as a pure router link to Section 4, rather than rebuilt as a 6-item planning hub — the map/profile content it would have carried is already reachable via 1.2/2.2/4

**New this round (Boss's inline review):**
- 2.3's NAP Summary bullet changed from freshly-duplicated text to a cross-reference back to 1.1.2
- Section 4 restructured from a 3-way category split (Data Catalog / Visualization App / External Hub) to a flat, tag-filterable tool list, matching how the mockup (`11_tools_and_services_hub_4.html`) was actually built — two of the mockup's tool cards (Climate Impact Explorer, Adaptation Options Explorer) are carried over but flagged as not yet cross-checked against any DRD deliverable, pending a Phase 3 pass
- 3.3.4 vs. 3.4.3 resolved: **not a duplicate.** 3.3.4 is case studies of the planning *process* (how organizations built their risk-management plans); 3.4.3 is case studies of the implemented *result* (flagship projects that came out of that process). Both nodes now say so explicitly, so this doesn't get re-flagged as a merge candidate in a future pass.
