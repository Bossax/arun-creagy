---
id: learning_2026-10-07_maw-multi-agent-orchestration-lifecycle-maw-new
type: learning
title: "MAW multi-agent orchestration lifecycle: `maw new <team>` must initialize the tm"
concepts: [rrr, maw, maw-js, tmux-lifecycle, multi-agent-orchestration, fan-out-traps]
tags: [rrr, maw, maw-js, tmux-lifecycle, multi-agent-orchestration, fan-out-traps]
created: 2026-10-07
indexed_at: 2026-10-07T06:12:52.037Z
updated_at: 2026-10-07T06:12:52.037Z
hash: sha256:6452b64424e0958e4b87774c04fd7d85bff0f438036753df30efa2fd06f9a7e1
source: rrr on 13.10_maw-team-orchestration-and-tri-layer-writing-knowledge
arra_id: learning_2026-10-07_maw-multi-agent-orchestration-lifecycle-maw-new
arra_type: learning
arra_concepts: [rrr, maw, maw-js, tmux-lifecycle, multi-agent-orchestration, fan-out-traps]
arra_created: 2026-10-07T06:12:52.037Z
---

# MAW multi-agent orchestration lifecycle: `maw new <team>` must initialize the tm

MAW multi-agent orchestration lifecycle: `maw new <team>` must initialize the tmux canvas before `maw team bring` can tile panes; members must be added via `maw team oracle-invite <oracle> --team <team>`. `maw hey team` executes parallel broadcast fan-out by injecting identical keystrokes across all panes; if a target pane drops to a bash prompt rather than an active agent CLI (e.g. agy), bash executes prompt text as shell commands, resulting in 'command not found'.

---
*Added via Oracle Learn*
