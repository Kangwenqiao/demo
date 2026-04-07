from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VISIBLE_TEST_FILE = ROOT / "tests" / "test_onboarding_visible.py"


def main() -> int:
    text = VISIBLE_TEST_FILE.read_text()
    module = ast.parse(text)
    test_functions = [
        node for node in module.body if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]

    failures: list[str] = []
    if len(test_functions) < 5:
        failures.append("expected at least 5 visible tests after the fix")
    if "pytest.raises" not in text:
        failures.append("expected at least one failure-path visible test using pytest.raises")
    if "UsernameTakenError" not in text:
        failures.append("expected a normalized-duplicate visible test")
    if "reserved" not in text.lower():
        failures.append("expected a reserved-username visible test")

    if failures:
        print("Visible test expansion check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Visible test expansion check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
