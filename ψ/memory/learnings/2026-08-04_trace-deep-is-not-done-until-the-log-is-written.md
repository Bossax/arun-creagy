# Lesson: /trace --deep is not done until the log is written and bonded

**Type**: learning
**Created**: 2026-08-04
**Tags**: trace, skill-execution, process-discipline

## The pattern

When running `/trace --deep`, it's easy to treat "parallel agents report back" as the finish line and jump straight to synthesizing a chat-facing summary from their findings. But the skill's actual deliverable is a trace log file written to `ψ/memory/traces/` plus an `oracle_trace` call bonding it to the trace chain — the chat summary is a courtesy, not the artifact.

This happened twice in one session with two different framings of the same underlying task (CRDB 9-pillar status audit): agents were launched, results came back, a nicely formatted comparison table was produced — and then the user had to ask "I thought you were doing trace deep" before the actual log-writing step happened.

## Why it happens

Synthesizing agent outputs into a readable answer is the *interesting* part — it's where the actual insight-generation happens. Writing a structured markdown log to a memory folder and calling a logging tool feels like bookkeping after the real work is done. But for a skill built around persistent, searchable memory (Oracle), the bookkeeping *is* the point — a great synthesis that never gets written down is invisible to every future session.

## How to apply

Before declaring a `/trace` (or any skill with a defined "Step 3: write X" / "Step 4: log to Y") complete, explicitly check the skill's own numbered steps against what's actually been done — not against a felt sense of "I did the hard part." If agents have returned and the only remaining steps are "write file" and "call the logging tool," those are not optional wrap-up — they're two more required steps in the same task.

Related: [[read-the-originating-document-not-the-successor]], the same session's other lesson about not confusing "the polished output" with "the actual deliverable."
