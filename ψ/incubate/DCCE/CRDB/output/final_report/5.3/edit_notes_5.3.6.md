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
- **บทบาทของหัวข้อนี้:**
  - ทำหน้าที่อธิบายจุดตัดระหว่างการเก็บข้อมูลระยะตอบสนองของ ปภ. กับกระบวนการประเมินหลังภัยพิบัติแบบ PDNA
  - ต้องทำให้ผู้อ่านเห็นว่า ปภ. มีระบบเก็บข้อมูลจริงอยู่แล้ว แต่ระบบนั้นตอบโจทย์คนละช่วงเวลาและคนละระดับความลึกกับ PDNA
- **โครงเรื่องที่ควรใช้:**
  1. เริ่มจากอธิบายแนวปฏิบัติการเก็บข้อมูลของ ปภ. ในระยะต้น
  2. ต่อด้วยการอธิบายว่า PDNA คือกรอบประเมินหลังภัยพิบัติที่เริ่มทำงานหลังพ้นช่วงแจ้งเหตุเร่งด่วน
  3. ปิดด้วยการชี้ให้ชัดว่า ข้อมูลของ ปภ. หยุดตรงไหน และ PDNA เริ่มตรงไหน
- **ข้อเท็จจริงหลักที่ต้องปรากฏ:**
  - ปภ. มีหลักฐานชัดเรื่องแบบประเมินระยะต้นและระยะประเมินเร่งด่วน ได้แก่ Phase 1 initial assessment และ Phase 2 MIRA/CLA style assessment ซึ่งเน้นจำนวนผู้ได้รับผลกระทบ การอพยพ ผู้เสียชีวิต ผู้บาดเจ็บ ความเสียหายเบื้องต้นของที่อยู่อาศัย สาธารณูปโภค และความต้องการเร่งด่วน
  - PDNA ในหลักฐานชุดนี้ไม่ได้เป็นแบบฟอร์มใบเดียว แต่เป็นกระบวนการระยะหลังที่เชื่อมข้อมูลฐานก่อนเกิดภัย การประเมินความเสียหาย การประเมินความสูญเสีย การทวนสอบ และการจัดทำแผนฟื้นฟู
  - หลักฐานที่มีน้ำหนักที่สุดในรายละเอียดฟิลด์ของ PDNA อยู่ในภาคเกษตร จึงใช้เพื่ออธิบายหลักการเชิงสถาปัตยกรรมข้อมูลได้ แต่ยังไม่ควรอ้างว่าเป็นภาพครบทุกภาคส่วน
- **คำอธิบาย PDNA ที่ควรแทรกในร่างต่อไป:**
  - PDNA เป็นกระบวนการประเมินความต้องการหลังภัยพิบัติที่ต้องอาศัยการเปรียบเทียบระหว่างสภาพปกติก่อนเกิดภัยกับสภาพหลังเกิดภัย และแยกผลกระทบออกอย่างน้อยเป็นความเสียหายทางกายภาพ ความสูญเสียทางเศรษฐกิจ และความต้องการฟื้นฟู/ฟื้นสภาพ
  - ต้องอธิบายให้เห็นว่า ความเสียหาย กับ ความสูญเสีย ไม่ใช่ข้อมูลชนิดเดียวกัน: ความเสียหายคือทรัพย์สินหรือโครงสร้างที่ถูกทำลาย ส่วนความสูญเสียคือการเปลี่ยนแปลงของผลผลิต รายได้ บริการ หรือค่าใช้จ่ายเมื่อเทียบกับสภาวะปกติ
- **ตัวอย่าง baseline data ที่มีหลักฐานรองรับและควรใช้เป็นตัวอย่างเชิงอธิบาย:**
  - ข้อมูลครัวเรือนเกษตร
  - ข้อมูลผลผลิตหรือปริมาณการผลิตก่อนเกิดภัย
  - ความพร้อมในการนำผลผลิตออกสู่ตลาดรายเดือน
  - แหล่งน้ำเพื่อการเกษตร
  - ปัจจัยการผลิตและทรัพย์สินทางการเกษตร
  - หมายเหตุ: ถ้าจะยกตัวอย่างนอกภาคเกษตร ต้องเขียนในเชิงหลักการ ไม่ใช่ยืนยันว่าปรากฏในแบบฟอร์ม DDPM ที่ตรวจพบแล้ว
