# Operational Manual — Service Package Vetting for [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1)

## 1. Purpose

This manual defines the editing protocol for vetting the service-package sections in [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1), with immediate priority on sections such as [`บริการที่ 1`](plans/5.3.3_perfect.md:47). Its purpose is to standardize how each service description is checked, revised, and accepted during this session so the prose remains aligned with the active NCAIF institutional style.

This is an internal editing control file. It is not audience-facing prose.

## 2. Binding style and source stack

All edits must be checked against the following files in this order:

1. Primary style control: [`ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md`](ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md:1)
2. Lexicon control: [`ψ/memory/style/LEXICON_NCAIF-Institutional.json`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:1)
3. Project writing plan: [`plans/ncaif-writing-plan.md`](plans/ncaif-writing-plan.md:1)
4. Session target file: [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1)
5. Grounding source A: [`ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md:19)
6. Grounding source B: [`ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-06-15_NCAIF-Service-Enrichment-Roadmap.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-06-15_NCAIF-Service-Enrichment-Roadmap.md:12)
7. Companion rule file for technical report discipline: [`ψ/incubate/DCCE/CRDB/output/final_report/5.3/2026-06-27_crdb-5.3.6-5.3.7-report-writing-rules.md`](ψ/incubate/DCCE/CRDB/output/final_report/5.3/2026-06-27_crdb-5.3.6-5.3.7-report-writing-rules.md:1)

If these files conflict, follow this precedence:

1. [`STYLE_PACK_NCAIF-Institutional.md`](ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md:1)
2. [`LEXICON_NCAIF-Institutional.json`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:1)
3. Ground-truth source logic from the two NCAIF source files
4. Local flow needs of [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1)

## 3. Section job definition

Before editing any service package, write down the section job in one sentence.

For a standard service package in this file, the section job must usually contain four parts:

1. the diagnosed user or institutional problem,
2. the service function,
3. the minimum service package or operating components,
4. the adoption test or evidence of success.

If a paragraph drifts outside that job, revise or move the content.

## 4. Required paragraph sequence for each service

Unless a section clearly requires another structure, vet each service package against the following sequence:

### Paragraph 1 — Problem and operational blockage
- Start with the real finding, not a decorative opening.
- Name who is blocked and by what condition.
- The paragraph must show why current data, workflow, or institutional arrangements are insufficient.

### Paragraph 2 — Service function
- Define what the service does.
- State the role of [`กรมฯ`](ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md:20) only in operational terms.
- Avoid ceremonial claims that the service is important unless the paragraph proves why.

### Paragraph 3 — Minimum service package
- Name the actual deliverables.
- Prefer concrete outputs such as registry, catalog, scorecard, standard, protocol, interface, form, or note.
- If the package contains more than three distinct components, consider a bullet list.

### Paragraph 4 — Technical or governance extension
- Introduce standards, certification logic, or architecture terms only after the service function is already clear.
- Keep technical references only where they increase precision.

### Paragraph 5 — Adoption test
- End with a real-world acceptance condition.
- Name the regulator, planning unit, or implementing actor that would rely on the service.
- The test must describe what successful use looks like.

## 5. Mandatory evidence payload test

Every substantive paragraph must contain all four of the following:

1. one concrete finding,
2. one operational consequence,
3. one institutional or technical basis,
4. one example, artifact, actor, or decision context.

If one element is missing, the paragraph is incomplete and must not pass.

## 6. Lexicon enforcement rules

Apply the lexicon in [`LEXICON_NCAIF-Institutional.json`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:1) as a hard filter.

### Required substitutions
- Use [`กรมฯ`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:70) instead of the English short form or repetitive formal naming in settled report prose.
- Use [`กรณีการใช้งาน`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:75) instead of `use case`.
- Use Thai functional wording for process terms instead of untranslated architecture language, except where the specific English term is itself a technical object under discussion.

### Terms to remove or rewrite on sight
- `ในเชิง...`
- `ในมิติ...`
- `ในลักษณะ...`
- `มุ่งเน้น`
- `มุ่งหวังที่จะ`
- `มีความพยายามในการ`
- abstract wording such as `สถาปัตยกรรม...` when a grounded operational noun can do the job better


