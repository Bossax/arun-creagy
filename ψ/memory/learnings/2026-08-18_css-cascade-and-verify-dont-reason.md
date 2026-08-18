# Lesson: Verify rendered output, don't re-reason about source when a fix is denied — and generalize recurring bug classes immediately

**Context**: Redesigning the Creagy Corporate slide deck style (WP11 DCCE Executive Briefing draft) in collaboration with the frontend-slides skill's bold-template-pack conventions.

## What happened

Across one session, three separate readability bugs surfaced, all with the identical root mechanism: a single-class CSS override (e.g. `.card-inverse { background: navy-gradient }`) losing a cascade fight against a later same-specificity rule on the same element (`.timeline-step { background: light-tint }`), because equal-specificity rules resolve by source order, not by which one "should" logically win. This pattern was fixed once (hero card background), then recurred immediately after in a different component (`.metric-num` opacity fade) and again in a third (`.timeline-step .step-num` opacity fade) before being generalized into a documented rule ("always use compound selectors for background/color overrides on shared base classes") instead of being treated as three unrelated instances.

Separately, when a font-size fix was reported as "same, nothing changed," the instinct was to re-examine the CSS source for duplicate rules or unclosed comments — reasonable-sounding but wrong, because the actual problem was an assumption about viewport scale (fixed 1920px stage rendering at 0.6x in a normal ~1150px browser window) that no amount of source-reading would surface. Only direct browser inspection (screenshot + computed styles via automation tools) revealed the real cause.

## The fix / what should happen instead

1. **On a second "still broken" report, stop reasoning about source and go inspect the actual rendered output.** Browser automation tools (screenshot, computed-style inspection) exist for exactly this — use them proactively rather than as a last resort after the user explicitly says "investigate your assumptions."
2. **The moment a bug's root cause could plausibly recur elsewhere in the same file, search for the pattern immediately** (e.g. `grep "opacity: 0\."` across the whole stylesheet) rather than waiting for it to be independently reported again.
3. **Any override rule meant to beat a base class's own property on the same element needs a compound selector**, not a bare single-class rule — CSS specificity math doesn't care about "logical" intent, only literal selector weight and source order as a tiebreaker.
4. **Never fade bare colored text against its own background** for visual sequencing/emphasis; fade a filled/bounded shape instead (a solid badge, a bar-fill on a visible track) so contrast is preserved as a ratio, not eroded toward the background it sits on.

## Why this matters going forward

This session's final output — a promoted `bold-template-pack/templates/creagy-corporate/design.md` — encodes all three contrast rules and the compound-selector rule explicitly as "Contrast Rules (non-negotiable)," each tied to the specific bug that caused it. That's the durable fix: the lesson is now load-bearing documentation that any future session generating a Creagy Corporate deck will read before writing CSS, rather than tribal knowledge that has to be rediscovered through user frustration each time.

**Tags**: css-cascade, specificity, verify-before-reasoning, browser-inspection, contrast-accessibility, frontend-slides, design-systems
