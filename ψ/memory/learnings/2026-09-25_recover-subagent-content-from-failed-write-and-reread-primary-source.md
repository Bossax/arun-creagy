# Lesson: recovering blocked subagent writes, and rereading primary sources on stakeholder pushback

## 1. When a hook blocks a subagent's Write, recover content from the transcript rather than redoing the work

A relative-path bug in `check_draft_preconditions.py` (a writing-th PreToolUse hook) resolves its own script path against the *session's launch cwd*, not the repo root. A subagent spawned with a non-root cwd hits `[Errno 2] No such file or directory` on **every** `Write` call, regardless of target path — even paths the hook's own logic would have allowed (it fails before its allow/deny logic ever runs).

The failed `Write` tool call still records its full `input.content` in the subagent's transcript (`ψ/…/tasks/<agentId>.output`, JSONL). Recovery pattern, proven twice in one session:

1. `Grep` the transcript file for `"file_path".*<target filename>` to find the line number(s) of the Write attempt(s).
2. `sed -n '<line>p'` that single line to a scratch file (the line can be 100KB+; don't try to view it directly).
3. A small Python script (`json.loads` the line, walk the structure for `{"name": "Write", "input": {...}}`, dump `input["content"]`) extracts the content cleanly.
4. Write it yourself, from the repo root, where the hook resolves correctly.

**Critical follow-up**: tell any resumed/retried subagent explicitly that a blocked write must still be *attempted with full content*, never summarized in its handback message. The first time this happened, the subagent's instinct was to hand back a compact prose summary of ~238 analyzed items instead of re-attempting the full write — which looks like a deliverable but isn't one; it would have meant silently losing the real analytical detail if accepted at face value.

## 2. When a stakeholder's pushback doesn't parse as a simple fix, reread the primary document whole

Boss's comment ("this can't be... check recent retro") initially looked unresolvable — no retro contained the exact "committee can't understand" framing he referenced. The actual resolution came from a different move entirely: rereading the TOR's objectives, target groups, and section heading together, end to end, rather than the specific clause in isolation or secondary commentary (checklists, retros, git log) about it. That surfaced a real framing mismatch — the draft answered a question of the team's own devising, not the TOR's actual ask — that no amount of searching secondary sources would have found.

**Generalizable rule**: when a stakeholder's pushback feels like it "doesn't match the work" and can't be resolved by finding the exact prior conversation they're recalling, the fastest path to ground truth is usually rereading the primary governing document whole (the contract, the TOR, the spec), not triangulating harder through what people have previously said about it.
