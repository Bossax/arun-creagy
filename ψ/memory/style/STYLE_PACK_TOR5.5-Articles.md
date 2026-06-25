# Style-Pack: TOR5.5-Articles
**Samples Learnt**: 5 | **Last Updated**: 2026-06-23

---

## 1. Ranked Style Rules

1. **Sensory & Conversational Openings**: Avoid formal academic introductions. Open with a relatable real-life experience, sensory detail (e.g., feeling unexpected heat on the skin in the morning), or a familiar daily-life analogy (e.g., managing a tight personal budget).
2. **Paragraph-Based Flow**: The writing must be heavily paragraph-based. Avoid creating too many subsections, subheadings, or bulleted/numbered lists. Keep the narrative flowing naturally from one paragraph to the next.
3. **No Decorative Elements**: 
   - **DO NOT** use emojis.
   - **DO NOT** use mermaid diagrams.
   - **DO NOT** add pictures or images.
4. **Punctuation Constraints**:
   - **DO NOT** use colons (":") anywhere in the text.
   - **DO NOT** use single quotes ("'") or double quotes to stress individual words or phrases. Use natural phrasing or markdown bold/highlight tools if necessary.
5. **Inline Highlights (`==text==`)**: Highlight key numbers, policy values, or critical warnings using markdown highlighter double equals to make the text highly scannable.
6. **Parenthetical Scientific Anchors**: Introduce English scientific concepts and abbreviations in parentheses immediately following their Thai translation (e.g., ดัชนีความร้อน (Heat Index), ความสามารถในการปรับตัว (Adaptive Capacity)). Do not use colons inside the parentheses.

---

## 2. Lexicon & Diction

| Banned/Common AI Transitions | Preferred Alternatives | Reason |
| :--- | :--- | :--- |
| **นอกจากนี้** | *Minimize or replace with direct continuation* | Sounds robotic and standardizes text flow. |
| **ยิ่งไปกว่านั้น** | *Omit* | Artificial transition word. |
| **มุ่งเน้น** | **เน้น**, **ให้ความสำคัญ** | Overused AI filler word. |
| **นับได้ว่า** | **ถือว่า**, **จัดเป็น** | Formal AI filler. |
| **ในยุคปัจจุบัน** | *Begin directly with the hook* | Generic introductory phrase. |
| **ในทางกลับกัน** | *Omit or use natural contrast* | AI transition filler. |
| **ถึงกระนั้น** | *Omit or use natural transition* | AI transition filler. |

### Technical Terminology Mapping (No Colons)
* **Climate Change** -> การเปลี่ยนแปลงสภาพภูมิอากาศ (Climate Change)
* **Non-Economic Loss and Damage** -> ความสูญเสียและความเสียหายที่ไม่ใช่เชิงเศรษฐกิจ (Non-Economic Loss and Damage: NELD)
* **Sea Surface Temperature (SST)** -> อุณหภูมิผิวน้ำทะเล (Sea Surface Temperature)
* **Marine Protected Areas (MPAs)** -> พื้นที่คุ้มครองทางทะเล (Marine Protected Areas)
* **Urban Heat Island** -> เกาะความร้อนเมือง (urban heat island)
* **Labor Productivity** -> ผลิตภาพแรงงาน (labor productivity)
* **Crop Failure** -> พืชผลการเกษตรเสียหาย (crop failure)
* **Heat Stress** -> ความเครียดจากความร้อน (heat stress)
* **Most Significant Change (MSC)** -> เรื่องเล่าความเปลี่ยนแปลงที่สำคัญที่สุด (Most Significant Change)
* **Adaptation Paradox** -> ความย้อนแย้งของการปรับตัว (Adaptation Paradox) *(Do NOT use "ปฏิทรรศนะของการปรับตัว" - it is too academic)*
* **Eco-Economic Cascade** -> ผลกระทบลูกโซ่จากระบบนิเวศสู่เศรษฐกิจ (Eco-Economic Cascade)
* **Economic Trap** -> ข้อจำกัดจากการพัฒนาที่เน้นแต่ผลกำไร *(Do NOT use "กับดักทางเศรษฐกิจ" or "กับดักทางเศรษฐกิ")*
* **Mass Tourism** -> การท่องเที่ยวแบบมวลชน (Mass Tourism)

---

## 3. Anti-AI Shield

* **DON'T**: Structure articles like standard academic summaries starting with "บทความนี้สรุปประเด็น..." or ending with "กล่าวโดยสรุป...".
* **DO**: Structure as a story (Causal Chaining) where a global event (e.g., El Niño) directly impacts a local livelihood (e.g., central plains rice yields), leading to a specific policy choice.
* **DON'T**: Write long, complex sentences with nested clauses.
* **DO**: Write short, active sentences that make a single, clear point.

---

## 4. Master Implementation Prompt

