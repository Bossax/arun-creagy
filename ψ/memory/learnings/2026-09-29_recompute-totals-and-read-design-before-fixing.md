---
title: Recompute totals from data; read the design docs before fixing shared tooling
tags: [verification, crdb, shared-skills, hooks, gap-analysis]
created: 2026-09-29
source: rrr: Arun_Creagy
---

# Recompute totals from data; read the design docs before fixing shared tooling

## Numbers

A figure repeated across a handoff, a plan and a counts file can still be wrong. In CRDB §5.1 "266 matched items" appeared in three places while the table beside it summed to 214. Adding the column was enough to catch it. Treat agreement between documents as a reason to recompute, since one copied error looks the same as three confirmations.

When a figure in prose disagrees with a data file, find the decision that produced the prose figure before choosing a side. The draft's 24 ready datasets came from a re-grade made in another tool and never written back to the register. The file was not wrong, it was older than the decision.

For readiness judgments, the rule that held up was concrete: a dataset counts as ready only if a Public catalog entry directly covers the core variable. Restricted matches are "have but hard to use", and product requirements are binary (exists or not). Items the plan called ready but whose matched entries were Restricted were left out, because they contradicted the draft's own definition.

## Shared tooling

The `.agents/skills/<name>` folders are real copies by design, and their `.venv` is deliberately not copied. A fix that replaces the copy with a junction contradicts the README. Read the README and sync script before proposing structure, then change the smallest part (here, link only `.venv`).

A hook that fails on every run and gets worked around is a broken control. Diagnose it at first sight. A temporary hook command that prints `$CLAUDE_PROJECT_DIR`, `$PWD` and the shell version settled in one run what reasoning had not: hooks run under bash, the variable is the project root, and a relative path fails whenever the session shell sits in a subfolder.

## Thai writing pipeline

The thai-writer agent reads the voice files and two Style-Pack sections, and gets the lexicon only through lint. If lint cannot run, the lexicon does not apply, and the voice-exemplars file was empty. Fix the inputs before blaming the agent. After fixing them, use the agent for Thai prose by default and diff its output against your own, since the differences show where each version drops a fact (for example a lost "because") or inherits a change of meaning.
