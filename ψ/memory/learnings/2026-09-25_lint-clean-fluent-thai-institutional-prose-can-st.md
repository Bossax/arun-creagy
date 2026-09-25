---
id: learning_2026-09-25_lint-clean-fluent-thai-institutional-prose-can-st
type: learning
title: "Lint-clean, fluent Thai institutional prose can still misstate facts — content f"
concepts: [content-fidelity, editorial-review, writing-th, crdb, verification, subagent-splitting]
tags: [content-fidelity, editorial-review, writing-th, crdb, verification, subagent-splitting]
created: 2026-09-25
indexed_at: 2026-09-25T15:07:41.294Z
updated_at: 2026-09-25T15:07:41.294Z
hash: sha256:fc2888052c11394b65e4c444e0cc7a913e7982e29e6a2dcfa273f896354dd4fa
source: "rrr: CRDB Arun_Creagy"
arra_id: learning_2026-09-25_lint-clean-fluent-thai-institutional-prose-can-st
arra_type: learning
arra_concepts: [content-fidelity, editorial-review, writing-th, crdb, verification, subagent-splitting]
arra_created: 2026-09-25T15:07:41.294Z
---

# Lint-clean, fluent Thai institutional prose can still misstate facts — content f

Lint-clean, fluent Thai institutional prose can still misstate facts — content fidelity must be checked separately from style. Asked to check CRDB full-report §5.1.5 (8 climate services) against its source narrative, found: a service baseline that directly contradicted the source (claimed an existing early-warning system where the source says none exists), a percentage with no supporting count (61/122 was just 122÷2), per-service reason-code counts that were actually totals across all items misattributed to one service, a model cited under the wrong internal work-package label, and a headline figure attributed to the wrong study with the wrong scope. None of this was catchable by style-pack lint or careful reading — it only surfaced by sending independent read-only agents to re-derive each claim from its named source file. Splitting claims across two agents by type (narrative/framing vs numeric/labeling) surfaced non-overlapping real defects, mirroring the known dual-Stage-5-review pattern (mechanical rubric + cold reader catch different things). Fix: when a fidelity question is asked ("does this match the source"), dispatch fresh read-only verification against named sources with file:line citations required, rather than relying on lint or a careful read. Separately: the writing-th skill's PostToolUse lint hook points at a nonexistent .agents/skills/writing-th/.venv; the working venv is at .claude/skills/writing-th/.venv — run the linter manually with that path until the hook is fixed.

---
*Added via Oracle Learn*
