---
id: learning_2026-09-24_when-a-hook-blocks-a-subagents-write-call-due-to
type: learning
title: "When a hook blocks a subagent's Write call due to a relative-path bug (script re"
concepts: [subagent-recovery, write-hook-bug, relative-path-bug, primary-source-rereading, stakeholder-pushback, writing-th, crdb]
tags: [subagent-recovery, write-hook-bug, relative-path-bug, primary-source-rereading, stakeholder-pushback, writing-th, crdb]
created: 2026-09-24
indexed_at: 2026-09-24T17:32:05.623Z
updated_at: 2026-09-24T17:32:05.623Z
hash: sha256:47b431c9325d52a0aeb2adae415fb011237f2393321d4b3527fda695eec057ec
source: "rrr: Arun_Creagy"
arra_id: learning_2026-09-24_when-a-hook-blocks-a-subagents-write-call-due-to
arra_type: learning
arra_concepts: [subagent-recovery, write-hook-bug, relative-path-bug, primary-source-rereading, stakeholder-pushback, writing-th, crdb]
arra_created: 2026-09-24T17:32:05.623Z
---

# When a hook blocks a subagent's Write call due to a relative-path bug (script re

When a hook blocks a subagent's Write call due to a relative-path bug (script resolves against launch cwd, not repo root), the failed tool call still records its full input.content in the subagent's transcript JSONL. Recover it: grep the transcript for the target filename, sed the matching line to a scratch file, parse it as JSON to extract input.content, then write it yourself from the repo root. Tell any resumed subagent explicitly to re-attempt the full write rather than hand back a compact summary — a summary looks like a deliverable but silently loses the real analytical detail. Separately: when a stakeholder's pushback doesn't match a specific prior conversation they're recalling, reread the primary governing document (TOR, contract, spec) whole rather than searching harder through secondary commentary about it — that's what actually surfaces framing mismatches.

---
*Added via Oracle Learn*