- **ประโยคแกนที่ควรสื่อในย่อหน้าสรุป:**
  - แนวปฏิบัติของ ปภ. ในปัจจุบันมีความเข้มแข็งมากกว่าสำหรับการบันทึกเหตุการณ์และผลกระทบเบื้องต้นในช่วงต้นของเหตุการณ์ ขณะที่ PDNA เริ่มต้นเมื่อจำเป็นต้องสร้างข้อมูลฐาน เปรียบเทียบก่อนและหลังภัย แยกความเสียหายออกจากความสูญเสีย และทวนสอบผลการประเมินร่วมกับหน่วยงานภาคส่วน
- **ข้อควรหลีกเลี่ยง:**
  - อย่าเขียนว่า ปภ. ยังไม่ทำ PDNA แบบเหมารวม เพราะหลักฐานชี้ว่ามีกรอบและบทบาทอยู่ใน workflow ระยะหลัง เพียงแต่ไม่ได้หมายความว่าข้อมูลหน้างานระยะต้นเท่ากับ PDNA
  - อย่าเขียนว่า PDNA ใช้ไม่ได้จริง ให้เขียนว่า PDNA ไม่ได้ถูกออกแบบมาเพื่อใช้เป็นแบบกรอกหน้างานในหน้าต่างเวลา 0-72 ชั่วโมง

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/Post Disaster Needs Assessment report by DDPM|Post Disaster Needs Assessment report by DDPM]]


## Topic 3: การทบทวนมาตรฐานข้อมูลสาธารณภัยระดับสากล
- **บทบาทของหัวข้อนี้:**
  - ไม่ใช่การลำดับว่าใครดีกว่าใคร แต่เป็นการอธิบายว่าแต่ละมาตรฐานถูกออกแบบมาเพื่อแก้ปัญหาคนละแบบ และจึงต้องอ่านแบบเสริมกัน
- **โครงเปรียบเทียบที่ควรใช้:**
  1. DesInventar = มาตรฐานสำหรับการลงทะเบียนเหตุการณ์และผลกระทบขั้นต่ำอย่างเป็นระบบ
  2. DaLA = มาตรฐานสำหรับการประเมินมูลค่าความเสียหาย ความสูญเสีย และความต้องการฟื้นฟู/ก่อสร้างใหม่ในเชิงเศรษฐกิจ
  3. PDNA = มาตรฐานหรือ workflow สำหรับเชื่อมการประเมินหลายภาคส่วนไปสู่การฟื้นฟูหลังภัยพิบัติ
  4. สรุปว่า 3 ระบบนี้ไม่ทับกันทั้งหมด แต่ต่อกันเป็นลำดับงานได้
- **ประเด็นที่ต้องอธิบายชัด:**
  - **DesInventar** ควรถูกอธิบายว่าเป็นระบบแบบ event card หรือ local event data card ที่เก็บอย่างน้อยประเภทภัย วันเวลา พื้นที่ ผลกระทบต่อคน ความเสียหายเบื้องต้น และข้อมูลเชิงพื้นที่/เขตการปกครอง เพื่อให้เกิดทะเบียนเหตุการณ์ที่เปรียบเทียบย้อนหลังได้
  - **DaLA** ต้องอธิบายว่าเน้นการตีมูลค่าทรัพย์สินที่เสียหายและการเปลี่ยนแปลงของกระแสทางเศรษฐกิจ จึงต้องพึ่งข้อมูลฐานก่อนเกิดภัย การประมาณการตามภาคส่วน และสมมติฐานด้านราคา/ต้นทุน
  - **PDNA** ต้องอธิบายว่าอยู่กึ่งกลางระหว่างการประเมินผลกระทบกับการกำหนดแผนฟื้นฟู โดยเพิ่มมิติของการทวนสอบ การมีส่วนร่วมของหน่วยงานภาคส่วน และการจัดทำ recovery strategy
