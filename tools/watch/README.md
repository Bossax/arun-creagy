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

## Where to check output

All scripts here write logs into `output/watch/` so you can inspect results even if terminal output scrolls away.

- Preflight log: [`output/watch/_preflight.log`](output/watch/_preflight.log:1)
- Captions diagnostics logs: `output/watch/_cc_diag_*.log` (example: [`output/watch/_cc_diag_20260303_230139.log`](output/watch/_cc_diag_20260303_230139.log:1))

If you ran a one-off MQTT self-test earlier, you can also save subscriber/broker outputs into files under `output/watch/` and open them from VS Code.

## Setting up yt-dlp JavaScript runtime (recommended)

If yt-dlp prints:

> `No supported JavaScript runtime could be found ...`

then configure it to use Node.

### Permanent (config file)

Create the yt-dlp config file at:

`C:/Users/sitth/AppData/Roaming/yt-dlp/config.txt`

Add this line:

```text
--js-runtimes node
```

Optional (helps with some YouTube JS challenges; requires downloading “remote components”):

```text
--remote-components ejs:github
```

### Ad-hoc (single command)

If you don't want a config file, you can run yt-dlp with:

```bash
python -m yt_dlp --js-runtimes node --list-subs "https://youtu.be/ESkB4_8YClI"
```

## MQTT tools verification

You need `mosquitto_pub` and `mosquitto_sub` available in PATH.

Quick smoke checks:

```bash
command -v mosquitto_sub
mosquitto_sub --help | sed -n '1,25p'
```

If those succeed, rerun preflight to ensure `BLOCKERS: none detected`.

## Interpretation rules

1) If `mosquitto_pub`/`mosquitto_sub` are missing → Gemini automation cannot work (MQTT transport layer is down).

2) If yt-dlp prints `No supported JavaScript runtime could be found` → treat it as a *primary extraction fragility* warning (fix before chasing captions).

3) Captions:
   - “Available automatic captions” means auto-captions exist.
   - “has no subtitles” often refers to *manual subtitles*; auto-captions can still exist.


