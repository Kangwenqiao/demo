#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
VENV_PYTHON="${REPO_ROOT}/.venv/bin/python"

if [[ -n "${PYTHON_BIN:-}" ]]; then
  RUNNER=("$PYTHON_BIN" -m pytest)
elif [[ -x "$VENV_PYTHON" ]]; then
  RUNNER=("$VENV_PYTHON" -m pytest)
elif command -v python3 >/dev/null 2>&1; then
  RUNNER=("python3" -m pytest)
elif command -v uv >/dev/null 2>&1; then
  RUNNER=("uv" run --project "$REPO_ROOT" pytest)
else
  echo "No usable Python runner found. Expected ${VENV_PYTHON}, python3, or uv." >&2
  exit 1
fi

cd "$REPO_ROOT"
"${RUNNER[@]}" tests_hidden/test_onboarding_hidden.py -q
"${RUNNER[@]}" scripts/check_layer_rules.py
