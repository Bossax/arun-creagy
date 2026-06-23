# Style-Pack: TOR5.5-Articles
**Samples Learnt**: 4 | **Last Updated**: 2026-06-23

---

## 1. Ranked Style Rules

1. **Sensory & Conversational Openings**: Avoid formal academic introductions. Open with a relatable real-life experience, sensory detail (e.g., feeling unexpected heat on the skin in the morning), or a familiar daily-life analogy (e.g., managing a tight personal budget).
2. **Paragraph & Structural Brevity**: Keep paragraphs short (1–3 sentences). Use clean headers with formatting like `## _อากาศร้อนขึ้นมากแค่ไหนแล้ว_` or `## แล้วจะทำอย่างไรกันดี?`.
3. **Strategic Blockquotes (`> `)**: Use callout blockquotes to isolate punchy, non-obvious conclusions, warnings, or transition hooks (e.g., `> ปรากฎว่านี่เพิ่งเป็นเวลา 7 โมงเช้า แต่ร่างกายรู้สึกเหมือนเวลา 9 โมง`).
4. **Interactive Image Captions**: Precede all diagrams, charts, or maps with the label `Press enter or click to view image in full size`, followed by the image and a clear credit source (e.g., `Cr. Climate reanalyzer`).
5. **Inline Highlights (`==text==`)**: Highlight key numbers, policy values, or critical warnings using markdown highlighter double equals to make the text highly scannable.
6. **Parenthetical Scientific Anchors**: Introduce English scientific concepts and abbreviations in parentheses immediately following their Thai translation (e.g., `ดัชนีความร้อน (Heat Index)`, `ความสามารถในการปรับตัว (Adaptive Capacity)`).

---

## 2. Lexicon & Diction

| Banned/Common AI Transitions | Preferred Alternatives | Reason |
| :--- | :--- | :--- |
| **นอกจากนี้** | *Minimize or replace with direct continuation* | Sounds robotic and standardizes text flow. |
| **ยิ่งไปกว่านั้น** | *Omit* | Artificial transition word. |
| **มุ่งเน้น** | **เน้น**, **ให้ความสำคัญ** | Overused AI filler word. |
| **นับได้ว่า** | **ถือว่า**, **จัดเป็น** | Formal AI filler. |
| **ในยุคปัจจุบัน** | *Begin directly with the hook* | Generic introductory phrase. |

### Technical Terminology Mapping
* **Climate Change** -> การเปลี่ยนแปลงสภาพภูมิอากาศ (Climate Change)
* **Non-Economic Loss and Damage** -> ความสูญเสียและความเสียหายที่ไม่ใช่เชิงเศรษฐกิจ (Non-Economic Loss and Damage: NELD)
* **Sea Surface Temperature (SST)** -> อุณหภูมิผิวน้ำทะเล (Sea Surface Temperature)
* **Marine Protected Areas (MPAs)** -> พื้นที่คุ้มครองทางทะเล (Marine Protected Areas)
* **Urban Heat Island** -> เกาะความร้อนเมือง (urban heat island)
* **Labor Productivity** -> ผลิตภาพแรงงาน (labor productivity)
* **Crop Failure** -> พืชผลการเกษตรเสียหาย (crop failure)
* **Heat Stress** -> ความเครียดจากความร้อน (heat stress)
* **Most Significant Change (MSC)** -> เรื่องเล่าความเปลี่ยนแปลงที่สำคัญที่สุด (Most Significant Change: MSC)

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
- Structure: Start with a sensory or real-world hook. Use short paragraphs (1-3 sentences). Add blockquotes (>) for punchy realizations.
- Vocabulary: Do NOT use filler words like "นอกจากนี้", "ยิ่งไปกว่านั้น", or "มุ่งเน้น".
- Terms: Translate scientific terms into plain Thai, but append the English term in parentheses, e.g., "ความเครียดจากความร้อน (heat stress)".
- Highlighting: Use ==double equals== to highlight key policy numbers or critical thresholds.
- Figures: Label images with "Press enter or click to view image in full size" followed by the markdown image and credit.
```
