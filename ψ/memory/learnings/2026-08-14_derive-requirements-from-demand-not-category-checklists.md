# Derive requirements from demand, not from a category checklist

**Date**: 2026-08-14
**Context**: CRDB WP6 — writing Business NFRs and service narratives for 9 climate-information services
**Trigger**: Boss rejected a completed NFR thresholds table as "too shallow to be useful at any... at all"

## The Mistake

I built a Business NFR thresholds table by walking an abstract category checklist — data freshness, compliance thresholds, access latency, retention, semantic consistency — and writing one plausible row per category per service. Nine services, 1–3 rows each, all well-formed, all with owners and priorities and quantified targets.

It looked complete. It was useless.

Service 2 had eight distinct stakeholder use cases documented in the project's own source material (urban risk, biodiversity, household economic resilience, evacuation planning, disability welfare targeting, resource/boundary matching, urban heat vulnerability, plot-level agricultural monitoring). My table gave it two NFR rows. The mismatch wasn't a coverage gap I could patch by adding rows — it was structural evidence that I'd derived in the wrong direction.

## The Correct Direction

**Wrong**: abstract requirement taxonomy → invent a plausible instance per service
**Right**: stated stakeholder demand → what the service must actually answer → then thresholds attached to *those* answers

Boss's framing: "without a clear picture of what these services should answer, how could you derive NFRs?" The requirement layer can't be authored before the conceptual layer exists. When it is, you get requirements that are internally well-formed and externally disconnected from anything a stakeholder said.

## The Detection Signal

**If a service has N stated use cases and your requirements table has far fewer than N rows, the table is wrong** — regardless of how well-formed each row is. Count the source material's own enumerated demands and compare. A large asymmetry means you generated rather than derived.

## Related Failure in the Same Artifact

The same table assigned Service 2 (a risk analytics product) to a single data domain — the one whose *name* matched, "Exposure & Vulnerability." But a risk product consumes hazard + exposure/vulnerability + impact together; it's cross-domain by construction. Matching on the domain's label rather than on what the product actually does is a category error, and the evidence to avoid it was already in the project's own governance doc, which named one group owning two domains jointly.

**Generalization**: when attributing an analytic/derived product to a category, check what it *consumes*, not what it's *called*.

## Concepts

requirements-engineering, business-analysis, derivation-direction, NFR, stakeholder-demand, category-error, domain-modeling
