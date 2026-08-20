# Handoff: NCAIF Sitemap v8 → v9 Practicality Pass

**Date**: 2026-08-20 15:11
**Context**: ~44% at handoff time
**Plan file**: `C:\Users\sitth\.claude\plans\vast-gliding-turtle.md` — read this first, it's the full working plan with all three audit tracks, all checkpoint decisions, and the exact next steps in Phase 3.

## What We Did

**Diagnosed why v8 over-claims content-sharing.** Started from one concrete case (the ECA/avoided-losses tool listed in both 2.3 and 3.3.1 as shared, but not actually built at 3.3). Traced the project's five-layer document chain (v8 sitemap → per-node requirement extraction → DRD's 14 deliverables/6 service briefs → downstream WP6/7/8 → this week's mockups) and found the DRD (D-068, sealed weeks earlier) had *already* correctly resolved most of these "is this shared" questions — the mockups just hadn't checked back against it. Found concrete evidence of the drift: the Finance Tracker built three times with three conflicting figures (฿100M Sankey at 3.3, ฿42,500M progress bar at Tools Hub, plus 2.3.1's directory), the risk map built three times with three different images, ECA built twice.

**Ran a v6-vs-v8 diff.** Boss named `NCAIF_Detailed_Sitemap_v6.md` as his original intention. Diffing it against v8 surfaced a second, independent problem: 47 inline `[N, MUST/SHOULD]` A-BTR compliance tags in v8, almost entirely absent from v6, concentrated exactly in the same zones the sharing audit had flagged (2.3/2.3.1/2.3.2, 3.3.1) — i.e. UNFCCC-reporting-section scope creep, not identified demand. Also found 6 v6 items quietly dropped from v8.

**Ran the full plan (see plan file for the 3-track structure — A: structural sharing, B: A-BTR bloat, C: v6 drops) through a sequence of `AskUserQuestion` checkpoints with Boss**, resolving every cluster: which builds are genuinely shared, which undecided-service content (Brief E-1/E-3/E-5/E-6) gets marked pending instead of built as finished, which v6 drops get restored (5 of 6 — 2.4 deliberately stays a router link), and drops all BTR tags entirely.

**Drafted `NCAIF_Detailed_Sitemap_v9.md`**, sent it to Boss, and went through two more rounds of his direct inline review (`%%comment%%` markers in the file itself) — resolved 6 more findings: confirmed 2.2's data is CCIC-sourced (verified against the asset registry), tightened the Finance Tracker naming across all 3 places it appears, changed 2.3's NAP Summary to a cross-reference instead of duplicated text, gave 2.3's legal/policy content a genuine home in Section 3 (new bullet at 3.3.1), merged 3.3.5's Project Tracking Status into 3.4.2 (both were claiming the same not-yet-built M&E Platform function), flattened Section 4 from a 3-way category split to a tag-filterable list matching the mockup's actual build. Final round: confirmed 3.3.4 and 3.4.3 are genuinely distinct (planning *process* vs. implemented *result*), not a duplicate — closed the plan's last open item.

**Sealed the result via `/seal`.** New ledger entries: **E-089/090/091** (v6 baseline, DRD's joined CSVs, the 11 mockup files), **T-049** (the trigger — explicitly framed as discovered during hands-on mockup/slide production, not a desk review, per Boss's correction), **CH-045** (full decision record), **D-075** (`NCAIF_Detailed_Sitemap_v9.md`, sealed, supersedes **D-050**). D-050's row now carries a correction note that its "de-bloated" framing was itself the source of the bloat found this session.

## Pending

- [ ] `ncaif_sitemap_nodes.csv` / `ncaif_sitemap_nodes.json` — **not yet synced** to v9's node tree. Still mirrors v8's structure. Do this before anything else in Phase 3, since the downstream regeneration should read from a consistent structured node list, not just the prose.
- [ ] Phase 3 — regenerate 4 downstream documents against v9 (all currently still reflect v8's structure):
  1. **Content Source Gap Analysis v2** + `wp4-requirement-items-v9.csv` — re-extract requirement items against v9's node list, re-tally FULL/PARTIAL/GAP (was 20/19/34 of 73 against v8).
  2. **DRD v2** + 5 companion CSVs — fold in every merge/cut/pending decision from this session; deliverable count will likely shrink from 14; also fix the standing REQ-011 DEL-1/DEL-12 disagreement between the old DRD and Storyboard that this session found (independent of Boss's asks).
  3. **Node Content Storyboard v2** — rewrite page-by-page build order/readiness against v9; keep its prose in sync with what DRD v2 actually says this time (the REQ-011 drift happened because these two documents disagreed with each other).
  4. **Node-Level Deep-Dives v2** — regenerate the per-node coverage rollup at v9's grain.
  Each should ship with a short delta note back to its sealed D-06x predecessor.
- [ ] Checkpoint 3 (per the plan) — Boss reviews the 4 regenerated docs for internal consistency before they become the new baseline.
- [ ] Explicitly out of scope for this pass, flagged as separate follow-ons: reconciling the 11 mockup HTML files against v9's structure (they still show the old duplicated/undecided-as-finished content — e.g. the 3× Finance Tracker, 3× risk map); re-deriving WP6/WP7/WP8 outputs (D-071–074) if the Phase 3 deliverable-count changes turn out to matter there.

## Next Session

- [ ] Sync `ncaif_sitemap_nodes.csv`/`.json` to v9's structure first.
- [ ] Start Phase 3 regeneration in the order listed above (Gap Analysis → DRD → Storyboard → Deep-Dives), since each depends on the previous.
- [ ] Bring the 4 regenerated docs back to Boss for Checkpoint 3 before considering this pass fully closed.
- [ ] Do **not** re-litigate any of the Checkpoint 1/2 decisions already made — they're all recorded in the plan file and the ledger (T-049/CH-045). If something looks like it needs revisiting, treat it as new information, not a re-ask.

## Key Files

- Plan: `C:\Users\sitth\.claude\plans\vast-gliding-turtle.md` (full audit-track structure + every decision made)
- Sealed asset: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/NCAIF_Detailed_Sitemap_v9.md` (D-075)
- Superseded: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/NCAIF_Detailed_Sitemap_v8.md` (D-050, kept on disk, not deleted)
- v6 baseline used for the diff: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/NCAIF_Detailed_Sitemap_v6.md`
- Node CSV/JSON needing sync: `ψ/incubate/DCCE/CRDB/output/04_Sitemap/ncaif_sitemap_nodes.csv` / `.json`
- DRD (Layer 3, still v1, to be regenerated): `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` + 5 CSVs
- Storyboard (still v1): `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-13-WP4-Node-Content-Storyboard-and-Synthesis-Guide.md`
- Content Gap Analysis (still v1): `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-10-WP4-Content-Source-Gap-Analysis.md` + `.csv`
- Node-Level Deep-Dives (still v1): `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-11-WP4-Node-Level-Deep-Dives.md`
- Ledgers touched: `CRDB-Evidence-Registry.md`, `CRDB-Trigger-Log.md`, `CRDB-Change-Log.md`, `CRDB-Deliverable-Map.md` (all at `ψ/incubate/DCCE/CRDB/`)
