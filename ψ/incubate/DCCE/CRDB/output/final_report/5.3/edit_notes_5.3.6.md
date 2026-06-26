# Edit Notes for 5.3.6

## Topic 1: การทบทวนกลไกการจัดการความเสี่ยงจากสาธารณภัยของประเทศไทย
- **Organization Names (อ้างอิง พ.ร.บ. ปภ. และ แผน ปภ. ชาติ):**  %% refer tothe source %%
  - แก้ไขระดับพื้นที่เป็น "ผู้อำนวยการท้องถิ่น/อำเภอ"
  - แก้ไขระดับจังหวัดเป็น "ผู้อำนวยการจังหวัด (ผู้ว่าราชการจังหวัด)"
  - แก้ไขระดับชาติเป็น "กองบัญชาการป้องกันและบรรเทาสาธารณภัยแห่งชาติ (บกปภ.ช.)"
- **Data Flow Source (สายการรายงาน):** %% refer tothe source %%
  - ลบประโยคที่ดูเยิ่นเย้อและใช้คำกริยาไม่เหมาะสมออก
  - ใช้คำอธิบายโครงสร้างแทน: "ระบบสายการรายงานสถานการณ์ฉุกเฉินตามระเบียบของกระทรวงมหาดไทย ซึ่งถูกออกแบบให้มีเส้นทางข้อมูลจากระดับท้องถิ่น (อปท.) ผ่านระดับอำเภอ และบูรณาการข้อมูลที่ ปภ. จังหวัด ก่อนส่งสู่ส่วนกลาง"
- **Style/Tone:**
  - ปรับคำว่า "สถาปัตยกรรมด้านการจัดการความเสี่ยง..." เป็น "การจัดการความเสี่ยง..."
  - ปรับคำว่า "แก่นแท้ของยุทธศาสตร์..." เป็น "ใจความหลักของยุทธศาสตร์..."
  - ตัดคำว่า "มุ่ง" ออกจาก "มุ่งเน้น"
  - เปลี่ยน "ก่อให้เกิดความท้าทายเชิงโครงสร้างอย่างมีนัยสำคัญ" เป็น "ก่อให้เกิดช่องว่างของข้อมูล"

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]]
## Topic 2: แนวปฏิบัติด้านการจัดเก็บข้อมูลของกรมป้องกันและบรรเทาสาธารณภัย และมาตรฐาน PDNA
- **Style/Tone:**
  - ลบภาษาอังกฤษในวงเล็บที่ฟุ่มเฟือยและไม่จำเป็นทิ้งทั้งหมด (เช่น Operational Reality, Central Coordinating Node)
  - ใช้คำศัพท์ทางการที่ชัดเจน เช่น เปลี่ยน 'เจ้าหน้าที่ระดับท้องถิ่น' เป็น 'เจ้าหน้าที่ป้องกันและบรรเทาสาธารณะภัยขององค์กรปกครองส่วนท้องถิ่น'
  - เปลี่ยน 'มาตรฐานฐานราก' เป็น 'มาตรฐานพื้นฐาน' %% ฐานราก is not natural Thai word %%
- **Structure/Content Addition (PDNA Explanation):**
  - *ปัญหา:* รายงานด่วนสรุปว่า PDNA ใช้ไม่ได้จริง โดยยังไม่ได้อธิบายว่ามันคืออะไร
  - *การแก้ไข:* ต้องแทรกย่อหน้าอธิบายว่า PDNA คืออะไร (หลักการของ World Bank, การคำนวณ Damage/Loss) เพื่อปูพื้นฐานให้ผู้อ่านเห็นความซับซ้อน ก่อนที่จะสรุปว่ามันใช้เป็นแบบฟอร์มหน้างานไม่ได้
