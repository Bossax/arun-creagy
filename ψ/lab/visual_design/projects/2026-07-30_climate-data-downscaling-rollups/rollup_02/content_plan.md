# Roll-up 02 Draft 3 — Content Plan

**Theme:** Downscaling and DCCE climate-data products
**Relationship to Roll-up 01:** Roll-up 01 explains why projections matter for planning. Roll-up 02 explains how global model information is translated into locally usable data and how users can choose among methods and products.

## Primary reader question and thesis

**Reader question:** แบบจำลองระดับโลกถูกแปลงให้เป็นข้อมูลที่ใช้วิเคราะห์ระดับพื้นที่ได้อย่างไร และควรเลือกผลิตภัณฑ์แบบใดให้เหมาะกับงาน?

**Thesis:** การลดสเกลช่วยแปลข้อมูลจากแบบจำลองระดับโลกให้เหมาะกับคำถามและพื้นที่มากขึ้น แต่แต่ละวิธีและผลิตภัณฑ์มีจุดเด่นต่างกัน จึงต้องเลือกใช้โดยดูจากกลไก ความละเอียด ตัวแปร และการตัดสินใจที่ต้องการสนับสนุน

## Reader-value gate — Insight Card 02

| Field | Content |
|---|---|
| **Reader question** | เหตุใดจึงต้องมีทั้งการลดสเกลเชิงพลศาสตร์และเชิงสถิติ แทนที่จะใช้วิธีเดียวกับทุกงาน? |
| **Source-specific finding** | การลดสเกลเชิงพลศาสตร์จำลองกระบวนการทางฟิสิกส์และภูมิประเทศ ขณะที่การลดสเกลเชิงสถิติใช้ความสัมพันธ์เชิงประจักษ์กับข้อมูลท้องถิ่น ทั้งสองวิธีจึงตอบโจทย์คนละแบบ |
| **Mechanism** | RCM คำนวณบรรยากาศในพื้นที่ย่อยของแบบจำลองระดับโลก ส่วนวิธีเชิงสถิติเรียนรู้ความสัมพันธ์ระหว่างตัวแปรแบบจำลองกับข้อมูลสถานีหรือข้อมูลอ้างอิง |
| **Consequence** | ผู้ใช้เลือกวิธีและผลิตภัณฑ์ให้เหมาะกับงานวิจัยเชิงฟิสิกส์ งานวิเคราะห์เชิงพื้นที่ งานคุณภาพอากาศ หรืองานประเมินทางเลือกอย่างรวดเร็วได้ดีขึ้น |
| **Visual proof** | ภาพเปรียบเทียบ “กล่องแบบจำลองระดับโลก → กลไกการลดสเกล 2 แบบ → ผลิตภัณฑ์ 4 กลุ่ม” |
| **Evidence anchor** | `SCI-01`, `SCI-02`, `WEB-01`, `IMG-02`, `IMG-03`, `IMG-04` ใน `00_project/evidence_map.md` |

## Message hierarchy

1. **Why:** ข้อมูลระดับโลกมีขนาดช่องตารางหยาบ จึงอาจไม่สะท้อนภูเขา ชายฝั่ง เมือง และความแตกต่างระดับพื้นที่ได้เพียงพอ
2. **How:** การลดสเกลมีสองแนวทางหลัก—เชิงพลศาสตร์และเชิงสถิติ—ซึ่งใช้กลไกและเหมาะกับงานต่างกัน
3. **What:** DCCE มีผลิตภัณฑ์ 4 กลุ่ม—GridData, WRF-Chem, RegCM5 และ Statistical Downscaling
4. **Choose:** เลือกผลิตภัณฑ์จากคำถาม วิธีการ ตัวแปร พื้นที่ และรูปแบบการใช้งาน ไม่ใช่เลือกจากชื่อผลิตภัณฑ์เพียงอย่างเดียว

## Content boundaries

- Do not claim that downscaling removes uncertainty or creates a single certain future.
- Do not present one resolution value as universal across all products.
- Keep product-specific resolution, coverage, and file metadata subject to the verified product record.
- Keep product names exactly as `GridData`, `WRF-Chem`, `RegCM5`, and `Statistical Downscaling`.
- Keep final text editable and separate from generated artwork.
