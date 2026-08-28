# Observation — Executive Summary 1.4 (Codex)

## Basis and method

- **Source agent:** Codex.
- **Compared:** committed draft (`HEAD`) against Boss's current working-tree edit; `writing-contract.json`, `editorial-review.json`, `evidence-traceability.md`, `STYLE_PACK_TH.md`, `LEXICON_TH.json`, and §§4, 6, and 10 of the approved Chapter 1 plan.
- **Counting method:** a paragraph is a non-empty prose block, excluding headings, list items, figure placeholders, and table rows. Character edit density is Git changed-character volume (1,675 deleted + 1,267 inserted = 2,942) divided by the committed draft's 5,942 characters. This deliberately counts a replacement on both sides.

## 1. Edit inventory

| # | Bucket | Before (committed) | After (working tree) | Diagnosis |
|---:|---|---|---|---|
| 1 | `SUBSTANCE` | `ผลงานนี้อยู่ในระดับการวางแผน การวิเคราะห์ข้อกำหนด และการออกแบบเชิงตรรกะ จึงเป็นฐานสำหรับจัดทำข้อกำหนดให้ผู้พัฒนาระบบในระยะถัดไป ยังไม่ใช่เว็บแพลตฟอร์มหรือแพลตฟอร์มข้อมูลที่เปิดใช้งานแล้ว` | `โดยมีจุดประสงค์ในการใช้จัดทำข้อกำหนดให้ผู้พัฒนาระบบในระยะถัดไป` | Deletes the blueprint-versus-live-system limitation and replaces a status claim with a purpose. This is a change in the executive conclusion, not merely wording. |
| 2 | `SUBSTANCE` | `ผลการพัฒนาเชื่อมสองส่วนที่ต้องทำงานร่วมกัน ส่วนแรกคือเว็บแพลตฟอร์มที่นำผู้ใช้ไปสู่ข้อมูลและบริการตามภารกิจ ส่วนที่สองคือแพลตฟอร์มข้อมูลและกฎการบริหารจัดการที่รับรองว่าข้อมูลด้านหลังมีความหมายตรงกัน มีผู้รับผิดชอบ และผ่านการตรวจสอบก่อนเผยแพร่ การพัฒนาเว็บไซต์โดยไม่มีกลไกด้านหลังนี้จะทำให้กรมฯ มีช่องทางเผยแพร่ข้อมูลเพิ่มขึ้น แต่ยังคงมีปัญหาความซ้ำซ้อน ความไร้มาตรฐาน และข้อมูลที่ขาดผู้รับผิดชอบ` | `ผลการพัฒนาเชื่อมโยงองค์ประกอบสองส่วนที่ทำงานร่วมกันภายใต้ระบบข้อมูลเดียวกัน ส่วนแรกคือคือแพลตฟอร์มข้อมูล (Data Platform) และกรอบการบริหารจัดการข้อมูลเบื้องต้น ที่ทำหน้าที่เป็นโครงสร้างพื้นฐาน ในการนำเข้าข้อมูล ดูแลตรวจสอบคุณภาพ ปนะมวลผลข้อมูล และผลิตข้อมูลสารสนเทศ องค์ความรู้ ชุดข้อมูล ที่เจ้าหน้าที่ภายในกรมฯ สามารถนำไปใช้ต่อยอด และส่วนที่สองคือเว็บแพลตฟอร์ม (web platform) ที่ดึงข้อมูลจากแพลตฟอร์มข้อมูลมาแสดงผล และออกแบบโครงสร้างของเว็บไซต์ เพื่อนำผู้ใช้ไปสู่ข้อมูลและบริการที่ต้องการอย่างรวดเร็วและแม่นยำ` | Reorders the model (data platform first, website as presentation), adds operational functions and an internal-user purpose, and deletes the original causal warning. This is substantive redesign of the explanation. The two typing slips within it are quarantined separately below. |
| 3 | `STYLE` | `## 1.4.1 วิสัยทัศน์ ผู้ใช้หลัก และคุณค่าของแพลตฟอร์ม` | `## 1.4.1 วิสัยทัศน์แพลตฟอร์ม` | Boss prefers the shorter heading. It removes explicit reader/value labels, so it is a local heading-style signal, not proof that those concepts should be omitted from the prose. |
| 4 | `STYLE` | `โครงสร้างข้อมูลฯ ช่วยให้ผู้ใช้เริ่มจากภารกิจที่ต้องทำ` | `โครงสร้างข้อมูลฯ นำทางผู้ใช้โดยเริ่มจากหมวดของภารกิจที่เกี่ยวข้อง` | Same broad claim, but Boss changes from an outcome-led phrasing to an explicit navigation mechanism. The working tree contains the typo `ภาพกิจ`; the intended comparison is marked here only to prevent the typo becoming a rule. |
| 5 | `SUBSTANCE` | `ส่วนเจ้าหน้าที่กรมฯ มีกรอบสำหรับจัดหมวด ตรวจสอบ และปรับปรุงข้อมูลให้มีมาตรฐานเดียวกัน` | *(deleted)* | Removes the stated value to departmental staff. This changes the named beneficiary/value proposition required by §4, rather than merely tightening prose. |
| 6 | `COMMENT` | *(none)* | `%%please include sub topics x.x. level%%` | Complaint/request for deeper sitemap detail. It is not a style rule. It conflicts in part with §4's exclusion of detailed subcategories; the valid underlying request is clearer objectives for main topics, not necessarily every subtopic. |
| 7 | `SUBSTANCE` | `โครงสร้างเป้าหมายมีความชัดเจนมากกว่าความพร้อมของเนื้อหาที่จะนำมาใช้กับแต่ละส่วน การตรวจแหล่งเนื้อหาตามข้อกำหนด 75 รายการ พบว่ามีเนื้อหาครบแล้ว 16 รายการ มีเนื้อหาบางส่วน 26 รายการ และยังขาดแหล่งเนื้อหา 33 รายการ ช่องว่างส่วนใหญ่กระจุกตัวอยู่ในเนื้อหาด้านการวางแผนและมาตรการปรับตัว รวมถึงข้อมูลปัจจัยขับเคลื่อนสภาพภูมิอากาศ ตัวเลขนี้เป็นผลการประเมินแหล่งเนื้อหาเทียบกับผังเป้าหมาย ไม่ใช่ความคืบหน้าของการพัฒนาซอฟต์แวร์ กรมฯ จึงควรใช้ผลนี้เพื่อจัดลำดับการพัฒนาเนื้อหาควบคู่กับการจัดซื้อจัดจ้างระบบ` | *(deleted)* | Deletes the entire readiness/gap claim and its decision implication. This is substantive. It also exposes the contract-versus-plan conflict assessed below. |
| 8 | `COMMENT` | *(none)* | `%%I think the plan states clearly that no gap analysis%%` | Direct scope complaint, not a style rule. It is supported by Chapter 1 plan §6's bar on detailed gap analysis. |
| 9 | `COMMENT` | *(none)* | `%%include more info about this website content. include objective of each topic and sub topic%%` | Request for content depth, not a style rule. §4 requires purposes/relationships for main groups but explicitly excludes detailed sitemap subcategories. |

