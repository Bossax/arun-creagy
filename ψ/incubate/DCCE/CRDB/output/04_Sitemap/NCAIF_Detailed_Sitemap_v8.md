# NCAIF Detailed Sitemap v8.0 (Compliance & Thematic Refined Baseline)

**Status**: PROPOSED BASELINE (Structural realignment based on BTR Gap Analysis)
**Constraint**: Keep the service intelligence DNA. Speak the language of practical stakeholders (อปท., วิศวกร, นักวางแผน, สตง.) on the front end, but embed UNFCCC A-BTR compliance requirements on the back end. No complex AI jargon.

> [!NOTE]
> Items introduced or enriched by UNFCCC A-BTR compliance requirements are annotated with `[Section Number, Requirement Level]` markers to show content alignment (e.g. `[2, MUST]`, `[5, SHOULD]`).
> 
> **BTR Section Numbers mapping:**
> - `1` = Section 1: National circumstances, institutional arrangements, legal framework
> - `2` = Section 2: Climate evidence, hazards, sector risks
> - `3` = Section 3: National adaptation priorities, strategies, barriers
> - `4` = Section 4: Implementation progress, indicators, funding flows
> - `5` = Section 5: Loss and Damage, disaster risk management support
> - `6` = Section 6: Good practices, lessons learned

---

## 1. หน้าแรก (Home: National Climate Adaptation Portal)

> [!NOTE]
> **Structure note (19 August 2026):** Per the Homepage Concept draft (`2026-08-19-WP4-Homepage-Concept.md`), Home is a router, not an info page. Its function: hero statement, area search (1.2 below), task-based routing into the site's sections, a thin national-context strip linking out to Country Overview (1B), latest updates, and help/feedback. It no longer carries the Executive Overview content — that moved to its own section, 1B, below. Detailed page design is next-project scope.

### 1.2 สืบค้นข้อมูลรายพื้นที่ (Interactive Area Search)
* ระบบสืบค้นข้อมูลความเสี่ยงเชิงพื้นที่แบบโต้ตอบ (Interactive Search Engine) เพื่อนำทางผู้ใช้ไปสู่ผลวิเคราะห์เชิงปฏิบัติการ
    *   **Search Hierarchy**: รองรับการค้นหารายระดับการปกครอง (จังหวัด -> อำเภอ -> ตำบล)
    *   **Map Integration**: แสดงตำแหน่งและขอบเขตการปกครองซ้อนทับบนแผนที่ความเสี่ยงเชิงพื้นที่ (Spatial Risk Map) `[2, MUST]`
    *   **Quick-view Dashboard**: แสดงบัตรข้อมูลสรุปความเปราะบางเฉพาะจุด ภัยคุกคามหลัก และมาตรการที่แนะนำในเบื้องต้น

---

## 1B. ภาพรวมประเทศ (Country Overview)

> [!NOTE]
> **Structure note (19 August 2026):** Formerly "1.1 สรุปสำหรับผู้บริหาร (Executive Overview)", nested under Home. Re-parented out to its own top-level section, sibling to Home — reached via Home's router, not shown on Home itself. Node code "1B" is provisional pending final site renumbering.

*   **1.1.1 ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย**: 
    *   ประวัติศาสตร์และแนวโน้มภัยธรรมชาติของประเทศ
    *   กรอบแนวคิดและนิยามความเสี่ยงตามมาตรฐาน IPCC (Hazard, Exposure, Vulnerability) `[2, MUST]`
    *   ความเข้าใจความเสี่ยงทางกายภาพ (Physical Risk) และความเสี่ยงจากการเปลี่ยนผ่าน (Transition Risk) `[2, MUST]`
    *   แผนภาพและบัตรข้อมูลสรุปความเสี่ยงระดับชาติ (National Risk Profile Summary Cards)
*   **1.1.2 ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย**: 
    *   พื้นที่เป้าหมายวิกฤต (Hotspots) รายสาขาและระดับภูมิภาค `[2, MUST]`
    *   สรุปสาระสำคัญของแผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศระดับชาติ (NAP Summary) `[1, MUST]`
    *   ตัวอย่างมาตรการปรับตัวเด่นเชิงรุกที่มีความคุ้มค่าสูง

