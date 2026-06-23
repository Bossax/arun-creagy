# Instruction: Update NotebookLM MCP Ruleset & Code templates
**Target**: Roo Code / Future AI Agents
**Date**: 2026-06-23
**Context**: Fixing persistent chat history and thinking process streaming bugs in NotebookLM MCP

Please apply these updates to the project's local/global configuration and skill definitions to prevent future NotebookLM MCP tool timeouts and cached response loops.

---

## 📅 1. Update Project Rules & Skills

### A. File to Update:
`C:\Users\sitth\OracleWorkspace\Arun_Creagy\.agents\skills\notebooklm-rules\references\notebooklm-mcp-ruleset.md`

### B. Add the following rules under Section 3 (Source fidelity) & Section 4 (Prompt design):
1. **Prior Answer Snapshot Timing**: Before reading the answer to a question, the prior answers snapshot (`snapshotPriorAnswers`) must be run **after** the query is typed and submitted (with a 2–2.5 second delay). Taking the snapshot before typing will yield an empty list because the chat history has not yet loaded or restored in the Playwright browser.
2. **Length-Bound Placeholder Filters**: If filtering out NotebookLM intermediate thinking headers (like `**Defining the Scope**`, `**Extracting Key Data Points**`, `**Begin Analyzing the Request**`), only treat them as placeholders if the message bubble's total inner text is short (e.g., `< 350 characters`). When the final answer is complete, the toggle remains in the HTML, so a simple text match will erroneously flag the completed long response as a placeholder and cause a timeout.
3. **Robust Selector Locators**: Do not target message bubbles with CSS `:last-child` (such as `.to-user-container:last-child`). Instead, locate all message bubbles (`.to-user-container .message-text-content`) and target the latest one using Playwright's `.last()` locator method. This prevents scroll-spacers or utility divs appended at the bottom from breaking the selector.

---

## 🛠️ 2. Apply Diffs to Local MCP Package

If the `notebooklm-mcp` node package is re-installed, updated, or runs on a fresh environment, verify that its distribution files contain these patches:

### Path 1: `.../node_modules/notebooklm-mcp/dist/session/browser-session.js`
*Ensure the prior answer snapshot runs after submission:*
```javascript
            // Submit the question (Enter key)
            log.info(`  📤 Submitting question...`);
            await sendProgress?.("Submitting question...", 3, 5);
            await page.keyboard.press("Enter");
            // Small pause after submit
            await randomDelay(2000, 2500);

            // Snapshot existing responses AFTER submit — ensuring the chat panel and history have loaded.
            log.info(`  📸 Snapshotting existing responses...`);
            let existingResponses = await snapshotPriorAnswers(page);
            if (existingResponses.length === 0) {
                existingResponses = await snapshotAllResponses(page);
            }
            log.success(`  ✅ Captured ${existingResponses.length} existing responses`);
```

### Path 2: `.../node_modules/notebooklm-mcp/dist/notebooklm/chat.js`
*Ensure placeholder filters are length-restricted and use the robust locator:*
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