- **Adding Examples for Baseline Data:**
  - *ปัญหา:* ตัวอย่างข้อมูลฐาน (Baseline Data) มีน้อยเกินไป ทำให้ไม่เห็นภาพความยาก
  - *การแก้ไข:* เพิ่มตัวอย่าง Baseline Data เชิงเศรษฐศาสตร์ เช่น 'ราคาผลผลิตเฉลี่ยย้อนหลัง', 'สถิติอัตราการเข้าพักของโรงแรมในสภาวะปกติ', หรือ 'โครงสร้างรายได้ครัวเรือนก่อนเกิดภัย' %% you must not make this up. refer to the sources %%

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/Post Disaster Needs Assessment report by DDPM|Post Disaster Needs Assessment report by DDPM]]


## Topic 3: การทบทวนมาตรฐานข้อมูลสาธารณภัยระดับสากล
- **Style/Tone (ห้ามเด็ดขาด):**
  - ห้ามใช้คำศัพท์แนว Hyperbolic/นิยาย เช่น 'เยี่ยมยุทธ์', 'อย่างแยบยล'
  - เลิกแปล 'as' เป็น 'ในฐานะ' พร่ำเพรื่อ
  - ห้ามใช้คำว่า 'มุ่งเน้น' ให้ใช้ 'เน้น' (ตามกฎ)
- **Content Corrections:**
  - *UNDRR:* แก้คำแปลเป็น 'สำนักงานลดความเสี่ยงจากภัยพิบัติแห่งสหประชาชาติ'
  - *Event Card:* อธิบายเพิ่มว่าเป็น 'แบบฟอร์มบันทึกเหตุการณ์รายพื้นที่ (Local Event Data Card)' %% ที่ประกอบไปด้วย field อะไรบ้าง %%
  - *ขอบเขตเชิงพื้นที่ที่ซ้อนทับกัน:* ตัดทิ้ง/แก้เป็น 'จัดเก็บข้อมูลตามพิกัดทางภูมิศาสตร์และระดับเขตการปกครอง'
  - *ECLAC:* เพิ่มชื่อภาษาอังกฤษ (Economic Commission for Latin America and the Caribbean) กำกับไว้
  - *Counterfactual Baselines:* อธิบายตามที่คุณเสริมไว้ (เทียบกรณีที่ไม่มีภัยพิบัติกับสิ่งที่เกิดขึ้นจริง) เพราะถูกต้องตามหลัก PDNA แล้ว
  - *ก้าวข้ามข้อจำกัดแบบครอบจักรวาล:* แก้ให้เป็นภาษาคน เช่น 'เปลี่ยนจากการประเมินแบบภาพรวม มาสู่การประเมินรายสินค้าเกษตร'
  - *ตัวชี้วัดทางจิตสังคม:* แก้เป็น 'ตัวชี้วัดด้านผลกระทบทางสังคมและสวัสดิภาพของมนุษย์'

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis|Disaster_Loss_Standards_Analysis]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]] for event card (change event card -> data card to be aligned with DesInventar)



## Topic 4: ความคาดหวังตามมาตรฐาน PDNA กับสถานการณ์การจัดการข้อมูลด้านสาธารณภัยของ ปภ.
- **Style/Tone (กฎหมายเหล็ก):**
  - ห้ามใช้เครื่องหมาย Em dash ('—') ในเอกสารภาษาไทยเด็ดขาด
  - เลิกนิสัยอวยระบบราชการ (Positivity Bias) ห้ามใช้คำว่า 'เป็นเลิศ', 'Operationally Robust', หรือ 'ทันท่วงที' เมื่อพูดถึงระบบเอกสาร ปภ.
