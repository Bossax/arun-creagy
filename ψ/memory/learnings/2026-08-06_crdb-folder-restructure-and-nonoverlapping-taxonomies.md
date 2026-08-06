# Lesson: Non-1:1 taxonomies need an explicit merge decision, not a rename

**Context**: CRDB had two folder numbering schemes — its own 9-pillar internal categories (00_Strategy_Reports...09_BuildingBlocks) and DCCE's 9-item requested deliverable list. The redirection plan's own Section 3 explicitly documented these don't map 1:1 (one DCCE item, Data Management Framework, spans four CRDB pillar folders: Glossary, CDM, Governance, Reference Data). When the user asked to "restructure the folder" to align with the new item list, treating this as a simple rename would have been wrong.

**Pattern**: When two organizing schemes for the same content don't map 1:1, don't default to the least-surprising interpretation (e.g., "just rename the folders"). Surface the actual shape of the mismatch (which items span multiple folders, which folders have no corresponding item) and let the user choose the execution approach — because the options genuinely trade off differently (keep-and-index = zero risk but doesn't physically reflect the new structure; full merge = matches intent but costs relinking effort across every file that references the old paths).

**Also learned**: `git mv` on this Windows/Git setup does not auto-create nested destination parent directories. `git mv old_folder new_parent/new_folder` fails with `fatal: renaming ... No such file or directory` if `new_parent/` doesn't exist yet. Fix: `mkdir -p new_parent` before the `git mv`. Cheap to always do preemptively when moving into any new nested path.

**Concepts**: folder-restructuring, taxonomy-mapping, git-mv, non-destructive-defaults, explicit-tradeoff-surfacing
