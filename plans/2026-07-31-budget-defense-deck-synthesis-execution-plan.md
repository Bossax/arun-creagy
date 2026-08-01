# Execution Plan: Multi-Subagent Slide Content Synthesis & Web Grounding

This plan details the synthesis of the 4-slide budget defense deck using parallelized subagents and external grounding tools.

---

## 🏗️ Slide Structure & Focus

* **Slide 1: Gaps, Issues & National Urgency**
  * Focus: Highlight current fragmentation, policy risks, and why resolving these gaps is a critical national capability protecting Thailand’s citizens and economy.
  * Evidence: `Report_Executive_Summary.md`, `NCAIF Structural Data Gap Analysis v5.0 (D-044)`. 
* **Slide 2: Demand-Driven Interface & Data Architecture**
* %%Plain language: สไลด์นี้จะมาอธิบายว่า ความต้องการข้อมูลสารสนเทศด้านความเสี่ยงและการปรับตัวจากการเปลี่ยนแปลงสภาพภูมิอากาศในปัจจุบันเป็นอย่างไร และในปีหน้าเราจะสร้างระบบอะไร เพื่อเป็นรากฐานในการพัฒนาบริการและผลิตภัณฑ์ข้อมูลสารสนเทศที่ตอบโจทย์ความต้องการเหล่านี้ %%
  * Focus: Translate surveyed stakeholder needs into the need to establish a Data System aligned with industry best practice to enable the development  of climate information products and services in the long run. The build consists of the back end system which is the engine of the country and the frontend interface where information products and services are showcased. Show the mock-up of the website pages and key insight people would gain from here
  * Evidence: `NCAIF Detailed Sitemap v8.0`, `Proposed Architecture Design (D-052)`. [[ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6|บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6]], [[ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-07-06_btr-me-reporting-pipeline-use-case|2026-07-06_btr-me-reporting-pipeline-use-case]]
* **Slide 3:National Climate Adaptation Data System**
*  %%Plain language: สไลด์นี้จะมาอธิบายว่า การออกแบบสถาปัตยกรรมข้อมูลหลังบ้านมีความสำคัญไม่แพ้กับการออกแบบหน้าเว็บไซต์ เพื่อสนับสนุนการจัดการข้อมูลและผลิตองค์ความรู้ระยะยาว ซึ่งเป็นหัวใจสำคัยของโครงการปีหน้าเช่นกัน %%
  * Focus: the conceptual design of the data system. The core idea is to build on country's data infrastructure provided by DGA, industry-best practice. This data system allows for data discovery and sharing in the climate risk impact and adaptation domains. Highlight one key prominent use case, A-BTR reporting, as a starting point of a new comprehensive and strategic use case around  which the system shall be build. 
  
* **Slide 4: FY2027 Key Platform Deliverables**
* %%Plain language: ในปีนี้ เราได้ทำการสำรวจสถานะทางข้อมูลของกรม ความต้องการข้อมูลของหน่วยงานต่างๆ และผู้มีส่วนได้ส่วนเสียในห่สวโซ่ข้อมูล พร้อมทั้งระบบุความต้องการบริการต่างๆ ในปีหน้าเราจะสร้างระบบต่างๆ เหล่านี้%%
..  * Focus: Concrete next-year build plan (ETL pipelines, Risk Profile Search, BTR reporting module, Metadata Service). แ้ำแา ธฯฑึจ
  * Evidence: [[ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026|TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026]]

---

## 🛠️ Subagent Tool Strategy

* **Local Evidence**: `view_file` to ingest primary CRDB resources.
* **Web Grounding**: `perplexity_ask`, `brave_web_search`, or `search_web` to integrate global precedents, DGA standards, and climate impact metrics.

---

## 🏁 Verification & Review
Each slide output must include:
1. Core Slide Headline (Thai/English)
2. Body Narrative & High-Density Bullet Points (Thai-first)
3. Graphic/Visual Suggestion
4. Grounded Research Reference
5. Speaker Notes with local CRDB Evidence Citations
