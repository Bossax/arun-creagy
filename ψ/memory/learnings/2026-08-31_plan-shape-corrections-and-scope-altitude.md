# Lesson: Ask plan altitude before drafting; a shape-correction needs re-derivation, not relabeling

**Context**: Planning the CRDB full report writing programme. Asked to prepare for writing after studying the redirect plan, exec-summary drafts, and old writing plans.

## What happened

Went through two scope corrections in one planning session, both from the same root cause.

1. Invoked `/writing-th` Stage 0 formally for chapter 5 (chosen as "prove the method on the hardest case" via an `AskUserQuestion` that offered it as the recommended default). Built a full Stage-0 plan for it in Plan Mode.
2. Boss rejected `ExitPlanMode` and corrected by voice: this pass should produce only a **spine** — storyline, main arguments, key outputs, in logical order, carried from the exec summary — not implementation-ready detail for any one chapter. Chapters also run forward sequentially (1→2→3→4→5), not starting wherever seemed riskiest.
3. Rewrote the plan around "spine" language, but kept the earlier chapter-5 subsection breakdown sitting inside it, because that thinking had already been done. Boss corrected again: intra-chapter design belongs in that chapter's own session, full stop — the content had to actually leave the spine document, not just get relabeled under a new heading.

## Lessons

- **When a correction changes the shape of a deliverable, not its size, salvaged content from the old shape needs re-derivation, not relabeling.** Individually-accurate content (the chapter-5 subsection design) was still a mistake to keep once the deliverable's actual shape changed to "spine only" — reflex was to preserve sunk work under a new heading rather than ask whether it belonged at all.
- **Ask what altitude a plan should sit at before drafting it**, for any open-ended multi-session programme — especially one that naturally decomposes across sessions (chapter by chapter here). Producing a complete artifact and having the user correct its altitude after the fact is more expensive than a single clarifying question up front.
- **A multi-choice question should include the user's likely unstated default as an explicit option**, not just the assistant's own risk-based reasoning. Offering "chapter 5 first, prove the hard case" as the recommended choice — without also offering "sequential from chapter 1" as a first-class option — meant the user's actual preference had to come back as a voice correction rather than a click.

## Secondary finding

Bash's `find -printf` / `wc -l` silently truncate or drop long Thai (multibyte) filenames in this repo. PowerShell (`Test-Path`, `Get-ChildItem`) is the reliable verification tool for Thai-named paths going forward.

Tags: plan-mode, scope-correction, ask-user-question-design, multi-session-planning, thai-filenames, writing-th
