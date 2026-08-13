# Lesson: Flag structural discoveries mid-execution, don't silently absorb them

**Context**: Executing an approved plan to edit the WP4 DRD document, I discovered mid-execution (not during the original review) that four requirements treated as separate items (REQ-042/043/044/045) were actually always one consolidated sitemap node, confirmed by the full sitemap v8 tree pulled in during research. This wasn't part of the approved plan.

**What happened**: Instead of quietly folding this into the edit pass to keep moving, I stopped, explained the discovery and its evidence, proposed the structural fix, and got explicit confirmation before deviating from the already-approved plan.

**Why this mattered**: The plan had been explicitly approved by the user (via ExitPlanMode). Silently changing its scope — even for a well-evidenced correction — would have meant the user's approval no longer matched what was actually being built. Stopping to flag it preserved that approval's meaning and let the user catch anything I'd misjudged (which they did, on adjacent points, throughout the session).

**Generalizable pattern**: A structural fact discovered while executing a plan (not while planning it) is a different kind of event than a normal implementation decision. It changes what the plan means, not just how it's carried out. The right move is to pause, show the evidence, and ask — even mid-flow, even when it costs momentum — rather than treat it as just another judgment call inside the approved scope.

**Tags**: plan-mode, execution-discipline, scope-changes, mid-task-corrections
