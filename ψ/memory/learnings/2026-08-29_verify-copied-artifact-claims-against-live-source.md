---
date: 2026-08-29
type: learning
topic: verification-discipline
---

# Verify Copied Artifact Claims Against the Live Source, Every Time

Numeric or status claims copied forward from a prior artifact, published page,
or summary document ("proposed, not built," "52 rules," "48 entries") must be
re-verified against the live file before being restated as current fact — not
assumed stable because they were true when the source snapshot was made.

## What happened

A published Artifact ("Writing-TH Harness," dated 2026-08-25) described
`miss_register.db` as "proposed, not built" and `LEXICON_TH.json` as "48
entries." Both claims were copied into a fresh `/fyi --important` log without
re-checking, then copied again into a downstream architecture-analysis
document by a second author. When Boss asked a direct question, a check
against the live repo showed the miss register was actually built and
actively used (48 candidates, 6 promotions, 17 runs logged in a real SQLite
database wired into `style-capture`'s workflow), and the lexicon had grown to
55 entries. Neither document had been wrong when first written — they had
gone stale, silently, and nobody re-counted before restating.

## Why it matters

Stale claims compound across documents faster than they get caught. Each
downstream author trusts the document before them rather than the source of
truth, so an error from one snapshot in time can outlive several rounds of
"verified" analysis built on top of it.

## How to apply

Any time a document states a count, a build status, or a "proposed vs.
shipped" claim about a file, script, or database — grep, count, or run the
thing before repeating the claim, even if a trusted-looking prior document
already states it. Treat "I read it in an artifact/log" as provenance for
*when the claim was true*, not evidence that it's true now.

## Related

- [[2026-08-29_writing-th-harness-architecture-skill-writing-th]] — the corrected architecture record
- ψ/inbox/2026-08-29_writing-harness-skill-architecture-analysis.md §5 — the full correction, signed
