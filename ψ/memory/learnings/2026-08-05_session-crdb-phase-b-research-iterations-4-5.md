---
id: learning_2026-08-05_session-crdb-phase-b-research-iterations-4-5
type: learning
title: "Session: CRDB Phase B research (iterations 4-5) + v2 redirection plan rewrite +"
concepts: [background-polling, process-detachment, nohup-disown, causality-tracing, trigger-framing, ted-a-methodology, seal-skill, jargon-detection, tone-review, self-check-blindspots, multi-agent-orchestration]
tags: [background-polling, process-detachment, nohup-disown, causality-tracing, trigger-framing, ted-a-methodology, seal-skill, jargon-detection, tone-review, self-check-blindspots, multi-agent-orchestration]
created: 2026-08-05
indexed_at: 2026-08-05T17:58:02.805Z
updated_at: 2026-08-05T17:58:02.805Z
hash: sha256:887773e885dd666816dcbbadf28d06bd721e865a0444ab3177e26e8c868f93c5
source: "rrr: Arun_Creagy (CRDB Phase B research + v2 redirection + seal)"
arra_id: learning_2026-08-05_session-crdb-phase-b-research-iterations-4-5
arra_type: learning
arra_concepts: [background-polling, process-detachment, nohup-disown, causality-tracing, trigger-framing, ted-a-methodology, seal-skill, jargon-detection, tone-review, self-check-blindspots, multi-agent-orchestration]
arra_created: 2026-08-05T17:58:02.805Z
---

# Session: CRDB Phase B research (iterations 4-5) + v2 redirection plan rewrite +

Session: CRDB Phase B research (iterations 4-5) + v2 redirection plan rewrite + /seal. Three mistakes: (1) Launched a background poller via `nohup bash -c '...' & disown` inside a synchronous Bash call — the outer call returned almost instantly and the harness reported "completed," but this only meant the launcher finished, not that the poll condition was met; the detached loop wasn't tracked by the harness and hadn't actually survived. Fix: never wrap a harness-notification poller in nohup/disown — use `run_in_background: true` directly on the loop itself so the harness tracks the real condition. (2) Running /seal's T-E-D-A trigger reconstruction, proposed the wrong Trigger twice before landing on the correct artifact-level causality: first substituted "Boss's critique" for the trigger, then substituted "comparing v1 against the TOR70 analysis" — both were downstream restatements centered on my own most recent work, not the two independent pre-existing artifacts (TOR70's validated failure modes + a separate CRDB deliverable-drift trace) that actually caused the reconsideration. Fix: for causality-tracing, explicitly ask "what things existed independently before my own analysis/output" rather than defaulting to what's freshest in context. (3) An already-completed hyperbole-removal pass on a report did not catch four coined/metaphorical jargon terms ("boiling-the-ocean", "spine", "next wave", "dual-seal") that Boss later flagged as jargon — these read as normal descriptive language from the inside because they were absorbed from source literature or invented as shorthand during drafting, not because they were dramatic. Fix: tone review needs two distinct passes — one for hyperbole/dramatic register, a separate one specifically hunting coined/metaphorical compound terms not in common English usage.

---
*Added via Oracle Learn*
