# WP4 Developer-Ready Design Requirements Specification v2 — Delta Note

Date: 2026-08-20
Supersedes: `2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` + 5 CSVs (D-068)
Companion node list: `NCAIF_Detailed_Sitemap_v9.md` (D-075); companion Layer-2 doc: `2026-08-20-WP4-Content-Source-Gap-Analysis-v2.md`

Per Boss's decision this session, this is a **delta note against the 5 CSVs**, not a full re-narration of v1's 126KB prose document. The 5 CSVs (`-requirements-v2.csv`, `-deliverables-v2.csv`, `-service-briefs-v2.csv`, `-data-specs-v2.csv`, `-assets-cited-v2.csv`) are the authoritative source of truth. Referential integrity was checked mechanically after every edit: every row-level `deliverable`/`service_brief`/`data_spec` reference resolves to a real ID, every deliverable/brief/data-spec's own requirement list resolves to a real `req_id`, and every requirement's `sitemap_node_id` resolves to a real node in the synced `ncaif_sitemap_nodes.csv`. Zero orphans found after the fixes below.

## What changed, and why

**1. Removed (3 requirements): REQ-027, REQ-028, REQ-029.** All three were SIT-2.4's content requirements (local vulnerability index, integrated spatial risk map, national data-security guidance). 2.4 collapsed to a pure router link in v9 — same removal as the companion Content Source Gap Analysis v2. Knock-on effect: **DS-03** (Vulnerability and adaptive capacity indicators), which existed solely to serve REQ-027, is now retired — struck from the sequence rather than renumbered, matching the existing DS-10 precedent (DS-10 was similarly retired in v1 when REQ-071 changed from a live connection to a curated-links page).

**2. Re-parented (6 requirements), no new judgment calls — same fixes as the CSGA delta:**
- REQ-034 ("Climate scenario usage guide") moved `SIT-3.1.2` → `SIT-3.1.3`: a pre-existing node misassignment, this content has always belonged under 3.1.3 (Climate Scenarios) per both v8 and v9 text.
- REQ-063, REQ-064 (both SIT-3.3.5, project-tracking and budget-readiness) moved to `SIT-3.4.2`: 3.3.5 merged into the Adaptation M&E Platform per Boss's decision this session; their `service_brief` assignments (E-3, E-1) are unchanged.
- REQ-069, REQ-070, REQ-071 (SIT-4.1/4.2/4.3) re-parented to flat `SIT-4`: Section 4's sub-node split is gone in v9.

**3. DEL-2 / DEL-13 risk-map cluster merge (Checkpoint 1a).** v9's own text states the risk map/profile layer is "one capability across 1.2, 2.2, 2.4-link, 4," confirmed to share one backend domain (`ccic.dcce.go.th`). v1's `deliverables.csv` already listed DEL-13 as touching 7 sections, but only one of DEL-13's 9 requirements (REQ-070) carried `DEL-13` in its own row — the other 8 were only linked via `deliverables.csv`'s aggregate list, not the requirement's own record (see the pre-existing gap noted below). Reading each of DEL-13's 9 requirements individually to determine which are genuinely the map/profile capability vs. unrelated migrated products:
   - **Folded into DEL-2** (same underlying data/capability as the map/profile layer): REQ-004 (1.1.1 risk summary cards — same `DCCE_3_x` composite index DS-01 already serves), REQ-009 (1.2 map integration), REQ-015 (2.2 sector risk profiles), REQ-070 (4/Climate Risk Map visualization app).
   - **Left in DEL-13**, now a narrower "migrate other existing analytical products" scope: REQ-005 (1.1.2 hotspots, already FULL), REQ-013 (2.1 exposure trends), REQ-041 (3.2.2 sector risk results) — none of these are about the risk map itself.
   - DEL-2 grows from 3 requirements to 6 (REQ-004, REQ-008, REQ-009, REQ-014, REQ-015, REQ-070); DEL-13 shrinks from 9 to 3.
   - `DS-01` (Provincial composite risk data)'s `serves_requirements` gained REQ-004 for the same reason — same `DCCE_3_x` source data DS-01 already documents.
   - **Net deliverable count: 14 → 13** (DEL-2 and DEL-13 remain distinct IDs — this is a scope reallocation between them, not a literal ID merge — but the map/profile capability that was split across both is now correctly attributed to one of them).

