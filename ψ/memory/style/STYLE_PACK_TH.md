# Style-Pack: TH (Thai institutional writing, repo-wide)
**Samples Learnt**: 23 (Technical Precision, Readability, Analytical Density, and Structural Flow) | **Last Updated**: 2026-08-28 | **Lexicon**: LEXICON_TH.json v4.1, 52 rules

## 1. Core Kernel (80/20)

These are the small set of rules that generate most of the desired NCAIF prose quality. Apply these before any secondary cleanup.

1. **Section Job First** — Before writing any section or paragraph, identify the section job in one sentence. Reject text that repeats the previous section's job or drifts into the next section's job.
2. **Evidence-First Institutional Opening** — Begin with the audit scale, named service, blocked task, or concrete finding. Do not open with a literary hook, scene-setting filler, or abstract thesis line.
3. **Analytical Payload Rule** — Every substantive paragraph must carry at least one claim, one concrete example or variable, one consequence, and one institutional or technical mechanism.
4. **Evidence-to-Action Chain** — Default paragraph logic should move from observed evidence → operational consequence → institutional cause → proposed mechanism.
5. **Product Naming** — Describe the deliverable, owner, or service artifact, not only the activity.
6. **One Paragraph, One Main Job** — Each paragraph should mainly define, diagnose, compare, or conclude. Do not mix multiple jobs unless the section explicitly requires it.
7. **Thai Institutional Voice Over Design-Memo Tone** — Rewrite any sentence that sounds like a translated design memo, software spec, or English argumentative skeleton.
8. **Active Institutional Agency When Actor Is Known** — When the actor is already known, state the duty directly. Prefer `กรมฯ จัดทำ...`, `บริการนี้ทำหน้าที่...`, `หน่วยงานใช้...` over passive or pseudo-passive framing such as `ถูกออกแบบให้...`.
9. **Banish Direct English Jargon** — Never use direct English operational jargon in audience-facing Thai prose when a functional Thai equivalent exists.
10. **Simplified Technical Prose** — Remove prestige descriptors like `ขั้นสูง`, `ที่สำคัญที่สุด`, or similar verbal inflation unless the distinction is materially necessary.

## 2. Stage / Scale Activation Map

This pack is no longer a flat checklist. Apply rules by stage and scale.

### Stage A / Scale 1 — Section architecture
- Section job first
- Evidence-first institutional opening
- Service-by-service discrimination
- Product naming

Use at outline time and first structural framing.

### Stage B / Scale 2 — First-draft content build
- Analytical payload rule
- Evidence-to-action chain
- One paragraph, one main job
- Preservation of source meaning and institutional distinctions

Use when building the first complete section. Do not over-optimize diction yet.

### Stage C / Scale 2 — Structural revision
- Split overloaded paragraphs
- Restore blocked actor / consequence clarity
- Separate package, mechanism, and adoption-test logic
- Use bullets or numbered lists when multiple service elements blur together

Use after the first draft exists but before sentence polish.

### Stage D / Scale 3 — Sentence agency and voice
- Thai institutional voice over design-memo tone
- Active institutional agency when actor is known
- Eliminate translated contrast scaffolding
- Direct assertion before contrast
- Remove composite-noun inflation

Use only after structure and payload already work.

### Stage E / Scale 4 — Lexicon and cleanup
- Department shorthand normalization
- English-jargon bans and Thai substitutions
- Parenthetical anchor discipline
- Banned/common phrase cleanup

Use as a late-pass consistency sweep, not as a first-pass drafting engine.

### Stage F — Release gate
- No invented sources
- No repo-internal leakage in audience-facing prose
- No unresolved placeholders unless explicitly marked
- Final style drift check against the context pack

## 3. Secondary Pass Rules

These rules matter, but they should not compete with the Core Kernel during early drafting.

1. **Precision in Resolution Scales** — Specify exact scale or range when discussing data resolution.
   - Use **"ระดับ 25-100 กิโลเมตร"** instead of "ระดับกิโลเมตร".
   - Use **"ระดับหลักสิบเมตร"** instead of "ระดับเมตร".
2. **Ground Gaps with Precise Baseline Parameters** — Specify resolutions, variables, or scenarios when discussing climate-model gaps.
3. **Parenthetical Technical Anchors** — Introduce English scientific concepts or abbreviations in parentheses only when they improve traceability.
4. **Paragraph-Based Flow with Controlled Compression** — Keep prose paragraph-led, but switch to bullets or tables when dense comparison would otherwise blur distinctions.
5. **Structured Breakdowns for Complex Lists** — When listing pillars, layers, or recommendations, prefer numbered lists over compressed inline prose.
6. **Direct Mandates Over Philosophical Preaching** — In recommendation mode, write operational mandates rather than moral advice or perspective shifts.
7. **The Anti-Vagueness Rule (The System Identity)** — Do not use `ระบบ` without specifying which system when the exact identity matters.

## 4. Hierarchical Vetting Stack (apply in order)
1. **Level 1 — Section Job First**
   - Before writing any paragraph, identify the section's job in one sentence.
   - Reject any paragraph that repeats the previous section's job or drifts into the next section's job.
2. **Level 2 — Paragraph Function**
   - Each paragraph must do only one main job: define, compare, diagnose, or conclude.
   - Do not mix background, evaluation, and recommendation in the same paragraph unless the section explicitly requires it.
3. **Level 3 — Evidence Payload**
   - Each paragraph must contain: one finding, one concrete example or variable, one implication, and one named institutional or technical basis.
   - If any of these four pieces is missing, the paragraph is incomplete.
4. **Level 4 — Thai Institutional Voice**
   - Rewrite any sentence that sounds like a translated design memo, software spec, or English argumentative skeleton.
   - Prefer Thai institutional explanation over imported system-design phrasing.
5. **Level 5 — Diction Cleanup**
   - Remove filler transitions, prestige words, and literal translations before accepting the paragraph.
   - Final prose must sound like a report written for Thai policy and technical readers, not like a polished translation.

