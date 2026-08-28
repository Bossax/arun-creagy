---
id: learning_2026-08-28_scope-subagent-tools-explicitly-not-just-in-prose
type: learning
title: "Scope subagent tools explicitly, not just in prose — general-purpose subagents d"
concepts: [subagent-scoping, tool-restriction, reporting, citations, citation-hygiene, multi-agent-synthesis]
tags: [subagent-scoping, tool-restriction, reporting, citations, citation-hygiene, multi-agent-synthesis]
created: 2026-08-28
indexed_at: 2026-08-28T18:49:45.084Z
updated_at: 2026-08-28T18:49:45.084Z
hash: sha256:9061e54f516f410295ac79f8e8d1d26ce55885a6813a059a33421d43b4966a25
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-28_scope-subagent-tools-explicitly-not-just-in-prose
arra_type: learning
arra_concepts: [subagent-scoping, tool-restriction, reporting, citations, citation-hygiene, multi-agent-synthesis]
arra_created: 2026-08-28T18:49:45.084Z
---

# Scope subagent tools explicitly, not just in prose — general-purpose subagents d

Scope subagent tools explicitly, not just in prose — general-purpose subagents default to full tool access and will use WebFetch/WebSearch even when a task says "project files only." One subagent independently web-verified citations when the plan explicitly deferred web search to a later step, and this wasn't caught until reviewing its report after the fact.

Separately: a closing summary after multi-agent work must inventory every finding evenly, not lead with whichever result matches the user's original framing. A "priority actions" list buried genuinely strong findings from other parts of a completed audit, and the user read the omission as the audit having missed them — "severe flaw in the plan" — when the real defect was presentation, not coverage.

Also: this project's citation-hygiene standard treats an undated ("n.d.") citation as equivalent to no citation. Ten undated citations were inserted into report drafts and had to be stripped back out after the fact — undated sources should be gap-logged from the start rather than inserted speculatively.

---
*Added via Oracle Learn*
