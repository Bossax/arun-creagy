# Lesson: A seal's Trigger must trace to the originating mandate, not the most recent session

## What happened

When sealing WP7 and WP8 into the CRDB project ledgers, the first T-E-D-A proposal framed the Trigger as "Boss's review of both drafts" — the event that caused this session's edits. Boss corrected this directly: the Trigger must go back to the original plan that mandated the deliverable's existence, not just the session that most recently touched it. The actual trigger (T-043, the 2026-08-06 final-sprint implementation plan) was already on disk, with WP7 and WP8's exact scope written into its own table rows.

## Why this matters

The seal skill's Hard Rule 1 separates Motive (Trigger) from Artifact (Evidence), but that rule alone doesn't prevent picking the wrong motive. "What caused this text to change today" and "why does this deliverable exist at all" are different questions, and only the second one is a Trigger. Conflating them makes the ledger's causality chain shallow — it would show why a paragraph got edited, not why the report was commissioned. Over many sealing sessions, this would leave every deliverable's Trigger pointing at whatever review happened last, erasing the actual project mandate trail the ledger exists to preserve.

## How to apply

Before proposing a T-E-D-A chain for any seal, check the deliverable's originating source of truth first — the sprint plan, TOR, or governing decision doc — for a row or clause that already names this specific deliverable's scope. If one exists, that's the Trigger, even if it predates the current session by weeks. Reserve "this session's changes" for the Decision (D/CH) entry, where it belongs. Also default to one seal per deliverable rather than batching multiple work packages into a single chain unless explicitly told to combine them — the Deliverable Map is structured per-artifact, and batching blurs which mandate justifies which asset.

Related: [[feedback_no_audit_tone_in_deliverables]], project context in `ψ/incubate/DCCE/CRDB/AGENTS.md` (ledger structure and seal-only-via-skill rule).
