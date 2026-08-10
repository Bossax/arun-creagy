# Lesson: check git diff/status before concluding a Read tool hallucinated content

**Context**: Mid-review of the WP9 Loss & Damage markdown deck, an `Edit` call failed to match an `old_string` that I had just read moments earlier via the `Read` tool. My first conclusion, stated to the user, was that the `Read` tool had fabricated/hallucinated the earlier content — a plausible-sounding theory given this project's memory already contains a precedent (Grep silently mangling Thai text on this Windows environment in a past session).

**What actually happened**: `git diff` against `HEAD` showed the file had a small, real, uncommitted change on disk — the user had edited the title line and a metadata block directly in their editor between my first read and my edit attempt. Not a tool bug at all.

**Why the wrong diagnosis happened**: I reached for the more dramatic/interesting explanation (tool hallucination) before checking the boring, cheap-to-verify one (file changed on disk since I last read it). This project has an established pattern — confirmed again later in the same session — of the user editing files directly and concurrently while I'm working on them.

**How to apply**: When a Read/Edit mismatch occurs on a file that a human has access to edit directly (which is essentially always, in this environment), run `git status`/`git diff HEAD -- <file>` before concluding a tool malfunctioned. Only escalate to "the tool is unreliable" after confirming the file's on-disk content genuinely doesn't match what a reliable secondary read (e.g. `git show HEAD:<file>` vs current, or a PowerShell `Get-Content` cross-check) produces. Never state a tool-failure diagnosis to the user before doing this cheap check — it costs one command and avoids a false narrative.

**Related**: [[frontend-slides-preset-vs-reference-implementation]] — same session had a second instance of "the user had already edited the file directly," this time the generated `index.html` itself, discovered via content search rather than a proactive check.
