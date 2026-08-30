# Style Diff Evidence — 2026-08-30 15:55 — Context: TH

**Source mode**: In-Place / Single File (working-copy `git diff`)
**File**: `ψ/incubate/drafts/crdb-exec-summary-4.3/section-4.3-draft.md`
**Session**: continuation of 2026-08-30 recap session (CRDB Ch.4 exec-summary review)
**Diff tool**: `diff_word_table.py --git` — 43 raw rows (see below), all dispositioned.

---

## Concrete Diff Log (semantic units)

1. **Whole sentence removed** — coverage-percentage claim ("ระยะที่ 1 มีความครอบคลุมเพิ่มขึ้นจากประมาณร้อยละ 35 เป็นประมาณร้อยละ 70...") plus the paragraph-opening clause built on it ("ความครอบคลุมที่เพิ่มขึ้นนี้มีความหมายเชิงปฏิบัติโดยตรง"). User's own inline annotation: *"what the actual fuck?????? ครอบคลุมที่เพิ่มขึ้น what? do we know the detail of the next TOR? NO! ... which is what I told you not to do so! we do not know about next project!"* — explicit fabrication/scope violation, not a style edit.
2. **Annotation inserted** — `%%add explanation of what the activities and outputs of this project are situated in the life cycle%%` — a TODO instruction for future drafting, not an edit.
3. **Inline enumeration → line-broken list** — `(1)...(2)...(3)...(6)` inside one paragraph sentence → `1)\n2)\n3)...6)` each on its own line.
4. **Opening sentence rewrite**:
   - Dropped full verbose project title clause ("โครงการจ้างที่ปรึกษาพัฒนาชุดข้อมูลองค์ความรู้ความเสี่ยงและผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ") → "ภายใต้โครงการนี้"
   - "วางตำแหน่งผลงานที่ส่งมอบไว้ใน" → "จัดวางหน้าที่ของผลผลิตที่ส่งมอบภายใต้" (ผลงาน→ผลผลิต; "position within" → "assign the function of...under")
   - "(Reference Integrated Data and Web Platform SDLC)" → "(Data and Web Platform Software Development Life Cycle)" — dropped "Reference Integrated" qualifier, spelled out SDLC
5. **List item 1**: "4 หมวดหลัก" → "4 หัวข้อหลัก" (หมวด→หัวข้อ) — **conflicts** with existing lexicon entry mapping โหนด→หมวด (i.e. หมวด is currently the *preferred* term for this same sitemap-structure concept).
6. **List item 2**: "ข้อกำหนดการออกแบบเชิงพัฒนา (Developer-Ready Design Requirements Specification: DRD v2)" → "เอกสารข้อกำหนดการออกแบบ (Design Requirements Document: DRD)"; "ชิ้นงานส่งมอบ 13 รายการ" → "สำหรับการควบคุมขอบเขตเนื้อหา สิ่งที่ต้องส่งมอบ (Deliverable) 13 รายการ"; "9 ฉบับ" → "9 รายการ", "12 ฉบับ" → "12 รายการ" (ฉบับ→รายการ, both occurrences); "ข้อกำหนดโครงสร้างข้อมูล (Data Specs)" → "ข้อกำหนดโครงสร้างข้อมูลอภิพันธ์" (already-promoted metadata-term rule, not new).
7. **List item 3**: "(Node Content Storyboard & Synthesis Guide v2)" → "(Content Storyboard & Synthesis Guide)" — dropped "Node" and "v2".
8. **List item 5**: "(Conceptual Data Model / Data Management Framework: CDM/DMF)" → "(Conceptual Data Model / Data Management Framework)" — dropped ": CDM/DMF"; "มาตรฐานเมทะดาตา" → "มาตรฐานข้อมูลอภิพันธ์" (already-promoted rule).
9. **New paragraph inserted** — roles paragraph rewritten:
   - "การใช้ประโยชน์จากชุดชิ้นงานพร้อมสร้างนี้ต้องอาศัยการแบ่งบทบาทหน้าที่ที่ชัดเจนระหว่าง..." (requires clear role division) → "ผลผลิตนี้สามารถช่วยให้การพัฒนาเนื้อหาเว็บไซต์และแพลตฟอร์มในระยะถัดไป มีทิศทางที่ชัดเจนมากขึ้น โดยตำแหน่งที่มีส่วนเกี่ยวข้องหลักคือ..." (can help provide clearer direction) — dependency framing → positive-enabling framing.
   - "ผู้จัดทำเนื้อหา" → "ผู้เขียนเนื้อหา" (×2)
   - "รับผิดชอบยกร่างเนื้อหา..." → "รับผิดชอบการยกร่างเนื้อหา..."; "รับผิดชอบสร้างกฎ..." → "รับผิดชอบการสร้างกฎ..." — bare verb → nominalized "การ+verb" after รับผิดชอบ (×2)
   - "(Storyboard)" → "(Content Storyboard)"
   - "ส่วนต่อประสานผู้ใช้" (UI) → "หน้าต่างปฏิสัมพันธ์และผลิตภัณฑ์ข้อมูลที่แสดงผลและข้อมูลตามที่กำหนด" — expanded from bare "UI" to cover interactive windows + data products
   - "(DRD v2)" → "(DRD)"
10. **Trailing sentence removed, new closing paragraph added** — old rationale sentence about "Logic Invention" and next-phase scope removed; replaced with a new paragraph on business logic grounded in climate-adaptation expert analysis, Business Requirement framing, System Design boundary, and Iterative Design Loop. Substantial new domain content, not a style edit.