- **ถ้อยคำสรุปเชิงเปรียบเทียบที่ควรใช้:**
  - DesInventar เน้นการตอบคำถามว่า เกิดอะไรขึ้น ที่ไหน เมื่อไร และกระทบใครบ้าง
  - DaLA เน้นการตอบคำถามว่า ทรัพย์สินเสียหายเท่าไร สูญเสียทางเศรษฐกิจเท่าไร และต้องใช้ทรัพยากรฟื้นฟูเท่าไร
  - PDNA เน้นการตอบคำถามว่า เมื่อประเมินผลกระทบแล้ว ภาคส่วนต่าง ๆ จะทวนสอบและแปลงผลประเมินนั้นไปสู่แผนฟื้นฟูอย่างไร
- **จุดเชื่อมที่ต้องโยงเข้าบทต่อไป:**
  - DesInventar ให้ตรรกะของชั้นข้อมูลตั้งต้น
  - DaLA ให้ตรรกะของการแยก physical damage ออกจาก economic loss
  - PDNA ให้ตรรกะของ workflow การประเมิน การทวนสอบ และการจัดทำ needs/recovery
  - ดังนั้น CRDB ไม่ควรลอกแบบใดแบบหนึ่งทั้งชุด แต่ควรสังเคราะห์เป็นสถาปัตยกรรมหลายชั้น
- **คำแก้เชิงสำนวน/เนื้อหา:**
  - ใช้คำว่า 'สำนักงานลดความเสี่ยงจากภัยพิบัติแห่งสหประชาชาติ' สำหรับ UNDRR
  - เพิ่มชื่อเต็มของ ECLAC ไว้ครั้งแรก
  - อธิบาย counterfactual baseline แบบตรงไปตรงมา: เปรียบเทียบสิ่งที่เกิดขึ้นจริงหลังภัย กับสิ่งที่คาดว่าจะเกิดขึ้นหากไม่มีภัย
  - เมื่อต้องอธิบายการเปลี่ยนระดับการประเมิน ให้ใช้ภาษาง่าย เช่น จากการสรุปภาพรวม ไปสู่การประเมินแยกรายภาคส่วนหรือรายสินค้า
- **ข้อควรหลีกเลี่ยง:**
  - อย่าเขียนว่า PDNA เป็นเพียงส่วนขยายของ DaLA หรือว่า DesInventar เป็นฐานข้อมูลที่ใช้แทน PDNA ได้ทั้งหมด
  - อย่าใช้สำนวนอวยเกินจริง ให้คงโหมดเปรียบเทียบเชิงหน้าที่และข้อจำกัด

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis|Disaster_Loss_Standards_Analysis]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]] for event card (change event card -> data card to be aligned with DesInventar)



## Topic 4: ความคาดหวังตามมาตรฐาน PDNA กับสถานการณ์การจัดการข้อมูลด้านสาธารณภัยของ ปภ.
- **บทบาทของหัวข้อนี้:**
  - เป็นหัวข้อที่ต้องพูดให้ตรงที่สุดเรื่องช่องว่างระหว่างสิ่งที่ PDNA ต้องการ กับสิ่งที่ ปภ. เก็บได้จริงในระบบงานปัจจุบัน
  - น้ำเสียงต้องเป็นการวิเคราะห์ข้อจำกัดเชิงโครงสร้าง ไม่ใช่การตำหนิหน่วยงาน และไม่ใช่การยกย่องเกินจริง
- **โครงสร้างการอธิบายที่ควรใช้:**
  1. ยืนยันก่อนว่า PDNA ต้องการข้อมูลแบบ baseline-driven, sectorally disaggregated, validation-heavy
  2. อธิบายว่า DDPM current practice เข้มแข็งที่การแจ้งเหตุ การรวบรวมผลกระทบเบื้องต้น และการประเมินเร่งด่วนหลายมิติ
  3. ชี้ความต่างว่า PDNA ต้องใช้เวลาหลังเหตุ ต้องมีทีมภาคส่วน ต้องมีการทวนสอบ และต้องมีข้อมูลฐานก่อนเกิดภัย
  4. สรุปว่า ปัญหาไม่ใช่เจ้าหน้าที่หน้างานกรอกข้อมูลไม่ครบ แต่เป็นภารกิจคนละประเภทกัน