## 5. Lexicon & Diction (Dos/Don'ts)
| Banned/Common | Preferred | Reason |
| :--- | :--- | :--- |
| "ความลักลั่น" | "ความซ้ำซ้อนและความไร้มาตรฐาน" | More descriptive of technical failure. |
| "ท่วมท้น" | [Technical Method] | Use "จากการสังเกตุผ่านดาวเทียม". |
| "ระดับเมตร" | "ระดับหลักสิบเมตร" | More realistic for current operational downscaling. |
| "ขั้นสูง" (Advanced) | [Omit] | Institutional prose avoids hyperbole. |
| "นอกจากนี้" | *Minimize or replace with direct continuation* | Reads like filler and weakens momentum. |
| "ยิ่งไปกว่านั้น" | *Omit* | Artificial transition word. |
| "มุ่งเน้น" | "เน้น" | Redundant prefix word in formal Thai (ตัดคำว่า "มุ่ง" ออก). |
| "นับได้ว่า" | "ถือว่า", "จัดเป็น" | Formal AI filler. |
| "ในยุคปัจจุบัน" | *Begin directly with the finding* | Generic introductory phrase. |
| "ในทางกลับกัน" | *Omit or use natural contrast* | AI transition filler. |
| "ถึงกระนั้น" | *Omit or use natural transition* | AI transition filler. |
| "สถาปัตยกรรมด้านการจัดการความเสี่ยง..." | "การจัดการความเสี่ยง..." | Avoids overly verbose AI framing for institutional risks. |
| "แก่นแท้ของยุทธศาสตร์..." | "ใจความหลักของยุทธศาสตร์..." | Avoids literal or literary AI phrasing. |
| "ก่อให้เกิดความท้าทายเชิงโครงสร้างอย่างมีนัยสำคัญ" | "ก่อให้เกิดช่องว่างของข้อมูล" | Replaces abstract AI filler with precise fact. |
| "ไร้รอยต่อ" / "สมบูรณ์แบบ" | *Omit or describe operational reality* | Avoids hyperbolic marketing terms. |
| "workflow" / "เวิร์กโฟลว์" เมื่อไม่จำเป็น | "ขั้นตอนการทำงาน", "ลำดับการประเมิน", "กระบวนงาน" | Prefer Thai institutional wording unless English is materially necessary. |
| "layer", "ชั้น", "ชั้นข้อมูล" เมื่อใช้เป็นคำแปลตรง | "ส่วนข้อมูล", "ส่วนที่ทำหน้าที่...", "ข้อมูลชุด...", "องค์ประกอบ..." | Avoid literal architecture translation in audience-facing prose. |
| "input" / "output" | "ข้อมูลที่ใช้", "ผลลัพธ์", "ข้อมูลที่ได้จากการประเมิน" | Reduce software-spec tone in report prose. |
| "อย่างเป็นทางการในระดับโครงสร้างข้อมูล" | "แยกออกจากกันให้ชัดในตัวฐานข้อมูล" | Composite noun is unnatural and over-translated. |
| ประโยคแบบ "ไม่ได้...แต่..." เพื่อเปิดย่อหน้า | เริ่มจากข้อเท็จจริงหรือหน้าที่โดยตรง | Thai report prose should state the actual basis first, not a negated pseudo-contrast. |
| "use case" | "กรณีการใช้งาน" | Avoid direct English jargon in formal reports. |
| "raster" | "ขนาดกริด", "ข้อมูลกริด" | Removes redundant technical phrasing. |
| "interoperability" | "ความสามารถในการทำงานร่วมกัน", "การเชื่อมต่อข้อมูลระหว่างระบบ" | Translates technical system terms to operational functions. |
| "usability" | "ความพร้อมใช้งาน", "ความง่ายในการนำข้อมูลไปใช้งาน" | Translates to plain operational language. |
| "lag time" | "จังหวะเวลา", "ช่วงเวลาดีเลย์ของข้อมูล" | Explains latency in a functional, reader-friendly format. |
| "DCCE" | "กรมฯ" | Standard official shorthand for the Department of Climate Change and Environment. |
| "อัปเดต" / "รอบการอัปเดต" | "ปรับปรุง" / "รอบการปรับปรุง" | Proper Thai policy terminology. |
| "dashboard" / "แดชบอร์ด" | "แดชบอร์ดแสดงผลข้อมูล" | Proper descriptive Thai localization. |
| "โครงสร้างไอที" | "โครงสร้างทางเทคโนโลยีสารสนเทศ" | Formal registrar terminology. |
| "หน่วยการจัดการจริง" | "ขอบเขตพื้นที่ที่หน่วยงานรับทุนจำเป็นต้องจัดการจริง" | Grounded spatial boundaries. |
| "ข้อเสนอเชิงยุทธศาสตร์ที่สุด" | "ข้อเสนอเชิงยุทธศาสตร์ที่สำคัญ" | Remove subjective superlatives. |
| "จุดยืน..." / "จุดตัดเวลา" | "กำหนด..." / "เส้นตาย" | Abstract positional nouns ("stance", "cutoff point") read as literal-translation scaffolding; state the decision or deadline directly. |
| "ประตูหลัก" | "โครงสร้างหลัก", "ศูนย์กลาง..." | Literal translation of the English "front door/gateway" metaphor; name the actual function instead. |
| Quoted English strategy/codename (e.g. "Blueprint-as-a-Shield") | Plain Thai description of the strategy's mechanism | Project-internal English branding should not carry into audience-facing Thai prose, even in quotes. |
| "ผู้สนับสนุนโครงการ" | "กรม สส." | Generic role noun for an already-named institutional actor; same typology as DCCE -> กรมฯ. |
| "ที่ขยายผลได้" | "ที่ปรับขยายได้ในอนาคต" | Awkward modifier construction; more natural phrasing for extensibility. |
| "ปิด[ผลงาน]" to mean "completed" (e.g. "ปิดผังเว็บไซต์", "ปิดพจนานุกรม") | "สรุป[ผลงาน]" or a concrete verb naming the actual action | "ปิด" reads as a literal translation of "close out." Reserve "ปิด"/"ผนึก" for an actual ledger Sealed status only. |