**4. DEL-8 scope note (Checkpoint 2).** v9 adds a legal-framework-compliance bullet at 3.3.1, explicitly reframing 2.3's existing legal/policy content (REQ-017) for planners — closing the gap Boss flagged: "2.3's legal summary previously had no home in Section 3." This is the *same* content, not a new build, so **no new `req_id` was created** — DEL-8's `sections_served` was refined from the general "2.3, 3.3" to the specific "2.3, 3.3.1, 3.3.2" to name where it's reframed, and its `name` field notes the reframing. `requirements` list unchanged (REQ-017; REQ-025; REQ-057).

**5. REQ-011 / DEL-1 vs. DEL-12 — verified, no change needed here.** The plan flagged a disagreement between the DRD and the Node Content Storyboard (D-069) over whether REQ-011 belongs to DEL-1 (Climatology Dashboard) or DEL-12 (Disaster statistics product). Checked: **the DRD's own `requirements.csv` already correctly assigns REQ-011 to DEL-12** — it was never wrong here. The disagreement is entirely on the Storyboard's side (it currently attributes this content to DEL-1). That fix belongs in Phase 3 step 3 (Node Content Storyboard v2), not here.

**6. New requirements (5): REQ-074 through REQ-078.** Three restored-from-v6 items matched against the asset registry this session (same delta-only scope as the CSGA), two mockup-sourced Section 4 tool cards logged as unvalidated:

| req_id | node | requirement | deliverable | data_spec | status |
|---|---|---|---|---|---|
| REQ-074 | SIT-2.3 | NAP Implementation Status | — | — | PARTIAL (DAT-014, same M&E platform as REQ-065/067, not a dedicated NAP tracker) |
| REQ-075 | SIT-3.1.3 | Climate scenario data source | DEL-5 | DS-06 | PARTIAL (same dataset as REQ-035 — folded into the same deliverable/spec, not a new one) |
| REQ-076 | SIT-3.2.2 | Other risk-assessment sources | — | — | GAP (deliberately left unassigned — a references/pointers task, not yet scoped, rather than folded into DEL-6 without a vetted rationale) |
| REQ-077 | SIT-4 | Climate Impact Explorer | — | — | GAP (mockup-sourced, unvalidated — flagged for a future DRD pass) |
| REQ-078 | SIT-4 | Adaptation Options Explorer | — | — | GAP (mockup-sourced, unvalidated — flagged for a future DRD pass) |

**Total: 73 → 75 requirements** (73 − 3 removed + 5 new — same net change as the companion CSGA v2, by construction, since both derive from the same v9 node deltas).

## Flagged, not fixed: pre-existing gap between requirements.csv and the aggregate tables

Per Boss's explicit decision this session, **left as-is**: several rows in `requirements.csv` carry a blank `deliverable`/`service_brief` column even though `deliverables.csv` or `service-briefs.csv` already lists that `req_id` in its aggregate `requirements` field (e.g. REQ-049, REQ-012, REQ-050, REQ-051 are all claimed by `LD-1` in `service-briefs.csv`, but each row's own `service_brief` column is blank; similarly REQ-005, REQ-013, REQ-041 — now DEL-13's remaining membership — still show blank `deliverable` in their own rows). This is a real pre-existing data-quality gap, not something introduced this session, and not something Boss asked to be fixed here. Flagged for a future pass — likely worth cleaning up before this DRD becomes a build-time reference, since a developer reading a single requirement row in isolation would not see its deliverable/brief assignment.

## Verification

- `2026-08-20-WP4-DRD-requirements-v2.csv`: 75 rows, no duplicate `req_id`s, every `sitemap_node_id` resolves against the synced `ncaif_sitemap_nodes.csv`.
- Every row-level `deliverable`/`service_brief`/`data_spec` value that is set resolves to a real ID in the corresponding v2 CSV.
- Every `deliverables-v2.csv` / `service-briefs-v2.csv` / `data-specs-v2.csv` requirement-list entry resolves to a real `req_id` in `requirements-v2.csv` (this caught and fixed one orphan: DS-03 referenced the now-removed REQ-027, resolved by retiring DS-03).
- `service-briefs-v2.csv` and `assets-cited-v2.csv` carried forward unchanged — none of this session's structural decisions touched their membership.
