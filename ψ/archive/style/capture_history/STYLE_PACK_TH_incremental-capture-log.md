# STYLE_PACK_TH — Archived Incremental Capture Log

Archived 2026-08-29 as part of the writing-th v6.0 overhaul (see
`ψ/inbox/2026-08-29_writing-th-v6-build-blueprint.md` §4). This was
§9 "Incremental Capture Log" of `ψ/memory/style/STYLE_PACK_TH.md` —
35,812 bytes, 62.9% of the file, an unbounded append-only history dating
to 2026-06-25. It never needed to enter a drafting or review model's
context; the operative rules it produced are already folded into the
active pack's §1–§8 and into `LEXICON_TH.json`. Nothing is deleted —
this is the full history, moved so it stops being loaded every time.

**Fix applied on archiving**: the original file had a stray duplicate
`## 5.` heading ("Strict Parenthetical Anchor") appended as a late capture
entry, colliding with the real `## 5. Lexicon & Diction` in the active
pack. It is demoted to a subsection heading below so it can never collide
again — capture-log entries get their own heading level from now on.

---

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

### Strict Parenthetical Anchor (Anti-regression Update)

*Originally appended to the active pack as a stray duplicate `## 5.` heading;
demoted here to a subsection so no future capture entry can collide with the
real `## 5. Lexicon & Diction` again.*

- **Rule**: Do **not** use English translations in parentheses unless absolutely necessary for technical precision.
- **Allowed**: Exact database schema names (`DISASTER_EVENT`), system keys, or official acronyms (`MVD`).
- **Banned**: Translating conceptual terms or phrases (e.g., `(Data Availability)`, `(Temporal completeness)`, `(Bounded Application Test)`). If it's a concept, write it in strong Thai and leave it alone.

### 2026-08-29 — Style-pack upgrade from CRDB Exec-Summary Section 1.1 Complete 14-Point Audit & Structural Capture

**Source of delta**: `ψ/memory/style/evidence/2026-08-29_17-00_TH_exec-summary-1.1_diff-evidence.md` — Smart Diff Resolver comparison between pre-revision baseline and Boss's in-place edited/annotated version in `ψ/incubate/drafts/crdb-exec-summary-1.1/02_th_draft.md` (Commit `31a244c`).

#### Multi-Layer Shifts Captured
- **L1/L2 Syntactic (Anti-AI Negation Scaffolding)**:
  - Struck through `ไม่ใช่เพื่อคัดลอก...` and WMO negation (`%%stop using this structure! explaining what something is not something%%`).
  - Enforced direct positive assertion of functions before stating limitations.
- **L3 Micro-Structure & Diction**:
  - Removed artificial quotes around problem concepts.
  - Eliminated high-level unspecific abstraction fluff (`%%as I said. you always fluff with high-level unspecific abstraction%%`).
- **L4 Logical Argumentation**:
  - `STR-002` (Parallel Framework Enumeration): Formatted 4 international standards as a numbered list with formal citations + 4-step shared cycle.
  - `STR-003` (Finding-to-Design Bridge & So-What Answer): Every UX/cognitive finding must explicitly dictate NCAIF design; deleted generic light logic (`%%what the fuck does that mean? deleted. the logic of this finding is light and very generic. the reader will say so what?%%`).
- **L5 Document Architecture**:
  - `STR-001` (4-Question High-Altitude Table): Intro maps 4 core questions to project deliverables in a structured 2-column table.
  - `STR-004` (4-Layer System Architecture): Explicit mapping of Web Platform (front) -> IA (nav) -> Data Landscape (assets) -> Data Platform & Governance (engine) + 6-step Modern Data Architecture context.

### 2026-08-29 — Style-pack upgrade from CRDB Exec-Summary Chapter 3 (Sections 3.1–3.4) Human Author Teach-In

**Source of delta**: `chapter_3_human_edits_learning.md` and in-place diff analysis of `ψ/incubate/drafts/crdb-exec-summary-3.*/02_th_draft.md` under direct line-by-line critique by Boss.

#### Multi-Layer Shifts Captured & Promoted
- **L1/L2 Lexical & Surface Regex**:
  - **Banned**: `เชิงประจักษ์` (empty filler when used with findings), `อย่างสิ้นเชิง` (dramatic exaggeration), `ฐานราคากลาง` (inaccurate shorthand -> `ฐานข้อมูลราคากลางสำหรับการซ่อมแซมและสร้างทดแทน`), `งานประจำวัน` (collocation error in disaster context), `แกน` (when referring to modular framework components -> `องค์ประกอบ`).
  - **Regex Gate**: Strict ban on colon (`:`) in Thai headings/subheadings (`^#{2,4}\s+[^:\n]+:[^\n]+`).