- **Content Corrections:**
  - *ความชัดเจนของมาตรฐาน:* ระบุชื่อ PDNA ให้ชัดเจน ไม่ใช้คำลอยๆ 'กรอบทฤษฎี...ของ...'
  - *Fact Check เรื่อง PDNA:* ลบเงื่อนไข 'ต้องมีพิกัดภูมิสารสนเทศที่แม่นยำ' ออก เพราะ PDNA ไม่ได้บังคับขนาดนั้น (บังคับแค่เรื่อง Baseline และ Sectoral Disaggregation)
  - *ย่อหน้าสรุป (The 'Horse Shit' paragraph):* ลบข้อความเวิ่นเว้อทิ้งทั้งหมด แล้วเขียนสรุปใหม่แบบตรงไปตรงมาว่า: 'ไม่สามารถนำแบบฟอร์ม PDNA ไปให้หน่วยปฏิบัติหน้างานกรอกได้โดยตรง แต่จะต้องแก้ปัญหาด้วยการออกแบบโครงสร้างฐานข้อมูล (Data Architecture) ที่เชื่อมโยงข้อมูลภัยพิบัติดิบ (Disaster Record) เข้ากับตารางประเมินมูลค่า (L&D Table) ในภายหลัง'
%% you need an analysis or thinking before writing this. We need to redo "ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel". archive old artifacts and create a new plan. It has to start with fully understand PDNA, then DesInventar and DaLA , before bridging between 1. what DDPM is capable right now 2. the PDNA that DDPM strives to achieve 3. the actual Loss and Damage databage that is systematic and traceable and comparable to international standards %%
sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/Post Disaster Needs Assessment report by DDPM|Post Disaster Needs Assessment report by DDPM]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm|2025-05-10-additional-note-about-loss-and-damage-from-ddpm]]


## Topic 5 & 6: โครงสร้าง MVD และ Relational L&D Tables (เชื่อมโยงกับบทสรุป Topic 4)
- **Strategic Link to Topic 4:**
  - Topic 5 และ 6 จะต้องสะท้อนการรื้อทำใหม่ (Redo) ของ `06_LDM_LossDamage_DataModel` ตามคอมเมนต์ใน Topic 4
  - การออกแบบจะต้องเกิดจากการวิเคราะห์และเข้าใจ (1) PDNA, (2) DesInventar, และ (3) DaLA อย่างถ่องแท้
  - สร้างสะพานเชื่อมระหว่าง: (1) ศักยภาพปัจจุบันของ ปภ. -> (2) PDNA ที่ ปภ. อยากไปให้ถึง -> (3) ฐานข้อมูล L&D ของจริงที่เป็นระบบ ตรวจสอบย้อนกลับได้ และเทียบเคียงสากลได้
- **Style/Tone:**
  - ตัดคำโฆษณาที่ฟุ่มเฟือยทิ้งทั้งหมด (เช่น 'ไร้รอยต่อ', 'ขุมพลังที่แท้จริง')
- **Design Answer: Timing of Data Collection:**
  - ระบุให้ชัดเจนว่า L&D Assessment **พึ่งพา Post-disaster Data Collection** (ทำโดยทีมเฉพาะกิจ) เป็นหลัก
  - ข้อมูลฉุกเฉิน (Response-phase) จากท้องถิ่น ทำหน้าที่แค่สร้าง 'เหตุการณ์ตั้งต้น (DISASTER_RECORD)' ไม่ได้มีหน้าที่เก็บข้อมูลประเมินเศรษฐศาสตร์
- **Data Architecture Visualization:**
  - ต้องนำเสนอหน้าตาของตารางให้เห็นภาพชัดเจน
  - แสดงความสัมพันธ์แบบ 1-to-Many ระหว่าง 'ตารางเหตุการณ์ (DISASTER_RECORD)' และ 'ตารางประเมินผลกระทบ (LOSS_DAMAGE_RECORD)'
  - ต้องมีเขตข้อมูล (Fields) ที่แยกส่วนระหว่าง Physical Damage, Damage Value (THB), และ Loss Value (THB) ให้ชัดเจน
- **Alignment Requirement:**
  - โครงสร้างเขตข้อมูลจะต้องล้อตามมาตรฐานจากสไลด์ของสภาพัฒน์ฯ (NESDC) และแบบฟอร์ม PDNA ของ ปภ.

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/NESDC-Loss-and-damage-database-presentation-slide|NESDC-Loss-and-damage-database-presentation-slide]]
- (อ้างอิงร่วมกับแหล่งข้อมูลใน Topic 4 ทั้งหมด)
