# Lesson: Lexicon swap rules fire on proper nouns that share a target word

**Context**: CRDB full-report §3.1 polish pass (pure P, qwen3.6-plus). A swap rule written for one narrow purpose — "ฉบับ" as a counting classifier for deliverable items should become "รายการ" — was pasted into a polishing prompt without checking whether "ฉบับ" also appears inside a fixed document name. It does: "รายงานฉบับกลาง" (the Interim Report). Qwen applied the rule literally and produced "รายงานระหว่างกลาง" in 3 places, an almost-plausible but wrong term, in an otherwise well-behaved polish pass.

**Also observed in the same pass**: a sentence using a "not X, but Y" contrast structure that did NOT contain the specific banned string ("ไม่ใช่เพียง") still got collapsed to just its Y half, dropping a real qualifying clause. The model generalized from "fix this rhetorical pattern" to structurally similar sentences beyond the literal ban list.

**Pattern**: any word- or pattern-level swap/ban rule handed to an LLM for mechanical text polishing will apply wherever it pattern-matches, not just where the rule's author intended. This includes:
1. A banned/target word appearing inside a proper noun, technical term, or fixed document name elsewhere in the source.
2. A banned rhetorical *pattern* being over-generalized to sentences that resemble it but don't contain the literal banned string.

**Mitigation**:
- Before handing a swap/ban list to a polishing model, scan the source for every occurrence of each target word/pattern and check whether any instance is a proper noun or fixed term — carve those out explicitly in the prompt.
- Never trust a lint-clean or rule-compliant output as proof of fidelity — diff every paragraph against the source, paragraph by paragraph, regardless of how strict the prompt was. This is the same conclusion as the §2.2 session's grounds-field-compression lesson, generalized: strict instructions reduce but do not eliminate drift; verification is the actual fidelity control, not the prompt.

**Related**: [[stage1-grounds-must-carry-full-supporting-detail]] (same underlying principle — trust verification, not instruction strictness, applied to a different pipeline stage)