- **ประเด็นเปรียบเทียบที่ต้องระบุให้ชัด:**
  - PDNA ต้องการการแยกข้อมูลรายภาคส่วนและการประเมินตามตรรกะของ damage, loss, validation, recovery strategy
  - ระบบข้อมูลระยะต้นของ ปภ. เน้น direct human impacts, housing/infrastructure damage counts, emergency needs, และข้อมูลการตอบสนอง
  - PDNA ต้องการ baseline และการเปรียบเทียบก่อน/หลังภัย ขณะที่ข้อมูลระยะต้นของ ปภ. ไม่ได้ถูกออกแบบมาเพื่อเก็บ baseline ทางเศรษฐกิจโดยตรง
  - PDNA ต้องอาศัยการทวนสอบและบทบาทของหน่วยงานภาคส่วน ขณะที่แบบประเมินระยะต้นของ ปภ. ถูกออกแบบมาเพื่อการรายงานสถานการณ์และประสานการตอบสนอง
- **ประเด็น fact check ที่ต้องรักษา:**
  - อย่าไปผูก PDNA ไว้กับเงื่อนไขว่าต้องมีพิกัดภูมิสารสนเทศละเอียดมากเป็นแกนหลัก เพราะหลักฐานที่ตรวจได้ชี้น้ำหนักไปที่ baseline, sector disaggregation, valuation, validation มากกว่า
  - ต้องเรียกชื่อ PDNA ให้ตรง ไม่ใช้คำลอย
- **ประโยคสรุปแกนกลางที่ควรใช้:**
  - ไม่สามารถนำแบบฟอร์มหรือความคาดหวังของ PDNA ไปใช้เป็นแบบกรอกข้อมูลหน้างานโดยตรงได้ เพราะ PDNA เป็นกระบวนการประเมินหลังภัยพิบัติที่ต้องพึ่งข้อมูลฐาน การวิเคราะห์เชิงภาคส่วน และการทวนสอบหลายรอบ
  - ทางออกที่เหมาะสมจึงไม่ใช่การบังคับให้ข้อมูลระยะต้นทำหน้าที่แทน PDNA แต่เป็นการออกแบบสถาปัตยกรรมข้อมูลที่เชื่อมระเบียนเหตุการณ์ตั้งต้นเข้ากับตารางประเมินความเสียหายและความสูญเสียในระยะหลัง
- **สะพานไป Topic 5 และ 6:**
  - ปิดหัวข้อนี้ด้วยเหตุผลเชิงออกแบบว่า เมื่อมาตรฐาน PDNA กับความสามารถเชิงปฏิบัติการปัจจุบันไม่อยู่ในชั้นข้อมูลเดียวกัน ฐานข้อมูลเป้าหมายจึงต้องออกแบบแบบ layered และ relational
  - ให้ผู้อ่านพร้อมรับการอธิบายต่อว่า event record, assessment context, damage table, loss table, และ needs table ต้องแยกกันแต่เชื่อมกัน
sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation|raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/Post Disaster Needs Assessment report by DDPM|Post Disaster Needs Assessment report by DDPM]]
- [[ψ/incubate/DCCE/CRDB/inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm|2025-05-10-additional-note-about-loss-and-damage-from-ddpm]]


## Topic 5 & 6: โครงสร้าง MVD และ Relational L&D Tables (เชื่อมโยงกับบทสรุป Topic 4)
- **บทบาทของ 2 หัวข้อนี้:**
  - ต้องเปลี่ยนจากการพูดเชิงนามธรรมเรื่องควรมีฐานข้อมูล ไปสู่การอธิบายโครงสร้างข้อมูลที่พร้อมใช้เป็นแนวร่างสำหรับการเขียนรายงานไทยในรอบถัดไป
  - ให้ถือว่า Topic 5 คือการอธิบายตรรกะของ layered MVD และ Topic 6 คือการอธิบาย relational table logic และการไหลของข้อมูล
