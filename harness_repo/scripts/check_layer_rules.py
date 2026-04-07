from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "src" / "api"
SERVICES_DIR = ROOT / "src" / "services"

FORBIDDEN_SNIPPETS = (
    ".strip(",
    ".lower(",
    ".replace(",
    "re.compile(",
    "re.sub(",
    "RESERVED_USERNAMES",
    "admin_",
    "root_",
    "system_",
    "USERNAME_PATTERN",
)


def collect_violations(directory: Path) -> list[str]:
    violations: list[str] = []
    for path in sorted(directory.rglob("*.py")):
        text = path.read_text()
        for snippet in FORBIDDEN_SNIPPETS:
            if snippet in text:
                relative_path = path.relative_to(ROOT)
                violations.append(f"{relative_path}: found forbidden snippet {snippet!r}")
    return violations


def main() -> int:
    violations = collect_violations(API_DIR) + collect_violations(SERVICES_DIR)
    if violations:
        print("Layer rule violations detected:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("Layer rule check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
