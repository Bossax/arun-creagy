# Style-Pack: TH (Thai institutional writing, repo-wide)
**Samples Learnt**: 28 (Technical Precision, Readability, Analytical Density, and Structural Flow) | **Last Updated**: 2026-09-02 | **Lexicon**: LEXICON_TH.json v4.6, 84 rules

## 1. Core Kernel (80/20)

These are the small set of rules that generate most of the desired NCAIF prose quality. Apply these before any secondary cleanup.

1. **Section Job First** — Before writing any section or paragraph, identify the section job in one sentence. Reject text that repeats the previous section's job or drifts into the next section's job.
2. **Evidence-First Institutional Opening** — Begin with the audit scale, named service, blocked task, or concrete finding. Do not open with a literary hook, scene-setting filler, or abstract thesis line.
3. **Analytical Payload Rule** — Every substantive paragraph must carry at least one claim, one concrete example or variable, one consequence, and one institutional or technical mechanism.
4. **Evidence-to-Action Chain** — Default paragraph logic should move from observed evidence → operational consequence → institutional cause → proposed mechanism.
5. **Product Naming** — Describe the deliverable, owner, or service artifact, not only the activity.
6. **One Paragraph, One Main Job** — Each paragraph should mainly define, diagnose, compare, or conclude. Do not mix multiple jobs unless the section explicitly requires it.
7. **Thai Institutional Voice Over Design-Memo Tone** — Rewrite any sentence that sounds like a translated design memo, software spec, or English argumentative skeleton.
8. **Active Institutional Agency When Actor Is Known** — When the actor is already known, state the duty directly. Prefer `กรมฯ จัดทำ...`, `บริการนี้ทำหน้าที่...`, `หน่วยงานใช้...` over passive or pseudo-passive framing such as `ถูกออกแบบให้...`. **Nuance, Boss confirmed 2026-09-02**: this does not mean naming the actor at the start of every single sentence in a run — when the same actor (e.g. `คณะที่ปรึกษา`) already opens the topic, repeating the name at the head of every following sentence in that run reads mechanical. Name it once per topic/paragraph-run, then let subsequent sentences in the same run drop or pronoun-reference it.
9. **Banish Direct English Jargon** — Never use direct English operational jargon in audience-facing Thai prose when a functional Thai equivalent exists.
10. **Simplified Technical Prose** — Remove prestige descriptors like `ขั้นสูง`, `ที่สำคัญที่สุด`, or similar verbal inflation unless the distinction is materially necessary.
11. **Elaborate, Don't Drop, Clarifying Nouns** — Thai prose keeps the noun that explains another noun rather than compressing it out. A bare abstract noun left unexplained (e.g. `แสดงเงื่อนไข...` with no statement of which conditions) reads as vague, not concise. Boss, 2026-08-31: "Thai language loves to be repetitive, dropping nouns that elaborate other nouns is bad style."

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
| "เชิงประจักษ์" (when stating test results) | "ชี้ให้เห็นว่า" / "สังเกตการณ์" / "ตามข้อมูลจริง" | Empty pseudo-academic filler. When stating findings ('ผลการทดสอบชี้ให้เห็นว่า'), 'เชิงประจักษ์' adds zero value. |
| "อย่างสิ้นเชิง" | "แตกต่างกัน" / (cut dramatic exaggeration) | Avoids theatrical melodrama and dramatic exaggeration in technical reports. |
| "ฐานราคากลาง" | "ฐานข้อมูลราคากลางสำหรับการซ่อมแซมและสร้างทดแทน" | Inaccurate shorthand. Use full official title (Standardized Replacement Cost Catalogs). |
| "งานประจำวัน" (in disaster management) | "การปฏิบัติงานในพื้นที่" / "การเผชิญเหตุ" | Disaster response is not routine daily work ('งานประจำวัน'); collocation error in disaster management. |
| "แกน" (when referring to subsystem/module) | "องค์ประกอบ" / "ส่วนประกอบ" / "ข้อมูลหลัก" | "แกน" is awkward and rarely used for modular framework components. |
| "ระดับภาค" / "ระดับสาขา" (when the referent is a category, not a geographic level) | "รายภาค" / "รายสาขา" | "ระดับ" wrongly implies a hierarchical/geographic level; "ราย-" is the correct Thai collocation for "per-category". Does not apply to genuine geographic levels (ระดับจังหวัด, ระดับภูมิภาค). Boss, 2026-09-02. |
| "การนำทาง" | "เส้นทางการใช้งาน" | Literal UX/software-spec jargon (navigation); Thai institutional prose names the user's path instead. Boss, 2026-09-02. |
| "โครงสร้างสารสนเทศของเว็บไซต์" (when meaning the sitemap artifact) | "ผังเว็บไซต์" | Abstracted paraphrase drifted from the project's established plain term for this artifact. Boss, 2026-09-02. |
| "ประตูทางเข้า" | "จุดเริ่มต้นของเส้นทางการใช้งาน" | Extension of the existing "ประตูหลัก" rule (front-door/gateway metaphor) to the role-based-entry-point sense. Does not apply to real engineering structures like "ประตูระบายน้ำ" (floodgate), which is a literal technical term, not a metaphor. Boss, 2026-09-02. |

