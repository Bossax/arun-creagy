# Archived style packs

Superseded on 2026-08-25 by the consolidation into `ψ/memory/style/STYLE_PACK_TH.md`
and `ψ/memory/style/LEXICON_TH.json` (v4.0). Kept for provenance — nothing deleted.

| File | Was | Superseded because |
|---|---|---|
| `STYLE_PACK_TOR5.5-Articles.md` | article-voice pack, 2 capture rounds (2026-06-24, 2026-06-25) | dormant since June; its 4 unique rules were universal and are now folded into `LEXICON_TH.json` as `scope: universal` |
| `LEXICON_TOR5.5-Articles.json` | 5 entries, v1.0 | folded; `มุ่งเน้น` already existed in the main lexicon and its `preferred` was enriched rather than duplicated |
| `LEXICON_NCAIF-Institutional_v3.2.json` | 44 entries, v3.2 | reissued as `LEXICON_TH.json` v4.0 with `kind` and `scope` on every entry, and four malformed rules repaired |

See the 2026-08-25 entry in the new pack's Incremental Capture Log for what changed and why.

---

## `capture_history/`

Archived 2026-08-29 as part of the writing-th v6.0 harness overhaul (design:
`ψ/inbox/2026-08-29_writing-th-v6-build-blueprint.md` §4/§8).

| File | Was | Superseded because |
|---|---|---|
| `STYLE_PACK_TH_incremental-capture-log.md` | `STYLE_PACK_TH.md` §9, 35,812 bytes (62.9% of the file) | an unbounded append-only history (2026-06-25 onward) that never needed to enter a drafting or review model's context; its rules are already folded into `STYLE_PACK_TH.md` §1–§8 and into `LEXICON_TH.json`. Fixes a stray duplicate `## 5.` heading found on archiving by demoting it to a subsection. |

`STYLE_PACK_TH.md` keeps a short pointer note where §9 used to be. Stage 3 of
the v6.0 harness loads `references/prose-kernel.md` instead of the full pack —
see `.agents/skills/writing-th/references/prose-kernel.md`.
