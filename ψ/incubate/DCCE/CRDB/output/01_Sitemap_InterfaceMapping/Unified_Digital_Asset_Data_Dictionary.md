# พจนานุกรมข้อมูลสินทรัพย์ดิจิทัลร่วมระดับองค์กร (DCCE Unified Digital Asset Data Dictionary)

เอกสารนี้กำหนด **พจนานุกรมข้อมูล (Data Dictionary)** สำหรับฐานข้อมูลสินทรัพย์ดิจิทัลแบบบูรณาการระดับองค์กรของกรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (DCCE) โดยอ้างอิงและปรับปรุงตามกรอบการจำแนกประเภทสากล เพื่อเป็นเครื่องมือในการทำธรรมาภิบาลข้อมูล (Data Governance)

---

## 1. คำนิยามประเภทสินทรัพย์ดิจิทัล (Asset Class Definitions)

เพื่อให้อ้างอิงมาตรฐานเดียวกันทั่วทั้งองค์กร การจำแนกคลาสของสินทรัพย์ยึดตามหลักเกณฑ์ดังนี้:

*   **Data Product (ผลิตภัณฑ์ข้อมูล)**: บริการหรือแอปพลิเคชันส่วนหน้า (User-facing offering) ที่พัฒนาขึ้นจากสินทรัพย์ข้อมูล ตั้งใจออกแบบมาสำหรับการทำงานหรือวิเคราะห์ข้อมูลของหน่วยงานและบุคคลภายนอก มี Use Case, ผู้ดูแลระบบ, และคู่มือเข้าใช้งานที่ชัดเจน
*   **Data Asset (สินทรัพย์ข้อมูล)**: ทรัพยากรข้อมูลที่องค์กรเป็นผู้ถือครอง กำกับดูแล และบำรุงรักษาเป็นการภายใน (Owned, governed, and maintained internally) เพื่อนำมาใช้ประมวลผลต่อ
*   **Knowledge Asset (สินทรัพย์ความรู้)**: ทรัพยากรสารสนเทศที่ผ่านกระบวนการเรียบเรียง วิเคราะห์ และสังเคราะห์โดยมนุษย์ เพื่อส่งต่อบริบท การตีความ หรือแนวทางปฏิบัติ (Information + Interpretation, Context, and Know-how) เช่น แผนยุทธศาสตร์ คู่มือ หรือรายงานวิจัย

---

## 2. โครงสร้างพจนานุกรมข้อมูลร่วม (Unified Schema Specification)

