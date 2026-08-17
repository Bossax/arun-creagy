# Methodology critique — C1–C6 rubric, thresholds, and Strict/Moderate/Preserve modes

Date: 2026-08-17
Scope: Critique of the review methodology described in `คู่มือการทบทวนตัวชี้วัดรายกิจกรรมใน Action Plan และการเชื่อมโยงกับระบบติดตามและประเมินผล (M&E Platform).md`, tested against `260814_GGGI_AAC_Indicator_Review.xlsx`.

## The three modes can't detect the error most likely to be present

Strict, Moderate, and Preserve Existing all run on the same C1–C6 scores. Only the weights and thresholds change. So what's being tested is the least uncertain part of the pipeline. The dominant error source here isn't whether C2 should carry 30% or 35% — it's whether C2 = 1 was the right judgment in the first place. If the scorer read an activity too narrowly and gave C2 = 1 where a sector expert would say 3, all three modes are wrong together, in the same direction, and the row shows a clean unanimous "cut" across three modes that looks like triangulation but is one judgment repeated three times.

A robustness check that varies weights while holding judgments fixed will always report high agreement. That agreement is an artifact. What would actually test durability is re-scoring a sample blind, or perturbing each C-score by ±1 and seeing how many verdicts flip. Neither is in the design.

## The stated minimum criteria are arithmetically dead

Section 8 says an existing indicator passes Moderate at score ≥ 65 with C1, C2, C4 ≥ 2. Run the numbers. Moderate weights are C1 25, C2 30, C3 15, C4 20, C5 10. Set the three core criteria to exactly 2 and max out everything else:

```
(2×25 + 2×30 + 4×15 + 2×20 + 4×10) / 4 = 250/4 = 62.5
```

62.5 < 65. A row at the stated minimum can never pass, even with perfect scores on C3 and C5. The minimum criteria line implies 2/2/2 is acceptable; the arithmetic says it never is. The same holds under Strict — C1=C2=C4=3 with perfect C3 and C5 lands on exactly 80.00, the threshold, so the minimums only bind in a razor-thin case.

This matters because anyone reading section 8 will believe there are two independent gates. There's effectively one, and it's stricter than advertised. Whoever set the weights and whoever set the thresholds don't appear to have checked them against each other.

## Under Preserve, continuity can outvote relevance

C6 carries 25% in Preserve mode — more weight than any substantive criterion. With C1 = C2 = C4 = 1 ("low — only partially related, weak linkage, or risks over-interpretation") and strong C3/C5/C6:

```
(1×20 + 1×20 + 3×10 + 1×15 + 4×10 + 4×25) / 4 = 225/4 = 56.25  → passes
```

An indicator that barely relates to the activity is retained because it has a long data series. That's institutional inertia written into a score. Switching cost is a real consideration, but it belongs after fit is established, as a tiebreaker — not as a summand that can rescue a bad fit.

The first data row in `Assessment_all` shows the pathology directly. ACT_OUT_WRM_007 scores C1=0, C2=0, C4=0, C6=4. Its Preserve score of 30 is composed almost entirely of continuity points. It gets cut on Critical Fail, correctly — and then the human reviewer wrote "ควรคงไว้แทนการตัด" with a link to the ONWR master plan.

That disagreement is the tell. The reviewer is answering "is this an important indicator?" The rubric is answering "does this indicator belong to this activity?" Those are different questions, and there's nowhere in the sheet to record "this matters, but not here." Expect that confusion to recur across the reviewer columns.

## C5 is three different constructs sharing one column

Section 5.1 defines C5 as necessity-within-the-old-set for existing indicators, a fixed 4/3/≤2 rubric for M&E candidates, and gap-necessity for new indicators. Three constructs, one weight, one scale, one threshold — and the `Recommended` sheet compares scores across sources as if they were commensurable. They aren't.

