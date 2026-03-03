# /watch hardening (local)

This folder exists to make `/watch` failures *diagnosable first*, before attempting fixes.

## What we observed

The most recent failure artifacts are in:

- [`output/watch/_diag.log`](output/watch/_diag.log:1)
- [`output/watch/_watch_run.log`](output/watch/_watch_run.log:1)

The failure mode is multi-causal (MQTT tooling + yt-dlp JS runtime + captions strategy).

## Preflight (diagnostics-only)

Run:

```bash
bash tools/watch/preflight.sh "https://www.youtube.com/watch?v=ESkB4_8YClI"
```

This writes a stable log to [`output/watch/_preflight.log`](output/watch/_preflight.log:1).

## Captions diagnostics (diagnostics-only)

If you see contradictory signals (e.g., “Available automatic captions” but your run yields `NO_CAPTIONS_AVAILABLE`), run:

```bash
bash tools/watch/cc_diag.sh "https://www.youtube.com/watch?v=ESkB4_8YClI" en
```

This creates a timestamped log under `output/watch/` (ignored by git).

## Interpretation rules

1) If `mosquitto_pub`/`mosquitto_sub` are missing → Gemini automation cannot work (MQTT transport layer is down).

2) If yt-dlp prints `No supported JavaScript runtime could be found` → treat it as a *primary extraction fragility* warning (fix before chasing captions).

3) Captions:
   - “Available automatic captions” means auto-captions exist.
   - “has no subtitles” often refers to *manual subtitles*; auto-captions can still exist.


