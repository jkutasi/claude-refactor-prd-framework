"""Check this template for retired Claude GitHub Action configuration."""

from __future__ import annotations

import sys
import re
from pathlib import Path


def failures(repo_root: Path) -> list[str]:
    workflow_dir = repo_root / ".github" / "workflows"
    problems: list[str] = []
    paths = {*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")}
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(repo_root).as_posix()
        if "anthropics/claude-code-action@beta" in text:
            problems.append(f"{relative}: uses retired @beta action")
        if "direct_prompt:" in text:
            problems.append(f"{relative}: uses retired direct_prompt input")
        if "anthropics/claude-code-action@" in text:
            if "anthropics/claude-code-action@v1" not in text:
                problems.append(f"{relative}: Claude action must use @v1")
            if "prompt:" not in text:
                problems.append(f"{relative}: Claude action is missing prompt input")
        for script in re.findall(r"python\s+(scripts/[A-Za-z0-9_./-]+\.py)", text):
            if not (repo_root / script).is_file():
                problems.append(f"{relative}: referenced script does not exist: {script}")
    ci_path = workflow_dir / "ci.yml"
    if ci_path.is_file():
        ci_text = ci_path.read_text(encoding="utf-8", errors="replace")
        if "branches: [main, master]" not in ci_text:
            problems.append(".github/workflows/ci.yml: must cover main and master")
        required_commands = (
            "python -m compileall -q scripts tests",
            'python -m unittest discover -s tests -p "test_*.py"',
            "python scripts/check_markdown_links.py",
            "python scripts/check_refactor_contract.py",
            "python scripts/check_github_workflows.py",
        )
        for command in required_commands:
            if command not in ci_text:
                problems.append(f".github/workflows/ci.yml: missing command: {command}")
    return problems


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    problems = failures(repo_root)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("GitHub workflow configuration: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