### Technical Terminology Mapping
* **Climate Change** -> การเปลี่ยนแปลงสภาพภูมิอากาศ (Climate Change)
* **Non-Economic Loss and Damage** -> ความสูญเสียและความเสียหายที่ไม่ใช่เชิงเศรษฐกิจ (Non-Economic Loss and Damage: NELD)
* **Data Catalog** -> บัญชีรายการข้อมูล (Data Catalog)
* **Metadata Standard** -> มาตรฐานข้อมูลอภิพันธ์ (Metadata Standard)
* **Risk Methodology Catalog** -> บัญชีระเบียบวิธีความเสี่ยง (Risk Methodology Catalog)
* **Service Portfolio** -> ชุดบริการข้อมูลสารสนเทศ (Service Portfolio)
* **Workflow** -> ขั้นตอนปฏิบัติ (Workflow)
* **Interoperability** -> การทำงานร่วมกันของระบบข้อมูล (Interoperability)
* **Uncertainty Communication** -> การสื่อสารความไม่แน่นอน (Uncertainty Communication)
* **Most Significant Change (MSC)** -> เรื่องเล่าความเปลี่ยนแปลงที่สำคัญที่สุด (Most Significant Change)
* **Logical Data Model** -> แบบจำลองข้อมูลเชิงตรรกะ
* **Conceptual Data Model** -> แบบจำลองข้อมูลเชิงแนวคิด
* **Loss and Damage Field Reporting Form** -> แบบฟอร์มการรายงานความสูญเสียและความเสียหาย
* **Data Field** -> เขตข้อมูล (Data Field)
* **Standardized Replacement Cost Catalogs** -> ฐานข้อมูลราคากลางสำหรับการซ่อมแซมและสร้างทดแทน

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
- **Direct Forward Syntax Over Inverted Conditionals**:
  - Avoid: "คณะที่ปรึกษาขอเน้นย้ำว่า โครงสร้าง... จะยังไม่สร้างคุณค่าในการใช้งานจริงจนกว่าจะถูกนำไปพัฒนาเป็น..." (Inverted, negative conditional, preachy tone)
  - Prefer: "โครงสร้างฐานข้อมูลเชิงสัมพันธ์ของ (ร่าง) MVD ทั้ง 6 ตารางจะต้องถูกนำไปพัฒนาเป็นส่วนหนึ่งของโครงสร้างข้อมูลบนแพลตฟอร์ม..." (Direct, positive action)
- **Domain Subject Anchoring in Titles**:
  - Never drop core domain nouns in H1/H2 titles for brevity (e.g. `# 3.1 มาตรฐานสากลสำหรับการประเมินความสูญเสียและความเสียหายจากสาธารณภัยและปัญหาของระบบรายงานสาธารณภัยของประเทศไทย` not bare `# 3.1 มาตรฐานสากลและปัญหา...`).
- **Strict Acronym First-Occurrence Protocol**:
  - Every institutional acronym on first mention must carry: Full English Name + Acronym + Thai Functional Definition: `กรอบการประเมินความต้องการหลังเกิดภัยพิบัติ (Post-Disaster Needs Assessment: PDNA) สำหรับการประเมินความเสียหายและความต้องการในการฟื้นฟู`.
- **Ban Colons (:) in Thai Headings**:
  - Keep headings integrated without Western colon punctuation (`### การทบทวนมาตรฐานสากล` not `### การทบทวนมาตรฐานสากล: การประสาน...`).

