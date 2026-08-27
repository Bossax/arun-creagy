---
timestamp: 2026-08-27 22:10
session: chapter-1-plan-sourcing
mode: in-place-manual (git diff on dirty file mixed committed baseline vs. mid-session Read snapshot, isolated to Boss's marks only)
file: ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่ 1 รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md
scope: ## 4. แผนบทที่ 1 ของรายงานฉบับย่อสำหรับผู้บริหาร (committed baseline dbacb7c vs. Boss's in-place review edits)
context: TH
---

# Diff Evidence: exec-summary chapter plan review marks

Baseline = commit `dbacb7c` (as originally drafted). Edited = the state after Boss reviewed
in Obsidian, adding `%%...%%` comments, `~~strikethrough~~` deletions, and rewriting several
bullets in place — before any subsequent source-linking edits.

## Concrete Diff Log

1. **Acronym-first spelled out.**
   - Before: `ปัญหาที่ NCAIF มุ่งแก้ไข`
   - After: `ปัญหาที่ โครงสร้างข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ หรือ National Climate Adaptation Information Framework (NCAIF) มุ่งแก้ไข`

2. **Abstract value bullet replaced with concrete, itemized problem list.**
   - Before: `คุณค่าต่อการกำหนดนโยบาย การวางแผน การปฏิบัติ และการเรียนรู้ด้านการปรับตัว`
   - After: two sub-bullets naming actual ecosystem problems with English parenthetical terms:
     `ข้อมูลไม่มี (availability) ความไม่มั่นใจในคุณภาพข้อมูล (quality) รูปแบบของข้อมูลไม่ตรงอย่าที่ต้องการ (format)`

3. **Explicit slide citation added.**
   - After: `(ยึดตาม Slide 14: โครงสร้างพื้นฐานของระบบดิจิตัลที่จำเป็น ของ CRDB slide deck for 26th dissemination event)`
   - No equivalent in Before — Boss added a traceable pointer instead of leaving the claim unsourced.

4. **Missing concept restored + English glosses added to every technical term.**
   - Before: `NCAIF เว็บแพลตฟอร์ม และระบบบริหารจัดการข้อมูล`
   - After: `โครงสร้างข้อมูลฯ เว็บแพลตฟอร์ม (Web Platform) แพลตฟอร์มข้อมูล (Data Platform) และระบบบริหารจัดการข้อมูล (Data Management System)`
   - "แพลตฟอร์มข้อมูล (Data Platform)" was entirely absent before — a substantive omission, not just wording.

5. **Abstract summary noun replaced with enumerated concrete list (recurs 3x).**
   - 1.1: `บทเรียนร่วมจากแพลตฟอร์มสากล` → `บทเรียนจากแพลตฟอร์มสากล จุดประสงค์ ลักษณะเนื้อหา การจัดหมวดหมู่ องค์ความรู้ ผลิตภัณฑ์ บริการบนเว็บไซต์`
   - 1.2: `ทุนเดิมที่นำมาใช้ต่อยอดได้` → `สถานภาพการจัดการข้อมูล โดยทีมของกองขับเคลื่อนการลดก๊าซเรือนกระจก (ทีม IT ของกอง ชั้น 6) และโครงการของกลุ่มพัฒนาเทคโนโลยีดิจิทัล`
   - 1.3: `กลุ่มผู้มีส่วนร่วมที่ให้ความเห็น` + `ประเด็นหลักที่ใช้ทดสอบร่าง` (two abstract bullets) → one bullet with parenthetical enumeration: `(การประชุมกลุ่มย่อยภายในกรมฯ การจัดประชุมรับฟังความคิดเห็นต่อร่างโครงสร้างข้อมูล และการประชุมเผยแพร่และรับฟังความคิดเห็น รวมถึงการสัมภาษณ์ผู้มีส่วนเกี่ยวข้อง)`

6. **Dropped head-noun flagged explicitly, recurs 3x with the same complaint.**
   - `ลำดับชั้นที่ไม่ซับซ้อน` flagged: `%%ลำดับชั้นของอะไร? ชอบละนามตลอด อ่านไม่รู้เรื่อง%%` (hierarchy of *what*? — habit of dropping the head noun makes it unreadable)
   - `การแยกเครื่องมือออกจากบัญชีข้อมูล` flagged: `%%??? เครื่องมืออะไร??%%` (which tools?)
   - `การนำทาง` → `การออกแบบการนำทางผู้ใช้`, flagged generally: `%%you omit the essential noun very often making reading incomprehensible%%`

7. **Stiff/formal phrase replaced with a natural Thai idiom.**
   - Before: `การเปิดเผยรายละเอียดตามลำดับ`
   - After: `การเปิดเผยรายละเอียดอย่างค่อยเป็นค่อยไป`

8. **Undefined abstraction rejected outright (struck through).**
   - `~~ข้อจำกัดเชิงโครงสร้าง~~` flagged: `%%what is this structural limits/ constraints????%%` — no defined referent, cut rather than kept.

9. **Causal-logic reversal, not just wording — flagged as the biggest substantive fix.**
   - `~~สรุปเป็นแผนภาพ "ทุนเดิม → ข้อจำกัด → คำตอบเชิงออกแบบ"~~` struck through.
   - Boss's correction: NCAIF is the ideal benchmark of content/products needed to complete a user's
     journey and expectations; existing DCCE resources (datasets, knowledge assets, data assets,
     products) are analyzed *against that benchmark* to surface gaps — not "existing capital → limits
     → design answer." Also flagged "คำตอบเชิงออกแบบ" as a bad translation of "design solution."

10. **Bare acronym in a heading replaced with the descriptive Thai phrase.**
    - Heading `1.4 ผลการพัฒนา NCAIF และโครงสร้างการบริหารจัดการข้อมูล` → `1.4 ผลการพัฒนาโครงสร้างข้อมูลด้านการปรับตัว และโครงสร้างการบริหารจัดการข้อมูล`

11. **Result-summary bullet replaced with a concrete process frame.**
    - Before: `ผลการยืนยันว่ากรอบตอบสนองภารกิจและความต้องการหลักอย่างไร`
    - After: `เน้นที่การประชุมกลุ่มย่อยว่าแต่ล่ะครั้งทำให้เจออะไรเพิ่ม ได้ยืนยันอะไรกลับไป` (each meeting round → what new finding → what got confirmed back)

## Linguistic Shift

- Consistent move from **abstract collective/summary nouns** (คุณค่า, ทุนเดิม, กลุ่มผู้มีส่วนร่วม,
  ประเด็นหลัก, ข้อจำกัดเชิงโครงสร้าง) toward **concrete, named, enumerated referents** — actual teams,
  actual meeting types, actual data-quality dimensions — usually inside a parenthetical list.
- Technical/English terms get a Thai-English parenthetical pairing on first use (Web Platform, Data
  Platform, availability, quality, format) rather than staying Thai-only or English-only.
- Any noun phrase built on a bare modifier without its head noun (ลำดับชั้น, เครื่องมือ, การนำทาง) draws
  an explicit rejection — this is flagged as a *recurring* problem, not a one-off typo.
- Claims tied to an external source (e.g. the slide-14 problem framing) get an explicit citation
  instead of floating unsourced.
- A structural/causal claim that inverts the actual reasoning (gap-analysis framed as "existing
  capital → limitation" instead of "benchmark → gap") is treated as a content defect, not a wording
  defect — struck through rather than merely reworded.

## Candidate Rules

1. Never introduce an abbreviation before its full Thai (and English, if the term is bilingual) name
   has appeared once in that document.
2. Replace abstract summary nouns (คุณค่า, ทุนเดิม, ข้อจำกัด, กลุ่มผู้มีส่วนร่วม, ประเด็นหลัก) with a
   concrete enumerated list of what they refer to, usually in parentheses.
3. Never build a noun phrase from a bare modifier (ลำดับชั้น, เครื่องมือ, การนำทาง, การเปลี่ยนแปลง) without
   its head noun — always name what it's a hierarchy/tool/navigation/change *of*.
4. Pair a Thai technical term with its English original in parentheses on first use.
5. Cite the concrete source (deck name + slide number, document name) inline when a claim traces to
   one, rather than leaving it as an unattributed assertion.
6. When a bullet's underlying causal logic is wrong (not just its wording), strike it and re-derive
   the correct causal chain — do not patch the sentence in place.