### `TYPO` quarantine — excluded from all rule extraction

| Working-tree text | Intended text | Location |
|---|---|---|
| `ส่วนแรกคือคือ` | `ส่วนแรกคือ` | Edited two-platform paragraph |
| `ปนะมวลผล` | `ประมวลผล` | Edited two-platform paragraph |
| `ภาพกิจ` | `ภารกิจ` | Edited navigation paragraph |

No quarantined token is a preferred form or a candidate lexicon entry.

## 2. Candidate style rules (proposals only)

| Candidate | Banned / less-preferred form | Preferred form | Reason | Kind / scope | Already covered? |
|---|---|---|---|---|---|
| Make the data foundation explicit before the presentation layer | Explain the website first and compress the data platform into its back-end consequence | State the data platform/governance foundation, then state that the web platform presents and navigates its information | Boss's substantive rewrite signals a preference for data-to-presentation architecture when explaining the two components. Because this changes explanatory emphasis, it must not be promoted as a mere diction rule. | `structural`; CRDB executive-summary platform sections | No. Existing pack bars vague “system” and architecture-note language but does not impose this ordering. |
| Concise subsection headings | `วิสัยทัศน์ ผู้ใช้หลัก และคุณค่าของแพลตฟอร์ม` | `วิสัยทัศน์แพลตฟอร์ม` | Boss shortened this heading, but the edit is single-sample and must preserve the omitted concepts in body text. | `literal`; executive-summary headings | No exact rule. |
| Describe navigation as a mechanism | `ช่วยให้ผู้ใช้เริ่มจากภารกิจที่ต้องทำ` | `นำทางผู้ใช้โดยเริ่มจากหมวดของภารกิจที่เกี่ยวข้อง` | More concrete about the information-architecture action. Candidate only; working-tree typo `ภาพกิจ` is explicitly excluded. | `literal`; CRDB platform sections | No. |

No terminology candidate is safe to promote: `(Data Platform)` and `(web platform)` were introduced in the working tree, but §10 and the Thai style pack favour audience-facing Thai unless English is materially necessary; neither insertion establishes a preferred lexicon form.

## 3. Gate-escape analysis (11 receipt dimensions)