## 7. Anti-pattern rejection list

Reject any paragraph that does any of the following:

1. opens with filler such as `ในเชิงระบบ`, `อย่างไรก็ตาม`, or another translated transition that does not perform real analytical work,
2. sounds like a design memo, software specification, or translated architecture note rather than Thai institutional prose,
3. uses abstract prestige phrasing without a blocked task or named artifact,
4. compresses problem, function, package, and adoption test into one overloaded paragraph,
5. states that a service is important without naming why the reader should care,
6. introduces technical standards before clarifying the service function,
7. uses negated contrast scaffolding such as `ไม่ได้... แต่...` when the sentence can be stated directly,
8. leaves `ระบบ` unspecified when the exact system can be named,
9. uses marketing adjectives such as `สมบูรณ์แบบ` or `ไร้รอยต่อ`,
10. exposes internal workflow scaffolding in audience-facing wording.

## 8. Service-package acceptance checklist

Do not accept a revised service package until all items below pass.

### A. Problem definition
- Is the opening grounded in a real obstacle?
- Is the blocked actor named?
- Is the consequence of the problem visible?

### B. Service definition
- Is the service defined by function, not prestige?
- Is the role of [`กรมฯ`](ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md:20) clear?
- Is the paragraph free from filler abstractions?

### C. Package definition
- Are the minimum outputs named concretely?
- Can the reader tell what the service package actually contains?
- If several outputs exist, are they separated clearly enough?

### D. Technical control
- Are technical terms introduced only where useful?
- Are `data broker`, `STAC`, and `ISO` anchored to a Thai explanation?
- Has stray pseudo-technical wording been removed?

### E. Adoption test
- Is there a named user, regulator, or institution?
- Does the closing sentence describe actual uptake or acceptance?
- Does success read as a testable condition rather than a ceremonial aspiration?

### F. Language control
- Has banned lexicon been removed?
- Has `ในเชิง...` been removed or rewritten?
- Does the prose sound like Thai report writing rather than translated advisory prose?

## 9. Editing procedure for this session

Use the following procedure every time a service section is revised:

1. Read the target service section in [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1).
2. Identify the section job in one sentence.
3. Compare the current text against the paragraph sequence in Section 4 of this manual.
4. Run the evidence payload test in Section 5.
5. Scan for lexicon violations using [`LEXICON_NCAIF-Institutional.json`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:1).
6. Remove anti-patterns from Section 7.
7. Re-check whether technical terms appear only after Thai explanation.
8. Re-check whether the closing sentence functions as an adoption test.
9. Only then accept the paragraph or proceed to the next service.

## 10. Scope boundary

This manual is written for the service-package editing pass in [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1).

Immediate use:
- [`บริการที่ 1`](plans/5.3.3_perfect.md:47)

Reusable if needed for later sections:
- [`บริการที่ 2`](plans/5.3.3_perfect.md:63)
- [`บริการที่ 3`](plans/5.3.3_perfect.md:75)
- [`บริการที่ 4`](plans/5.3.3_perfect.md:89)
- [`บริการที่ 5`](plans/5.3.3_perfect.md:103)
- [`บริการที่ 6`](plans/5.3.3_perfect.md:117)
- [`บริการที่ 7`](plans/5.3.3_perfect.md:131)
- [`บริการที่ 8`](plans/5.3.3_perfect.md:145)

## 11. Short operational prompt

When editing a service package in [`plans/5.3.3_perfect.md`](plans/5.3.3_perfect.md:1), do the following:

1. open with the actual institutional blockage,
2. define the service by job,
3. name the minimum package concretely,
4. introduce technical standards only after the Thai explanation is stable,
5. end with a real adoption test,
6. remove `ในเชิง...`, translated contrast scaffolding, and prestige filler,
7. enforce [`STYLE_PACK_NCAIF-Institutional.md`](ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md:1) and [`LEXICON_NCAIF-Institutional.json`](ψ/memory/style/LEXICON_NCAIF-Institutional.json:1) before accepting the section.
