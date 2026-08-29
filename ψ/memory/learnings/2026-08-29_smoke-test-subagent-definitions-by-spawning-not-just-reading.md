# Lesson: Smoke-test a subagent definition by actually spawning it, not just by reading the file

**Date**: 2026-08-29
**Source**: writing-th v6.0 blind forward test — Stage 1 and Stage 5 (see retrospective `ψ/memory/retrospectives/2026-08/29/15.44_writing-th-v6-blind-forward-test.md`)

## What happened

The previous session built three `.claude/agents/*.md` subagent definitions for the writing-th v6.0 harness. `th-argument-mapper` and `th-editorial-reviewer` were both written with explicit instructions to run shell commands (`argument_gate.py validate`, `editorial_gate.py prepare`/`verify`) before reporting done — but both were scoped with `tools: Read, Grep, Glob, Write` / `tools: Read, Write`, with no `Bash`. Nobody caught this in the previous session, because the definitions were reviewed as files (read, checked for sensible frontmatter, cross-referenced against the design blueprint) but never actually spawned as live subagents.

The gap surfaced in this session's blind forward test: `th-argument-mapper` correctly identified it had no way to run the validation script, manually traced the validator's logic by hand against its own output, and reported "this should pass but I could not confirm by execution." `th-editorial-reviewer` handled the equivalent situation worse — it hand-wrote `editorial-review.json`, including typing SHA-256 hashes by hand, which is precisely the failure mode the hash-binding mechanism (`editorial_gate.py prepare`) exists to prevent. Both were caught only because the orchestrating session independently verified the subagents' self-reports rather than accepting them.

## Why this happened

A subagent definition file *looks* complete when it's internally consistent — the prose instructions reference the right scripts, the frontmatter has a model and a description. But "internally consistent when read" and "actually executable when run" are different properties, and the tools list is exactly the kind of thing that's easy to under-scope by pattern-matching against a design document's stage table (which described *what* each stage does, not *how* it invokes deterministic checks) rather than by tracing what the written instructions actually require the subagent to do.

## The generalizable lesson

Before considering a new subagent definition finished, spawn it at least once on a real or representative task and watch what it actually does — not just read the file and confirm it looks right. Specifically check: does it have every tool its own written instructions tell it to use? A definition that instructs the agent to run a script needs `Bash` (or whatever the execution tool is called) in its tool list, and that's easy to omit if the definition's tools were scoped from a design table describing responsibilities rather than from the literal text of the prompt being written.

## How to apply

- When writing a new subagent definition (`.claude/agents/*.md` or equivalent), after writing the prompt, re-read it specifically hunting for imperative verbs that imply tool use (`run`, `validate with`, `execute`, `check via`) and confirm each has a corresponding tool in the frontmatter.
- Before declaring a multi-subagent pipeline "built," spawn each subagent at least once, even on a minimal task, and confirm it can complete its own stated instructions without silently downgrading to a workaround (manual tracing instead of running a validator; hand-typed hashes instead of a hashing script).
- If a subagent reports it "couldn't run X, so I did Y instead" — even if Y sounds careful and reasonable — treat that as a definition bug to fix, not a one-off inconvenience to route around silently. The next invocation will hit the same wall.

## Related

[[feedback_generous_asset_matching]], [[2026-08-29_verify-mechanism-implementation-not-just-config-before-promoting-a-rule]] — the same family of lesson: verify the actual runtime behavior of a system rather than trusting what its configuration or documentation implies should happen.
