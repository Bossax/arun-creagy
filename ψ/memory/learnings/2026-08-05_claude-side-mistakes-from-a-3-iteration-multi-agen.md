---
id: learning_2026-08-05_claude-side-mistakes-from-a-3-iteration-multi-agen
type: learning
title: "Claude-side mistakes from a 3-iteration multi-agent (Claude + agy/Antigravity) r"
concepts: [multi-agent-orchestration, bash-state-persistence, background-polling, peer-agent-handoff, report-tone, audience-calibration, citation-jargon, markdown-formatting, self-diagnosis, final-document-hygiene, decision-framing, semantic-lock-protocol-counterpattern]
tags: [multi-agent-orchestration, bash-state-persistence, background-polling, peer-agent-handoff, report-tone, audience-calibration, citation-jargon, markdown-formatting, self-diagnosis, final-document-hygiene, decision-framing, semantic-lock-protocol-counterpattern]
created: 2026-08-05
indexed_at: 2026-08-05T15:22:13.751Z
updated_at: 2026-08-05T15:22:13.751Z
hash: sha256:ed14b44a1392b09a914d314253039761346f7f23069f83d669c4713c278f3ac0
source: "rrr --deep: Arun_Creagy (CRDB research orchestration)"
arra_id: learning_2026-08-05_claude-side-mistakes-from-a-3-iteration-multi-agen
arra_type: learning
arra_concepts: [multi-agent-orchestration, bash-state-persistence, background-polling, peer-agent-handoff, report-tone, audience-calibration, citation-jargon, markdown-formatting, self-diagnosis, final-document-hygiene, decision-framing, semantic-lock-protocol-counterpattern]
arra_created: 2026-08-05T15:22:13.751Z
---

# Claude-side mistakes from a 3-iteration multi-agent (Claude + agy/Antigravity) r

Claude-side mistakes from a 3-iteration multi-agent (Claude + agy/Antigravity) research-orchestration session grounding a CRDB redirection plan:
1. Stale bash cwd (left over from an earlier throwaway `cd`) caused a background poller launched with a relative path to silently watch a nonexistent location — no error, just permanent silence, until the human noticed the mismatch between "work finished" and "nothing happened."
2. Briefly overrode a peer agent's own already-documented watch-loop by planning to manually invoke it directly, despite having authored the peer's self-polling instructions earlier in the same session — a gap in own tooling ("I have no watcher") was mistaken for evidence the peer lacked one too.
3. First draft of a decision-facing report used hyperbolic language (scare-quoted anti-patterns, superlatives) and internal bookkeeping jargon (notebook nicknames, query-response codes) that had to be corrected twice via explicit user complaints, rather than defaulting to plain report register given an executive/decision-facing audience.
4. When told own output "looked broken," guessed at causes and asked a clarifying question instead of first auditing own recent formatting choices (manual hard-wrapping at ~90 chars, bold-pseudo-numbered lists) — the actual cause was self-authored and should have been self-diagnosable.
5. A document was treated as "final" while still containing unresolved `%%...%%` review-markup (the user's own inline pushback) left inside the reader-facing body text — never grepped for before shipping as final.
6. Counter-pattern to the Semantic Lock Protocol (which documents agents wrongly skipping human-in-the-loop checks): this session manufactured decision points that didn't need to exist — one built a paradigm-choice framework onto a question that was actually a category error (a required, mandated deliverable was framed as a free architecture choice), another flagged something as an open decision when it was inferable from already-known project context (blueprint/pre-system-design phase with no physical system yet built).

General lessons: (a) verify/reset shell cwd or use absolute paths before any path-relative background launch, especially pollers, since their failure mode is silent; (b) before manually driving a peer agent, re-read the standing contract you already gave it; (c) default to plain, neutral report language for decision-facing audiences without waiting to be told, and strip internal bookkeeping shorthand before merging research artifacts into human-facing deliverables — verify removal by grepping, don't assume; (d) audit your own recent formatting choices first when told your own output looks wrong; (e) before calling any document "final," grep for leftover non-prose review markup; (f) don't skip real human decisions, but also don't manufacture fake ones — check whether a "decision needed" framing actually fits the thing being decided, and whether the answer is already inferable from context on hand.

---
*Added via Oracle Learn*