---

## 2. ศูนย์ข้อมูลสำหรับผู้กำหนดนโยบายและแผน (Policy Maker Information Center)
### 2.1 สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ:
*   สถิติเหตุการณ์อากาศสุดขั้วในอดีต (เช่น อุณหภูมิสูงสุด-ต่ำสุดประวัติศาสตร์ สถิติปริมาณฝนสะสม)
*   ฐานข้อมูลสถิติความสูญเสียและความเสียหายทางเศรษฐกิจระดับชาติ (Macroeconomic Loss & Damage Database) `[5, MUST]`
*   สรุปแนวโน้มภัยคุกคามและการเปิดรับภัยของประเทศ (Exposure Trends) `[2, MUST]`
### 2.2 สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน:
*   สรุปโปรไฟล์ความเสี่ยงและความเปราะบางรายพื้นที่ (รายภูมิภาค, 77 จังหวัด, และระดับท้องถิ่น/อปท.) `[2, MUST]`
*   สรุปโปรไฟล์ความเสี่ยงเฉพาะสาขาเป้าหมายหลัก 6 สาขา (เกษตรกรรม, น้ำ, สาธารณสุข, ท่องเที่ยว, ป่าไม้/ระบบนิเวศ, พลังงานและการตั้งถิ่นฐาน) `[2, MUST]`
### 2.3 เครื่องมือทางนโยบาย กฎหมาย และการเงิน:
*   สถานะการดำเนินการและแผนดำเนินงานภายใต้ พ.ร.บ. การเปลี่ยนแปลงสภาพภูมิอากาศ (พ.ร.บ. โลกร้อน) `[1, MUST]`
*   สรุปมาตรการทางกฎหมายและนโยบายที่ส่งเสริมการปรับตัว (เช่น พ.ร.บ. ป้องกันและบรรเทาสาธารณภัย, กฎกระทรวงผังเมือง) `[1, MUST]`
*   ระบบรับรองความเป็นทางการของเครื่องมือการวิเคราะห์การหลีกเลี่ยงความสูญเสีย (Avoided Losses Certification Model) `[3, MUST]`
*   **2.3.1 แหล่งทุนและการติดตามงบประมาณปรับตัว (Adaptation Finance Directory & Support Tracking)**:
    *   รายการแหล่งทุนภาครัฐ/เอกชน/ต่างประเทศ และคู่มือวิเคราะห์ความคุ้มค่าโครงการเพื่อประกอบการจัดทำงบประมาณชี้แจง สตง. `[4, MUST]`
    *   รายงานสถิติการจัดสรรงบประมาณแผ่นดินสำหรับการปรับตัวและการจัดทำระบบงบประมาณจำแนกรายจ่ายภูมิอากาศ (Climate Budget Tagging) `[4, SHOULD]`
    *   การติดตามการรับเงินช่วยเหลือ เทคโนโลยี และความช่วยเหลือด้านวิชาการจากต่างประเทศ (GCF, AF, GEF) `[4, MUST]`
    *   การประเมินและการดึงดูดการมีส่วนร่วมของภาคการเงินและภาคเอกชนในการจัดหาทุนเพื่อการปรับตัว `[4, SHOULD]`
*   **2.3.2 กลไกเชิงสถาบันและการประสานงาน (Institutional Governance & Coordination)**:
    *   บทบาทและหน้าที่ของกรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (DCCE) ในฐานะจุดประสานงานกลางของประเทศ `[1, MUST]`
    *   โครงสร้างคณะกรรมการนโยบายการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ และคณะอนุกรรมการรายสาขา `[1, MUST]`
    *   กลไกการประสานงานและบูรณาการการดำเนินงานปรับตัวระหว่างหน่วยงานรัฐระดับชาติและระดับท้องถิ่น (อปท.) `[1, MUST]`
    *   ช่องทางและสถิติการมีส่วนร่วมของภาคประชาสังคม ภาคเอกชน และสถาบันวิชาการในวงจรการปรับตัว `[1, SHOULD]`
