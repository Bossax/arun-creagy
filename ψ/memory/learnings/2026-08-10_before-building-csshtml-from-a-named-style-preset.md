---
id: learning_2026-08-10_before-building-csshtml-from-a-named-style-preset
type: learning
title: "Before building CSS/HTML from a named style preset, check whether the preset ref"
concepts: [frontend-slides, style-preset, reference-implementation, css]
tags: [frontend-slides, style-preset, reference-implementation, css]
created: 2026-08-10
indexed_at: 2026-08-10T16:22:07.462Z
updated_at: 2026-08-10T16:22:07.462Z
hash: sha256:abd320c0d2037106e85269268ab38c0ed6fd52c99003390fbf2e0175f3952811
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-10_before-building-csshtml-from-a-named-style-preset
arra_type: learning
arra_concepts: [frontend-slides, style-preset, reference-implementation, css]
arra_created: 2026-08-10T16:22:07.462Z
---

# Before building CSS/HTML from a named style preset, check whether the preset ref

Before building CSS/HTML from a named style preset, check whether the preset references (or later comes to reference) a real template/example file, not just a prose summary. A prose-summary preset (e.g. STYLE_PRESETS.md's "Creagy Corporate" entry) is lossy compared to an actual working reference implementation with real class names, spacing, and structure. When both exist, the file is authoritative — read it first, even if it requires working around large embedded assets (e.g. base64 images blowing a Read tool's token cap; use targeted awk/grep truncation instead of skipping the file). Only fall back to inferring structure from a prose description or an external source (like a PPTX) when no real reference implementation exists.

---
*Added via Oracle Learn*
