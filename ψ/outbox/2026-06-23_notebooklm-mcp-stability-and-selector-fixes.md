# Incident Resolution: NotebookLM MCP Stability & Selector Drift
**Author**: Arun Creagy (Technical Assistant)
**Date**: 2026-06-23
**Context**: CRDB Project - TOR 5.5 Extraction

## 1. The Incident (Friction & Drift)

During Phase 1 raw extraction for TOR 5.5, the NotebookLM MCP server fell into a loop, repeatedly returning the first query's cached JSON outline instead of the new query's results, eventually leading to a 10-minute timeout. 

Investigation revealed two architectural friction points in the MCP server's browser-automation layer:

1. **New Streaming "Thinking" Headers**: Google NotebookLM now streams bold reasoning paragraphs (e.g., `**Defining the Scope**`, `**Extracting Key Data Points**`) into the UI before the real response generates. Because these paragraphs are longer than 50 characters and remain static for a few seconds, the MCP's text-stability detector mistook them for final, stable responses and returned them prematurely.
2. **Brittle `:last-child` Selector**: The selector used to read the latest response (`.to-user-container:last-child`) was designed under the assumption that the message bubble is always the last child in the DOM. However, if NotebookLM appends scroll-spacers or utility divs at the bottom of the chat panel, the selector fails to match the new bubble and falls back to reading the old restored chat history.
3. **Pre-Submit Snapshot Race**: The MCP server snapshotted prior answers *before* typing. When loading the notebook freshly, the chat panel is closed, yielding `[]` (empty list of prior answers). Once the query is submitted, the chat history loads from Google Cloud, but since the ignore-list is empty, the stability detector immediately matches the old JSON outline.

---

## 2. Applied Remediation

We applied three code modifications directly to the local node package under:
`C:\Users\sitth\AppData\Local\npm-cache\_npx\0d29dd9f4e472da9\node_modules\notebooklm-mcp\dist\`

### Fix 1: Length-Bound Placeholder Blacklist
Updated `isPlaceholder()` in `notebooklm/chat.js` to only flag blacklisted thinking headers if the message length is short (`text.length < 350`). Once the completed JSON response loads, its massive size (>1,000 characters) bypasses the blacklist filter and is captured immediately:

```javascript
function isPlaceholder(text) {
    const lower = text.toLowerCase();
    // Only treat as placeholder if the text is short AND contains placeholder snippets
    if (text.length < 350 && PLACEHOLDER_SNIPPETS.some((s) => lower.includes(s)))
        return true;
    if (text.length < 50 && text.trim().endsWith("..."))
        return true;
    return false;
}
```

### Fix 2: Transition to Robust `.last()` Selector
Replaced `latestAnswerText` in `notebooklm/chat.js` with `answerText` (`.to-user-container .message-text-content`) and then calling `.last()`. This ensures Playwright always targets the latest answer bubble regardless of CSS `:last-child` nesting:

```javascript
async function readLatestAnswer(page) {
    try {
        const raw = await page
            .locator(Selectors.chat.answerText)
            .last()
            .innerText({ timeout: 2_000 });
        const cleaned = sanitizeAnswer(raw);
        return cleaned.length > 0 ? cleaned : null;
    } catch {
        return null;
    }
}
```

### Fix 3: Delayed prior answer snapshot
In `session/browser-session.js`, moved the `snapshotPriorAnswers()` invocation to after the query has been submitted and a 2.5-second delay has occurred. This ensures the chat panel and its history are fully rendered in the DOM before we capture the list of prior responses to ignore.

---

## 3. Operations Runbook

To prevent these issues from recurring:
1. **Always Restart MCP Processes After Code Edits**: The CLI host caches MCP connections in memory. If you edit code, run a command to terminate the node processes:
   ```powershell
   Stop-Process -Id <id_list> -Force
   ```
2. **Stateless Session Disposals**: Avoid reusing session IDs for unrelated queries. Close sessions using `close_session` to prevent the browser context from growing slow or dirty.
