---
date: 2026-09-25 10:30
type: info
status: raw
significance: important
---

# Mistake: a methodology section that explains nothing (CRDB §5.1, 2026-09-25)

**What went wrong.** The §5.1 gap-analysis method paragraph listed four abstract steps ("แจกแจง → จัดกลุ่มตามองค์ประกอบความเสี่ยง 8 ด้าน → ตรวจสอบกับบัญชีรายการ → กำหนดสถานะ"). It did not say what question the analysis answers, why each step is needed, or how each step was applied. There were no classification rules, no search rules, no rules for deciding a status, and no count at each step.

**Root cause.**
- The Phase A analysis never wrote down its own decision rules. Category tags were "the analyst's best-guess reading".
- The argument map and the verbalizer turned that missing logic into fluent but empty prose.
- The pipeline's gates (lint, editorial rubric, cold reader) checked style and structure. None checked whether the method was actually explained.

**Related errors in the same section.**
- Coined a wrong label, "องค์ประกอบความเสี่ยง", for TOR 5.3.5's 8 information categories. Climatic Driver, Impact, Loss and Damage and Response are not components of risk.
- Assumed the baseline catalog uses the same 8 categories. It uses 4 domains and 10 sub-domains, so a crosswalk is needed.
- Let a catch-all "Response" tag hide system and governance requests. As a result, the TOR's real Response category was never matched against the catalog.

**Rule going forward.** A methodology section must answer three things.
- **WHAT**: the exact question, taken from the TOR wording.
- **WHY**: why each step is necessary, with a concrete example.
- **HOW**: the written decision rules for each step, the inputs and fields used, and the count at each step, shown as a funnel.

**Before verbalizing any method section:**
- Check that a written method reference with those rules exists.
- If the analysis never recorded its rules, stop and write them first.
- Verify every taxonomy claim against the source file (TOR text, catalog fields), never against earlier drafts.

**Reference fix:** `ψ/incubate/drafts/crdb-full-report-5.1/methodology.md`

Logged via /fyi
