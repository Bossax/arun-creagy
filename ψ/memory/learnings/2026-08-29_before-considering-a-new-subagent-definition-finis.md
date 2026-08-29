---
id: learning_2026-08-29_before-considering-a-new-subagent-definition-finis
type: learning
title: "Before considering a new subagent definition finished, spawn it at least once on"
concepts: [subagent-design, testing, verification, writing-th, tool-scoping]
tags: [subagent-design, testing, verification, writing-th, tool-scoping]
created: 2026-08-29
indexed_at: 2026-08-29T08:46:12.876Z
updated_at: 2026-08-29T08:46:12.876Z
hash: sha256:9f40ffd5a59e40df2dbe06d8d62200f45a0247aa564139957e24d4490e597cba
source: "rrr: writing-th-v6-blind-forward-test"
arra_id: learning_2026-08-29_before-considering-a-new-subagent-definition-finis
arra_type: learning
arra_concepts: [subagent-design, testing, verification, writing-th, tool-scoping]
arra_created: 2026-08-29T08:46:12.876Z
---

# Before considering a new subagent definition finished, spawn it at least once on

Before considering a new subagent definition finished, spawn it at least once on a real or representative task rather than just reading the file for internal consistency. During the writing-th v6.0 blind forward test, two subagent definitions (th-argument-mapper, th-editorial-reviewer) had written instructions to run shell validation scripts but were scoped without a Bash tool -- nobody caught this in the prior build session because the definitions were reviewed as files, never actually spawned. One subagent worked around it by manually tracing validator logic by hand; the other hand-typed SHA-256 hashes into a receipt, exactly the failure the hash-binding mechanism exists to prevent. Both were caught only because the orchestrating session independently verified subagent self-reports rather than trusting them. When writing a subagent definition, re-read the prompt hunting for imperative verbs implying tool use (run, validate with, execute) and confirm each has a corresponding tool in the frontmatter; then smoke-test by actually spawning it once before calling the definition done.

---
*Added via Oracle Learn*
