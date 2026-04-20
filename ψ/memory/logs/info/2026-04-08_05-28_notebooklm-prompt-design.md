---
date: 2026-04-08T05:28:22Z
type: info
status: raw
significance: important
---

# NotebookLM Prompt Design: Principles of Extraction

NotebookLM is a data extraction machine with minimal context capacity, not an extension of the Oracle's brain. Overly strict, rule-heavy prompts (micromanagement with detailed prohibitions) are counterproductive and waste resources.

### Key Principles:
1. **Extraction over Brain:** Focus on *what* information to extract, not rules and desired behaviors.
2. **Length Limit:** Prompts should generally not exceed what a human can type in a minute (~800 words).
3. **Summarize Prohibitions:** Retain structural framing (JSON, table framing) but summarize rules/prohibitions to save space and focus.
4. **Atomic Breakdown:** If a prompt is too long, break it down or move general instructions to a system prompt/independent instruction.

Logged via /fyi