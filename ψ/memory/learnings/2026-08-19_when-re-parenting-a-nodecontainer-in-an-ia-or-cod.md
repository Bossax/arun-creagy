---
id: learning_2026-08-19_when-re-parenting-a-nodecontainer-in-an-ia-or-cod
type: learning
title: "When re-parenting a node/container in an IA or code structure (moving its conten"
concepts: [information-architecture, refactoring, documentation, self-review, gap-detection]
tags: [information-architecture, refactoring, documentation, self-review, gap-detection]
created: 2026-08-19
indexed_at: 2026-08-19T08:19:42.039Z
updated_at: 2026-08-19T08:19:42.039Z
hash: sha256:d410261b1e6f0c95f74755fc45bac1e5906a10b48dd1dd402741f32f827dbea6
source: "rrr: ncaif-homepage-ia-redesign"
arra_id: learning_2026-08-19_when-re-parenting-a-nodecontainer-in-an-ia-or-cod
arra_type: learning
arra_concepts: [information-architecture, refactoring, documentation, self-review, gap-detection]
arra_created: 2026-08-19T08:19:42.039Z
---

# When re-parenting a node/container in an IA or code structure (moving its conten

When re-parenting a node/container in an IA or code structure (moving its content elsewhere), explicitly audit what the container is left holding as a separate step — don't treat "content moved successfully" as done. Three times in one session (NCAIF homepage redesign), the same underlying mistake produced different symptoms: Home lost its content but never gained formal requirements of its own; task-based homepage shortcuts were designed without a stated navigation fallback for sections they don't cover; a "fold this into the doc" promise was said aloud but never executed. Fix: after any edit that empties/splits/hollows a container, ask "what does this hold now, and does that stand on its own?" before considering the change done — treat it as a mandatory last step, like checking imports after deleting a function.

---
*Added via Oracle Learn*
