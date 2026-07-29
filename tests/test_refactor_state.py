from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from check_refactor_state import validate_state  # noqa: E402


class RefactorStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = {
            "version": 1,
            "stage": "complete",
            "snapshot": {
                "commit": "a" * 40,
                "tag": "refactor/baseline-2026-07-29",
                "reference_branch": "reference/old-code",
                "reference_worktree": "../reference-old-code",
                "verified": True,
            },
            "strategy": {
                "type": "incremental",
                "rationale": "Small reversible increments reduce migration risk.",
                "approved_by_user": False,
                "approval_evidence": None,
            },
            "baseline": {
                "behavior_inventory": "refactor/behavior-inventory.md",
                "parity_commands": ["python -m unittest"],
                "gherkin_executable": False,
                "gherkin_command": None,
            },
            "increment": {
                "id": "extract-auth-boundary",
                "allowed_paths": ["src/auth", "tests/auth"],
                "verification_commands": ["python -m unittest tests.auth"],
                "rollback_command": f"git revert {'b' * 40}",
            },
            "cutover": {
                "verification_status": "PASS",
                "data_reconciliation": "NOT_REQUIRED",
                "rollback_rehearsed": True,
                "rollback_evidence": "Revert tested in the staging worktree.",
                "monitoring_window": "24 hours",
                "monitoring_owner": "project owner",
                "approved_by_user": True,
                "approval_evidence": "Approval recorded in change request 42.",
            },
        }

    def _validate(self, state: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "refactor-state.json"
            path.write_text(json.dumps(state), encoding="utf-8")
            return validate_state(path)

    def test_missing_state_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            failures = validate_state(Path(temp) / "missing.json")
        self.assertTrue(any("not found" in item for item in failures))

    def test_snapshot_stage_requires_verified_snapshot(self) -> None:
        state = {"version": 1, "stage": "snapshot", "snapshot": {}}
        failures = self._validate(state)
        self.assertTrue(any("snapshot.commit" in item for item in failures))
        self.assertTrue(any("snapshot.verified" in item for item in failures))

    def test_example_placeholders_do_not_pass_snapshot_gate(self) -> None:
        example = (
            Path(__file__).resolve().parents[1] / "refactor-state.example.json"
        )
        failures = validate_state(example)
        self.assertTrue(any("snapshot.commit" in item for item in failures))
        self.assertTrue(any("snapshot.verified" in item for item in failures))

    def test_rebuild_requires_explicit_approval(self) -> None:
        state = copy.deepcopy(self.state)
        state["stage"] = "strategy"
        state["strategy"]["type"] = "rebuild"
        state["strategy"]["approved_by_user"] = False
        state["strategy"]["approval_evidence"] = None
        failures = self._validate(state)
        self.assertTrue(any("explicit user approval" in item for item in failures))
        self.assertTrue(any("approval evidence" in item for item in failures))

    def test_baseline_requires_executable_parity_commands(self) -> None:
        state = copy.deepcopy(self.state)
        state["stage"] = "baseline"
        state["baseline"]["parity_commands"] = []
        failures = self._validate(state)
        self.assertTrue(any("parity_commands" in item for item in failures))

    def test_executable_gherkin_requires_runner_command(self) -> None:
        state = copy.deepcopy(self.state)
        state["stage"] = "baseline"
        state["baseline"]["gherkin_executable"] = True
        state["baseline"]["gherkin_command"] = None
        failures = self._validate(state)
        self.assertTrue(any("gherkin_command" in item for item in failures))

    def test_increment_requires_rollback(self) -> None:
        state = copy.deepcopy(self.state)
        state["stage"] = "implementation"
        state["increment"]["rollback_command"] = None
        failures = self._validate(state)
        self.assertTrue(any("rollback_command" in item for item in failures))

    def test_git_reflog_syntax_is_valid_evidence(self) -> None:
        state = copy.deepcopy(self.state)
        state["increment"]["rollback_command"] = "git checkout stash@{0}"
        self.assertEqual(self._validate(state), [])

    def test_cutover_requires_approval_and_rollback_evidence(self) -> None:
        state = copy.deepcopy(self.state)
        state["stage"] = "cutover"
        state["cutover"]["approved_by_user"] = False
        state["cutover"]["rollback_evidence"] = None
        failures = self._validate(state)
        self.assertTrue(any("explicit user approval" in item for item in failures))
        self.assertTrue(any("rollback_evidence" in item for item in failures))

    def test_complete_state_passes(self) -> None:
        self.assertEqual(self._validate(self.state), [])


if __name__ == "__main__":
    unittest.main()