- **ประเด็นเชิงยุทธศาสตร์ที่ต้องยืนพื้น:**
  - แบบจำลองนี้เกิดจากการสังเคราะห์ 3 ตรรกะพร้อมกัน: DDPM current practice, PDNA workflow, และ DaLA damage/loss logic โดยมี DesInventar เป็นฐานคิดของ event registration
  - เป้าหมายไม่ใช่ทำสำเนาวิธีใดวิธีหนึ่ง แต่สร้างโครงสร้างไทยที่ตรวจสอบย้อนกลับได้และต่อยอดสู่มาตรฐานสากลได้
- **โครงเรื่องที่ควรใช้ใน Topic 5:**
  1. ย้ำผลสรุปจาก Topic 4 ว่าข้อมูลระยะต้นกับข้อมูลประเมินหลังภัยเป็นคนละชั้น
  2. อธิบาย three-layer logic ให้ชัด
     - Layer A: event capture reality ของ ปภ.
     - Layer B: PDNA/DaLA post-disaster assessment requirements
     - Layer C: CRDB target architecture ที่เชื่อมสองชั้นนี้เข้าด้วยกัน
  3. ชี้ว่า Layer A ต้องใกล้กับตรรกะแบบ DesInventar มากกว่า เพราะเป็นชั้นลงทะเบียนเหตุการณ์ขั้นต่ำ
  4. ชี้ว่า Layer B เป็นพื้นที่ของ baseline, valuation, validation, recovery/reconstruction needs
- **โครงเรื่องที่ควรใช้ใน Topic 6:**
  - อธิบาย entity หลักและความสัมพันธ์แบบ one-to-many ให้เห็นภาพ โดยอย่างน้อยควรมี:
    - `DISASTER_EVENT` เป็น master event anchor
    - `EVENT_LOCATION` สำหรับหลายพื้นที่ที่ได้รับผลกระทบจากเหตุเดียวกัน
    - `ASSESSMENT_CONTEXT` สำหรับเก็บ phase, method family, หน่วยงานรับผิดชอบ, สถานะการทวนสอบ, และ provenance
    - `LD_PHYSICAL_DAMAGE` สำหรับความเสียหายทางกายภาพ
    - `LD_ECONOMIC_LOSS` สำหรับความสูญเสียทางเศรษฐกิจ
    - `LD_RECOVERY_RECONSTRUCTION_NEEDS` สำหรับผลลัพธ์เชิงความต้องการฟื้นฟู/ก่อสร้างใหม่
  - ต้องอธิบายว่าความสัมพันธ์หลักไม่ใช่ event 1 record ต่อ 1 impact record แต่เป็น event 1 รายการ เชื่อมไปสู่หลาย assessment contexts และหลาย damage/loss records
- **ประเด็นเนื้อหาที่ต้องเน้นเป็นพิเศษ:**
  - ข้อมูลฉุกเฉินจากท้องถิ่นทำหน้าที่สร้าง event anchor ไม่ได้ทำหน้าที่แทนตารางประเมินเศรษฐศาสตร์
  - ตาราง damage กับ loss ต้องแยกกัน เพราะตรรกะข้อมูล หน่วยวัด วิธีคิด และช่วงเวลาการประเมินต่างกัน
  - needs table เป็นผลลัพธ์ปลายทางหลังผ่านการประเมินและทวนสอบแล้ว ไม่ใช่ข้อมูลตั้งต้นจากการแจ้งเหตุ
  - `ASSESSMENT_CONTEXT` เป็นองค์ประกอบสำคัญ เพราะช่วยกันไม่ให้ข้อมูลระยะต้นกับข้อมูลระยะประเมินเชิงลึกถูกยุบรวมเป็นระเบียนเดียว
