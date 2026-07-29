"""Fail-closed validation for the declared refactor lifecycle stage."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

STAGES = ("snapshot", "strategy", "baseline", "implementation", "cutover", "complete")


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolved(value: Any) -> bool:
    return _nonempty(value) and not re.search(r"<[^>]+>|\{\{[^}]+\}\}", value)


def _nonempty_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(_resolved(item) for item in value)
    )


def _read(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"refactor state not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid refactor state JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("refactor state must be a JSON object")
    return value


def validate_state(path: Path) -> list[str]:
    """Return failures for evidence required by the declared stage."""
    try:
        state = _read(path)
    except ValueError as exc:
        return [str(exc)]

    failures: list[str] = []
    if state.get("version") != 1:
        failures.append("refactor state version must be 1")
    stage = state.get("stage")
    if stage not in STAGES:
        return [*failures, f"stage must be one of: {', '.join(STAGES)}"]
    stage_index = STAGES.index(stage)

    snapshot = state.get("snapshot")
    if not isinstance(snapshot, dict):
        failures.append("snapshot evidence is required")
    else:
        commit = snapshot.get("commit")
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
            failures.append("snapshot.commit must be a full 40-character Git SHA")
        for field in ("tag", "reference_branch", "reference_worktree"):
            if not _resolved(snapshot.get(field)):
                failures.append(f"snapshot.{field} is required")
        if snapshot.get("verified") is not True:
            failures.append("snapshot.verified must be true")

    strategy = state.get("strategy")
    if stage_index >= STAGES.index("strategy"):
        if not isinstance(strategy, dict):
            failures.append("strategy evidence is required")
        else:
            strategy_type = strategy.get("type")
            if strategy_type not in {"incremental", "rebuild"}:
                failures.append("strategy.type must be incremental or rebuild")
            if not _resolved(strategy.get("rationale")):
                failures.append("strategy.rationale is required")
            if strategy_type == "rebuild":
                if strategy.get("approved_by_user") is not True:
                    failures.append("rebuild strategy requires explicit user approval")
                if not _resolved(strategy.get("approval_evidence")):
                    failures.append("rebuild strategy approval evidence is required")

    baseline = state.get("baseline")
    if stage_index >= STAGES.index("baseline"):
        if not isinstance(baseline, dict):
            failures.append("baseline evidence is required")
        else:
            if not _resolved(baseline.get("behavior_inventory")):
                failures.append("baseline.behavior_inventory is required")
            if not _nonempty_list(baseline.get("parity_commands")):
                failures.append("baseline.parity_commands must contain executable commands")
            if baseline.get("gherkin_executable") is True and not _resolved(
                baseline.get("gherkin_command")
            ):
                failures.append("executable Gherkin requires baseline.gherkin_command")

    increment = state.get("increment")
    if stage_index >= STAGES.index("implementation"):
        if not isinstance(increment, dict):
            failures.append("increment evidence is required")
        else:
            if not _resolved(increment.get("id")):
                failures.append("increment.id is required")
            if not _nonempty_list(increment.get("allowed_paths")):
                failures.append("increment.allowed_paths must be non-empty")
            if not _nonempty_list(increment.get("verification_commands")):
                failures.append("increment.verification_commands must be non-empty")
            if not _resolved(increment.get("rollback_command")):
                failures.append("increment.rollback_command is required")

    cutover = state.get("cutover")
    if stage_index >= STAGES.index("cutover"):
        if not isinstance(cutover, dict):
            failures.append("cutover evidence is required")
        else:
            if cutover.get("verification_status") != "PASS":
                failures.append("cutover.verification_status must be PASS")
            if cutover.get("data_reconciliation") not in {"PASS", "NOT_REQUIRED"}:
                failures.append("cutover.data_reconciliation must be PASS or NOT_REQUIRED")
            if cutover.get("rollback_rehearsed") is not True:
                failures.append("cutover.rollback_rehearsed must be true")
            for field in (
                "rollback_evidence",
                "monitoring_window",
                "monitoring_owner",
                "approval_evidence",
            ):
                if not _resolved(cutover.get(field)):
                    failures.append(f"cutover.{field} is required")
            if cutover.get("approved_by_user") is not True:
                failures.append("cutover requires explicit user approval")
    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--state",
        type=Path,
        default=Path("refactor-state.json"),
        help="Refactor state file. Defaults to refactor-state.json.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    path = args.state if args.state.is_absolute() else Path.cwd() / args.state
    failures = validate_state(path)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Refactor state: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