- **L3 Micro-Structure & Anti-AI Shield**:
  - **Direct Forward Syntax**: Strict ban on inverted negative conditionals (`"จะยังไม่...จนกว่า..."`) which sound preachy and unnatural in Thai. Replaced with direct positive requirements (`"โครงสร้างข้อมูล X จะต้องถูกนำไปพัฒนาเป็น..."`).
  - **Eliminating Tautological Self-Doubt**: Ban empty assertions of semantic separation (`"แยกบทบาทระหว่าง X กับ Y"`) when X and Y are already distinct words; anchor distinctions to architectural design components (`"ออกแบบองค์ประกอบที่แยกบทบาทชัดเจน"`).
  - **Purging Repetitive Trailing Case Tags**: Recommendations in Section 3.4 must stand self-contained without mechanically attaching case study names to every bullet.
- **L4/L5 Structural & Document Architecture**:
  - `STR-006` (Domain Subject Anchoring in Titles): Strictly prohibit aggressive noun-dropping in H1/H2 headings. Keep full subject domain (`สำหรับการประเมินความสูญเสียและความเสียหายจากสาธารณภัย`).
  - `STR-007` (Direct Forward Syntax): Structural enforcement of direct active statements over negative conditional syntax.
  - `STR-008` (Educational Inset Boxes): Insertion of targeted blockquote callout definitions (`> เขตข้อมูล (Data Field) คือ...`) for executive clarity.
  - **Acronym Protocol**: Enforce Full English + Acronym + Thai Functional Definition on first occurrence.
  - **Root Cause Accuracy**: Disentangle data processing proxy misuse (relief budget misused as damage proxy) from semantic classification errors.

### 2026-08-29 — Style-pack upgrade from CRDB Exec-Summary Section 2.2 Refinement

**Source of delta**: `ψ/incubate/drafts/crdb-exec-summary-2.2/draft.md` under direct critique by Boss.

#### Multi-Layer Shifts Captured
- **L4/L5 Structural & Rhetorical**:
  - **Elimination of Artificial Causal Linkage**: Strictly avoid inventing artificial causal links that claim general/demand-side data needs "determine" or "create" specific use cases (e.g. banning `ที่มีผลต่อการกำหนดกรณีการใช้งาน`). Keep demand-side interview findings (systemic data needs/readiness) clearly distinct from workshop use-case generation, combining them only at the final synthesis stage.
- **L3 Micro-Structure & Parallelism**:
  - **Nominal Parallelism in Multi-Item Lists**: Headings in bulleted requirement lists must maintain strict parallel structure using substantive nominal phrases denoting systemic attributes (`การมีข้อมูลอ้างอิงกลาง...`, `ความละเอียดเชิงพื้นที่...`, `รูปแบบข้อมูลที่เข้าถึง...`, `ความพร้อมในการนำไปใช้...`) rather than mixing clauses and nouns.
  - **Decision-Ready Concrete Diction**: Ground abstract concepts like "decision-ready" with concrete operational dimensions (`ตัวเลข ภาษา หน่วยวัด และตัวแปร`) to prevent them from devolving into generic IT boilerplate.

### 2026-08-29 — Style-pack upgrade from CRDB Exec-Summary Section 2.3 Refinement & A-BTR Strategic Integration

**Source of delta**: `ψ/incubate/drafts/crdb-exec-summary-2.3/draft.md` under direct refactoring and critique by Boss.

#### Multi-Layer Shifts Captured
- **L4/L5 Structural & Strategic Rhetoric**:
  - **Strategic Driver Framing over Passive Exclusion**: Transform cross-cutting mandates (such as A-BTR under UNFCCC) and complex technical items from administrative exclusions or deferred items (`ถูกเลื่อนออก`, `ไม่ใช่บริการลำดับที่ 9`) into proactive strategic drivers that determine platform integration scope across data domains and adaptation stages.
  - **Streamlined Executive Architecture**: Eliminate redundant separate status summaries by embedding the development roadmap directly into the concluding strategic driver narrative.
- **L4 Argumentation & Multi-Stakeholder Grounding**:
  - Ground interdisciplinary requirements in named actor trinities (`ระหว่างนักวิทยาศาสตร์ วิศวกรและสถาปนิก และผู้ออกนโยบาย`) instead of vague "expert collaboration".
- **L1/L2 Lexical & Diction**:
  - Ban passive administrative deferral syntax (`ถูกเลื่อนออกด้วยข้อจำกัด`) in favor of positive-conditional developmental framing (`มีความสำคัญสูง แต่ยังต้องพัฒนาองค์ความรู้...`).

