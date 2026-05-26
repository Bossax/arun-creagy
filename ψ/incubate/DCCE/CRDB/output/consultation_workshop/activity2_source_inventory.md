# Phase 0: CRDB Workshop Activity 2 Source Inventory

This inventory maps the mixed-format workshop results in `ψ/incubate/DCCE/CRDB/output/consultation_workshop/result/`.

## 1. File Inventory & Audit

| File Name | Format | Activities Covered | Primary Structure | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `ผลการหารือกิจกรรมกลุ่ม (Group 1 ).md` | Markdown | 1 & 2 | Table + Narrative | Narrative blocks for Activity 2. |
| `ผลการหารือกิจกรรมกลุ่ม ช่วงที่ 1 (Group 3 ).md` | Markdown | 1 & 2 | Table + Narrative | Narrative blocks for Activity 2. |
| `ผลการหารือกิจกรรมกลุ่ม ช่วงที่ 1 (Group 5-6).md` | Markdown | 1 & 2 | Table + Narrative | Narrative blocks for Activity 2. |
| `ผลการหารือกิจกรรมกลุ่ม ช่วงที่ 1 (Group 7-8).md` | Markdown | 1 & 2 | Table + Narrative | Narrative blocks for Activity 2. |
| `สรุปกิจกรรมที่ 2 - กลุ่ม 2.md` | Markdown | 2 | Table | Converted from Excel. High structural density. |
| `สรุปกิจกรรมที่ 2 - กลุ่ม 4.md` | Markdown | 2 | Table | Converted from Excel. High structural density. |
| `สรุปกิจกรรมที่ 2 - กลุ่ม 5 - 6.md` | Markdown | 2 | Table | Converted from Excel. High structural density. |

## 2. Activity 2 Extraction Protocol

Based on the audit, extraction will target:

1.  **Tabular Data (Excel-converted):** Columns typically mapping to Title, Objective, Data Needs, Challenges, and Votes (Orange, Pink, Green).
2.  **Narrative Blocks (Direct Markdown):** Usually structured under headers or within "Activity 2" sections, answering the three core questions (Objective, Requirements, Challenges).

## 3. Metadata Mapping (Initial)

| Column in Master | Mapping from Narrative | Mapping from Table |
| :--- | :--- | :--- |
| `service_title` | Section Header / Title line | `ชื่อชิ้นงาน` / `ชื่อการใช้งาน` |
| `service_objective` | Question 1 Answer | `คำถามที่ 1` / `วัตถุประสงค์` |
| `required_data` | Question 2 Answer (Substantive) | `คำถามที่ 2` (Data part) |
| `required_format` | Question 2 Answer (Presentation) | `คำถามที่ 2` (Format part) |
| `build_challenges` | Question 3 Answer | `คำถามที่ 3` / `ความท้าทาย` |
| `votes` | Sticker counts (if mentioned) | `สีส้ม`, `สีชมพู`, `สีเขียว` columns |

---
*Created: 2026-05-26*
*Status: Phase 0 Complete*
