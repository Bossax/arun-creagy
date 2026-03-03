#!/usr/bin/env bash
set -euo pipefail

# /watch preflight (diagnostics only)
# - No behavior changes to /watch itself
# - Emits a structured summary + raw command outputs
# - Writes a stable log to: output/watch/_preflight.log
#
# Usage:
#   bash tools/watch/preflight.sh "https://www.youtube.com/watch?v=..."

URL="${1:-}"
if [[ -z "${URL}" ]]; then
  echo "Usage: bash tools/watch/preflight.sh <youtube-url>" >&2
  exit 2
fi

OUT_DIR="output/watch"
OUT_LOG="${OUT_DIR}/_preflight.log"
mkdir -p "${OUT_DIR}"

timestamp() { date -Iseconds; }

section() {
  echo
  echo "--- ${1} ---"
}

have_cmd() { command -v "$1" >/dev/null 2>&1; }

resolve_ytdlp() {
  if have_cmd "yt-dlp"; then
    echo "yt-dlp"
    return 0
  fi

  if have_cmd "python" && python -m yt_dlp --version >/dev/null 2>&1; then
    echo "python -m yt_dlp"
    return 0
  fi

  echo ""
  return 1
}

{
  echo "=== /watch preflight: $(timestamp) ==="
  echo "URL: ${URL}"
  echo

  section "host"
  echo "pwd: $(pwd)"
  echo "shell: ${SHELL:-unknown}"
  echo "uname: $(uname -a 2>/dev/null || echo n/a)"

  section "tooling"
  for c in bun node deno python mosquitto_pub mosquitto_sub yt-dlp; do
    if have_cmd "$c"; then
      echo "${c}: OK ($(command -v "$c"))"
    else
      echo "${c}: MISSING"
    fi
  done

  section "yt-dlp availability"
  YTDLP_CMD="$(resolve_ytdlp || true)"
  if [[ -z "${YTDLP_CMD}" ]]; then
    echo "yt-dlp: MISSING (neither 'yt-dlp' nor 'python -m yt_dlp' is runnable)"
  else
    echo "yt-dlp: OK (${YTDLP_CMD})"
    echo "yt-dlp version:"
    # shellcheck disable=SC2086
    ${YTDLP_CMD} --version 2>&1 || true
  fi

  section "yt-dlp list-subs (trimmed)"
  if [[ -n "${YTDLP_CMD}" ]]; then
    # shellcheck disable=SC2086
    LIST_OUT="$(${YTDLP_CMD} --list-subs "${URL}" 2>&1 || true)"
    echo "${LIST_OUT}" | sed -n '1,80p'

    echo
    echo "-- key signals --"
    if echo "${LIST_OUT}" | grep -q "No supported JavaScript runtime"; then
      echo "WARN: yt-dlp reports missing supported JS runtime (EJS)"
    else
      echo "OK: no JS runtime warning detected in list-subs output"
    fi

    if echo "${LIST_OUT}" | grep -q "Available automatic captions"; then
      echo "OK: automatic captions advertised"
      echo "auto-caption languages (en/en-orig):"
      echo "${LIST_OUT}" | grep -E '^(en|en-orig)\s' || true
    else
      echo "INFO: no 'Available automatic captions' section found"
    fi

    if echo "${LIST_OUT}" | grep -q "Available subtitles"; then
      echo "OK: manual subtitles advertised"
    else
      echo "INFO: no 'Available subtitles' section found"
    fi
  else
    echo "SKIP: yt-dlp unavailable"
  fi

  section "summary"
  blockers=()
  warnings=()

  if ! have_cmd mosquitto_pub; then blockers+=("missing mosquitto_pub"); fi
  if ! have_cmd mosquitto_sub; then blockers+=("missing mosquitto_sub"); fi
  if [[ -z "${YTDLP_CMD}" ]]; then blockers+=("yt-dlp not runnable"); fi

  if [[ ${#blockers[@]} -gt 0 ]]; then
    echo "BLOCKERS:"; for b in "${blockers[@]}"; do echo "- ${b}"; done
  else
    echo "BLOCKERS: none detected"
  fi

  if [[ -n "${YTDLP_CMD}" ]] && echo "${LIST_OUT:-}" | grep -q "No supported JavaScript runtime"; then
    warnings+=("yt-dlp missing supported JS runtime (EJS); extraction may be degraded")
  fi

  if [[ ${#warnings[@]} -gt 0 ]]; then
    echo "WARNINGS:"; for w in "${warnings[@]}"; do echo "- ${w}"; done
  else
    echo "WARNINGS: none detected"
  fi

  echo
  echo "Log: ${OUT_LOG}"
  echo "=== end preflight ==="
} | tee "${OUT_LOG}"