### Technical Terminology Mapping
* **Climate Change** -> การเปลี่ยนแปลงสภาพภูมิอากาศ (Climate Change)
* **Non-Economic Loss and Damage** -> ความสูญเสียและความเสียหายที่ไม่ใช่เชิงเศรษฐกิจ (Non-Economic Loss and Damage: NELD)
* **Data Catalog** -> บัญชีรายการข้อมูล (Data Catalog)
* **Metadata Standard** -> มาตรฐานข้อมูลกำกับ (Metadata Standard)
* **Risk Methodology Catalog** -> บัญชีระเบียบวิธีความเสี่ยง (Risk Methodology Catalog)
* **Service Portfolio** -> ชุดบริการข้อมูลสารสนเทศ (Service Portfolio)
* **Workflow** -> ขั้นตอนปฏิบัติ (Workflow)
* **Interoperability** -> การทำงานร่วมกันของระบบข้อมูล (Interoperability)
* **Uncertainty Communication** -> การสื่อสารความไม่แน่นอน (Uncertainty Communication)
* **Most Significant Change (MSC)** -> เรื่องเล่าความเปลี่ยนแปลงที่สำคัญที่สุด (Most Significant Change)

## 6. Structural DNA
- **Traceable Intro**: Start with the audit scale, named service, or concrete finding.
- **Evidence-to-Action Chain**: Default paragraph logic should move from observed evidence → operational consequence → institutional cause → proposed mechanism.
- **Scale-Specific Impact**: Link technical gaps to concrete resolutions (25km vs 10m), and specify what task fails at each scale.
- **Service-by-Service Discrimination**: When multiple services differ, separate them into bullets or a table rather than compressing them into one dense paragraph.
- **Audit Risk**: Frame technical hurdles as a threat to **"ความชอบธรรมในการใช้งบประมาณ"** and to decision usefulness.
- **Product Naming**: Recommendations should resolve into named artifacts, owners, or standards, not only verbs.

### Thai Sentence Shape Guardrails
- Start with the real subject, institution, dataset, or finding whenever possible.
- When the institutional actor is already known, prefer active-duty phrasing over passive intention language.
- Avoid opening a sentence by denying what something is **not** before stating what it **is**.
- Ban pseudo-balanced translated structures such as:
  - "...ไม่ได้...แต่..."
  - "ไม่ใช่เพียง...แต่ยัง..."
  when they are used as rhetorical scaffolding rather than real contrast.
- Preferred pattern: state the actual function first, then state the limitation or contrast in the next clause or next sentence.
- Preferred active transformation:
  - Avoid: `บริการนี้ถูกออกแบบให้ทำหน้าที่...`
  - Prefer: `บริการนี้ทำหน้าที่...` or `กรมฯ จัดทำ...`
- Example preferred transformation:
  - Avoid: "การออกแบบชุดข้อมูล...ไม่ได้เริ่มจาก...แต่เริ่มจาก..."
  - Prefer: "การออกแบบชุดข้อมูล...เริ่มจากข้อมูลที่ ปภ. มีอยู่จริงในระบบงานปัจจุบัน แล้วจึงพิจารณาว่าข้อมูลส่วนใดยังไม่เพียงพอสำหรับการประเมินความเสียหายและความสูญเสีย"

## 7. Anti-AI Shield (Counter-examples)
- **CRITICAL DON'T**: Start with "อย่างไรก็ตาม..." or "แม้ว่า..." unless the contrast is doing real analytical work.
- **CRITICAL DON'T**: Use "ระบบ" without identifying *which* system.
- **CRITICAL DON'T**: Use hyperbolic marketing/commercial words like "ไร้รอยต่อ" or "สมบูรณ์แบบ". Describe actual operational workflows or technical constraints instead.
- **DON'T**: Use high-precision decimals in summaries; round to nearest 10 or 5 unless the precision itself is essential.
- **DON'T**: Write abstract gap statements without a concrete blocked task, service, or example.
- **DON'T**: Write recommendation paragraphs that name only a direction. Name the artifact, owner, or mechanism.
- **DON'T**: Compress multiple service gaps into one dense paragraph when the distinctions matter to the reader.
- **DON'T**: Issue blanket criticisms of institutional practices (e.g., claiming "ปภ. ยังไม่มีการดำเนินการ...") without distinguishing operational scopes (e.g., initial 0-72h emergency response reporting vs. post-disaster recovery/needs assessment).
- **DON'T**: Let a paragraph sound like a translated architecture note by piling up composite nouns such as "ระดับโครงสร้างข้อมูล", "ชั้นข้อมูลส่วนขยาย", or "บูรณภาพเชิงวิเคราะห์" when simpler Thai can name the same function.
- **DON'T**: Explain by negation first if the same point can be stated directly from the actual evidence or institutional role.
- **DON'T**: Open sentences or build key arguments using the translated contrast template `ไม่ควรถูกมองเป็น... แต่ควรถูกมองเป็น...` or `ไม่ได้... แต่...`.
- **DON'T**: Use conceptual/philosophical prefixes like `ตรรกะหลักของ...` in report summaries.
- **DON'T**: Use subjective superlatives like `ข้อเสนอเชิงยุทธศาสตร์ที่สุด` (use `ข้อเสนอเชิงยุทธศาสตร์ที่สำคัญ` instead).
- **DON'T**: Use passive or pseudo-passive agency like `ถูกออกแบบให้...` when the institutional actor is already known and can be named directly.
- **DON'T**: Compress by deleting governance content. Cut scaffolding first, not institutional duties, evidence, or conditions of use.

## 8. Master Implementation Prompt
> **Writing Mode**: TH-Institutional (v5.0 - Stage-Aware, Evidence-Dense, Institution-Led)
> 
> **How to use this pack**:
> 1. First secure the section job and paragraph payload.
> 2. Then repair structure and service-package sequencing.
> 3. Only after that polish sentence agency and diction.
> 4. Use the lexicon as a late-pass cleanup layer, not a first-pass drafting engine.
>
> **Core behavior**: Write in a punchy, authoritative Thai institutional voice. Start from the evidence, blocked task, or service function, not a literary hook. Make each paragraph do one clear job. Ensure each substantive paragraph contains a finding, example, consequence, and mechanism. Name the deliverable, owner, or service artifact directly. Prefer active institutional agency when the actor is known. Remove translated contrast scaffolding, prestige filler, and design-memo tone. Keep technical specificity where it matters, but never let micro-style optimization outrank content logic.

## 9. Incremental Capture Log

### 2026-06-25 — Style-pack upgrade from institutional analysis failure

