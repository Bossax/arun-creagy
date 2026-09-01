---
name: lexicon-bans-apply-to-self-authored-prose-too
description: A phrase quoted or lifted from source material into new composed prose is not exempt from lexicon/pattern bans just because it existed in the original — check borrowed phrasing the same way model output gets checked.
metadata:
  type: feedback
---

**Context**: CRDB full-report §3.2 (merging EX 2.2 + DFR 5.3.2). Both source documents used the phrase "ห่วงโซ่ข้อมูล" / "ห่วงโซ่การใช้ข้อมูล" (data chain/value-chain metaphor). This metaphor is banned project-wide as of 2026-08-31 (see spine document review), except when citing the canonical artifact title "ห่วงโซ่คุณค่าข้อมูล" verbatim. When composing a new merged intro paragraph directly (not through qwen), I carried the phrase over from the source text without checking it against the lexicon — treating "it's already in the original" as a pass, when the ban applies to the phrase itself regardless of where it came from. The Stage 4 lint hook caught it before it reached Boss.

**Pattern**: this is the same underlying failure mode as [[2026-09-01_a-lexicon-swapban-rule-handed-to-an-llm-for-mecha]] (lexicon rules fire wherever they pattern-match), but on the authoring side rather than the polishing-model side. A rule doesn't know or care whether the banned phrase came from an LLM's rewrite or from the human-authored source material being carried forward — a ban is a ban on the string/pattern, not on who or what introduced it.

**Mitigation**: when composing new sentences that borrow phrasing from source material — not just when reviewing a polishing model's output — check that phrasing against the current lexicon/pattern rules before writing it down. Don't treat "preserving the original wording" as automatic license; a wording being original doesn't mean it's still compliant with rules adopted after that source was written. The lint gate is a safety net, not a substitute for this check — relying on it to catch self-authored violations works, but means the correction cost lands after the fact rather than being avoided.

**Related**: [[a-lexicon-swapban-rule-handed-to-an-llm-for-mecha]] (same principle, different failure surface)
