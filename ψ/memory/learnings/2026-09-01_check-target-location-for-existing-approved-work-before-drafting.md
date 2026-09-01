# Lesson: Check the target location for existing work before drafting a new artifact in a multi-session pipeline

## Context

Asked to "read the spine doc and get ready to work on §2.3" of the CRDB full report, in a project where writing-contract.json files for different topics get produced across separate batch sessions (Stage 0 for §2.1, §2.2, and §2.3 were all created together in one earlier session, 2026-09-01T00:32:03+07:00, before the session covered by this retrospective started).

## The near-miss

Read the spine document, gathered §2.3's source materials, and was about to compose a new `writing-contract.json` from scratch — the natural next step given the spine doc's guidance alone. Ran `mkdir -p` on the target drafts directory as a first step. Almost as an afterthought, listed the directory's existing contents before writing the contract file. That listing surfaced an already-approved `writing-contract.json` for §2.3, created and approved in an earlier session this same day, which the spine document read alone gave no indication of.

## Why this matters

A planning document (spine doc, writing plan, project plan) describes the *intended* shape of work, not necessarily what has *already executed*. In a project where sessions run in batches and hand off to each other, the authoritative record of what's done is the actual file state in the target directory, not the plan. Treating "I've read the plan, I know what to build" as sufficient before checking the target location risks either overwriting a human-approved artifact or producing a conflicting duplicate that the human then has to notice and reconcile.

## The fix

Before creating any new artifact in a location with session/batch history, list or check that location first — as a default habit, not a conditional one triggered by suspicion. In this case the check happened almost by accident (`mkdir -p` prompted a directory listing) rather than by design; it should be a deliberate first step whenever "check for existing work" is even plausible, especially in any pipeline where Stage 0/1/2/3 artifacts accumulate across sessions and approval state (like `approval.status` and `approved_by`) is meaningful and must not be silently overwritten.

## Secondary note

This generalizes beyond this project: any time a task is "produce artifact X at path Y" in a system with iterative/staged history at that path, the correct first action is inspecting Y's current state, not composing X from requirements alone.
