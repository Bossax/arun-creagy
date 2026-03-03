#!/usr/bin/env bash
set -euo pipefail

# Caption diagnostics (does not change /watch behavior)
# - Attempts to download auto captions + manual subs using yt-dlp
# - Uses `python -m yt_dlp` if `yt-dlp` is not in PATH
# - Writes stable logs under output/watch/
#
# Usage:
#   bash tools/watch/cc_diag.sh "https://www.youtube.com/watch?v=..." [lang]

URL="${1:-}"
LANG="${2:-en}"

if [[ -z "${URL}" ]]; then
  echo "Usage: bash tools/watch/cc_diag.sh <youtube-url> [lang]" >&2
  exit 2
fi

OUT_DIR="output/watch"
mkdir -p "${OUT_DIR}"
TS="$(date +%Y%m%d_%H%M%S)"
LOG="${OUT_DIR}/_cc_diag_${TS}.log"
WORK="${OUT_DIR}/_cc_tmp_${TS}"
mkdir -p "${WORK}"

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

YTDLP_CMD="$(resolve_ytdlp || true)"
if [[ -z "${YTDLP_CMD}" ]]; then
  echo "ERROR: yt-dlp not runnable (need yt-dlp or python -m yt_dlp)" | tee "${LOG}" >&2
  exit 1
fi

# Resolve video id early so we can avoid output templates like %(id)s.
# On some Windows setups (e.g., pyenv-win python shim), invoking `python` from bash may
# traverse through cmd.exe, and `%(` output templates can explode with:
#   "s was unexpected at this time."
# Using an explicit base output name avoids that entire class of quoting/escaping bugs.
# shellcheck disable=SC2086
VID="$(${YTDLP_CMD} --get-id "${URL}" 2>/dev/null | head -n 1 || true)"
if [[ -z "${VID}" ]]; then
  VID="video"
fi
OUT_BASE="${WORK}/${VID}"

cleanup() {
  rm -rf "${WORK}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

{
  echo "=== /watch cc_diag: ${TS} ==="
  echo "URL: ${URL}"
  echo "LANG: ${LANG}"
  echo "YTDLP: ${YTDLP_CMD}"
  echo "VID: ${VID}"
  echo "WORK: ${WORK}"
  echo

  echo "--- list-subs (trimmed) ---"
  # shellcheck disable=SC2086
  ${YTDLP_CMD} --list-subs "${URL}" 2>&1 | sed -n '1,120p'
  echo

  echo "--- attempt: auto captions (write-auto-subs) ---"
  echo "cmd: ${YTDLP_CMD} --write-auto-subs --sub-lang ${LANG} --sub-format srt --skip-download -o ${OUT_BASE} ${URL}"
  # shellcheck disable=SC2086
  ${YTDLP_CMD} --write-auto-subs --sub-lang "${LANG}" --sub-format srt --skip-download -o "${OUT_BASE}" "${URL}" 2>&1 || true
  echo "files:"; ls -la "${WORK}" || true
  echo

  if have_cmd node; then
    echo "--- attempt: auto captions + js runtime (node) ---"
    echo "cmd: ${YTDLP_CMD} --js-runtimes node --write-auto-subs --sub-lang ${LANG} --sub-format srt --skip-download -o ${OUT_BASE} ${URL}"
    # shellcheck disable=SC2086
    ${YTDLP_CMD} --js-runtimes node --write-auto-subs --sub-lang "${LANG}" --sub-format srt --skip-download -o "${OUT_BASE}" "${URL}" 2>&1 || true
    echo "files:"; ls -la "${WORK}" || true
    echo
  fi

  echo "--- attempt: manual subs (write-subs) ---"
  echo "cmd: ${YTDLP_CMD} --write-subs --sub-lang ${LANG} --sub-format srt --skip-download -o ${OUT_BASE} ${URL}"
  # shellcheck disable=SC2086
  ${YTDLP_CMD} --write-subs --sub-lang "${LANG}" --sub-format srt --skip-download -o "${OUT_BASE}" "${URL}" 2>&1 || true
  echo "files:"; ls -la "${WORK}" || true
  echo

  if have_cmd node; then
    echo "--- attempt: manual subs + js runtime (node) ---"
    echo "cmd: ${YTDLP_CMD} --js-runtimes node --write-subs --sub-lang ${LANG} --sub-format srt --skip-download -o ${OUT_BASE} ${URL}"
    # shellcheck disable=SC2086
    ${YTDLP_CMD} --js-runtimes node --write-subs --sub-lang "${LANG}" --sub-format srt --skip-download -o "${OUT_BASE}" "${URL}" 2>&1 || true
    echo "files:"; ls -la "${WORK}" || true
    echo
  fi

  echo "--- result candidates ---"
  find "${WORK}" -maxdepth 1 -type f -name "*.srt" -print || true
  echo

  echo "Log: ${LOG}"
  echo "=== end cc_diag ==="
} | tee "${LOG}"