## 7. Anti-AI Shield (Counter-examples)
- **CRITICAL DON'T**: Start with "อย่างไรก็ตาม..." or "แม้ว่า..." unless the contrast is doing real analytical work.
- **CRITICAL DON'T**: Use "ระบบ" without identifying *which* system.
- **CRITICAL DON'T**: Use hyperbolic pseudo-formal intensifiers like "อย่างชัดเจน", "อย่างแท้จริง", or "อย่างยิ่งยวด". Boss directive (2026-08-30 §4.2): this hyperbolic overclaim language must be eliminated altogether in favor of direct empirical evidence or neutral institutional quality requirements.
- **CRITICAL DON'T**: Construct sentences with 'ไม่ใช่ [X] แต่ [Y]' or contrastive negative scaffolding. Boss confirmed 2026-08-30 (§4.2): affirmative-first institutional presentation is strictly required; do not explain by contrasting against what a service is not.
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
- **DON'T**: Use inverted negative conditional sentences (`"จะยังไม่...จนกว่า..."`) which sound preachy and awkward in Thai. Use direct forward active phrasing.
- **DON'T**: Assert empty semantic separations (`"แยกบทบาทระหว่าง X กับ Y"`) when X and Y are already inherently distinct concepts. Anchor the distinction to architectural components (`"ออกแบบองค์ประกอบที่แยกบทบาทชัดเจน"`).
- **DON'T**: Mechanically append repetitive case study names (e.g. `"...ช่วยปิดช่องว่างที่พบในกรณี จ.พิจิตร"`) to universal recommendation lists. Let recommendations stand self-contained.
- **DON'T**: Misdiagnose data processing proxy misuse as a semantic classification problem. Distinguish operational reality from vocabulary definitions.
- **DON'T**: Overclaim national governance scope (`"โครงสร้างข้อมูลของประเทศ"`); strictly anchor deliverables to the commissioning entity (`"แพลตฟอร์มข้อมูลของกรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม"`).
- **DON'T**: Close a diagnostic sentence with a blunt absolute-negative conclusion (e.g. `"...จึงไม่มีระดับความละเอียดใดที่ให้บริการได้อย่างน่าเชื่อถือ"`, a dimension titled `"วิธีคำนวณที่ยังไม่มีอยู่จริง"`). Boss confirmed 2026-08-30 this is a tone correction, not a content one — cut the clause or reframe as a neutral institutional category (`"ระเบียบวิธีการในการวิเคราะห์ข้อมูล"`) only when the underlying claim itself is still accurate.
- **DO** (unconfirmed, filed by analogy to the rule above — flag if wrong): Hedge a claim the evidence doesn't fully support — add `เป็นส่วนใหญ่` or `มัก` rather than stating it as absolute, when the underlying data only shows a majority/typical pattern rather than a universal one.
- **CRITICAL DON'T**: Use metaphor in technical/institutional writing (e.g. `ห่วงโซ่คอขวด` "bottleneck chain" for interlocking gaps). Boss, CRDB full-report spine review 2026-08-31: "ban metaphor in technical writing" — state the mechanism plainly instead of reaching for an image.
- **DON'T**: Add a bare adjective or quantifier that contributes no information the reader needs (e.g. `บริการสารสนเทศจำนวนจำกัดชุดหนึ่ง` — `จำนวนจำกัด` "a limited number of" adds nothing; cut to `บริการสารสนเทศชุดหนึ่ง`). Be conservative about reflexively translating an English adjective into a `เชิง-` prefix; check whether the adjective is carrying real information first.
- **DO**: Use a helping/auxiliary verb (e.g. `ช่วย`) when describing an instrument that enables an outcome rather than causes it outright (e.g. `แบบฟอร์มรายงาน**ช่วย**ปิดช่องว่างนั้น`, not the bare `แบบฟอร์มรายงานปิดช่องว่างนั้น`). Boss, 2026-08-31: "Thai report loves helping verb, adding ช่วย is a preferred option."

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

## 9. Incremental Capture Log (archived)

Archived 2026-08-29 as part of the writing-th v6.0 overhaul — this section was
35,812 bytes, 62.9% of this file, and never needed to be in a drafting or
review model's context. Full history, unchanged:
`ψ/archive/style/capture_history/STYLE_PACK_TH_incremental-capture-log.md`.

The rules it produced are already folded into §1–§8 above and into
`LEXICON_TH.json`. The stray duplicate `## 5.` heading that used to sit at the
end of this section ("Strict Parenthetical Anchor") is demoted to a
subsection in the archived copy so it can no longer collide with the real
`## 5. Lexicon & Diction` above — that rule's enforcement already lives in
`LEXICON_TH.json` (the `Data Availability` / `Temporal completeness` /
`Bounded Application Test` literal entries), so nothing here changes what the
linter blocks.

