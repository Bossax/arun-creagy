# Learning: Jargon De-categorization in Institutional Synthesis

**Date**: 2026-06-09 | **Status**: Active | **Tags**: #writing-th #synthesis #prompt-engineering

## 💡 The Pattern
When transitioning from a "Consultant/Contractor" writing style to an "Institutional/Grounded" style, it is not enough to edit the prose. You must **de-categorize** the metaphors.

### 🛑 The Trap (AI-Consultant Logic)
AI agents often latch onto metaphors (like "Institutional Shield" or "Budgeting Wall") as **Structural Categories**. 
*   **Symptom**: You fix the Thai text to be formal, but the AI continues to use `Regulatory_Shield` as a column header or a logical anchor for grouping data.
*   **Result**: "Jargon Leakage." Even if the sentences look good, the underlying structure still feels like a consultant deck.

### ✅ The Fix (Institutional Grounding)
1.  **Rename the Headers**: Change column names from metaphorical to procedural (e.g., `ความชอบธรรมตามกฎข้อบังคับ`).
2.  **Verbs over States**: Replace "Status/Readiness" (filler words) with specific procedural verbs (e.g., "ตรวจสอบความเหมาะสม," "ทวนสอบความถูกต้อง").
3.  **Audit-First Narrative**: Frame every service/use-case as a response to a potential audit gap or regulatory necessity. In Thai bureaucracy, "Legitimacy" (ความชอบธรรม) is the currency of survival.

## 📝 Example
- **BAD**: "Service 08 provides an Institutional Shield for decision-makers."
- **GOOD**: "Service 08 สร้างความชอบธรรมตามกฎข้อบังคับในการตัดสินใจ เพื่อลดความเสี่ยงจากการถูกโต้แย้งในเชิงคุณภาพของหลักฐานเชิงประจักษ์"

## 📍 Implementation
Applied in the `style-capture` skill and the `NCAIF-Institutional` Style-Pack v2.1.