### 2.4 บริการข้อมูลสำหรับการวางแผน:
*   สถิติและดัชนีความเปราะบางระดับท้องถิ่น (Local Vulnerability & Adaptive Capacity Indices) `[2, MUST]`
*   แผนที่ความเสี่ยงเชิงพื้นที่แบบบูรณาการ (Integrated Spatial Risk Maps)
*   แนวทางและข้อกำหนดความปลอดภัยข้อมูลระดับประเทศสำหรับการสืบค้นเชิงวิชาการ

---

## 3. วงจรขับเคลื่อนการปรับตัว (Adaptation Knowledge Cycle)
### 3.1 วิทยาศาสตร์ของสภาพภูมิอากาศ (Climate Science)
*   **3.1.1 ข้อมูลสังเกตุการณ์**:
    *   ชุดข้อมูลสภาพอากาศรายสถานีสังเกตการณ์ระยะสั้นและระยะกลาง (ความร่วมมือกรมอุตุนิยมวิทยา)
    *   ชุดข้อมูลสังเกตการณ์ผ่านดาวเทียม (Satellite-based observation parameters: พื้นที่ป่าไม้, การใช้ประโยชน์ที่ดิน Land Cover, แหล่งน้ำ, แนวปะการังฟอกขาว) `[2, MUST]`
    *   ข้อมูลการติดตามปรากฏการณ์สภาพภูมิอากาศที่มีนัยสำคัญระดับสากล (เช่น ดัชนี ENSO, การชะลอตัวของ AMOC) `[2, SHOULD]`
*   **3.1.2 ปัจจัยขับเคลื่อนทางภูมิอากาศ**:
    *   ข้อมูล Climatologyและตัวแปรทางสภาพภูมิอากาศที่สำคัญ (Temperature trends, Rainfall intensity changes) `[2, MUST]`
    *   คลังชุดข้อมูลคาดการณ์อนาคตความละเอียดสูงระดับประเทศ (Downscaled climate projections) `[2, MUST]`
*   **3.1.3 ฉากทัศน์ภูมิอากาศในอนาคต** (Climate Scenarios)  :
    *  คู่มือและบทอธิบายการใช้งานฉากทัศน์ภูมิอากาศ 
    * มาตรฐานการบริหารจัดการความไม่แน่นอนและแนวทางการเลือกชุดข้อมูลคาดการณ์อนาคต (National Climate Uncertainty Governance Standard) `[2, MUST]`
    *   ตัวอย่างกรณีศึกษาการประยุกต์ใช้แบบจำลองคาดการณ์สภาพภูมิอากาศในการวางแผนกลยุทธ์ระยะยาว

### 3.2 การวิเคราะห์ผลกระทบ ความเสี่ยง และความเปราะบางเสี่ยง (Impact, Vulnerability, and Risk Assessment)
*   **3.2.1 การวิเคราะห์ความเปราะบางและการเปิดรับภัย**:
    *   บทนิยามและแนวคิดเชิงทฤษฎี (Exposure, Sensitivity, Adaptive Capacity, Resilience)
    *   คลังแบบจำลองฟังก์ชันความเสียหาย (Damage Functions) รายภาคส่วนสำหรับการประเมินภัย `[2, MUST]`
*   **3.2.2 การวิเคราะห์ความเสี่ยง** (Risk Analysis):
    *   กรอบแนวทางและขั้นตอนการประเมินความเสี่ยงที่เป็นมาตรฐานเดียวกันของประเทศ
    *   ผลวิเคราะห์ความเสี่ยงรายสาขา (เช่น ความมั่นคงทางอาหาร, ความมั่นคงด้านน้ำ, ผลกระทบต่อสุขภาพจากภัยความร้อน, ความเสี่ยงต่อการชะงักทางธุรกิจของ SME) `[2, MUST]`
    *   **3.2.2.1 การติดตามภัยคุกคามที่เกิดขึ้นช้า (Slow-Onset Hazards Profile)**:
        *   รายงานสถิติและการประเมินภัยคุกคามระยะยาวที่เกิดขึ้นอย่างช้าๆ (Slow-Onset Events) เช่น การเพิ่มขึ้นของอุณหภูมิเฉลี่ย และการเปลี่ยนแปลงคาบการกระจายน้ำฝน `[5, MUST]`
        *   ข้อมูลอัตราการเพิ่มขึ้นของระดับน้ำทะเล (Sea-Level Rise) ตลอดแนวชายฝั่งไทยและบริเวณอ่าวไทย `[5, MUST]`
        *   ข้อมูลการทรุดตัวของแผ่นดิน (Land Subsidence) ในเขตกรุงเทพมหานครและปริมณฑล และการหนุนของน้ำเค็ม (Salinity Intrusion) `[5, MUST]`
        *   ดัชนีการกัดเซาะชายฝั่งและการสูญเสียพื้นที่ชายหาดเชิงสถิติ `[5, SHOULD]`