```text
You are an expert science communicator drafting an article for the general public in Thailand about climate risks.
Follow these constraints strictly:
- Tone: Conversational, engaging, human-centric, yet scientifically accurate.
- Structure: Start with a sensory or real-world hook. Heavily paragraph-based, avoiding too many subheadings and subsections.
- Restrictions: Do NOT use emojis, mermaid diagrams, pictures, colons, or single quotes for stress.
- Vocabulary: Do NOT use filler words like "นอกจากนี้", "ยิ่งไปกว่านั้น", or "มุ่งเน้น".
- Terms: Translate scientific terms into plain Thai, but append the English term in parentheses without colons.
- Highlighting: Use ==double equals== to highlight key policy numbers or critical thresholds.
```

---

## 5. Incremental Capture Log

### 2026-06-24 — ART01 human edit delta

**Source of delta**: human edits in [`03_Draft_Article.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/ART01_CMIP6_Water_Crop/03_Draft_Article.md) compared against the prior AI draft via local git diff.

#### Preferred direction detected
- **Broader civilizational framing before technical narrowing**: the human shifted the opening away from an immediate sensory-weather hook toward a larger food-security and rice-civilization frame grounded in Thai identity and regional importance.
- **Explicit rhetorical questioning is acceptable when opening a strategic article**: the edit strengthens the use of large framing questions about food security, resilience, and adaptation rather than only scene-setting.
- **Demand for denser substantive scaffolding**: the human inserted placeholders asking for more detail on `BAU irrigated rice yields`, `BAU rain-fed rice yields`, model inputs, and mixed-cropping logic, signaling that thin elegance is less preferred than well-supported explanatory density.
- **Thai-first strategic framing can precede model explanation**: the edit privileges context, stakes, and national meaning before method.

#### New style rule candidates
7. **Strategic Stakes Openings Are Allowed**: A draft may open with a broad Thai food-security, livelihood, or civilizational frame when the article topic is foundational to national resilience, provided it still flows into concrete evidence.
8. **Human Edits May Prefer Detail-Rich Exposition Over Lean Minimalism**: When the human adds placeholders asking for more mechanism, comparisons, or model detail, future drafts should not over-compress explanation.
9. **Preserve the Human’s Chosen Framing Layer**: If a human edit expands the frame from a local climate vignette to a wider historical, agricultural, or societal lens, the final draft should preserve that lens instead of reverting to the earlier AI opening pattern.

#### Anti-regression note
- Do **not** automatically force every article back to the narrow “felt weather moment” opening if the human has deliberately expanded the article into a larger strategic Thai framing.
- Do **not** treat concise prose as the only goal when the human is signaling a need for more explanatory structure and evidence-bearing detail.

### 2026-06-25 — ART08 human edit delta

**Source of delta**: Human inline comments and review in [`03_Draft_Article.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/ART08_Tourism_Risk_GIZ/03_Draft_Article.md).

#### Preferred direction detected
- **Clean Separation of Impacts**: The human explicitly criticized mixing different types of impacts. Natural capital degradation (e.g., coral bleaching) should not be lumped into paragraphs discussing direct threats to human safety and comfort (e.g., heat, floods, landslides).
- **Demand for Granular Detail**: The human rejected vague, hand-wavy impact descriptions ("can be much more detailed"). Evidence must be specific and grounded in the source data.
- **Rejection of Weird Phrasing/Jargon**: The human reacted negatively to incomplete or awkward direct translations like "กับดักทางเศรษฐกิ" (economic trap). The language must be natural, complete, and idiomatic Thai.
- **Urgent Tone for Recommendations**: When presenting policy or adaptation recommendations, the human wants a tone that conveys high urgency rather than passive suggestion.
- **Rejection of Forced Melodrama**: The human completely rewrote the opening to remove a forced, fluffy string of "If" conditions, preferring a direct, authoritative macroeconomic hook (e.g., "Can Thai tourism survive...?").
- **Grammatical Cohesion**: The original draft referred to "this question" without ever asking one. Transitions must logically connect to the preceding sentence.

#### New style rule candidates
10. **Do Not Mix Impact Categories**: Keep a strict narrative boundary between direct human safety threats (floods, extreme heat, landslides) and ecological/natural capital degradation (coral bleaching, water scarcity). Do not blend them in the same paragraph.
11. **Avoid Awkward Translated Jargon**: Do not invent unnatural Thai phrases or portmanteaus (like "กับดักทางเศรษฐกิจ"). Use plain, descriptive Thai language that feels natural to native speakers.
12. **Recommendations Must Convey Urgency**: Frame concluding recommendations and adaptation policies with strong, urgent language that highlights the immediate necessity of action.
13. **Authoritative Openings Override Sensory Hooks**: When an article deals with massive systemic risk (like 15% of GDP), open with the strategic stakes immediately rather than forcing a melodramatic "felt weather moment."
14. **Logical Transition Integrity**: Never use phrases like "คำถามนี้" (This question) or "ปัญหาเหล่านี้" (These problems) unless the preceding text actually asked a question or explicitly listed problems.

#### Anti-regression note
- **DON'T** use vague umbrella statements to cover complex environmental cascades. Be specific about what is happening (e.g., where exactly coral bleaching fits into the eco-economic cascade).
- **DON'T** try to shoehorn a poetic or sensory opening into an article that demands a serious, macroeconomic framing.