| Dimension marked `pass` | Did Boss's edit contradict the verdict? | Assessment |
|---|---|---|
| `section_job` | Partly | Boss replaces the opening conclusion and redefines the two-component explanation. The original covered the job, but the receipt did not identify that the brief's framing could be contested. |
| `audience_decision_value` | Partly | The deleted readiness decision mattered to the contract, but Boss rejects its scope. The receipt certified decision value against the contract without reconciling the approved plan. |
| `evidence_payload` | Yes, at instruction-chain level | The 16/26/33 payload is traceable, yet its reader-facing inclusion conflicts with the plan's no-detailed-gap boundary. Evidence fidelity is not the same as scope fidelity. |
| `causal_logic` | Yes | Boss rewrites the causal/functional relationship: data platform and governance become the foundation, with the website drawing and displaying its output. The receipt approved the original website-first causal framing without detecting this possible architecture emphasis. |
| `reader_facing_appropriateness` | Partly | The two `%%` comments identify missing explanatory depth/structure. The request for subtopic detail exceeds §4, but the receipt could have tested whether each main topic's purpose was sufficiently visible. |
| `terminology_agency` | No clear contradiction | Boss adds English parentheticals, which are not a reliable preference signal and sit uneasily with the Thai-first pack. The original terminology and roles remain intact. |
| `source_fidelity` | No clear contradiction | The sidecar supports the committed claims. Boss's changes are editorial/substantive preferences, not evidence that the source claims were false. |
| `form_readability` | Yes | A shorter heading and a request for visible x.x-level structure show that the “clear subsections/list/table” finding missed a desired hierarchy and scan path. The requested detail must still respect §4 exclusions. |
| `altitude` | Mixed | Boss asks for more website explanation, while §4 excludes detailed subcategories. The committed draft's altitude was defensible; the receipt did not surface the tension between useful explanation and over-detail. |
| `headline_conclusion` | No agent failure; post-edit contradiction | Boss removed the blueprint-not-live-system caveat, although it was contractually required and traceable. This is a Boss substantive change, not evidence that Codex's conclusion was wrong. |
| `findings_over_process` | No clear contradiction | Neither the edits nor comments introduce process chronology. This pass remains supported. |

## 4. Performance assessment — Codex / 1.4

### Comparable metrics

| Metric | Result |
|---|---|
| Total committed prose paragraphs | 9 |
| Changed prose paragraphs | 4 of 9 (**44.4%**) |
| Committed characters | 5,942 |
| Git changed-character volume | 2,942 (1,675 deleted + 1,267 inserted) |
| Character edit density | **49.5%** of committed characters |
| Edit bucket mix | 4 `SUBSTANCE`, 1 `STYLE`, 3 `COMMENT`, 3 `TYPO` tokens |
| `SUBSTANCE` : `STYLE` ratio | **4 : 1** by changed-span count |

The high substantive share means this was not principally copy polishing. Boss changed the framing, causal explanation, named beneficiary, and readiness conclusion; comments also request a different presentation depth.

### Contract compliance of the committed draft

**Complete.** The committed draft supplied all five `required_structures`: three named subsections; reader-facing 16/26/33 readiness metrics; the required value table; one website-structure figure placeholder; and one data-governance figure placeholder. It also observed the contract's blueprint-not-live-system limitation and terminology distinction. The current working tree no longer contains the reader-facing 16/26/33 structure, but that is not attributable to Codex.

### Receipt honesty

**Mechanically complete but materially overconfident.** The receipt had zero findings and correctly tied the committed claims to the evidence sidecar. It nevertheless failed to surface: (1) the contract's conflict with the controlling plan on readiness/gap analysis; (2) the possibility that the website/data-platform causal ordering did not match Boss's intended architecture explanation; and (3) the desired information hierarchy/degree of explanation. “Pass” therefore means contract-and-source compliance, not confirmed Boss acceptance.

### Top failure patterns

1. **Instruction-chain blind spot:** Codex followed a contract that mandated a readiness/gap paragraph even though the approved plan excludes detailed gap analysis; this is a contract-author defect, not a content-fidelity failure by Codex.
2. **Architecture explanation not calibrated to Boss's preferred order:** the original began with the web platform and made the data platform a condition behind it; Boss wants the data platform/governance foundation stated first and the website described as its presentation/navigation layer.
3. **Under-signalled website hierarchy and purposes:** despite six well-described main areas, the presentation did not make the requested x.x-level hierarchy or each topic's objective sufficiently visible to Boss. Any correction must stop short of §4's excluded detailed sitemap subcategories.

### Genuine strengths

1. **Strong delivery discipline:** all contractually required structures were present, including both figures, table, three-part organization, clear Thai shorthand, and the evidence-backed blueprint/not-live-system caveat.
2. **High source and institutional specificity:** the sidecar supports the 74-term, eight-domain, role, approval-sequence, and 16/26/33 claims; the draft distinguished output design from operational implementation and assigned concrete pre-development decisions to the department.

## Contract-versus-plan ruling: 16/26/33 readiness/gap paragraph

The contract required the exact `16/26/33` result in reader-facing text and asked for a description of readiness and gaps. The approved Chapter 1 plan is controlling: §4 for Executive Summary 1.4 requires vision/users/value, main information architecture, and governance, while excluding detailed sitemap subcategories; §6 expressly excludes detailed website-content and data-governance gap analysis and permits only the amount of readiness/limitation necessary to explain the design.

The committed paragraph went beyond a bare readiness caveat: it gave the 75-item distribution, named concentrations of gaps, and derived a content-development/procurement prioritization implication. Boss's `%%I think the plan states clearly that no gap analysis%%` is therefore a valid signal that the contract over-specified this content. The instruction chain was internally inconsistent. **Attribute this defect to the contract author/workflow calibration, not to Codex:** Codex complied with the written contract and its evidence sidecar; it should not be penalized for including a metric the contract explicitly required.