---

## Exhaustive Word-by-Word Table (from `diff_word_table.py`, every row dispositioned)

| Draft | Edit | Category | Disposition |
|---|---|---|---|
| โครงการจ้างที่ปรึกษา...ของประเทศ | ภายใต้โครงการนี้ | Filler/scope pruning | Candidate — ask (recurrence likely) |
| วางตำแหน่งผลงานที่ส่งมอบไว้ใน | จัดวางหน้าที่ของผลผลิตที่ส่งมอบภายใต้ | Institutional precision | Candidate — ask |
| ผลงาน | ผลผลิต | Institutional precision | Candidate — ask (bundled w/ above) |
| (Reference Integrated Data and Web Platform SDLC) | (Data and Web Platform Software Development Life Cycle) | Possible fabricated-name correction | content_correction — logged, not asked (pattern self-evident given item 1's explicit fabrication complaint) |
| (1)...(2)...(3)... inline | 1)\n2)\n3)... line-broken | Structural/formatting | Candidate — ask |
| หมวด | หัวข้อ | Institutional precision | **Conflict with existing rule** — must ask |
| ข้อกำหนดการออกแบบเชิงพัฒนา (...Specification: DRD v2) | เอกสารข้อกำหนดการออกแบบ (...Document: DRD) | Deliverable-name accuracy | content_correction — logged (bundled w/ version-tag pattern below) |
| ชิ้นงานส่งมอบ | สิ่งที่ต้องส่งมอบ (Deliverable) | Institutional precision | Candidate — bundled with version-tag question |
| ฉบับ | รายการ (×2) | Lexical / classifier | Candidate — ask |
| (Node Content Storyboard & Synthesis Guide v2) | (Content Storyboard & Synthesis Guide) | Version-tag dropping | Candidate — ask (recurs 3×) |
| (Conceptual Data Model / Data Management Framework: CDM/DMF) | (Conceptual Data Model / Data Management Framework) | Version-tag dropping | Candidate — ask (same pattern) |
| มาตรฐานเมทะดาตา | มาตรฐานข้อมูลอภิพันธ์ | Already-promoted rule | Not new — application of existing LEXICON_TH.json entry (เมทะดาตา→ข้อมูลอภิพันธ์, confirmed 2026-08-30) |
| ต้องอาศัยการแบ่งบทบาทหน้าที่ที่ชัดเจนระหว่าง... | สามารถช่วยให้...มีทิศทางที่ชัดเจนมากขึ้น โดย... | Passive/defeatist → positive-conditional | Candidate — ask (matches skill's own taxonomy category 4) |
| ผู้จัดทำ | ผู้เขียน (×2) | Institutional precision | Candidate — ask |
| รับผิดชอบยกร่าง / รับผิดชอบสร้างกฎ | รับผิดชอบการยกร่าง / รับผิดชอบการสร้างกฎ | Grammar (nominalization) | Candidate — mechanical (proposed, not asked) |
| (Storyboard) | (Content Storyboard) | Naming consistency | Logged only — tied to item-3 rename, too minor to register standalone |
| ส่วนต่อประสานผู้ใช้ (UI) | หน้าต่างปฏิสัมพันธ์และผลิตภัณฑ์ข้อมูลที่แสดงผลและข้อมูลตามที่กำหนด | Scope expansion | content_correction — logged, not asked (document-specific broadening from UI to data products) |
| (DRD v2) | (DRD) | Version-tag dropping | Same pattern as above — bundled |
| coverage-% sentence + paragraph opener | removed entirely | Fabrication/scope | content_correction — logged (user's own annotation is the rationale) |
| trailing "Logic Invention" sentence | removed; new paragraph on business-logic grounding added | New domain content | content_correction/one_off — logged, not asked |

---

## Linguistic Shift Summary

- Two whole-paragraph content changes are driven by a scope/fabrication complaint (assuming detail of a future, unscoped project TOR) and a request for new content (life-cycle situating) — these are drafting-fidelity issues for `writing-th`, not durable style rules.
- A cluster of deliverable-name edits (DRD v2→DRD, Node...v2→dropped, CDM/DMF→dropped) all drop version/abbreviation suffixes — recurring 3× in one section, worth confirming as either a fabrication-avoidance habit or a one-off correction to this specific document's deliverable list.
- One direct lexicon conflict: หมวด vs หัวข้อ for the same "sitemap main-grouping" concept, opposite direction from the existing โหนด→หมวด rule.
- One instance matches the skill's own "Passive/Defeatist Syntax Elimination" taxonomy category almost exactly (dependency framing → positive-enabling framing).

## Candidate Rules (by layer)

- **lexical**: ผลงาน→ผลผลิต; ผู้จัดทำ→ผู้เขียน; ฉบับ→รายการ (classifier); หมวด vs หัวข้อ (conflict, needs resolution)
- **structural**: inline-enumeration→line-broken list; project-name-clause→"โครงการนี้" pruning; passive-dependency→positive-enabling reframe
- **regex/grammar**: รับผิดชอบ + bare verb → รับผิดชอบ + การ+verb (proposed mechanical)
- **content_correction (log only, not for promotion)**: coverage-% fabrication removal; version-tag/abbreviation dropping on deliverable names; UI-term scope expansion; new business-logic closing paragraph
