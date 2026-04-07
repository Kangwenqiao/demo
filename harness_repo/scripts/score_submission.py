from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Check:
    name: str
    points: int
    command: list[str]


CHECKS = [
    Check("Visible tests", 4, [sys.executable, "-m", "pytest", "tests/test_onboarding_visible.py", "-q"]),
    Check("Hidden tests", 6, [sys.executable, "-m", "pytest", "tests_hidden/test_onboarding_hidden.py", "-q"]),
    Check("Architecture check", 4, [sys.executable, "scripts/check_layer_rules.py"]),
    Check("Visible test expansion", 2, [sys.executable, "scripts/check_visible_test_expansion.py"]),
]


def run_check(check: Check) -> tuple[bool, str]:
    result = subprocess.run(check.command, cwd=ROOT, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def main() -> int:
    earned = 0
    automated_total = sum(check.points for check in CHECKS)

    print("Automated scoring")
    print("=================")
    for check in CHECKS:
        passed, output = run_check(check)
        status = "PASS" if passed else "FAIL"
        if passed:
            earned += check.points
        print(f"{status} | {check.name} | {check.points if passed else 0}/{check.points}")
        if output:
            print(output)
        print()

    print(f"Automated subtotal: {earned}/{automated_total}")
    print("Manual review remaining: 4/20")
    print("- Change quality: 2 points")
    print("- Delivery explanation: 2 points")

    return 0 if earned == automated_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