### 2026-08-30 — Style-pack upgrade from CRDB Exec-Summary Section 4.2 Human Edit

**Source of delta**: `ψ/incubate/drafts/crdb-exec-summary-4.2/section-4.2-draft.md` under direct line-by-line edit and critique by Boss.

#### Multi-Layer Shifts Captured & Promoted
- **L1/L2 Lexical & Surface Regex**:
  - **Banned**: `ถือครองภารกิจ` (unnatural English calque -> `มีภารกิจในการ`), `ขัดขวาง` (colloquial/confrontational -> `เป็นอุปสรรคต่อ`), `ความทันเวลา` (when describing dataset baseline quality -> `ความทันสมัย`).
  - **Hyperbolic Intensifier Regex Ban**: Complete ban on pseudo-formal intensifiers (`อย่างชัดเจน`, `อย่างแท้จริง`, `อย่างยิ่งยวด`) via regex `(อย่างชัดเจน|อย่างแท้จริง|อย่างยิ่งยวด)` per explicit Boss directive. Replace with direct empirical evidence or neutral quality framing.
- **L3 Micro-Structure & Anti-AI Shield**:
  - **Zero-Tolerance for Negation-First Contrast Scaffolding**: Absolute ban on `ไม่ใช่ [X] แต่ [Y]` or explaining services by contrasting against what they are not (`ไม่ใช่บริการที่เกิดจากความต้องการของหน่วยงานภายนอก...`). Affirmative-first institutional presentation is non-negotiable.
  - **Pruning Bureaucratic Scaffolding**: Cut bureaucratic explanations that do not contribute to the core strategic significance of the mandate.
- **L4/L5 Structural & Document Architecture**:
  - `STR-009` (Executive Summary Strategic Driver Prose): Replace isolated multi-stage taxonomy bullet lists with cohesive strategic driver prose linking mandates to platform data architecture and short-term development strategy.

### 2026-08-30 — Style-pack upgrade from CRDB Exec-Summary Section 4.3 Human Edit

**Source of delta**: `ψ/incubate/drafts/crdb-exec-summary-4.3/section-4.3-draft.md`, working-copy diff, direct line-by-line edit and critique by Boss.

#### Multi-Layer Shifts Captured & Promoted (all confirmed via rationale gate, LEXICON_TH.json v4.2)
- **L1/L2 Lexical & Surface Regex**:
  - **Banned**: `ผลงาน` as the noun for a project's deliverables (-> `ผลผลิต`); `ฉบับ` as a counting classifier for deliverable/document items (-> `รายการ`); `ผู้จัดทำ` as a content-writer role noun (-> `ผู้เขียน`).
  - **หมวดหลัก -> หัวข้อหลัก (supersedes prior rule)**: The 2026-06-xx `โหนด -> หมวด` sitemap rule is now superseded for the grouping-label sense — `หัวข้อ` is canonical for the sitemap's main-grouping term as of 2026-08-30. 11 stale `หมวดหลัก` usages remain across §1.4 and two WP11/§4.2 draft/archive files, flagged to Boss, not auto-fixed.
  - **Internal Artifact Metadata Ban, broadened**: Boss's correction — "the rule bans leaking internal code, logic, artifact names" — extends the existing internal-artifact-locator rule (previously scoped to slide/page locators only) to internal deliverable version tags and abbreviation codenames (`DRD v2` -> `DRD`, `Node Content Storyboard...v2` -> `Content Storyboard...`, `CDM/DMF` -> dropped). New regex entry added rather than editing the narrower existing one, same underlying principle.
  - **Mechanical grammar rule** (bypassed 2x threshold on first sighting, tagged `mechanical`): nominalize the verb after `รับผิดชอบ` — `รับผิดชอบยกร่าง...` -> `รับผิดชอบการยกร่าง...`.
- **Corrective note for next capture round (structural, still below 2x threshold — logged, not yet promoted)**:
  - **Don't restate self-evident premises as filler**: Boss's correction on the roles paragraph rewrite ("your original prose is unclear... roles are needed to be clear without stating out loud. it is common sense. you['re] just restating common sense") was *not* a generic passive->positive reframe as first hypothesized — it specifically targets declaring an obvious requirement (e.g. "clear role division is needed") before stating the substantive point. Narrower than the pack's existing Passive/Defeatist Syntax Elimination category; watch for a second occurrence before promoting as its own rule.
  - Project-title-clause pruning (full official project name -> `โครงการนี้` once established) and inline-enumeration-to-line-broken-list reformatting were both confirmed generalizable by Boss but await a second sighting per the 2x structural-pattern threshold.
