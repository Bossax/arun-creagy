# Lesson: Audit "N of M" Claims in Your Own Output Against What You Actually Presented

**Context**: TOR70 briefing deck session. The deck's speaker notes referenced "7 validated failure modes" (FM1-FM7) from a literature-validation report I had written earlier the same week. But when I built the gap-analysis slides (Part 3), I only turned 4 of those 7 into actual slides — FM5 (documentation overload/tech-stack lock-in) and FM7 (dashboards without use case + unmeasurable quality — the *most* strongly-evidenced finding of all seven) never got their own slide. The user had to ask "why are there 4 shown?" for me to catch it.

**Why it happened**: When compressing a large validated body of work into a fixed-size deliverable, I picked a subset that read well narratively and moved on, without cross-checking the subset against the total I myself had already established elsewhere in the same document (the speaker notes citing "all 7"). The citation was accurate at the time I wrote it; the slide selection silently drifted away from matching it.

**This is a repeat**: the prior session's retrospective already named this exact failure shape ("any time I'm compressing validated findings into a fixed-size deliverable, I should trace forward from findings to conclusions and back") after a near-identical incident (a recommendation with no supporting gap slide). Naming the lesson once did not prevent reproducing it in the very next session on the same document.

**The fix that would actually work**: not "be more careful" (already tried, didn't work) but a concrete, mechanical check — before presenting any compressed deliverable, grep/count every "N of M," "all X," or "7 failure modes"-style quantifier claim made elsewhere in the same work, and verify the compressed version's actual count matches. Treat it as a literal pre-flight step, not a vibe check.

**How to apply**: Whenever finalizing a deck, report, or summary that references a total count established in prior work (N findings, M requirements, X sources), explicitly enumerate what's presented and diff it against the claimed total before calling the work done — do this even when (especially when) the compression felt complete on a narrative level.

Related: [[tor70-deck-strengthening]], see also the prior lesson on tracing compressed claims to sources.
