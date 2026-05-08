# Learning: Atomic execution and ledger edit discipline

When updating CRDB ledgers (Evidence / Trigger / Change / Deliverable), treat the workflow itself as a governance control surface:

1) **Explicit green-light boundaries**
   - Approval is required not only for the content decision (e.g., “make sitemap v4”), but for each ledger write.
   - Enforce “one ledger at a time” to keep changes auditable.

2) **Atomic execution**
   - Keep each shell command to **≤ 2 independent operations**.
   - Avoid large command blocks and chaining across multiple ledgers.

3) **Markdown table updates (deterministic)**
   - Build a complete new table block in a tmp file and use [`replace-md-table.ts`](.roo/skills/markdown-table-edit/scripts/replace-md-table.ts:1) to replace the entire table block under an anchor.
   - Prefer writing tmp files via patching (deterministic repo-state edits) rather than ad-hoc shell scripting.

4) **Rule files are runtime constraints**
   - Treat `.roo/rules/*` (and the Thinking Companion mandates) as non-negotiable. If execution pressure conflicts with these rules, stop and re-plan.