Worse, C5 is order-dependent by design. Principle 2 scores all existing indicators before the candidate pool opens. So the incumbent's C5 is assessed in a world where the challenger doesn't exist, and the challenger's C5 is assessed in a world where the incumbent does. Combine that with the M&E rule — equivalent metrics are capped at C5 ≤ 2, which automatically fails the C5 ≥ 3 minimum — and a well-specified M&E indicator is structurally barred from displacing a poorly-specified incumbent that scraped 66, precisely because they measure the same thing. For a project whose stated purpose is harmonizing the Action Plan with the M&E Platform, that rule cuts against the goal.

The 43-added / 43-harmonization-reference split in `ME_Alignment_Check` is suspiciously balanced. A criterion that discriminates rarely produces a near-perfect coin flip; that pattern suggests the "equivalent vs. better operational fit" boundary was drawn by feel.

## Ordinal scores, ratio arithmetic, false precision

The 0–4 scale is labelled qualitatively. Multiplying those labels by percentage weights assumes equal spacing between adjacent levels — that the gap between 3 and 4 equals the gap between 1 and 2. The guide's own design contradicts this, since 0 needs a separate Critical Fail rule precisely because it isn't just "one less than 1." If the scale needed a special case at zero, it isn't interval, and the weighted sum has no arithmetic warrant.

Then scores get reported to two decimals: 96.25, 71.25, 6.25. Under Moderate, one point of C2 moves the total by 7.5 — which is wider than the entire 65-to-70 band separating a kept incumbent from an added candidate. Every borderline row is one analyst judgment away from flipping, and the sheet displays that as 0.25 resolution.

## Three structural rules that manufacture their own findings

The same-sector Critical Fail forbids using an M&E candidate from another sector even when it's the correct measure. Adaptation outcomes are cross-sectoral — upstream forest restoration drives water security, urban form drives heat-health. This rule mechanically converts "the right indicator lives in another sector" into "no suitable M&E candidate exists," which then licenses a new indicator. CCT's result — 19 activities, 0 kept, 0 M&E, 19 new — is exactly what this rule produces when a sector has thin or absent M&E Platform presence. That's a rule artifact reported as a finding.

Nothing scores the set. Coverage is a set-level property, but every score is pairwise and the Coverage sheet is derived afterward, with labels assigned rather than scored. An activity can end up with three indicators measuring the same easy-to-count thing and none measuring the hard thing, and every row passes.

Data readiness is excluded from the decision by section 13 and then never enters any threshold — no column for it appears in `Assessment_all`. And since prior NotebookLM research established there are no targets anywhere in these frameworks, C3 (result-level fit) is partly unanswerable on its own terms. You can't judge whether an indicator sits at the right result level when nobody has stated what result is being aimed for.

## What's sound

The formula is implemented correctly — spot-checked Strict/Moderate/Preserve values against the stated weights and they reconcile exactly. Critical Fail as a non-compensatory override is the right instinct. Forcing a full pass over the old set before opening the candidate pool produces a genuinely useful record of the incumbent set's quality, even though it biases the comparison. Per-row reasons make it auditable. Section 15 is honest about the thresholds not being empirical.

The design isn't careless. It's over-engineered in the parts that are easy to formalize and thin in the parts that decide the answer.

## Mechanically checkable follow-ups (not yet run)

- Dead minimum criteria: confirm no row exists at exactly the 2/2/2 boundary that the guide implies should pass.
- Continuity-rescued rows: find Preserve-mode passes where C1, C2, or C4 ≤ 1.
- The 43/43 equivalence split: sample the harmonization-reference rows to check whether the "equivalent vs. better fit" boundary is applied consistently.
- Cross-sector candidates that were barred: check whether any of them would have scored well if the same-sector rule were relaxed.
- Borderline density: count how many rows sit within one C-point (roughly one criterion level) of their applicable threshold, to size how much of the recommended set is judgment-sensitive rather than robust.
