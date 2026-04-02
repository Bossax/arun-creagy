## Deep Research QuickCommand ENSO Test – Plan

### Objective

Verify the end to end flow:

1. Trigger Gemini Deep Research via quickCommand `/deep-research` on topic:
   - ENSO forecast next year and a chance of a record breaking heat (limit sources to 5)
2. Wait until Deep Research finishes in Gemini.
3. Copy the final Deep Research report into markdown file:
   - `ψ/inbox/deep-research-enso-record-heat-test.md`

### TODO

1. Configure or confirm the quickCommand for `/deep-research` is available and mapped to:
   - `bun ~/.claude/skills/deep-research/scripts/deep-research.ts "<topic>"`
2. Run the quickCommand with the specific topic and source limit (5 sources) from your editor or terminal.
3. Observe Gemini Deep Research in the browser and wait until the research status shows completion for the ENSO topic.
4. In Gemini, locate the synthesized Deep Research report section (the main final answer with citations).
5. Copy the full report content (including headings, bullet points, and citations) to clipboard.
6. Create or open `ψ/inbox/deep-research-enso-record-heat-test.md` in your workspace.
7. Paste the Deep Research content into `ψ/inbox/deep-research-enso-record-heat-test.md`, preserving headings and structure.
8. Manually verify that citations and links are intact and readable in markdown.
9. Optionally, add a short header block to the markdown file documenting:
   - Topic
   - Date/time of research
   - Source limit used
   - Any manual edits you made.

### Notes

- This test assumes MQTT broker, Claude Browser Proxy, and Gemini Deep Research are already configured and working.
- If the browser automation stalls, you can complete steps 3–5 manually and still validate the markdown capture workflow.

### Next Mode

- After you are satisfied with this plan and have run at least one test, switch to `💻 Code` mode to automate writing to `ψ/inbox/deep-research-enso-record-heat-test.md` (e.g., via a small script that listens to MQTT or a dedicated export step).

