# ตัวอย่างระเบียนข้อมูล: กรณีอุทกภัยในเมืองจากฝนตกหนักต้นน้ำ (ไม่ใช่พายุหมุนเขตร้อน)
**Database Record Example: Upstream Heavy Rain Causing Downstream Urban Flooding (Non-cyclone Event)**

ตัวอย่างนี้สาธิตวิธีการจัดเก็บข้อมูลในระบบฐานข้อมูลสัมพันธ์ **MVD** ตามการแบ่งระดับสถาปัตยกรรม 3 ชั้น (Three-Layer Architecture) สำหรับกรณีเหตุการณ์น้ำหลากเข้าท่วมตัวเมือง เนื่องจากฝนตกหนักสะสมในพื้นที่ป่า/ภูเขาตอนบนของลุ่มน้ำยม (Upstream Catchment) ซึ่งไม่มีพายุหมุนเขตร้อนพาดผ่านโดยตรง

---

## 1. ข้อมูลในชั้นตั้งต้นเหตุการณ์ (Layer A - Event Capture)

### 1.1 ตาราง `DISASTER_EVENT` (บันทึกตัวเหตุการณ์หลัก - แม่)
*บทบาท: บันทึกข้อมูลพยากรณ์อากาศและภัยพิบัติต้นเหตุ (Trigger Event)*

| ฟิลด์ข้อมูล (Field) | ตัวอย่างค่าข้อมูล (Example Value) | คำอธิบาย (Description) |
| :--- | :--- | :--- |
| `disaster_event_id` | **`EVT-2026-FL-UPSTREAM-YOM`** | รหัสเฉพาะเหตุการณ์ภัยพิบัติ (Primary Key) |
| `event_name` | `อุทกภัยจากน้ำระบายหลากตลิ่งลุ่มน้ำยมตอนบน พ.ศ. 2569` | ชื่อเหตุการณ์อธิบายลักษณะภัย ( descriptive name) |
| `hazard_type` | `Flood` | ประเภทของภัยตาม ENUM |
| `event_start_date` | `2026-08-12` | วันที่เริ่มได้รับผลกระทบ |
| `event_end_date` | `2026-08-25` | วันสิ้นสุดเหตุการณ์ |

```json
{
  "disaster_event_id": "EVT-2026-FL-UPSTREAM-YOM",
  "event_name": "อุทกภัยจากน้ำระบายหลากตลิ่งลุ่มน้ำยมตอนบน พ.ศ. 2569",
  "hazard_type": "Flood",
  "event_start_date": "2026-08-12",
  "event_end_date": "2026-08-25"
}
```

### 1.2 ตาราง `EVENT_LOCATION` (บันทึกขอบเขตพื้นที่ประสบภัย - ลูก)
*บทบาท: เชื่อมโยงหนึ่งเหตุการณ์หลักไปยังพื้นที่ประสบภัยปลายน้ำหลาย ๆ อำเภอ/จังหวัด (Spatial Intersection)*

**ระเบียนที่ 1: พื้นที่เมืองต้นน้ำ (รับฝนตกหนักสะสมและน้ำป่าหลาก)**
```json
{
  "location_id": "LOC-YOM-2026-001",
  "disaster_event_id": "EVT-2026-FL-UPSTREAM-YOM",
  "location_code": "640100", 
  "province_name": "Sukhothai"
}
```

**ระเบียนที่ 2: พื้นที่ตัวเมืองใหญ่ปลายน้ำ (รับผลกระทบจากแม่น้ำเอ่อล้นตลิ่ง/น้ำท่วมถนนการค้า)**
```json
{
  "location_id": "LOC-YOM-2026-002",
  "disaster_event_id": "EVT-2026-FL-UPSTREAM-YOM",
  "location_code": "650100", 
  "province_name": "Phitsanulok"
}
```

---

## 2. ข้อมูลในชั้นบริบทการประเมิน (Layer B - Assessment Context)

### 2.1 ตาราง `ASSESSMENT_CONTEXT` (คั่นกลางเพื่อรักษาสายธารการบันทึก)
*บทบาท: ป้องกันไม่ให้ข้อมูลแจ้งเหตุฉุกเฉินระดับตำบลทับซ้อนกับการวิเคราะห์เศรษฐกิจมหภาครายภาคส่วน*

```json
{
  "assessment_context_id": "CTX-PLK-MUN-20260830",
  "disaster_event_id": "EVT-2026-FL-UPSTREAM-YOM",
  "location_code": "650100",
  "lead_agency": "Phitsanulok Municipality",
  "assessment_phase": "In-depth",
  "validation_status": "Validated",
  "assessment_date": "2026-08-30",
  "assessor_name_or_team": "ทีมกองสวัสดิการสังคมและเทศกิจ เทศบาลนครพิษณุโลก"
}
```

---

## 3. ข้อมูลในชั้นการประเมินเศรษฐกิจตามมาตรฐานสากล (Layer C - Economic Assessment)

