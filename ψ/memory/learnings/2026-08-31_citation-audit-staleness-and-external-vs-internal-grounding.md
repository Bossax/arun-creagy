# Lesson: citation audits go stale silently; internal docs identify claims, they don't ground them

**Context**: CRDB exec-summary writing-th work — compiling a merged references chapter, and tracing a citation for §1.4's Data Platform / Web Platform claim.

## Lesson 1 — A citation audit is a snapshot, not a living fact

The project had per-chapter citation-audit files (`ch{1-4}-references.md`) built 2026-08-29. Chapter 4's section drafts were then completely rewritten (revision-mode pipeline, 08-29 23:04 → 08-30 18:46) with no update to its citation audit. The audit file still confidently listed two citations that no longer appeared anywhere in the live prose. Nothing in the audit file's own content signaled this — it read as current.

**Rule**: before treating any citation/evidence audit as authoritative, compare its build timestamp against the target draft's last-modified timestamp (file mtime or `git log` on the draft path). If the draft moved after the audit, the audit needs re-verification, not blind trust — grep the audit's cited author names/terms against the live draft text as a cheap sanity check.

## Lesson 2 — An internal, unsealed working doc can name a concept precisely without being allowed to source it

WP1's `Business-Objective-Platform-Rationale.md` §1a coined the exact "Web Platform vs. Data Platform" framing later echoed in the exec-summary draft. It was tempting to just cite it. But the project's own established rule (independently reinforced across ch1-ch3 audits) is that internal repo documents cannot be back-matter citations — and WP1 additionally self-flags as "preliminary draft, not sealed, this session's analysis," making it doubly unsuitable as an evidentiary anchor.

**Rule**: when a claim's clearest source is an internal/unsealed doc, use that doc to precisely name *what concept* needs external grounding (its terminology, its exact boundary claim), then search externally for the real-world analog of that concept — don't stop at "well, it's written down somewhere internal." In this case "Data Platform pulls to Web Platform" mapped exactly onto the standard industry term "headless/decoupled architecture," which had genuine external, dated, attributable sources.

## Lesson 3 — A harness write-gate on a missing sidecar file is a legitimate signal, not friction

Attempting to insert the sourced citation into `section-1.4-draft.md` was refused by the writing-th v6.0 PreToolUse hook because that file has no sibling `argument-map.json` (it predates the v6.0 argument-map pipeline entirely). This is not a bug to route around — it's the harness correctly identifying that this specific draft hasn't gone through the map-approval gate the current pipeline requires for any prose write.

**Rule**: when a write is refused by a structural gate (missing sidecar, unapproved status field, etc.), treat the refusal as informative rather than an obstacle — it usually means the target artifact needs an upstream step (here: Stage 1 revision-mode recovery) before the requested edit is actually safe to make. Park the already-verified work product (the citation, fully sourced and ready) rather than forcing the write or silently dropping the request.

## Tags
`crdb`, `citation-audit`, `writing-th-v6`, `evidence-traceability`, `staleness-check`, `external-vs-internal-sourcing`, `pretooluse-gate`