**Source of delta**: review of CRDB section [`5.3.8`](ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/2026-06-25_draft_section-5.3.8.md) and [`5.3.9`](ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/2026-06-25_draft_section-5.3.9.md), plus comparison with [`STYLE_PACK_TOR5.5-Articles.md`](ψ/memory/style/STYLE_PACK_TOR5.5-Articles.md).

#### Preferred direction detected
- **Readable prose is useful, but it must not become a license for abstraction**.
- **Paragraph-led flow still matters for institutional writing, but dense multi-service comparisons should use bullets or tables**.
- **Anti-AI cleanup is helpful, yet it must be paired with payload rules or the model will produce polished emptiness**.
- **Article-style readability controls are transferable only when they do not force sensory openings or narrative hooks into report writing**.

#### New style rule candidates
11. **Analytical Payload Cannot Be Dropped**: No paragraph may survive if it loses its example, consequence, or mechanism.
12. **Service Comparisons Prefer Structured Forms**: Use bullets or tables when the reader must discriminate among multiple services, gaps, or standards.
13. **Readable Does Not Mean Literary**: Keep the prose crisp and human, but never add a sensory opening or story hook to an institutional section unless the section function truly requires it.
14. **Recommendations Must Name a Deliverable**: Every recommendation should name the output artifact, responsible owner, or service mechanism.

#### Anti-regression note
- Do **not** borrow TOR 5.5-style opening moves into institutional sections.
- Do **not** let paragraph flow override analytical completeness.
- Do **not** allow style smoothing to erase concrete examples, blocked workflows, or institutional causes.

### 2026-06-26 — Style-pack upgrade from Disaster Management analysis

**Source of delta**: [edit_notes_5.3.6.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/final_report/5.3/edit_notes_5.3.6.md)

#### Preferred direction detected
- **Eliminate AI puffery and abstract filler**: Replaced complex-sounding phrases with concrete facts (e.g., using "ช่องว่างของข้อมูล" instead of "ความท้าทายเชิงโครงสร้างอย่างมีนัยสำคัญ", and "การจัดการความเสี่ยง..." instead of "สถาปัตยกรรมด้านการจัดการความเสี่ยง...").
- **Avoid commercial/marketing hype**: Banned words like "ไร้รอยต่อ" or "สมบูรณ์แบบ" to preserve institutional gravity and accuracy.
- **Contextual and precise institutional critiques**: Refrain from broad criticisms about organizational gaps; ground observations in distinct timeframes (e.g., initial response window vs. post-disaster assessment process).

### 2026-06-27 — Style-pack upgrade from CRDB Topic 3–5 language correction

**Source of delta**: review of [`5.3.6_edited_v1.md`](ψ/incubate/DCCE/CRDB/output/final_report/5.3/5.3.6_edited_v1.md:39) against human-edited Thai sections in [`5.3.6_edited_v1.md`](ψ/incubate/DCCE/CRDB/output/final_report/5.3/5.3.6_edited_v1.md:19).

#### Preferred direction detected
- **Thai report prose should not sound like translated architecture writing**.
- **Design sections must still read like institutional analysis, not technical product notes**.
- **Sentence openings should name the real subject and function first, instead of using negated contrast scaffolding**.

#### New style rule candidates
15. **Hierarchical Vetting Before Acceptance**: Check section job, paragraph job, evidence payload, Thai voice, and diction cleanup in that order.
16. **No Composite-Noun Inflation**: Replace overbuilt translated clusters with simple Thai phrasing that names the function directly.
17. **Direct Assertion Before Contrast**: State what the subject does first; only then explain what it cannot do or does not yet support.
18. **Architecture Terms Must Be Naturalized**: Replace literal imports like `layer`, `input`, `output`, and stray `workflow` wording with Thai institutional equivalents unless the English term is itself the object of explanation.

#### Anti-regression note
- Do **not** open key explanatory paragraphs with "ไม่ได้...แต่..." unless the negative contrast is essential and cannot be rewritten more directly.
- Do **not** let MVD or database sections drift into software-spec Thai.
- Do **not** preserve English design vocabulary when a normal Thai report term can carry the meaning more naturally.

### 2026-07-01 — Style-pack upgrade from Section 5.3.8 in-place edits

**Source of delta**: [2026-07-01_15-02_NCAIF-Institutional_diff-evidence.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-07-01_15-02_NCAIF-Institutional_diff-evidence.md)

#### Preferred direction detected
- **Banish direct English jargon**: Replaced direct English terms like `use case`, `workflow`, `raster`, and `usability` with natural, functional Thai policy terminology to fit the target audience.
- **Use standard official shorthand**: Replaced `DCCE` with `กรมฯ` to match official report registers.
- **Ground model descriptions with precise parameters**: Replaced general comments on downscaling with exact grid sizes, parameters, and IPCC scenarios.

#### New style rule candidates
19. **Banish Direct English Jargon**: Replaced English terms (`use case` -> `กรณีการใช้งาน`, `workflow` -> `ขั้นตอนการทำงาน`, `usability` -> `ความพร้อมใช้งาน`).
20. **Refer to Department as กรมฯ**: Use `กรมฯ` in Thai report body text instead of `DCCE`.
21. **Ground Gaps with Precise Baseline Parameters**: Always specify specific resolutions (25 km, 5 km), variables, and scenarios when discussing climate projections.

#### Anti-regression note
- Do **not** allow stray English architecture vocabulary like `use case` or `workflow` in final audience-facing summaries.
- Do **not** generalize downscaling gaps without specifying what variables or scenarios are blocked or enabled at that scale.

### 2026-07-01 (Session 2) — Style-pack upgrade from Section 5.3.9 in-place edits

**Source of delta**: Section 5.3.9 in-place edits.

#### Preferred direction detected
- **Direct Mandates Over Philosophical Preaching**: Shifted general advice and perspective shifts to action-oriented institutional mandates.
- **Eliminated English Contrast Scaffolding**: Avoided structured negations like `ไม่ได้... แต่...` or `ไม่ควรถูกมองเป็น...`.
- **Structured Breakdowns**: List core items/pillars as numbered lists with line breaks instead of single inline sentences.