- **ภาพจำเชิงคำอธิบายที่ควรใช้ในร่างต่อไป:**
  - `DISASTER_EVENT` ตอบว่าเกิดอะไรขึ้น ที่ไหน เมื่อไร และกระทบใครเบื้องต้น
  - `LD_PHYSICAL_DAMAGE` ตอบว่าอะไรเสียหาย เสียหายเท่าไร และตีมูลค่าอย่างไร
  - `LD_ECONOMIC_LOSS` ตอบว่ามูลค่าทางเศรษฐกิจที่หายไปหรือค่าใช้จ่ายที่เพิ่มขึ้นคืออะไร เมื่อเทียบกับสภาพปกติ
  - `LD_RECOVERY_RECONSTRUCTION_NEEDS` ตอบว่าหลังจากประเมินและทวนสอบแล้ว ต้องใช้ทรัพยากรอะไรเพื่อฟื้นฟูหรือสร้างกลับ
- **ข้อกำกับเรื่อง alignment:**
  - ให้โยงกับสไลด์ของ สศช. และตรรกะฟอร์ม PDNA ในระดับโครงสร้างข้อมูล ไม่ใช่อ้างว่าฟิลด์ทั้งหมดมีรายละเอียดพร้อมใช้อยู่แล้วในระบบปัจจุบัน
  - ต้องคง caveat ว่ารายละเอียด field-level ของ PDNA ที่ใช้รองรับการออกแบบยังมีน้ำหนักไปทางภาคเกษตร
- **ข้อควรหลีกเลี่ยง:**
  - อย่าใช้คำโฆษณาเชิงระบบ เช่น ไร้รอยต่อ หรือ สมบูรณ์แบบ
  - อย่าทำให้ดูเหมือนว่าฐานข้อมูลนี้จะเก็บทุกอย่างได้ตั้งแต่วันแรก ให้เขียนในฐานะ staged target architecture

sources:
- [[ψ/incubate/DCCE/CRDB/inbox_source/NESDC-Loss-and-damage-database-presentation-slide|NESDC-Loss-and-damage-database-presentation-slide]]
- (อ้างอิงร่วมกับแหล่งข้อมูลใน Topic 4 ทั้งหมด)


## Consolidated source inventory for 5.3.6 / 5.3.7 repair

### A. Core DDPM / PDNA / loss-and-damage evidence
- [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:1)
- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:1)
- [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:1)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:1)
- [`DesInventar as a Disaster Information Management System.md`](../../inbox_source/DesInventar%20as%20a%20Disaster%20Information%20Management%20System.md:1)
- [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:1)

### B. CRDB LDM design and gap-analysis artifacts
- [`comparative_analysis_DaLA_DesInventar_PDNA.md`](../../06_LDM_LossDamage_DataModel/comparative_analysis_DaLA_DesInventar_PDNA.md:1)
- [`DaLA_methodology_report.md`](../../06_LDM_LossDamage_DataModel/DaLA_methodology_report.md:1)
- [`DDPM_CRI_to_CRDB_MVD_gap_analysis.md`](../../06_LDM_LossDamage_DataModel/DDPM_CRI_to_CRDB_MVD_gap_analysis.md:1)
- [`DDPM_data_review_from_CRI_project.md`](../../06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:1)
- [`DDPM_PDNA_methodology_report.md`](../../06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:1)
- [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](../../06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:1)

### C. NotebookLM raw runs and traceability files
- [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json:1)
- [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json:1)
- [`notebooklm_runs/2026-06-26_0903_raw_ddpm.txt`](../../../../notebooklm_runs/2026-06-26_0903_raw_ddpm.txt:1)
- [`notebooklm_runs/2026-06-26_0852_raw_dala_error.json`](../../../../notebooklm_runs/2026-06-26_0852_raw_dala_error.json:1)
- [`notebooklm_runs/2026-06-26_0852_raw_ddpm_error.json`](../../../../notebooklm_runs/2026-06-26_0852_raw_ddpm_error.json:1)

### D. Why these were added
- The DDPM / PDNA / DesInventar files provide the factual basis for Topics 1–4.
- The LDM design artifacts provide the target schema and the gap analysis for Topics 5–6.
- The NotebookLM raw runs preserve the verbatim evidence trail for the DDPM / DaLA conclusions.
- The NotebookLM error files are retained for traceability of retrieval failures and authentication issues.
