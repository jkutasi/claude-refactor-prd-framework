"""Validate this template's lean refactor contract and path inventory."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REQUIRED_PATHS = {
    "AGENTS.md",
    "CLAUDE.md",
    "WORKFLOW.md",
    "REFACTOR_WORKFLOW.md",
    "workflow.config.json",
    "refactor-state.example.json",
    ".claude/agents/orchestrator.md",
    ".claude/agents/worker.md",
    ".claude/agents/utility.md",
    ".claude/skills/frontier-workflow/SKILL.md",
    ".claude/settings.json",
    "hooks/session-start.sh",
}

FORBIDDEN_TOP_LEVEL = {
    ".taskmaster",
    "contract-templates",
    "decision-journal",
    "examples",
    "getting-started",
    "reference",
    "SLICE_TEMPLATE",
    "gate_check.config.example.json",
}

ALLOWED_TOP_LEVEL = {
    ".claude",
    ".git",
    ".github",
    ".gitignore",
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "REFACTOR_WORKFLOW.md",
    "WORKFLOW.md",
    "assessment-templates",
    "cutover-templates",
    "decomposition-templates",
    "gherkin-templates",
    "high-risk-review.example.json",
    "hooks",
    "refactor-guide",
    "refactor-state.json",
    "refactor-state.example.json",
    "regression-templates",
    "reviews",
    "risk-downgrade.example.json",
    "scripts",
    "tests",
    "workflow.config.json",
    "workflow.handoff.example.json",
}

FORBIDDEN_TEXT = {
    "OpenAI 5.5": re.compile(r"\bOpenAI\s+5\.5\b", re.IGNORECASE),
    "Gemini reviewer": re.compile(r"\bGemini\b", re.IGNORECASE),
    "Grok reviewer": re.compile(r"\bGrok\b", re.IGNORECASE),
    "QA swarm": re.compile(r"\bQA\s+swarm\b", re.IGNORECASE),
    "nuclear rules": re.compile(r"\bnuclear\s+rules\b", re.IGNORECASE),
    "Whiskey Team": re.compile(r"\bWhiskey\s+Team\b", re.IGNORECASE),
    "Professor agents": re.compile(r"\bProfessor(?:s)?\b", re.IGNORECASE),
    "old phase workflow": re.compile(r"\bPhase\s+[A-J](?:\.\d+)?\b", re.IGNORECASE),
    "old CTO agent": re.compile(r"\bCTO\s+agent\b", re.IGNORECASE),
    "retired Claude action": re.compile(r"claude-code-action@beta", re.IGNORECASE),
    "retired direct_prompt": re.compile(r"\bdirect_prompt\s*:", re.IGNORECASE),
    "bare Opus model": re.compile(r"\bmodel\s*:\s*opus\b", re.IGNORECASE),
    "bare Sonnet model": re.compile(r"\bmodel\s*:\s*sonnet\b", re.IGNORECASE),
    "bare Haiku model": re.compile(r"\bmodel\s*:\s*haiku\b", re.IGNORECASE),
}


def _git_ignored(repo_root: Path, relative: str) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--", relative],
        cwd=repo_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.returncode == 0


def failures(repo_root: Path, enforce_inventory: bool | None = None) -> list[str]:
    """Return template contract failures.

    The strict top-level allowlist protects this reusable template. Once the
    template is installed into an existing project, refactor-state.json marks
    project mode and application-specific top-level paths are allowed.
    """
    problems: list[str] = []
    if enforce_inventory is None:
        enforce_inventory = not (repo_root / "refactor-state.json").is_file()
    for relative in sorted(REQUIRED_PATHS):
        if not (repo_root / relative).is_file():
            problems.append(f"required file missing: {relative}")
    for relative in sorted(FORBIDDEN_TOP_LEVEL):
        if (repo_root / relative).exists():
            problems.append(f"retired path still exists: {relative}")

    ignored = {".ai-workflow", "__pycache__"}
    if enforce_inventory:
        for entry in repo_root.iterdir():
            if entry.name in ignored or entry.name.startswith("workflow.config.local"):
                continue
            if _git_ignored(repo_root, entry.name):
                continue
            if entry.name not in ALLOWED_TOP_LEVEL:
                problems.append(f"unclassified top-level path: {entry.name}")

    scan_paths: list[Path] = []
    document_paths = [
        "WORKFLOW.md",
        "REFACTOR_WORKFLOW.md",
        "AGENTS.md",
        "CLAUDE.md",
    ]
    if enforce_inventory:
        document_paths.append("README.md")
    for relative in document_paths:
        path = repo_root / relative
        if path.is_file():
            scan_paths.append(path)
    owned_directories = [
        ".claude",
        "hooks",
        "refactor-guide",
        "assessment-templates",
        "decomposition-templates",
        "gherkin-templates",
        "regression-templates",
        "cutover-templates",
    ]
    if enforce_inventory:
        owned_directories.append(".github")
    for relative in owned_directories:
        root = repo_root / relative
        if root.is_dir():
            scan_paths.extend(path for path in root.rglob("*") if path.is_file())

    for path in sorted(set(scan_paths)):
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(repo_root).as_posix()
        for label, pattern in FORBIDDEN_TEXT.items():
            if pattern.search(text):
                problems.append(f"{relative}: contains {label}")
        if "Gherkin Files ARE the Regression Test" in text:
            problems.append(f"{relative}: treats Gherkin text as an executable test")
    return problems


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    problems = failures(repo_root)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("Refactor contract: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
