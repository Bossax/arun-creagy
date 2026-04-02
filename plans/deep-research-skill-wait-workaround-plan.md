## Deep Research Skill Wait Workaround – Plan

### Constraint

- The `deep-research` script in [`.roo/skills/deep-research/scripts/deep-research.ts`] can include `Bun.sleep` and polling, but from the IDE/CLI side the command still appears to return almost immediately.
- The tool layer only shows final stdout and exit code, with no streaming timestamps; I cannot empirically enforce or verify a real-time 30s wait between step 3 and 4 from here.
- Browser DOM and Gemini output are not accessible to this environment, so I cannot auto-copy the Deep Research report into [`ψ/inbox/deep-research-enso-record-heat-test.md`].

### Goal

Create a robust, practical workflow that:

1. Starts Gemini Deep Research via the `deep-research` skill.
2. Ensures a human-visible wait window before clicking **Start research**.
3. Captures the final Deep Research report text into [`ψ/inbox/deep-research-enso-record-heat-test.md`].

### Workaround Strategy (High-Level)

1. **Split responsibilities:**
   - Let the `deep-research` script handle steps 1–3 (new tab, select Deep Research, send prompt).
   - Use **you + browser** (or a future browser-side helper) for the precise timing of step 4 (click Start research after plan appears) and for copying the final report.
2. **Use log cues instead of hard waits:**
   - Treat the Bun script as a *fire-and-guide* tool: it brings Gemini to the right state quickly, then exits.
   - You watch the Gemini tab; when the Deep Research plan is ready and the button appears, you click **Start research** yourself.
3. **Standardize markdown capture:**
   - Always paste Deep Research results for this test into [`ψ/inbox/deep-research-enso-record-heat-test.md`], keeping a consistent header and separator.

### Detailed Workflow

1. **Trigger Deep Research (script)**
   - From your terminal or quickCommand:
     - `bun ~/.roo/skills/deep-research/scripts/deep-research.ts "ENSO forecast next year and a chance of a record breaking heat; limit to 5 key sources so research finishes quickly"`
   - Expected outcome:
     - New Gemini tab opened at `gemini.google.com/app`.
     - Deep Research mode selected.
     - Prompt sent (Gemini starts generating the Deep Research plan).

2. **Manual wait + Start research (browser)**
   - Switch to the new Gemini tab.
   - Watch until the Deep Research plan finishes generating and the **Start research** button appears.
   - Click **Start research** manually (this is the reliable substitute for the script’s timing).

3. **Wait for research completion (browser)**
   - Allow Gemini to run Deep Research to completion for this ENSO query (progress bar / status in UI).
   - Once the final report is displayed, select the full answer text (headings, bullets, citations).

4. **Capture into markdown (repo)**
   - Open [`ψ/inbox/deep-research-enso-record-heat-test.md`].
   - Under the `---` separator, paste the Deep Research report.
   - Optionally add a short metadata block at the top noting:
     - Date/time of research.
     - Any constraints (5 sources, etc.).
     - Whether Start research was clicked manually or by script.

### Optional Enhancements (Future)

1. **Sidepanel helper in Browser Proxy**
   - Extend [`tools/claude-browser-proxy-main/sidepanel.js`] to show:
     - Current mode (Deep Research).
     - Status of last `chat` and `clickText` commands.
     - A manual **“Click Start research now”** control that sends the MQTT `clickText` when you see the button.

2. **Answer export helper**
   - In the browser extension, add a small button:
     - **“Copy answer as markdown for Arun_Creagy”**.
   - This would:
     - Read the Deep Research answer DOM.
     - Convert to markdown.
     - Copy to clipboard with a template expecting paste into [`ψ/inbox/deep-research-enso-record-heat-test.md`].

3. **Session discipline**
   - For each Deep Research run, create a dedicated file under `ψ/inbox/` or `ψ/lab/` and link it from your plan files, similar to [`plans/deep-research-quickcommand-test-plan.md`].

### Summary

Given the current architecture, the only reliable workaround is to:

- Use the `deep-research` skill to automate setup (tab + mode + prompt).
- Rely on you (or future browser-side helpers) for the precise 30-second+ wait and Start-research click timing.
- Standardize capture of Gemini’s final Deep Research output into [`ψ/inbox/deep-research-enso-record-heat-test.md`] so that downstream workflows can treat it as the canonical artifact for this ENSO test.

