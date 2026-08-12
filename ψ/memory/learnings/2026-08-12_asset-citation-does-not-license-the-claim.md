# Lesson: An Asset Citation Proves Existence, Not Adequacy

**Date**: 2026-08-12
**Context**: Building the WP4 Developer-Ready Design Requirements Specification for CRDB

## The pattern

While tiering 55 requirements against DCCE's asset registry, I built a whole category ("Tier B: Handoff") on the reasoning "the matched asset ID shows one of the 3 existing analytical products covers this data, so the remaining work is just interface." That felt like a grounded, evidence-based claim because it cited a real asset ID from a real registry.

Boss's pushback: "I don't think you have full lists of what data is behind this product. You cannot use them to assume anything."

Checking further confirmed Boss was right in a way that made the original claim worse than just unproven — actively unverifiable. The catalog entry for the composite risk index describes its *output* (a published index), not its *inputs*. WP2's own prior findings state the index's method (multiplicative, equal-weighted, normalized) is irreversible, so the published number cannot be decomposed back into the line-agency data that fed it. There was no path to verifying the claim even in principle from the assets available.

## The general lesson

A citation to a real record proves the record exists and says what it says. It does not automatically license every claim someone might want to build on top of it. Before writing "X is true because asset Y exists," check specifically: does Y's content actually establish X, or does it just establish something adjacent that X was inferred from?

In this case the adjacent-but-different facts were "a product with this name exists" and "it publishes on this URL" — both true — versus the actual claim being made, "the data behind it is sufficient for this specific requirement" — unverifiable from what was cited.

## How it changed the output

Instead of quietly asserting adequacy, the tier was redefined as "Existing-Product Surface" — stating only the observable fact (a page could host this product) and explicitly marking data adequacy as unassessed. The unknown became a stated recommendation (investigate the 3 products' underlying data before the next project builds on them) rather than a silent assumption buried in a tier label.

## Where to apply this again

Any time a data-catalog or asset-registry match is used to close or downgrade a gap, check whether the matched record's actual content covers the specific claim being made, not just whether a plausible-looking match exists. This applies beyond CRDB — anywhere an evidence trail is used to justify a status change.

Related: [[project-crdb-wp4-drd-tiering]] (memory)
