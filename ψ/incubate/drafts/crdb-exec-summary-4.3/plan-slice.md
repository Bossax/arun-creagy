# Plan slice — Executive Summary §4.3 พิมพ์เขียวสำหรับการพัฒนาระบบข้อมูลในระยะถัดไป

Source: `ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่ 4 รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md`,
Executive Summary Chapter 4 plan (§4, lines 504–531).

## Section brief (verbatim scope)

> ### 4.3 พิมพ์เขียวสำหรับการพัฒนาระบบข้อมูลในระยะถัดไป
>
> **วัตถุประสงค์การเขียน**
> อธิบายตำแหน่งของโครงการในวงจรชีวิตซอฟต์แวร์ และนำเสนอชุดผลงานพร้อมสร้าง
> (Ready-to-Build Artifacts) พร้อมแนวทางการแบ่งหน้าที่ระหว่าง Content Writer
> และ Software Developer
>
> **ห้ามเขียนในลักษณะที่รู้แล้วว่า TOR โครงการฉบับถัดไปมีเนื้อหาอย่างไร**
>
> **สาระสำคัญที่ต้องเขียน**
> - เปรียบเทียบกับวงจรชีวิตการพัฒนาแบบบูรณาการสำหรับแพลตฟอร์มข้อมูลและเว็บ
>   (Reference Integrated Data and Web Platform SDLC, 6 ระยะ) โดยระบุให้ชัดเจน
>   ว่าโครงการฯ ส่งมอบผลงานที่ทำให้ระยะที่ 1 (Requirements Elicitation &
>   Analysis) และระยะที่ 2 (Functional Analysis & Solution Design) มีความ
>   ครบถ้วนสูง (ประมาณร้อยละ 70 และ 80 ตามลำดับ) เพื่อส่งมอบ "Engineering
>   Design Specification" ให้โครงการถัดไปดำเนินการในระยะที่ 3 ถึง 6
>   (Implementation, Integration & Validation, Deployment, Operations) ได้
>   ทันทีโดยไม่ต้องเริ่มนับหนึ่งจากศูนย์ (Discovery Trap)
> - นำเสนอชุดผลงานส่งมอบพร้อมสร้าง 4-5 รายการหลัก:
>   1) ผังเว็บไซต์ Sitemap v9 (38 โหนด 4 หมวด),
>   2) ข้อกำหนดการออกแบบ DRD v2 (75 ข้อกำหนด, 13 Deliverables, 9 Service
>      Briefs, 12 Data Specs),
>   3) คู่มือเค้าโครงเนื้อหา Storyboard v2 (wireframe 38 หน้า พร้อม
>      Source-Content Mapping),
>   4) Business narrative ของบริการสารสนเทศ (WP6),
>   5) แบบจำลองข้อมูล CDM/DMF (8 โดเมน, เมทะดาตา 12 ฟิลด์, พจนานุกรม 74 คำ)
> - กำหนดแนวทางการแบ่งบทบาทหน้าที่ชัดเจน: Content Writer รับผิดชอบยกร่าง
>   เนื้อหาวิชาการปิดช่องว่าง 33 Gaps ตาม Storyboard; Software Developer
>   รับผิดชอบสร้าง CMS Validation Rules, วาง Data Pipelines และสร้าง UI ตาม
>   DRD v2
> - ข้อเสนอแนะการวางขอบเขตงานในโครงการระยะถัดไปแบบกระชับ ก่อนที่รายละเอียด
>   จะอยู่ใน 4.4
>
> **ไม่รวม**
> - ตารางความสัมพันธ์ฐานข้อมูล 5 ตารางของ DRD
> - รายละเอียดเค้าโครงเนื้อหารายหน้าครบทั้ง 38 หน้า

This is the "concept → ready-to-build artifact" transition section: it positions
CRDB's output as an engineering design specification that lets the next
contractor (referred to generically — never by presuming knowledge of the next
TOR's actual content) skip straight to implementation instead of restarting
discovery. The role split (Content Writer vs. Software Developer) is descriptive
guidance for how the ready-to-build package should be used, not a claim about
what the next contract will say.

## Hard constraint (explicit in the plan)

> ห้ามเขียนในลักษณะที่รู้แล้วว่า TOR โครงการฉบับถัดไปมีเนื้อหาอย่างไร

Do not write as though the content of the next procurement's TOR is already
known. Frame the ready-to-build artifacts as reducing risk/discovery time for
whatever the next project turns out to be, not as predictions about its text.

## Storyline position (§2 of the plan)

- Point 3 of the shared storyline: the chapter moves from concept to
  ready-to-build artifact using the Reference Integrated Data and Web Platform
  SDLC (synthesized from TOGAF, IBM Data Architecture, Australian National
  Archives, BrowserStack) as the shared framework — 6 phases: (1) Requirements
  Elicitation & Analysis, (2) Functional Analysis & Solution Design,
  (3) Implementation, (4) System Integration Verification & Validation,
  (5) Deployment & Operational Transition, (6) Operations, Maintenance &
  Continuous Improvement. CRDB's own delivered work raises phase 1 from ~35%
  to ~70% and phase 2 from ~40% to ~80% coverage (independent assessment).
- The Content Writer / Software Developer split exists specifically to prevent
  the next contractor from having to invent business logic on their own
  (Logic Invention risk).

## Evidence base (§9.4, §9.5 of the plan)

- WP4 Sitemap v9 (E-075, E-089) — full 38-node, 4-category site structure.
  `04_Sitemap/NCAIF_Detailed_Sitemap_v9.md`
- WP4 Developer-Ready Design Requirements Specification v2 / DRD v2 (E-094) —
  75 requirements, 13 deliverables, 9 service briefs, 12 data specs.
  `04_Sitemap/2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md`
- WP4 Node Content Storyboard & Synthesis Guide v2 (E-095) — 38-node
  wireframe/content structure with Source-Content Mapping.
  `04_Sitemap/2026-08-20-WP4-Node-Content-Storyboard-and-Synthesis-Guide-v2.md`
- WP6 Service Business Narratives — business narrative basis for the
  information services. `06_Use_Case_Demand_Analysis/2026-08-14-WP6-Service-Business-Narratives.md`
- WP5 Data Management Framework Report (D-065) — CDM 8 domains, 74-term
  glossary, RACI matrix. `05_Data_Management_Framework/WP5-Data-Management-Framework-Report.md`
- TOR70 SDLC storyline / Reference Integrated Data and Web Platform SDLC —
  primary framework source for the 6-phase reference cycle and the coverage
  percentages. `2026-05-18_TOR-Review/2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md`

## Global writing-format rules

Same nine rules as `crdb-exec-summary-4.1/plan-slice.md` — see that file for
the full text. Additionally for this section: never phrase content as though
the next TOR's specifics are already known (hard constraint above).

## Exclusions (this section)

- Full 5-table DRD relational-database relationship diagram
- Full 38-page node-by-node content storyboard detail