### 3.1 ตาราง `LD_ECONOMIC_LOSS` (ความสูญเสียทางเศรษฐกิจ)
*บทบาท: วิเคราะห์ความสูญเสียต่อเนื่องของร้านค้าในเมืองจากการหยุดบริการ (Downtime) อิงตรรกะ Baseline*

| ฟิลด์ข้อมูล (Field) | ค่าข้อมูล (Value) | คำอธิบาย (Description) |
| :--- | :--- | :--- |
| `loss_record_id` | **`LOSS-PLK-COM-001`** | รหัสเฉพาะระเบียนความสูญเสีย (Primary Key) |
| `assessment_context_id` | `CTX-PLK-MUN-20260830` | รหัสเชื่อมกลับบริบทการประเมิน (Foreign Key) |
| `disaster_event_id` | `EVT-2026-FL-UPSTREAM-YOM` | รหัสตรวจสอบย้อนกลับเหตุภัยพิบัติหลัก (Redundant FK) |
| `sector_id` | `Production_Manufacturing` | ภาคเศรษฐกิจตามกรอบ สศช. |
| `subsector_id` | `Commercial_Shops` | ภาคส่วนย่อยธุรกิจร้านค้าค้าปลีก |
| `loss_category` | `Foregone_Revenue` | รูปแบบสูญเสีย: รายได้ขายสินค้าที่สูญหายไป |
| `analysis_horizon_start` | `2026-08-14` | วันที่เริ่มปิดกิจการเนื่องจากน้ำท่วมขังถนน |
| `analysis_horizon_end` | `2026-08-19` | วันที่น้ำลดและเปิดกิจการได้ปกติ |
| `baseline_quantity_or_value` | `15000.00` | ยอดขายเฉลี่ยของร้านค้าย่านธุรกิจในช่วงปกติ (บาท/วัน) |
| `actual_post_disaster_quantity_or_value` | `2000.00` | ยอดขายจริงที่ยังไหลเวียนได้ระหว่างน้ำท่วม (บาท/วัน) |
| `price_or_valuation_basis` | `ประเมินจากสมุดบัญชีภาษีรายได้เฉลี่ยของหอการค้าจังหวัด` | แหล่งข้อมูลเปรียบเทียบกรณีฐาน (Counterfactual) |
| `increased_costs_thb` | `5000.00` | ค่าใช้จ่ายฉุกเฉิน (ค่าเช่าเครื่องสูบน้ำออกจากร้านค้า) |
| `monetary_loss_thb` | **`70000.00`** | มูลค่าสูญเสียรวมคำนวณอัตโนมัติ: `(15,000 - 2,000) x 5 วัน + 5,000` |
| `loss_formula_note` | `Downtime = 5 days. Shops flooded due to upstream discharge overflowing river bank.` | หมายเหตุสูตรและการทวนสอบเชิงลึก |
| `validation_status` | `Validated` | สถานะผ่านการทวนสอบทางเศรษฐกิจ |

```json
{
  "loss_record_id": "LOSS-PLK-COM-001",
  "assessment_context_id": "CTX-PLK-MUN-20260830",
  "disaster_event_id": "EVT-2026-FL-UPSTREAM-YOM",
  "sector_id": "Production_Manufacturing",
  "subsector_id": "Commercial_Shops",
  "loss_category": "Foregone_Revenue",
  "analysis_horizon_start": "2026-08-14",
  "analysis_horizon_end": "2026-08-19",
  "baseline_quantity_or_value": 15000.00,
  "actual_post_disaster_quantity_or_value": 2000.00,
  "price_or_valuation_basis": "ประเมินจากสมุดบัญชีภาษีรายได้เฉลี่ยของหอการค้าจังหวัด",
  "increased_costs_thb": 5000.00,
  "monetary_loss_thb": 70000.00,
  "loss_formula_note": "Downtime = 5 days. Shops flooded due to upstream discharge overflowing river bank.",
  "validation_status": "Validated"
}
```

---

## 4. ประโยชน์เชิงนโยบายการออกแบบนี้ (Methodological Benefits)

1. **การตรวจสอบย้อนกลับ (Traceability):** สามารถระบุที่มาของผลกระทบทางเศรษฐกิจในเมืองใหญ่ Phitsanulok ได้ว่า มีต้นเหตุหลักมาจากภัยสะสมที่ต้นน้ำ `EVT-2026-FL-UPSTREAM-YOM`
2. **การลบความทับซ้อนเชิงงบประมาณ:** แยกความเสียหายทางตรง (เช่น ซ่อมแซมตึกร้านค้า) ออกจากรายได้ที่สูญหายระหว่างปิดกิจการ (Loss) ป้องกันปัญหางบประมาณเยียวยาฟื้นฟูซ้ำซ้อนตามระเบียบ PDNA ของธนาคารโลก
