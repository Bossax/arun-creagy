# Style-Capture Diff Evidence — TH context

**Timestamp**: 2026-09-22 12:30
**Source mode**: In-Place / Single File (git working-copy diff)
**File**: `ψ/incubate/drafts/Sub-law_TOR-annotated-notes.md`
**Context**: TH (generic Thai institutional — shared LEXICON_TH.json / STYLE_PACK_TH.md, not project-scoped)

## Concrete diff log (annotated by Boss with `%%comment%%` and `~~strikethrough~~`)

1. **Opening slogan cut**: "ที่ปรึกษาจะใช้กรอบการดำเนินงานแบบ **"Legal Mandate to Operational Readiness"** หรือ "จากบทบัญญัติสู่การปฏิบัติจริง" โดย..." replaced with a plain principle statement: "หลักการพื้นฐานที่ที่ปรึกษาใช้ในการวางกรอบการดำเนินโครงการนี้คือ การทำให้บทบัญญติทางกฎหมายสามารถถูกนำไปปฏิบัติได้จริงภายใต้บริบททางกฎหมายและสถาบันของประเทศไทย โดย..."
   Boss's inline rationale: "we lack the background info about Chapter 12. We need to interpret the original intent of this Chapter in a strategic way; how it will shape the country... the existing draft does imply this but never explicitly state (it jumps to cliche/ hyperbolic naming)"
   → also requests new content ahead of this: overview of Part 1/Part 2 of the chapter, interpretation of intent, summary of what the chapter's design achieves.
2. **Throat-clearing lead-in trim**: "การดำเนินงานจะยึดหลักการสำคัญ ดังนี้" → "หลักการสำคัญ ดังนี้"
3. **Inline English tag flagged**: "SOP ในลักษณะ Step-by-step" — Boss's comment: "this is unnecessary English word should be vetted out"
4. **Decorative adjective cut**: "๕ องค์ประกอบที่เ~~ชื่อมโยงกัน~~" — Boss's comment: "a prime example of unnecessary adjective that makes the sentence hyperbole"
5. **Inline enumeration → numbered list**: "(๑) ... (๒) ... (๓) ... (๔) ... (๕) ..." run-on paragraph converted to a real markdown numbered list. Boss's comment: "always use numbered list for this kind of list"
6. **Structural relocation (deletion at this location)**: the two-part chapter breakdown + data→risk→plan→implement→monitor cycle sentence, previously placed after the detailed §2 scope table, struck through entirely. Boss's comment: "should have been well above this section where we already discuss detai[l]" — i.e. belongs in the opening framing section (§1), not after the detail table.
7. **English methodology brand-names → Thai** (table, §2 "แนวทางดำเนินงานหลัก" column):
   - "Legal Obligation Mapping, Institutional Mapping และ Gap Analysis" → "จัดทำแผนผังภารผูกพันธ์ทางกฎหมายของหน่วยงาน การทำแผนผังหน่วยงานที่เกี่ยวข้อง และการวิเคราะห์ช่องว่างเชิงสถาบันและกฎหมาย"
   - "Process Architecture และ Workflow รายภารกิจ" → "โครงสร้างกระบวนงานและรายละเอียดกระบวนการทำงาน รายภารกิจ"
   - "SOP แบบ Step-by-step, Process Flow, RACI Matrix, Template และ Checklist" → "SOP แบบเป็นลำดับขั้น, ผังกระบวนการทำงาน, ตารางความรับผิดชอบ, Template และ Checklist" (Template, Checklist left as English)
   - "Regulatory Roadmap และร่างประกาศ/หลักเกณฑ์/คู่มือที่จำเป็น" → "แผนที่ทำทางการใช้ข้อกำหนดและร่างประกาศ/หลักเกณฑ์/คู่มือที่จำเป็น" (note: "ทำทาง" is non-standard Thai — possible typo for "นำทาง", flagged for confirmation, not auto-corrected)
   - "Readiness Assessment, Target Operating Model" → "การประเมินความพร้อม, แบบจำลองเป้าหมายการดำเนินงาน"

## Exhaustive word-by-word table (from `diff_word_table.py --git`, 89 rows total)

Most of the 89 rows are markdown table cell-padding/whitespace churn from reformatting the §2 table (pipe-table column widths changed when Boss edited cell contents) — dispositioned below as "not lexical — formatting noise," not individually enumerated here. The substantive rows are items 1–7 above. Full raw tool output preserved in this session's tool-call log; not re-pasted here to avoid duplicating ~60 whitespace-only rows.

## Candidate rules by layer

**Lexical (L1/L2)** — mechanical, meaning-invariant English→Thai swaps:
- Step-by-step → เป็นลำดับขั้น
- Process Flow → ผังกระบวนการทำงาน
- RACI Matrix → ตารางความรับผิดชอบ
- Process Architecture → โครงสร้างกระบวนงาน
- Legal Obligation Mapping → แผนผังภารผูกพันธ์ทางกฎหมายของหน่วยงาน
- Institutional Mapping → การทำแผนผังหน่วยงานที่เกี่ยวข้อง
- Gap Analysis → การวิเคราะห์ช่องว่างเชิงสถาบันและกฎหมาย
- Readiness Assessment → การประเมินความพร้อม
- Target Operating Model → แบบจำลองเป้าหมายการดำเนินงาน
- Regulatory Roadmap → แผนที่ทำทางการใช้ข้อกำหนด (flag: possible typo, confirm before registering)
- NOT banned (kept as-is by Boss): SOP, Template, Checklist, TOR

**Regex/pattern (lexical, generalized)**:
- decorative "ที่เชื่อมโยงกัน" / similar connective-adjective tacked onto an enumerated-item count → cut (extends existing hyperbole-intensifier pattern already in LEXICON_TH)
- throat-clearing subject+verb lead-in immediately before "ดังนี้" list ("[หัวข้อ]จะยึด...ดังนี้" → "[หัวข้อ] ดังนี้")

**Structural (L4/L5)**:
- Opening section must ground the reader in the legal provision's own structure and intent (chapter parts, legislative purpose, what the design achieves) before naming the consultant's own operating framework/methodology.
- A framing-level process-cycle diagram belongs in the opening context section, not after a detailed scope-mapping table.
- Any inline enumerated list of ≥3 named items (previously written as "(๑) ... (๒) ... (๓)" run-on prose) must render as a real numbered markdown list.