*   **3.2.3 ผลกระทบลูกโซ่ (Impact Chain)**:
    *   แผนภูมิแสดงแนวคิดผลกระทบเชื่อมโยงแบบลูกโซ่ (Multi-hazard Impact Chain Analysis) `[2, MUST]`
    *   กรณีศึกษาแบบจำลอง Impact Chain ในภาคส่วนเกษตรกรรมและการตั้งถิ่นฐานเมือง
*   **3.2.4 ความสูญเสียและความเสียหาย (Loss and Damage)**:
    *   กรอบทฤษฎี Loss and Damage ภายใต้กรอบอนุสัญญา UNFCCC `[5, MUST]`
    *   แดชบอร์ดสรุปสถิติความสูญเสียทางเศรษฐกิจ (Economic Losses) และทางกายภาพจากภัยสภาพอากาศในอดีต `[5, MUST]`
    *   การบันทึกสถิติความสูญเสียที่ไม่ใช่เศรษฐกิจ (Non-economic Losses: เช่น ผลกระทบด้านสุขภาพจิต ความหลากหลายทางชีวภาพ มรดกวัฒนธรรมที่สูญหาย) `[5, SHOULD]`
*   **3.2.5 กรอบทฤษฎีและเอกสารคู่มือ**:
    *   ระเบียบวิธีและเอกสารมาตรฐาน (Manuals) การประเมินความเสี่ยง ผลกระทบ และการคำนวณ Loss and Damage ของหน่วยงานรัฐ `[5, MUST]`

### 3.3 การวางแผนการปรับตัวและการปฏิบัติ (Planning and Implementation)
*   **3.3.1 แนวทางการวางแผนและการออกแบบโครงการแบบมีส่วนร่วม (Planning Guidelines & Participatory Project Design)**:
    *   ระเบียบวิธีประเมินต้นทุนและผลประโยชน์ (Cost-Benefit Analysis) และความคุ้มค่าในการลงทุนปรับตัว (Avoided Losses Calculus) `[3, MUST]`
    *   แนวปฏิบัติการบูรณาการมิติด้านเพศวิถี ความเท่าเทียมทางเพศ และสิทธิมนุษยชนในมาตรการปรับตัว (Gender & Social Inclusion Integration) `[3, SHOULD]`
    *   ข้อมูลมาตรการคุ้มครองและช่วยเหลือกลุ่มเปราะบาง (เด็ก ผู้สูงอายุ ผู้พิการ และชุมชนชายแดน/ชายฝั่ง) `[3, SHOULD]`
    *   การประยุกต์ใช้ภูมิปัญญาท้องถิ่น องค์ความรู้ดั้งเดิม และมรดกทางวัฒนธรรมในการปรับตัวของชุมชน `[3, SHOULD]`
*   **3.3.2 เส้นทางกลยุทธ์การปรับตัวของประเทศ (Adaptation Roadmap & Planning)**:
    *   แผนภาพและเส้นทางกลยุทธ์การดำเนินงาน (NAP Roadmap Execution Staging) `[3, MUST]`
    * ฉากทัศน์การวางแผนมาตรการปรับตัว (Adaptation Scenarios)

*   **3.3.3 ห้องสมุดมาตรการปรับตัวตามสาขา**:
    *   ระบบสืบค้นและคัดกรองมาตรการเชิงเทคนิคและนโยบาย (Searchable Database) จำแนกตามภัย ภาคส่วน และงบประมาณ
    *   รายการมาตรการแบบผสมผสานระหว่างมาตรการวิศวกรรมโครงสร้าง (Grey Infrastructure) และการปรับตัวโดยใช้ธรรมชาติเป็นฐาน (Nature-based Solutions - NBS)