#### New style rule candidates
22. **Direct Mandates Over Philosophical Preaching**: Frame recommendations as concrete operational mandates (e.g. `ต้องจัดตั้งแนวทาง...`, `จะต้องบริหาร...`).
23. **Eliminate English Contrast Scaffolding**: Never build key arguments using the translated contrast pattern `ไม่ควรถูกมองเป็น... แต่ควรถูกมองเป็น...` or `ไม่ได้... แต่...`.
24. **Structured Breakdowns for Complex Lists**: Format multi-item recommendations or pillars as numbered lists with line breaks.

#### Anti-regression note
- Do **not** use academic preaching or moral advice structures.
- Do **not** use translated English contrasting templates.
- Do **not** compress multi-item recommendations into single inline text blocks.

### 2026-07-02 — Style-pack upgrade from Full_Report_Final.md in-place edits

**Source of delta**: [2026-07-02_16-02_NCAIF-Institutional_diff-evidence.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-07-02_16-02_NCAIF-Institutional_diff-evidence.md)

#### Preferred direction detected
- **Systems Thinking**: Shifted from treating the 6 NAP sectors as isolated theoretical buckets to describing cascading impacts ("ห่วงโซ่ผลกระทบที่ข้ามสาขา ข้ามระบบ") using biophysical and economic lenses.
- **Analytical Critique**: Added critical reflection on disaster frameworks, pointing out that human-centric definitions overlook natural resource impacts.
- **Humanizing Impact**: Anchored macro-economic threats to human well-being and quality of life.
- **Paragraph Cohesion**: Respected sectoral boundaries by not cramming different sectors into one paragraph.

#### New style rule candidates
25. **Systems Thinking Over Silos**: Emphasize cascading impacts across systems rather than treating NAP sectors as isolated buckets.
26. **Analytical Critique Over Fact-Stating**: Critically evaluate frameworks instead of just describing them (e.g., noting the limitations of human-centric disaster definitions).
27. **Humanize the Macro-Impact**: Anchor macro-economic risks to actual human well-being and quality of life.
28. **Paragraph Cohesion (Sectoral Boundaries)**: Do not compress multiple distinct sectors into a single paragraph; respect sectoral boundaries.

#### Anti-regression note
- Do **not** use AI "fluff" or poetic drama (e.g., `ตีกรอบความไม่แน่นอน`, `เปลี่ยนจุดศูนย์กลาง...`).
- Do **not** use English translations in parentheses unless absolutely necessary for technical precision.


### 2026-08-05 — Style-pack upgrade from CRDB timeline-th synthesis corrections

