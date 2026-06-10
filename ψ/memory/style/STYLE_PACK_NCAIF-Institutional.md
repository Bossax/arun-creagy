# Style-Pack: NCAIF-Institutional
**Samples Learnt**: 10 (Technical Precision & Simplified Prose) | **Last Updated**: 2026-06-11

## 1. Ranked Style Rules
1. **Precision in Resolution Scales** - ALWAYS specify the exact scale or range when discussing data resolution.
    - Use **"ระดับ 25-100 กิโลเมตร"** instead of "ระดับกิโลเมตร".
    - Use **"ระดับหลักสิบเมตร"** instead of "ระดับเมตร".
2. **Simplified Technical Prose** - Strip "Expert-AI" descriptors like "ขั้นสูง" (advanced) or "ที่สำคัญที่สุด" (most important). Let the fact stand alone.
3. **The Anti-Vagueness Rule (The System Identity)** - NEVER use "ระบบ" (system) without a modifier.
    - **Banned**: "ความมั่นคงของระบบ"
    - **Preferred**: "ความมั่นคงของสถาปัตยกรรมบริการสารสนเทศ" or "เสถียรภาพของระบบสนับสนุนการตัดสินใจ".
4. **Direct Evidence Lead (No Padding)** - NEVER use causal hedging (e.g., "แม้ว่า...", "อย่างไรก็ตาม..."). Jump straight to the facts.
5. **Product over Process** - Describe the *deliverable* (e.g., "ระเบียบวิธีและเครื่องมือคำนวณมาตรฐาน"), not the activity.
6. **Fact-Impact Snapping** - Break long sentences. Every claim should be a standalone evidence-impact pair.

## 2. Lexicon & Diction (Dos/Don'ts)
| Banned/Common | Preferred | Reason |
| :--- | :--- | :--- |
| "ความลักลั่น" | "ความซ้ำซ้อนและความไร้มาตรฐาน" | More descriptive of technical failure. |
| "ท่วมท้น" | [Technical Method] | Use "จากการสังเกตุผ่านดาวเทียม". |
| "ระดับเมตร" | "ระดับหลักสิบเมตร" | More realistic for current operational downscaling. |
| "ขั้นสูง" (Advanced) | [Omit] | Institutional prose avoids hyperbole. |

## 3. Structural DNA
- **Traceable Intro**: Always start with the audit scale (260 datasets).
- **Scale-Specific Impact**: Link technical gaps to concrete resolutions (25km vs 10m).
- **Audit Risk**: Frame technical hurdles as a threat to **"ความชอบธรรมในการใช้งบประมาณ"**.

## 4. Anti-AI Shield (Counter-examples)
- **CRITICAL DON'T**: Start with "อย่างไรก็ตาม..." or "แม้ว่า...". 
- **CRITICAL DON'T**: Use "ระบบ" without identifying *which* system.
- **DON'T**: Use high-precision decimals in summaries; round to nearest 10 or 5.

## 5. Master Implementation Prompt
> **Writing Mode**: NCAIF-Institutional (v3.3 - Precise & Direct)
> **Instructions**: Write in a punchy, authoritative Thai institutional voice. Specify all data resolutions (e.g., "25-100 กม.", "หลักสิบเมตร"). Avoid vague terms like "ระบบ" alone; use "สถาปัตยกรรมบริการสารสนเทศ". Strip all causal padding and "advanced/important" descriptors. Round statistics. Link every technical gap to budget legitimacy and engineering risk.
