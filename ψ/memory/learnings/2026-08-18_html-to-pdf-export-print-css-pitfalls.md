---
id: learning_2026-08-18_html-to-pdf-export-print-css-pitfalls
type: learning
title: "HTML-to-PDF export via headless Chrome: three print-CSS pitfalls that silently corrupt output"
concepts: [pdf-export, headless-chrome, print-css, slidedoc, verification-methodology]
tags: [pdf-export, headless-chrome, print-css, slidedoc, verification-methodology]
created: 2026-08-18
project: github.com/bossax/arun_creagy
---

# HTML-to-PDF Export via Headless Chrome: Three Print-CSS Pitfalls

Context: exporting a Creagy-template slide deck (`02_DCCE_Executive_Briefing.html`, WP11 CRDB project) to PDF via `chrome --headless --print-to-pdf`. The first export "succeeded" by page-count and file-size checks but was visibly broken when actually opened.

## The three bugs, and the fixes

1. **CSS `zoom` is not reliably honored by headless `--print-to-pdf`.** The deck's print stylesheet targeted physical A4 paper via `@page { size: A4 landscape }` plus a `zoom: 0.585` scale-down hack (tuned for a different print pipeline). Under headless print-to-pdf, this produced content confined to roughly the top-left 60% of the page instead of filling it. Fix: set `@page` size to match the slide's native pixel dimensions exactly (e.g. `1920px 1080px`) and drop the zoom hack entirely — 1:1 pixel mapping, no DPI/zoom ambiguity.

2. **JS-driven "reveal on active slide" animations print as blank.** Common in slide-deck templates: `.reveal { opacity: 0 }` flips to `opacity: 1` only via a `.slide.visible .reveal` selector, where `.visible` is added by JS to whichever slide is currently on screen. Print rendering captures a static DOM snapshot — only the one slide active at print time has visible content; every other slide's body renders blank even though the container itself is forced visible. Fix: add `.reveal { opacity: 1 !important; transform: none !important; }` inside `@media print`.

3. **`<table>` elements can silently drop rows under headless Chrome print pagination.** No error, no inserted page break — rows simply don't appear in the rendered output or the PDF's text layer, even when there's ample blank space left on the page (ruling out simple height-overflow clipping as the cause). This is a known-fragile pattern. Fix: avoid `<table>` in print-exported HTML; use a grid-of-cards layout instead (already proven reliable elsewhere in the same deck).

## Verification methodology lesson

Page count and file size are not sufficient signals that a PDF export succeeded — neither says anything about whether the content is legible or complete. What worked:
- Rendering PDF pages to PNG (via `pymupdf`, since `poppler`/`pdftoppm` wasn't installed and the browser extension wasn't connected) and visually checking a sample of pages.
- More importantly: extracting the underlying text layer with `page.get_text('dict')`, sorted by y-coordinate, to programmatically confirm content presence — this caught the table row-drop bug that a compressed-resolution screenshot made ambiguous.
- Doing a full page-by-page sweep after *every* fix, not just re-checking the page that was known-broken. Bug 2's fix looked complete after spot-checking 3-4 pages; bug 3 was hiding in a specific page (the one with a `<table>`) that wouldn't have been caught without a full sweep.

## Candidate rule for future PDF-export work

- Never declare an HTML→PDF export complete based on page-count/file-size alone. At minimum, visually spot-check a sample of pages; ideally, extract and sanity-check the text layer across all pages.
- When building or reusing a slide-deck HTML template intended for PDF export, apply all three fixes above from the start: native-pixel `@page` size (no zoom hack), a print override forcing reveal-animation elements visible, and grid/card layouts instead of `<table>` for any tabular content.

---
*Added via /rrr*
