# Lesson: Track cumulative staged edits, not just the latest one, before writing

## Context

Adaptation-finance rollup panels (`ψ/lab/visual_design/projects/2026-07-27_adaptation-finance-rollups`). Across several turns, drafted longer GCF/AF intro lines, then in a later turn drafted AF step detail and a reframed differences box, then wrote the file — but only wrote the latest draft, silently dropping the earlier-promised intro update. The user had to catch it and ask why the old short intro was still there.

## Pattern

When a conversation stages multiple content drafts over several turns before any of them get committed to disk, editing based only on the most recent exchange risks losing earlier-agreed changes that haven't been written yet. The failure mode is invisible until the user re-reads the file and notices something they'd already agreed on is missing.

## Fix

Before executing a write/edit that follows multiple rounds of drafting, re-read the target file and mentally (or explicitly) diff it against the *full* set of changes promised across the conversation so far — not just the change being discussed in the current turn. If a prior draft was shown and implicitly approved but not yet written, it's still pending and must be included.

## Related

[[feedback_auto_spawn_watchers_on_handoff]]