| ลำดับที่ | ชื่อฟิลด์ (Field Name) | ประเภทข้อมูล (Data Type) | ข้อบังคับ (Nullable) | คำอธิบายฟิลด์ (Field Description) | กฎการสืบสายข้อมูล (Data Lineage & Mapping Rules) |
| :---: | :--- | :---: | :---: | :--- | :--- |
| 1 | `asset_id` | Text | PK | รหัสประจำตัวสินทรัพย์ดิจิทัลระดับองค์กร | รันรหัสใหม่แยกตามคลาส:<br>• `SYS-` = ผลิตภัณฑ์ข้อมูล (Systems)<br>• `DAT-` = สินทรัพย์ข้อมูล (Datasets/DB)<br>• `PUB-` / `MED-` / `RES-` = สินทรัพย์ความรู้ (Docs)<br>• `VID-` = สินทรัพย์ความรู้ (Videos) |
| 2 | `asset_title` | Text | Not Null | ชื่อเต็มของระบบสารสนเทศ, ชุดข้อมูล, หรือเอกสารความรู้ | • **Sitemap**: `asset_title`<br>• **CKAN Data Catalog**: `Title` |
| 3 | `asset_type` | Text (Enum) | Not Null | ประเภทคลาสหลักของสินทรัพย์ดิจิทัล ได้แก่:<br>• `Data Product`<br>• `Data Asset`<br>• `Knowledge Asset` | จัดหมวดหมู่ใหม่ตามความหมายสากล:<br>• ระบบและหน้าเพจตอบโต้ $\rightarrow$ `Data Product`<br>• ข้อมูลดิบประมวลผล (CSV/XLSX/SHP) $\rightarrow$ `Data Asset`<br>• รายงาน/คู่มือ/วีดีโอนำเสนอ $\rightarrow$ `Knowledge Asset` |
| 4 | `description` | Text | Nullable | คำอธิบายเนื้อหาโดยสังเขป ขอบเขต หรือชุดข้อมูลเมทาดาตา | • **Sitemap**: `description`<br>• **CKAN Data Catalog**: `Description` (notes) |
| 5 | `format_type` | Text (Enum) | Not Null | รูปแบบกายภาพ/ฟอร์แมตข้อมูลปลายทาง:<br>• `Dataset` (ไฟล์ตาราง/ฐานข้อมูล)<br>• `Document` (ไฟล์เอกสาร/PDF/Word)<br>• `Web Application` (ระบบโปรแกรมย่อย)<br>• `YouTube Video` (วีดีโอมัลติมีเดีย)<br>• `E-book Reader` (โปรแกรมอ่านหนังสืออิเล็กทรอนิกส์)<br>• `Web Page` (หน้าเพจบทความที่ไม่มีไฟล์แนบ) | จำแนกตามลักษณะทรัพยากรปลายทางจริง (แทนการอิงประเภทแคตตาล็อก):<br>• ถ้าไฟล์เป็น CSV/XLSX/JSON/SHP/DB $\rightarrow$ `Dataset`<br>• ถ้าไฟล์เป็น PDF/DOCX/PPTX $\rightarrow$ `Document`<br>• ลิงก์ระบบโต้ตอบ $\rightarrow$ `Web Application` |
| 6 | `owner_division` | Text | Not Null | หน่วยงาน/กอง/กลุ่มงานที่รับผิดชอบและเป็นเจ้าของสิทธิ์ | • **Sitemap**: `owner`<br>• **CKAN Data Catalog**: `Maintainer` |
| 7 | `owner_email` | Text | Nullable | อีเมลติดต่อของกลุ่มงานที่รับผิดชอบสินทรัพย์ | • **Sitemap**: `owner_email` (หากมี)<br>• **CKAN Data Catalog**: `Maintainer Email` |
| 8 | `front_end_url` | Text (URL) | Nullable | ลิงก์หน้าเว็บหลักสำหรับเข้าชม (เป็นมิตรกับผู้ใช้งานทั่วไป) | • **Sitemap**: `front_end_url`<br>• **CKAN Data Catalog**: ลิงก์รายละเอียดแคตตาล็อกปลายทาง |
| 9 | `resource_url` | Text (URL) | Nullable | ลิงก์ตรงดาวน์โหลดไฟล์ทรัพยากร (Direct file / API link) | • **Sitemap**: `resource_url`<br>• **CKAN Data Catalog**: ลิงก์ดาวน์โหลดไฟล์จริง (Resource URLs) |
| 10 | `source_catalog` | Text (Enum) | Not Null | แหล่งที่มาเริ่มต้นของระเบียนเมทาดาตานี้ | กำหนดเป็นค่าคงที่ตามแหล่งนำเข้าข้อมูล:<br>• `Sitemap (DCCE Website)` หรือ `Data Catalog (CKAN DGF)` |
| 11 | `source_group` | Text | Nullable | หมวดหมู่ย่อยในสารบบข้อมูลปลายทาง | • **Sitemap**: `source_group` (เช่น ศูนย์ข้อมูลกลาง > พ.ร.บ.)<br>• **CKAN Data Catalog**: `Groups` (กลุ่มงานวิจัย/นโยบาย) |
| 12 | `data_category` | Text (Enum) | Not Null | การจัดชั้นความมั่นคงปลอดภัยข้อมูล:<br>• `ข้อมูลสาธารณะ`<br>• `ข้อมูลใช้ภายใน`<br>• `ข้อมูลส่วนบุคคล`<br>• `ข้อมูลความลับทางราชการ` | • **Sitemap**: กำหนดเริ่มต้นเป็น `ข้อมูลสาธารณะ`<br>• **CKAN Data Catalog**: ค่าตรงจากฟิลด์ `Data Category` |
| 13 | `update_frequency`| Text | Nullable | ความถี่ในการปรับปรุงความถูกต้องของสินทรัพย์ | • **Sitemap**: กำหนดเป็น `ไม่มีการปรับปรุง` สำหรับสิ่งพิมพ์เผยแพร่<br>• **CKAN Data Catalog**: ค่าตรงจาก `Update Frequency` |
| 14 | `objective` | Text | Nullable | วัตถุประสงค์ในการเผยแพร่ข้อมูล | • **Sitemap**: ระบุเริ่มต้นตามบริบทเอกสาร<br>• **CKAN Data Catalog**: ค่าตรงจาก `Objective` |
| 15 | `tags` | Text | Nullable | คำสำคัญเพื่อประกอบการจัดทำดัชนีและการค้นหา | • **Sitemap**: คำสำคัญจากบริบทหน้าเพจ<br>• **CKAN Data Catalog**: ดึงจาก `Tags` |
| 16 | `geo_coverage` | Text | Nullable | ขอบเขตพื้นที่จัดเก็บของข้อมูล (เช่น ประเทศ, จังหวัด) | • **Sitemap**: กำหนดเริ่มต้นเป็น `ประเทศ`<br>• **CKAN Data Catalog**: ดึงจาก `Geo Coverage` |
| 17 | `created_date` | Date | Nullable | วันที่ระเบียนเมทาดาตานี้ถูกนำเข้าระบบครั้งแรก | • ดึงจากระบบบันทึกเวลา/ประวัติการจัดเก็บ |
| 18 | `last_updated` | Date | Nullable | วันที่แก้ไขหรือปรับปรุงสินทรัพย์นี้ล่าสุด | • ดึงจากบันทึกการแก้ไขล่าสุดบนเว็บไซต์หรือไฟล์อัปเดต |

---

## 3. กฎและข้อจำกัดการตรวจสอบข้อมูล (Validation Rules)

1.  **ความสอดคล้องระหว่าง Asset Type และ Format Type**:
    *   ถ้า `asset_type` = `Data Asset` $\rightarrow$ ฟิลด์ `format_type` ต้องถูกจำแนกเป็น `Dataset` เท่านั้น
    *   ถ้า `asset_type` = `Data Product` $\rightarrow$ ฟิลด์ `format_type` ต้องเป็น `Web Application` หรือ `Web Page`
    *   ถ้า `asset_type` = `Knowledge Asset` $\rightarrow$ ฟิลด์ `format_type` ต้องเป็น `Document`, `YouTube Video`, `E-book Reader` หรือ `Web Page`
2.  **ความถูกต้องของลิงก์ URL**:
    *   ลิงก์ในฟิลด์ `front_end_url` และ `resource_url` ต้องขึ้นต้นด้วย `http://` หรือ `https://` หรือเว้นว่างไว้กรณีไม่มีลิงก์ (ห้ามใส่ "No link" ในฟิลด์ฐานข้อมูล)
3.  **การระบุผู้รับผิดชอบ**:
    *   ทุกสินทรัพย์ต้องมี `owner_division` ที่ชัดเจนตามโครงสร้างการแบ่งส่วนราชการของ DCCE เพื่อประโยชน์ในการทำ Data Stewardship
