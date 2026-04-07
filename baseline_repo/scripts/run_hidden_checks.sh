#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  PYTHON_BIN="uv"
fi

"$PYTHON_BIN" -m pytest tests_hidden/test_onboarding_hidden.py -q
"$PYTHON_BIN" scripts/check_layer_rules.py