**Source of delta**: [2026-08-05_16-44_NCAIF-Institutional_diff-evidence.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-08-05_16-44_NCAIF-Institutional_diff-evidence.md) — direct user corrections to `ψ/incubate/DCCE/CRDB/.timeline-th/curated-events.json` (the `timeline-th` skill's curated project-timeline synthesis, first time this style pack was applied outside the main report body).

#### Preferred direction detected
- **No abstract positional nouns for decisions**: "จุดยืน" (stance) and "จุดตัดเวลา" (cutoff point) are literal-translation scaffolding around a decision or deadline that should just be stated directly.
- **No metaphor-translation for institutional roles**: "ประตูหลัก" (front door) reads as an imported English metaphor; name the function ("โครงสร้างหลัก") instead.
- **No quoted English strategy names in Thai prose**: project-internal codenames like "Blueprint-as-a-Shield" should be described in plain Thai, not carried through in quotes — this generalizes the existing parenthetical-anchor discipline from acronyms/schema names to strategy names.
- **Named actor over generic role noun**: "ผู้สนับสนุนโครงการ" should become "กรม สส." when it refers to one already-known department — same typology as the existing DCCE -> กรมฯ rule.
- **"ปิด" is not a general completion verb**: applying "ปิด" to a sitemap, glossary, or dataset ("ปิดผังเว็บไซต์") reads as literal-translated "close out." Use "สรุป" or a concrete verb. The one exception is an actual ledger `Sealed` status, which uses this system's own term "ผนึก" (from `/seal`) — a precision fix, not a naturalization fix.

#### New style rule candidates
29. **No Abstract-Noun Scaffolding for Decisions**: State the decision or deadline directly rather than naming an abstract position ("จุดยืน", "จุดตัด").
30. **No Metaphor-Translation for Institutional Roles**: Avoid literal English metaphors translated into Thai nouns ("ประตูหลัก"); name the actual function.
31. **No Quoted English Strategy Names**: Describe a strategy's mechanism in plain Thai rather than carrying its English codename through in quotes.
32. **Named Actor Over Generic Role**: Use the real institutional shorthand ("กรม สส.") instead of a generic role noun when the actor is already known.
33. **"ปิด" Reserved for Ledger-Sealing Status Only**: Use "สรุป" or a concrete verb for "finished producing X"; "ปิด"/"ผนึก" is reserved for an actual sealed ledger entry.

#### Anti-regression note
- Do **not** reintroduce "จุดยืน"/"จุดตัด" as decision-naming nouns.
- Do **not** carry a project's internal English strategy codename into Thai prose in quotes.
- Do **not** use "ปิด" as a stand-in for "we finished making X."

### 2026-08-17 — Style-pack upgrade from CRDB Executive Briefing SlideDoc in-place edits

**Source of delta**: [2026-08-17_12-51_NCAIF-Institutional_diff-evidence.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-08-17_12-51_NCAIF-Institutional_diff-evidence.md) — human refinement on [`02_DCCE_Executive_Briefing.html`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/11_Communication_Deck/02_DCCE_Executive_Briefing.html).

#### Preferred direction detected
- **De-metaphorization (No dramatic mechanical/retail analogies in institutional decks)**: Replace AI metaphors like `หน้ากากแดชบอร์ดโดยไร้เครื่องยนต์ข้อมูล`, `หน้าร้านเว็บไซต์`, `เครื่องยนต์ข้อมูล`, `เกราะป้องกันเชิงระบบ`, `หลุมพรางระบบสารสนเทศร้าง` with precise modern data architecture and web terms (`ส่วนแสดงเนื้อหาและข้อมูลโดยไม่มีการจัดการข้อมูลหลังบ้าน`, `ระบบหน้าบ้าน (frontend)`, `ระบบหลังบ้าน (backend)`, `Data Platform`, `กลไกการป้องกันความผิดพลาด`, `Information Architecture`, `semantic layer`).
- **De-hyping and metric deflation**: Eliminate ungrounded dramatic multipliers (`25 เท่า`, `ก้าวกระโดด`, `ขุมพลังทางวิทยาศาสตร์ใหม่`) in favor of clear qualitative precision (`แม่นยำขึ้น`).
- **Project deliverable neutrality**: Use standard deliverable terms (`ผลผลิตของโครงการ`, `ผลลัพธ์ของโครงการ`) over self-praising consulting adjectives (`ผลสัมฤทธิ์ที่ส่งมอบครบถ้วน`).
- **Natural taxonomy**: Use `ผังเว็บไซต์ 15 หมวด` rather than graph-theory `15 โหนด`, and standardize `ทรัพย์สินดิจิทัล / Digital Assets`.

#### New style rule candidates
34. **Zero Dramatic/Mechanical Metaphors**: Never use machine or storefront analogies (`เครื่องยนต์ข้อมูล`, `หน้าร้านเว็บไซต์`, `หน้ากากแดชบอร์ด`, `เกราะป้องกันเชิงระบบ`). Use standard architecture terms: `ระบบหน้าบ้าน (frontend)`, `ระบบหลังบ้าน (backend)`, `Data Platform`, `Information Architecture`, `semantic layer`.
35. **No Artificial Metric Multipliers / Dramatic Claims**: Do not invent or emphasize quantitative multiplier leaps (`25 เท่า`, `ก้าวกระโดด`, `ขุมพลังใหม่`). State qualitative or empirical improvements directly (`แม่นยำขึ้น`).
36. **Institutional Deliverable Terminology Neutrality**: Use standard project terms (`ผลผลิตของโครงการ`, `ผลลัพธ์ของโครงการ`) instead of self-congratulatory consulting jargon (`ผลสัมฤทธิ์ที่ส่งมอบครบถ้วน`).
37. **Information Architecture Taxonomy**: Use `หมวด` (sections/categories) for website navigation rather than graph-theory abstractions like `โหนด`.

#### Anti-regression note
- Do **not** use `เครื่องยนต์ข้อมูล` or `หน้าร้านเว็บไซต์` in presentation decks or reports.
- Do **not** add artificial multiplier hype (`25 เท่า`) without cited benchmark verification.
- Do **not** use `ผลสัมฤทธิ์ที่ส่งมอบครบถ้วน` — use `ผลผลิตของโครงการ`.

### 2026-08-25 — Consolidation: one pack, typed rules

**Source of delta**: harness audit, not a writing sample. No new style rules were learned in this round.

#### What changed
- **Renamed** `STYLE_PACK_NCAIF-Institutional` → `STYLE_PACK_TH`. The pack governs every Thai deliverable in this repo, not the NCAIF report alone. Prior capture-log entries keep their original evidence filenames.
- **Consolidated** `STYLE_PACK_TOR5.5-Articles` into this pack and archived it to [`ψ/archive/style/`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/archive/style/). Its four unique lexicon rules — `นอกจากนี้`, `ยิ่งไปกว่านั้น`, `นับได้ว่า`, `เอฟเฟกต์` — were dormant since 2026-06-25 and had never been enforced, because the linter hardcoded the NCAIF lexicon path. They now apply repo-wide as `scope: universal`.
- **Lexicon v4.0** (`LEXICON_TH.json`, 48 entries) adds two fields to every rule:
  - `kind`: `literal` (exact string) · `regex` (explicit `pattern`) · `structural` (needs a grader, never blocks)
  - `scope`: `universal` (default) · `report` · `article` · `letter`

#### Rules repaired
Four entries were silently inert or self-defeating before this round:
- `จุดยืน... / จุดตัด...`, `quoted English strategy/codename (…)`, and `ปิด[ผลงาน/deliverable] …` were prose descriptions sitting in a field the linter compiles as regex. They matched nothing. All three are now `kind: regex` with real patterns.
- `สมมติฐานแบบเหมารวมนั้นไม่เพียงพอ` had a prescribed replacement containing its own banned string, so applying the fix still failed the rule. It is an expand-the-claim instruction rather than a term swap, and is now `kind: structural`.

#### Anti-regression note
- A rule that cannot be expressed as an exact string or a compiling pattern belongs in `kind: structural`. Do **not** write its English description into `banned` — that field is matched, not read.
- `validate_lexicon.py` now blocks all four failure shapes at write time. Run it after every `/style-capture` round.

### 2026-08-26 — Style-pack upgrade from TOR70 Director Toey Briefing Deck (Anti-Fragmentation & Readability Cadence)

**Source of delta**: [`2026-08-26_20-08_Thai-Briefing_diff-evidence.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-08-26_20-08_Thai-Briefing_diff-evidence.md) — review and refinement of executive briefing deck [`2026-08-26_TOR70-director-toey-briefing-deck-TH.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/archive/2026-08-26_TOR70-director-toey-briefing-deck-TH.md).

#### Preferred direction detected
- **Elimination of Fragmented Floating Phrases**: Never start an introductory or scoping section with a detached metadata count or standalone noun phrase (e.g., `สไลด์หลัก 14 แผ่น... เอกสารนี้...`). Unify scope metadata and purpose into a single, cohesive sentence (`เอกสารนี้ประกอบด้วย... ซึ่งจัดทำขึ้นเพื่อ...`).
- **Enumeration Cadence & Punctuation in Tables/Summaries**: In table cells and dense artifact inventories, avoid stringing items together with only spaces. Use commas (`,`) and formal conjunctions (`และ`, `รวมถึง`, `พร้อมด้วย`) to create clean parsing cadence.
- **List / Bullet Parallelism**: Maintain strict grammatical symmetry across all items in a bulleted list (e.g., all outcome noun phrases with relative clauses `ที่สามารถ...` / `ซึ่งผ่าน...`, rather than mixing full declarative sentences with bare fragments).
- **Task Table Verb-Object Uniformity**: In operational schedules and modification tables, consistently lead every task item with an active operational verb (`จัดทำ...`, `กำหนด...`, `ออกแบบ...`, `เพิ่ม...`).

#### New style rule candidates (Observed in Miss Register)
- `ประโยคเกริ่นนำขึ้นต้นด้วยกลุ่มคำนามลอยโดยไม่มีกริยาหลัก` -> Unify into complete sentence with relational connectors.
- `รายการคำนามในตารางหรือเนื้อหาเว้นวรรคต่อกันโดยไม่มีจุลภาคหรือคำเชื่อม` -> Use commas and connectors (`และ`, `รวมถึง`).
- `โครงสร้างข้อความย่อยในลิสต์ขาดความสอดคล้องคู่ขนาน (Parallelism)` -> Enforce parallel grammatical structure.

#### Anti-regression note
- Do **not** leave floating count noun phrases at the start of briefing sections.
- Do **not** rely on plain whitespace to delimit multiple dense deliverables in table cells.
- Do **not** alternate between verb clauses and noun fragments within the same bullet list.

### 2026-08-27 — Style-pack upgrade from CRDB chapter-1 plan, exec-summary review marks

**Source of delta**: [`2026-08-27_22-10_TH_diff-evidence.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-08-27_22-10_TH_diff-evidence.md) — Boss's in-place `%%comment%%`/`~~strikethrough~~` review of [`แผนการเขียนบทที่ 1...md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่%201%20รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md), section 4 (exec-summary chapter plan).

#### Preferred direction detected
- **No bare modifier without its head noun**: a noun phrase like `ลำดับชั้นที่ไม่ซับซ้อน` or `การแยกเครื่องมือออกจากบัญชีข้อมูล` reads as incomprehensible when the thing being modified is never named — Boss's own words: "ชอบละนามตลอด อ่านไม่รู้เรื่อง" (habitually drops the noun, unreadable) and "you omit the essential noun very often making reading incomprehensible." This recurred 3x in one review pass (ลำดับชั้น, เครื่องมือ, การนำทาง) — a habit, not a typo.
- **Abstract summary/collective noun replaced with a concrete enumerated list**: `คุณค่าต่อการกำหนดนโยบาย...`, `ทุนเดิมที่นำมาใช้ต่อยอดได้`, `กลุ่มผู้มีส่วนร่วมที่ให้ความเห็น` + `ประเด็นหลักที่ใช้ทดสอบร่าง` were each replaced with a bullet naming the actual concrete referents (named teams, named meeting types, named data-quality dimensions), usually inside a parenthetical list. This generalizes the existing "abstract gap statement without concrete example" ban (§ line 183) from paragraph prose to bullet-point outline drafting specifically.
- **Wrong causal logic gets struck through, not reworded**: `ทุนเดิม → ข้อจำกัด → คำตอบเชิงออกแบบ` was cut entirely rather than patched, because the underlying reasoning was backwards — NCAIF is the benchmark of what content/products a user's journey needs; existing DCCE resources get analyzed *against* that benchmark to find gaps, not the other way around. When a bullet's logic (not just its wording) is wrong, treat it as a content defect.
- **Tension with an existing rule, flagged not resolved**: this same review pass *added* English glosses in parentheses for conceptual terms — `(availability)`, `(quality)`, `(format)`, `(Web Platform)`, `(Data Platform)` — which directly contradicts § 5 below ("Strict Parenthetical Anchor," banned: translating conceptual terms/phrases). Only observed once this round (below the promotion threshold), so it was **not** promoted into a rule. Flagged here so the next capture round checks whether this is genuine style evolution for planning/outline documents specifically, or a one-off Boss wanted for internal traceability that shouldn't generalize to prose.

#### New style rule candidates (promoted from Miss Register, both at 3x within this round)
38. **No Bare Modifier Without Head Noun**: Never write a noun phrase built on a modifier (ลำดับชั้น, เครื่องมือ, การนำทาง, การเปลี่ยนแปลง) without naming what it modifies. State what it is a hierarchy/tool/navigation/change *of*.
39. **Concretize Abstract Summary Nouns in Outlines**: When drafting bullet-point outlines or plans, replace an abstract collective noun (คุณค่า, ทุนเดิม, ข้อจำกัด, กลุ่มผู้มีส่วนร่วม, ประเด็นหลัก) with the concrete enumerated list it stands for — named actors, named activity types, named dimensions — typically inside a parenthetical list.

#### Anti-regression note
- Do **not** leave a noun phrase's head noun implicit — reread every "ลำดับชั้น/เครื่องมือ/การนำทาง"-style phrase and confirm the object is named.
- Do **not** leave `คุณค่า`/`ทุนเดิม`/`ข้อจำกัด`/`กลุ่มผู้มีส่วนร่วม`/`ประเด็นหลัก` standing alone in an outline bullet — expand it or cut it.
- Do **not** silently reword a bullet whose underlying causal claim is wrong; strike it and re-derive the correct chain.
- **Open tension, do not auto-apply**: do not add conceptual English parentheticals (e.g. `(quality)`, `(Data Platform)`) to prose sections based on this round alone — that contradicts § 5. Confirm with Boss whether planning/outline documents get an exception before generalizing.

### 2026-08-27 — Style-pack upgrade from CRDB exec-summary Stage B draft, internal-artifact leak (severity-promoted, not threshold-promoted)

**Source of delta**: Boss's in-place review of `ψ/incubate/drafts/crdb-exec-summary-intro-1.1/02_th_draft.md` (introduction section) — rated 2/10, most of it manually rewritten rather than incrementally corrected. Documented in full at [`23.55_exec-summary-stage-b-internal-artifact-leak.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/retrospectives/2026-08/27/23.55_exec-summary-stage-b-internal-artifact-leak.md). Promoted on severity and explicitness of Boss's correction rather than the usual 2-sighting miss-register threshold — three distinct sub-patterns each appeared once this round, but the underlying complaint ("I cant believe that you still leak internal artifacts and references into an audience facing report... This mean the style packs does not incorporate these rules") is unambiguous, not a candidate needing a second sighting to confirm.

#### Preferred direction detected
- **No internal process/sourcing artifacts in reader-facing prose.** Three manifestations found in one draft: (a) slide/artifact citations woven into narrative sentences (`สไลด์ที่ 13 ของชุดนำเสนอเผยแพร่ผลการศึกษา CRDB`, `สไลด์ที่ 9 จึงระบุ...`) — sourcing belongs only in a traceability sidecar, never inline in the reader's sentence; (b) a process flow the brief calls for as a diagram, rendered instead as an arrow-chain sentence (`การรวบรวมหลักฐาน → การสังเคราะห์ → ...`) — must be an actual figure/diagram placeholder, not prose with unicode arrows; (c) meta-commentary describing the report's own section structure (`...ตามตรรกะเดียวกัน กล่าวคือ บทเรียนจากต่างประเทศ (หัวข้อ 1.1)...`) — cut entirely; say what's true about the subject, not about the document.
- **A full rejection with no replacement offered means cut, not patch.** Boss struck the closing roadmap paragraph and rated it "0/10" with nothing to salvage — the correct response is removal, not a rewrite attempt.

#### New style rule candidates
40. **No Internal Process Artifacts in Reader-Facing Prose**: Never cite internal working-document locators (slide numbers, page numbers, artifact IDs) inside a narrative sentence meant for the final audience. Never render a called-for process diagram as an inline arrow-chain sentence — represent it as a figure/diagram placeholder instead. Never include meta-commentary describing what the report's own upcoming sections will cover.

#### Anti-regression note
- Do **not** write `สไลด์ที่ N`, `หน้า N`, or any internal artifact locator into a sentence meant for DCCE or any other final reader — sourcing lives in the evidence-traceability sidecar only.
- Do **not** translate a requested "diagram"/"figure" brief instruction into an inline arrow-chain sentence — flag it as a figure to be designed, or omit it, rather than faking it in prose.
- Do **not** write "this section discusses X, the next section discusses Y" — every sentence must be about the subject matter, not about the document's own structure.
- This is a `kind: structural` check (per `validate_lexicon.py`'s taxonomy) — it depends on recognizing sourcing/process metadata in context, not a fixed string or pattern. It cannot be fully caught by `lint_thai_writing.py` alone; the more reliable fix is an explicit instruction in the content-drafting stage's own prompt, plus an explicit item on any human accuracy-gate checklist: "does this sentence belong in the document, or is it metadata about how the document was made."

### 2026-08-28 — CRDB-project-specific: never write the bare acronym "NCAIF"

**Source of delta**: Boss's own rewrite of the exec-summary introduction eliminated every instance of "NCAIF" (roughly 8 places it could have appeared) in favor of the full Thai name at first mention and "โครงสร้างข้อมูลฯ" as the standing shorthand thereafter — not even a one-time "(NCAIF)" parenthetical gloss. Section 1.1, revised separately in the same document, still had 8 bare "NCAIF" mentions and drew an immediate, emphatic correction ("why NCAIF still gets throufh!!!!!!!!!!!!!!!! dont you see I replaced it all? in the บทนำ"). Promoted immediately on severity/clarity, same basis as rule 40 — this is Boss's own systematic writing choice repeated 8 times, not an ambiguous single instance.

#### New style rule candidate
41. **No Bare "NCAIF" in Audience-Facing Prose (CRDB project-specific)**: Never write the acronym "NCAIF" in report/exec-summary body text, including as a parenthetical gloss. Use the full Thai name ("โครงสร้างข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ") at first mention in a document, then "โครงสร้างข้อมูลฯ" as the standing shorthand for every subsequent mention. This generalizes past the single-document case: whenever a human's own rewrite of one section eliminates a term/acronym entirely, check every other section of the same document for the same term before considering a revision pass complete — a pattern established once in a document applies to the whole document, not just the section it was corrected in.

#### Anti-regression note
- Do **not** write "NCAIF" anywhere in CRDB exec-summary or full-report body prose — use "โครงสร้างข้อมูลฯ".
- When a human rewrites one section of a multi-section document, scan every other section for the same corrected pattern before calling a revision pass complete, rather than treating the correction as scoped to only the section it appeared in.

### 2026-08-28 — Style-pack audit from executive-summary 1.2–1.4 three-agent human review

**Source of delta**: [`2026-08-28_12-57_TH_diff-evidence.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/evidence/2026-08-28_12-57_TH_diff-evidence.md), with section-level evidence in `ψ/incubate/analysis/2026-08-28_exec-summary-1.2-1.4-review/obs-1.2.md`, `obs-1.3.md`, and `obs-1.4.md`.

#### What the review established
- **A passing editorial receipt is not enough to certify a causal bridge.** In Section 1.2, Boss explicitly rejected an inference that treated ownership distribution as the cause of a design action. The existing Evidence-to-Action Chain remains valid, but its gate must check the truth of the mechanism, not only whether a claim → implication sequence is present.
- **Substantive correction outweighs surface polish in this corpus.** The three edit inventories record substance-to-style ratios of 9:3 (1.2), 5:1 (1.3), and a contract-conflict-led structural correction in 1.4. A stylistic rewrite must never conceal a changed or unsupported claim.
- **No new rule was promoted.** Ten candidates were recorded in the miss register, each with one evidenced sighting. None reached the two-sighting threshold; all remain local hypotheses rather than binding Style-Pack or lexicon rules.

#### Guardrails confirmed, not expanded
- Keep reader-facing prose within the approved chapter plan: detailed content-gap analysis belongs outside this executive-summary chapter. The deleted 16/26/33 readiness paragraph in Section 1.4 is a contract-calibration error, not a drafting failure by the agent that followed the contract.
- Keep Boss's inline comments and typing slips separate from style evidence. Comments diagnose a problem but do not automatically provide a replacement; slips such as `แต่ล่ะ` or `ปนะมวลผล` are quarantined and must never enter the lexicon.
- Treat repeated full-name use after a document-level introduction, generic artifact naming, heading compression, and platform-ordering as pending hypotheses until another independent human correction confirms each pattern.

## 5. Strict Parenthetical Anchor (Anti-regression Update)
- **Rule**: Do **not** use English translations in parentheses unless absolutely necessary for technical precision.
- **Allowed**: Exact database schema names (`DISASTER_EVENT`), system keys, or official acronyms (`MVD`).
- **Banned**: Translating conceptual terms or phrases (e.g., `(Data Availability)`, `(Temporal completeness)`, `(Bounded Application Test)`). If it's a concept, write it in strong Thai and leave it alone.
