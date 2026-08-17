---
id: learning_2026-08-17_html-to-pdf-export-via-headless-chrome-chrome
type: learning
title: "HTML-to-PDF export via headless Chrome (`chrome --headless --print-to-pdf`) has"
concepts: [pdf-export, headless-chrome, print-css, verification-methodology, slidedoc]
tags: [pdf-export, headless-chrome, print-css, verification-methodology, slidedoc]
created: 2026-08-17
indexed_at: 2026-08-17T17:22:30.715Z
updated_at: 2026-08-17T17:22:30.715Z
hash: sha256:c42754fc725cf0f0a57714a987e37787b52033b4fa2e3c1e8eaadca2bf5ef290
source: "rrr: html-to-pdf-export-debugging"
project: github.com/bossax/arun_creagy
arra_id: learning_2026-08-17_html-to-pdf-export-via-headless-chrome-chrome
arra_type: learning
arra_concepts: [pdf-export, headless-chrome, print-css, verification-methodology, slidedoc]
arra_created: 2026-08-17T17:22:30.715Z
---

# HTML-to-PDF export via headless Chrome (`chrome --headless --print-to-pdf`) has

HTML-to-PDF export via headless Chrome (`chrome --headless --print-to-pdf`) has three common silent-failure modes worth checking for every time:

1. CSS `zoom` is not reliably honored during headless print-to-pdf. If a print stylesheet scales content to fit a physical paper size via `zoom:`, it can render shrunk/misplaced into a corner of the page. Fix: size `@page` to match content's native pixel dimensions exactly (e.g. `@page { size: 1920px 1080px }`) and skip zoom-based scaling entirely — 1:1 pixel mapping avoids all DPI/zoom ambiguity.

2. JS-driven "reveal on active slide" animations (common in slide-deck HTML) print as blank on every slide except whichever was on-screen at print time, since the CSS that makes `.reveal` elements visible depends on a `.visible` class JS only adds to the active slide. Fix: force `.reveal { opacity: 1 !important; transform: none !important; }` inside `@media print`.

3. `<table>` elements can silently drop rows under headless Chrome print pagination — no error, no page break, rows just vanish from the rendered output and the PDF's text layer, even with ample blank space left on the page (so it's not simple overflow clipping). Fix: avoid `<table>` for print-exported HTML; use a grid-of-cards layout instead.

Verification methodology: page count and file size are NOT sufficient signals that a PDF export succeeded. Extract the text layer per page (e.g. via pymupdf's `page.get_text('dict')` sorted by y-coordinate) to programmatically confirm content presence, and do a full page-by-page sweep after every fix — not just re-checking the one page known to be broken, since different bugs can hide on different pages.

---
*Added via Oracle Learn*