*   **3.3.4 กรณีศึกษาการวางแผนการปรับตัว**:
    *   คลังข้อมูลแนวทางการทำแผนจัดการความเสี่ยงสภาพภูมิอากาศ ของหน่วยงานราชการและภาคเอกชน
*   **3.3.5 โครงการที่กำลังดำเนินการ (Project Tracking Status)**:
    *   ระบบติดตามสถานะและการดำเนินงานโครงการปรับตัวของประเทศ (เช่น โครงการประกันภัยพืชผล, การใช้งานระบบฐานข้อมูล Agri-Map, การปรับปรุงโครงสร้างควบคุมน้ำ) `[4, SHOULD]`
    *  Adaptation Finance Tracker: Sankey diagram of finance streams and annual estimates

### 3.4 การติดตาม ประเมินผล และถอดบทเรียน (M&E and Learning)
*   **3.4.1 แนวทางการติดตามและประเมินผลการปรับตัว**:
    *   กรอบการวิเคราะห์ระดับความก้าวหน้าทางเทคโนโลยีและนวัตกรรมปรับตัว (Technology Readiness Levels - TRL in Adaptation) `[4, SHOULD]`
    *   ความเชื่อมโยงกับตัวชี้วัดเป้าหมายการปรับตัวระดับโลก (Global Goal on Adaptation - GGA Indicators) `[4, MUST]`
*   **3.4.2 ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย (Adaptation M&E Platform)**:
    *   ดัชนีติดตามความก้าวหน้าและระดับการลดความเปราะบางรายภาคส่วนและรายจังหวัด (National M&E Tracker) `[4, MUST]`
*   **3.4.3 กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ**:
    *   คลังบทเรียนโครงการเด่น (Flagship Projects Case Studies) ถอดบทเรียนความสำเร็จ อุปสรรค และแนวทางปฏิบัติที่เป็นเลิศ (Best Practices) `[6, SHOULD]`

---

## 4. เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ (Tools & Services)
*   **4.1 บัญชีข้อมูล (Data Catalog)**: ระบบสืบค้นชุดข้อมูลดิบ (Raw Datasets) ผลิตภัณฑ์วิเคราะห์ข้อมูล และข้อมูลอธิบาย (Metadata Directory) ตามเกณฑ์มาตรฐานความมั่นคงปลอดภัย
*   **4.2 Visualization and Analytics Application (Climate Risk Map Tools)**: ระบบโปรแกรมประยุกต์แสดงแผนที่ภัยและวิเคราะห์ความเสี่ยงเชิงโต้ตอบ สำหรับดึงตัวแปรไปใช้งานวิศวกรรมโยธา (เช่น ค่าคาดการณ์ปริมาณฝนและอุณหภูมิในระดับแปลงที่แปลงเป็นเกณฑ์ออกแบบ Design Curves/IDF Curves) `[2, MUST]`
*   **4.3 ศูนย์รวมเครื่องมือและแหล่งข้อมูลภายนอก**: จุดเชื่อมต่อไปยังพอร์ทัลข้อมูลระดับสากลและพอร์ทัลเฉพาะทาง (เช่น TMD Weather API, GISTDA Geo-Informatics Portal, Copernicus Climate Data Store)

---

## 5. ข่าว ประกาศ และช่องทางการติดต่อ (News and Contact)
*   **5.1 ประกาศและกิจกรรมการมีส่วนร่วม**: ระบบกระจายข่าวสารการอัปเดตข้อมูล กิจกรรมอบรมเชิงปฏิบัติการ (Workshops) ในการวิเคราะห์และตีความข้อมูลสภาพภูมิอากาศเพื่อการวางแผนเชิงพื้นที่
*   **5.2 ช่องทางการรับฟังข้อคิดเห็นและบริการผู้ใช้ (Feedback & Helpdesk)**: แพลตฟอร์มรับเสียงสะท้อนจากหน่วยงานผู้ใช้งานในแบบที่เป็นระบบเพื่อปรับปรุงคุณภาพชุดข้อมูล ขยายขอบเขตการบริการ และทวนสอบการตอบสนองความต้องการเชิงสถาบัน
