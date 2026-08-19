---
type: trace
traceId: 5774f9d2-c7ec-4cbe-ac0c-d9c8564f3174
date: 2026-08-19
query: "find issues with html slide scales and format"
target: "HTML Slide Scaler & Viewport Format"
mode: smart
timestamp: 2026-08-19 13:49
friction_score: 0.70
coverage: [oracle, files, session-history]
confidence: high
---

# Trace: find issues with html slide scales and format

**Target**: HTML Slide Scaler & Viewport Format  
**Mode**: smart | **Friction**: 0.70 | **Confidence**: high  
**Time**: 2026-08-19 13:49  

## Oracle Results
- Pointer index matched related frontend/HTML architecture notes across memory, but no prior dedicated forensic log existed for fixed 16:9 stage scaling bugs.

## Files Found & Inspected
- `C:\Users\sitth\.gemini\config\skills\frontend-slides\SKILL.md` (Fixed 16:9 Stage invariants & Density constraints)
- `C:\Users\sitth\.gemini\config\skills\frontend-slides\viewport-base.css` (Canonical 1920×1080 stage architecture)
- `C:\Users\sitth\OracleWorkspace\Arun_Creagy\ncaif-sitemap-overview.html` (Current generated deck)

## Findings & Forensic Audit of Slide Scales & Format Issues

### 1. Slide Visibility Invariant Violation (Display None vs. Visibility/Opacity)
- **The Issue**: In `ncaif-sitemap-overview.html`, slides were toggled using `display: none` and `.slide.active { display: flex; }`.
- **The Risk**: As documented in `SKILL.md` and `viewport-base.css`, using `display: none / block / flex` disrupts CSS transition timings and allows subsequent layout classes (such as `.slide-content { display: flex; }`) to override the display property, potentially causing all slides to become visible simultaneously or fail smooth cross-fade opacity transitions.
- **Remedy**: Revert to `visibility: hidden; opacity: 0; pointer-events: none;` with `.slide.active, .slide.visible { visibility: visible; opacity: 1; pointer-events: auto; }` and place `display: flex;` in the static `.slide` declaration.

### 2. Stage Centering & Flex-Viewport Coordinate Interaction
- **The Issue**: `.deck-viewport` was declared with `display: flex; align-items: center; justify-content: center;` while `.deck-stage` used absolute translation `transform: translate(${left}px, ${top}px) scale(${scale})` from `(0, 0)`.
- **The Risk**: On certain web browsers or iframe embeds, flex centering combined with translate-based canvas scaling can cause double-offsetting or jitter during window resize events.
- **Remedy**: Pin `.deck-stage` with `position: absolute; left: 0; top: 0; transform-origin: 0 0;` inside a full-window fixed viewport without competing flex centering.

### 3. Hardcoded Content Grid Heights vs. Viewport Vertical Rhythm
- **The Issue**: `.s2-grid`, `.s3-stages-grid`, and `.s4-container` were assigned fixed `height: 600px;` alongside an outer flex container with `justify-content: space-between`.
- **The Risk**: When action headlines or subtitles vary in length (e.g. 1 line vs 3 lines across slides), hardcoded child heights cause the footer bar to shift vertically or create disproportionate whitespace at the bottom.
- **Remedy**: Use `flex: 1;` on the central content grid so it dynamically occupies the exact remaining vertical space between the header and footer within the 1920×1080 design boundary.

### 4. Double-Scaling Risk with Relative CSS Units
- **The Issue**: Any use of viewport units (`vw`, `vh`) or `clamp()` inside the slide canvas.
- **The Risk**: Because the stage itself is scaled via CSS `transform: scale()`, using relative viewport units inside slides applies scaling twice, breaking exact layout geometry on mobile devices or 4K monitors.
- **Verification**: Verified that all typography and spacing in the deck use fixed pixels (`px`), adhering to fixed 16:9 stage rules.

## Friction Analysis
**Score**: 0.70 — Present in workspace files; full rules extracted from skill guidelines and confirmed against live generated artifact.  
**Coverage**: oracle, files, session-history  
**Goal check**: Yes, forensically mapped 4 specific scaling and formatting issues and provided exact remedial patterns.

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: Need for zero-dependency, pixel-perfect 16:9 fixed-canvas scaling that resists device reflow and font jumping during live presentations.
- **[E] Supporting Evidence**: `C:\Users\sitth\.gemini\config\skills\frontend-slides\viewport-base.css`, `ncaif-sitemap-overview.html`
- **[D] Potential Decision**: Standardize on `visibility`/`opacity` state switching and `flex: 1` content container scaling across all frontend slides.
- **[A] Target Asset**: `C:\Users\sitth\OracleWorkspace\Arun_Creagy\ncaif-sitemap-overview.html`
