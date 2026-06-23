# NotebookLM MCP Remediation Implementation Plan

## Scope
Codify the June 23 NotebookLM MCP stability fixes into the local guardrail docs and verify whether the runtime package already contains the required patches.

## Execution sequence
1. Update the repo-local ruleset at [`notebooklm-mcp-ruleset.md`](../.roo/skills/notebooklm-rules/references/notebooklm-mcp-ruleset.md) with the new source-fidelity and prompt-design guardrails.
2. Align [`SKILL.md`](../.roo/skills/notebooklm-rules/SKILL.md) with the revised guardrails so the skill points future work at the same rules.
3. Confirm the installed NotebookLM MCP runtime already has the delayed snapshot, length-bounded placeholder filter, and `.last()` selector fixes.
4. If any runtime fix is missing, prepare the smallest possible patch plan for [`browser-session.js`](C:/Users/sitth/AppData/Local/npm-cache/_npx/0d29dd9f4e472da9/node_modules/notebooklm-mcp/dist/session/browser-session.js:1) and [`chat.js`](C:/Users/sitth/AppData/Local/npm-cache/_npx/0d29dd9f4e472da9/node_modules/notebooklm-mcp/dist/notebooklm/chat.js:1).
5. Record the verification workflow: restart the affected MCP processes, run a focused NotebookLM query, and confirm the response reader no longer reuses cached chat history.

## Boundary
- Keep implementation work inside the repo-local Roo surface and `ψ` artifacts.
- Do not modify `.agents/` for this task.

## Observed runtime state
- [`browser-session.js`](C:/Users/sitth/AppData/Local/npm-cache/_npx/0d29dd9f4e472da9/node_modules/notebooklm-mcp/dist/session/browser-session.js:1) already snapshots prior answers after submission and includes the 2–2.5 second delay.
- [`chat.js`](C:/Users/sitth/AppData/Local/npm-cache/_npx/0d29dd9f4e472da9/node_modules/notebooklm-mcp/dist/notebooklm/chat.js:1) already uses the length-bounded placeholder filter and the `.last()` locator path.
- No runtime patch appears necessary at this moment; the remaining work is documentation alignment and verification discipline.
