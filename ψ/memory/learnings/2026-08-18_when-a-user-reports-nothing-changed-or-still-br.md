---
id: learning_2026-08-18_when-a-user-reports-nothing-changed-or-still-br
type: learning
title: "When a user reports \"nothing changed\" or \"still broken\" after a claimed fix, sto"
concepts: [css-cascade, specificity, verify-before-reasoning, browser-inspection, contrast-accessibility, frontend-slides]
tags: [css-cascade, specificity, verify-before-reasoning, browser-inspection, contrast-accessibility, frontend-slides]
created: 2026-08-18
indexed_at: 2026-08-18T05:14:00.500Z
updated_at: 2026-08-18T05:14:00.500Z
hash: sha256:a5a492ff292c9c2079b0ab51779146f1e201358526ef274db6e3afa5cccaba5c
source: "rrr: creagy-corporate-template-promotion"
arra_id: learning_2026-08-18_when-a-user-reports-nothing-changed-or-still-br
arra_type: learning
arra_concepts: [css-cascade, specificity, verify-before-reasoning, browser-inspection, contrast-accessibility, frontend-slides]
arra_created: 2026-08-18T05:14:00.500Z
---

# When a user reports \"nothing changed\" or \"still broken\" after a claimed fix, sto

When a user reports "nothing changed" or "still broken" after a claimed fix, stop re-reasoning about source code and directly inspect the rendered output (screenshot, computed styles via browser automation) instead — the root cause is often an assumption invisible to static code review (e.g. a fixed-stage 1920px deck actually rendering at 0.6x scale in a normal ~1150px browser window). On CSS: any override rule meant to beat a base class's own property on the same element must use a compound selector (e.g. `.card.card-inverse`), never a bare single-class rule — equal-specificity rules resolve by source order, not logical intent, so a "later" base-class background/color declaration will silently win over an "earlier" override every time. The moment one instance of this bug is found, grep the whole stylesheet for the same pattern (e.g. `opacity: 0\.` fading bare colored text against its own background) instead of waiting for it to be independently reported again in a different component. Never fade bare colored text for visual sequencing/emphasis — fade a filled/bounded shape (a solid badge, a bar-fill on a track) instead, so contrast is preserved as a ratio rather than eroded toward the background.

---
*Added via Oracle Learn*
