import csv
import os

csv_file = 'ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Platforms_Summary_v2.0.csv'

services = [
    {
        "Service ID": "S01",
        "Service Name": "National Authoritative Data Catalog & Discovery (SSOT)",
        "What it is": "A centralized, federated metadata catalog ensuring a 'Single Source of Truth' across national data repositories.",
        "How it answers use cases": "Resolves inter-agency data fragmentation for planners (UDDC) and provides a secure, PDPA-compliant data exchange highway (DGA) for sharing sensitive information. It also provides verified 'Green Impact' data for financial institutions (FTI).",
        "Core Technical Spec & Function": "DCAT-AP 3.0.0 metadata standards, GDX API integration, Article 8/15 DGA compliance, and automated masking/anonymization protocols.",
        "Thai Policy Description": "แพลตฟอร์มส่วนกลางสำหรับการค้นหาและแลกเปลี่ยนข้อมูลระดับชาติที่ทำหน้าที่เป็น 'แหล่งข้อมูลความจริงเพียงหนึ่งเดียว' (Single Source of Truth) ช่วยทะลวงคอขวดการทำงานของหน่วยงานรัฐโดยการรวมศูนย์เมทาดาทาและเชื่อมโยงข้อมูลผ่านระบบเครือข่าย GDX ของ สพร. ทำให้หน่วยงานระดับนโยบายอย่าง กรมการเปลี่ยนแปลงสภาพภูมิอากาศฯ (DCCE) และผู้ปฏิบัติงานพื้นที่ สามารถแลกเปลี่ยนข้อมูลได้อย่างปลอดภัยและถูกต้องตามกฎหมาย PDPA ตลอดจนใช้เป็นฐานข้อมูลอ้างอิงที่ภาคเอกชนและสถาบันการเงินเชื่อถือ"
    },
    {
        "Service ID": "S02",
        "Service Name": "Socio-Economic & Sectoral Vulnerability Analytics",
        "What it is": "An advanced analytics platform overlaying physical hazard data with high-resolution socio-economic and sectoral indicators (e.g., agriculture, tourism).",
        "How it answers use cases": "Moves beyond coarse averages to identify household-level exposure (NSO), track agricultural crop impacts at the plot level (LDD), and locate vulnerable groups for proactive welfare assistance (MSDHS).",
        "Core Technical Spec & Function": "Enumeration Area (EA) spatial logic (~250 buildings per block), plot-level agricultural tracking, integration with Civil Registry IDs, and SSP3/SSP5 downscaled projections.",
        "Thai Policy Description": "ระบบวิเคราะห์ความเปราะบางเชิงพื้นที่และรายภาคส่วน ที่ยกระดับความละเอียดจากการประเมินภาพรวมระดับจังหวัด ลงลึกถึงระดับชุมชน ครัวเรือน และแปลงเกษตร โดยการซ้อนทับข้อมูลภัยพิบัติเข้ากับข้อมูลทางเศรษฐกิจ สังคม และการเกษตร (LDD) ทำให้ภาครัฐสามารถระบุ 'จุดเปราะบางซ้อนทับ' ได้อย่างแม่นยำ เช่น การล็อกเป้าหมายอพยพผู้ป่วยติดเตียง หรือการกำหนดนโยบายเยียวยาพืชผลเศรษฐกิจรายแปลง"
    },
    {
        "Service ID": "S03",
        "Service Name": "Climate Investment ROI & Fiscal Planning",
        "What it is": "A financial analytics toolset designed to evaluate the economic feasibility and justify climate-related capital expenditure.",
        "How it answers use cases": "Provides local governments (DLA) with a 'Regulatory Shield'—certified Return on Investment (ROI) metrics—to justify the use of Accumulated Funds to the State Audit Office. It also helps national economists (NESDC) capture 'True Economic Loss' to adjust GDP forecasts.",
        "Core Technical Spec & Function": "World Bank 'Triple Dividend of Resilience' framework, Cost-Benefit Analysis (CBA) calculators, and direct asset damage vs. indirect logistics bottleneck modeling.",
        "Thai Policy Description": "เครื่องมือสนับสนุนการตัดสินใจทางการเงินและการคลังที่ออกแบบมาเพื่อปลดล็อกอุปสรรคด้านงบประมาณของท้องถิ่น โดยระบบจะทำหน้าที่คำนวณ 'ความคุ้มค่าของการลงทุน' (ROI) ในโครงการปรับตัวฯ และประเมิน 'ความสูญเสียทางเศรษฐกิจที่แท้จริง' เพื่อให้หน่วยงานท้องถิ่น (อปท.) มีหลักฐานเชิงประจักษ์ที่ได้รับการรับรองในการชี้แจงต่อสำนักงานการตรวจเงินแผ่นดิน (สตง.) ทำให้สามารถดึง 'เงินสะสม' ออกมาใช้ในโครงการป้องกันภัยเชิงรุกได้อย่างโปร่งใสและถูกต้องตามระเบียบ"
    },
    {
        "Service ID": "S04",
        "Service Name": "Climate Loss & Damage Assessment",
        "What it is": "A standardized accounting platform for tracking economic and non-economic losses from climate events.",
        "How it answers use cases": "Allows DDPM operators to document true asset damage, enables commercial banks (TBA) to perform asset-level financial stress tests, and empowers MOTS to quantify the economic vulnerability of tourism destinations.",
        "Core Technical Spec & Function": "Sendai Framework Target C (Economic Loss) sub-indicators, 'Replacement Cost' methodology, probabilistic flood metrics (depth/duration), and tourism sensitivity analysis.",
        "Thai Policy Description": "แพลตฟอร์มมาตรฐานสำหรับการประเมินและติดตามบัญชีความสูญเสียและความเสียหาย (Loss & Damage) จากภัยสภาพภูมิอากาศ ครอบคลุมทั้งความเสียหายเชิงสินทรัพย์และมูลค่าทางเศรษฐกิจในภาคการท่องเที่ยว (MOTS) ระบบนี้มีความสำคัญอย่างยิ่งต่อการรายงานผลระดับชาติ การจัดสรรงบเยียวยาที่สะท้อนความจริง และยังช่วยให้สถาบันการเงินสามารถทำ Stress Test พอร์ตสินเชื่อเพื่อป้องกันความเสี่ยงเชิงระบบของประเทศได้"
    },
    {
        "Service ID": "S05",
        "Service Name": "Infrastructure Risk & Engineering Specifications",
        "What it is": "A technical advisory platform that integrates future climate projections into infrastructure design codes and asset management.",
        "How it answers use cases": "Empowers engineers (DPT) to design tunnels using 'Rain Bomb' climate-adjusted rainfall curves, helps transport planners (OTP) justify retrofitting budgets down to the kilometer marker, and assists Marine Dept (MD) with port maintenance against sea-level rise.",
        "Core Technical Spec & Function": "PIANC 4-Stage Adaptation logic, climate-adjusted Intensity-Duration-Frequency (IDF) coefficients, coastal erosion rates, and 100-year hydrological flow maps linked to GIS asset IDs.",
        "Thai Policy Description": "แพลตฟอร์มสนับสนุนงานวิศวกรรมและโครงสร้างพื้นฐาน ที่ช่วยยกระดับมาตรฐานการออกแบบของประเทศ โดยการนำข้อมูลคาดการณ์สภาพภูมิอากาศในอนาคตและระดับน้ำทะเลที่สูงขึ้น (MD) มาปรับปรุงเกณฑ์การออกแบบ (Design Codes) ทำให้วิศวกรสามารถคำนวณและออกแบบระบบระบายน้ำ ท่าเรือ หรือปรับปรุงทางหลวงได้อย่างรัดกุม ตลอดจนมีหลักฐานทางวิศวกรรมที่หนักแน่นในการขออนุมัติงบประมาณ"
    },
    {
        "Service ID": "S06",
        "Service Name": "Multi-Hazard & Environmental Resource Monitoring",
        "What it is": "An operational monitoring platform providing near real-time intelligence on environmental thresholds for rapid disaster warning and slow-onset resource management.",
        "How it answers use cases": "Translates raw weather data into actionable impacts. Warns of productivity losses (FTI), heatwaves (DOH), manages critical water scarcity across basins (ONWR/HII), and monitors marine ecosystem health and coral bleaching (DMCR).",
        "Core Technical Spec & Function": "Near Real-Time API Ingestion (1-3 hour lead times), Wet Bulb Globe Temperature (WBGT) intensity thresholds, dynamic water absorption thresholds, and marine temperature forecasts.",
        "Thai Policy Description": "ระบบเฝ้าระวังและเตือนภัยล่วงหน้าแบบพหุภัยและทรัพยากรสิ่งแวดล้อม ที่ต่อยอดจากการพยากรณ์อากาศไปสู่การประเมินผลกระทบทางเศรษฐกิจ สุขภาพ และการบริหารจัดการทรัพยากรธรรมชาติ เช่น การบริหารจัดการแหล่งน้ำระดับลุ่มน้ำ (ONWR/HII) และการเฝ้าระวังปะการังฟอกขาวทางทะเล (DMCR) เพื่อให้หน่วยงานภาครัฐสามารถสั่งการเตือนภัยล่วงหน้าหรือปรับแผนการใช้น้ำได้อย่างทันท่วงที ปกป้องชีวิตประชาชนและรักษาเสถียรภาพทางเศรษฐกิจ"
    },
    {
        "Service ID": "S07",
        "Service Name": "Policy Monitoring & NAP Compliance",
        "What it is": "A strategic monitoring system for automating the tracking of national and international climate targets.",
        "How it answers use cases": "Ensures local government performance indicators align with national Climate Change Act goals (DLA), helps research councils (NXPO, PMUA) direct innovation and area-based funding toward actual capability gaps.",
        "Core Technical Spec & Function": "AI-driven thematic clustering and gap analysis, unstructured data ingestion, regional API access, and automated tracking of SDG/GGA and National Adaptation Plan (NAP) indicators.",
        "Thai Policy Description": "เครื่องมือบริหารจัดการระดับนโยบายสำหรับติดตามและประเมินผลความก้าวหน้าตามแผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ (NAP) และเป้าหมายระดับโลก (SDGs/GGA) ระบบนี้ใช้ AI วิเคราะห์ช่องว่างทางนโยบายและงานวิจัย ทำให้ผู้บริหารประเทศและหน่วยงานให้ทุน (NXPO, PMUA) สามารถจัดสรรงบประมาณกองทุนสิ่งแวดล้อมหรือทุนวิจัยไปยังพื้นที่และจุดที่ประเทศยังขาดแคลนได้อย่างตรงจุด ลดความซ้ำซ้อนของการทำงานภาครัฐ"
    }
]

with open(csv_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Service ID", "Service Name", "What it is", "How it answers use cases", "Core Technical Spec & Function", "Thai Policy Description"])
    writer.writeheader()
    writer.writerows(services)

print("Service Platforms CSV v1.1 generated successfully.")
