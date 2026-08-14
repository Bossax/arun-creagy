# Audience-facing documents must not narrate the project's own discovery process

**Date**: 2026-08-14
**Context**: CRDB WP6 — service business narratives for DCCE and a downstream contractor
**Trigger**: Boss: "should read like a narrative of the service and products, not project evolutionary timeline or project internal artifacts with internal codes and logics"

## The Pattern

I wrote a business-case document whose every section closed with framing like:

> "WP4's build-phase work found no dedicated requirement cluster for this service... REQ-069 is recorded as covered... Brief E-4 confirms this is out of scope... the Enrichment Roadmap suggests..."

The content was accurate. The *voice* was wrong. The document was narrating **the project's discovery process** — which work package found what, in which artifact, at which stage — rather than describing **the services themselves**.

## Why It's Wrong

The readers were DCCE leadership and a downstream implementation contractor. Neither cares:
- which internal work package discovered a finding
- what a requirement's internal ID is
- that a fourth cross-check pass reclassified eight items
- what an internal document is named

To an external reader, internal codes *feel* like precision but function as noise — they obscure the actual argument behind a layer of project-internal bookkeeping.

## The Fix

| Instead of | Write |
|---|---|
| "WP4's build-phase work found the composite index can't be disaggregated" | "DCCE's existing risk index can't be broken down below the province level" |
| "REQ-008, 014, 015, 027, 035 are marked ready to build" | "much of its content is ready to build" |
| "The Enrichment Roadmap suggests a 90m resolution benchmark" | "One design direction worth exploring: a real resolution target — roughly the size of a city block" |
| "Brief E-4 confirms this is a future-project workstream" | "This work is explicitly being deferred, not attempted in the current phase" |
| "STAC and ISO ontologies", "TPMAP", "CMIP6", "PDPA" | "international metadata conventions", "existing national poverty data", "global climate projections", "a privacy review" |

**State findings as facts about the subject, not as reports on who discovered them when.** Keep the honest current-state assessment — omitting blockers would be misleading — but frame it as the service's real standing, not as an audit result.

## Why This One Matters More

This is a **repeat correction**. Boss has now given the same feedback across three separate sessions — on the Node Content Storyboard, on the NCAIF Design Summary Report, and again here. Each time the underlying instinct is the same: showing my work. That instinct serves the author, not the reader.

**Check before drafting any audience-facing document**: who reads this, and would they recognize a single internal code in it? If the answer is no, none should appear.

## Concepts

technical-writing, audience-awareness, documentation-voice, internal-codes, repeat-feedback, deliverable-quality