- **Content-fidelity issue surfaced, not a style rule**: a coverage-percentage claim (35%->70%, 40%->80%) was cut entirely — Boss's annotation identified it as based on an unscoped future-project TOR he explicitly said not to assume knowledge of. Logged as `content_correction` in the miss register for audit, not a lexical/structural pattern.


### 2026-08-31 — CRDB Full-Report Spine Review (Boss's inline review of 00-โครงเรื่องฯ.md)

**Source of delta**: `ψ/incubate/DCCE/CRDB/output/final_deliverable/Full report/00-โครงเรื่องและแผนการเขียนรายงานฉบับสมบูรณ์.md`, Obsidian `%%...%%` inline review comments plus direct edits, resolved and cleaned in-session. No clean draft/edit file pair existed for a computed `diff_word_table.py` pass — comments were already resolved into the file before capture ran, so this round is captured from the assistant's own structured transcript of Boss's stated corrections and rationale, not a mechanical diff. Rationale for every item below is Boss's own stated words, not inferred — treated as already satisfying the Stage 4c rationale gate without a redundant re-ask.

#### Multi-Layer Shifts Captured & Promoted (LEXICON_TH.json v4.5, all `confirmed_generalizable`)

- **L1/L2 Lexical**:
  - `ความล้มเหลว` -> `อุปสรรค` (scope: universal). "never use ความล้มเหลว too negative and personal in technical report."
  - `ชิ้นงาน` -> `ผลผลิต` (scope: report). Verified against `Final-report-redirect-plan.md`'s own phrase "Software Artifacts (ผลผลิตจากโครงการนี้)" — not asserted on Boss's word alone.
  - `ห่วงโซ่` and `คอขวด` -> `อุปสรรค` (scope: report, both entries). "ban both and the metaphor" — bans the bare words and the ห่วงโซ่คอขวด construction. **Exception carried in the lexicon reason field**: does not block citing the established artifact title ห่วงโซ่คุณค่าข้อมูล / `DCCE Data Value Chain.md` verbatim as a document name — that is citation, not authored metaphor. Complements a pre-existing report-scoped entry mapping a คอขวด-phrase to an อุปสรรค-phrase (same direction, not a conflict — checked via `check_lexicon_conflict.py`).
- **L1 Structural (STYLE_PACK_TH.md, Core Kernel #11 + Anti-AI Shield)**:
  - **Elaborate, don't drop, clarifying nouns**: "Thai language loves to be repetitive, dropping nouns that elaborate other nouns is bad style." Instance: `...แสดงเงื่อนไข...` left เงื่อนไข unexplained — flagged "what is condition? did you drop something to elaborate on this noun?"
  - **Ban metaphor in technical writing**: standalone generalization beyond the ห่วงโซ่/คอขวด lexicon ban — no metaphor at all in Thai technical/institutional report prose.
  - **Bare/hyperbolic adjectives; conservative on เชิง-prefix reflex**: instance `บริการสารสนเทศจำนวนจำกัดชุดหนึ่ง` -> จำนวนจำกัด contributed nothing, told to cut it entirely.
  - **Prefer helping/auxiliary verbs** (e.g. ช่วย) when an instrument enables rather than causes an outcome. Boss's own edit: `...แบบฟอร์มรายงานปิดช่องว่างนั้น` -> `...แบบฟอร์มรายงาน**ช่วย**ปิดช่องว่างนั้น`, rationale "Thai report loves helping verb, adding ช่วย is a preferred option."

**Consistency note**: this project's own `01-ข้อกำหนดรูปแบบการเขียนรายงานฉบับสมบูรณ์.md` §6 independently bans `ได้จริง`, `อย่างต่อเนื่อง`, `เชิง...` outright — the เชิง item above generalizes that existing report-local instinct into the cross-project pack rather than duplicating it.

**Not captured this round**: §§11–13 of the same project's `01-...md` (universal acronym-full-name mandate; Thai-naming for the 7 adaptation categories/6 NAP sectors; PDPA redaction in appendices) were deleted by Boss without an inline rationale comment. Checked: the acronym mandate substantially duplicates an existing rule already in this pack (§6 Structural DNA, "Strict Acronym First-Occurrence Protocol") — likely why it was cut as redundant. The sector-naming and PDPA items are content-compliance requirements tied to specific committee-sheet page references, not general style patterns, and Boss's own framing ("the plan should be taken as preliminary, writing sessions will need to work on outline details later") suggests these are deliberately left for the relevant chapter sessions to pull from the primary source (`ความเห็นต่อเล่มร่างรายงานฉบับสมบูรณ์ (Draft Final Report).md`) directly rather than pre-captured here. Not promoted to this pack; flagged so a future session doesn't assume the omission was accidental.
