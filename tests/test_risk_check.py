from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from risk_check import (  # noqa: E402
    MAX_UNTRACKED_REVIEW_BYTES,
    canonical_diff_sha256,
    changed_files,
    detect_risk,
)
from workflow_config import load_config  # noqa: E402


class RiskCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.config = load_config(cls.repo_root)

    def test_auth_path_forces_high_risk(self) -> None:
        findings = detect_risk(
            ["src/auth/session.py"],
            "",
            self.config,
        )
        self.assertTrue(any(item.source == "path" for item in findings))

    def test_destructive_sql_forces_high_risk(self) -> None:
        findings = detect_risk(
            ["src/reporting/query.py"],
            "+ cursor.execute('DROP TABLE accounts')",
            self.config,
        )
        self.assertTrue(any(item.trigger == "destructive SQL" for item in findings))

    def test_routine_file_is_normal(self) -> None:
        findings = detect_risk(
            ["src/widgets/format_title.py"],
            "+ return title.strip()",
            self.config,
        )
        self.assertEqual(findings, [])

    def test_lowercase_words_do_not_trigger_behavior_decision(self) -> None:
        findings = detect_risk(
            ["src/widgets/format_title.py"],
            "+ # correct the layout and drop empty values",
            self.config,
        )
        self.assertFalse(
            any(item.trigger == "behavior correction or removal" for item in findings)
        )

    def test_uppercase_behavior_decision_is_high_risk(self) -> None:
        findings = detect_risk(
            ["refactor/behavior-inventory.md"],
            "+ Decision: DROP undocumented export",
            self.config,
        )
        self.assertTrue(
            any(item.trigger == "behavior correction or removal" for item in findings)
        )

    def test_routine_refactor_state_update_is_not_high_risk_by_path(self) -> None:
        findings = detect_risk(
            ["refactor-state.json"],
            '+ "stage": "implementation"',
            self.config,
        )
        self.assertEqual(findings, [])

    def test_rebuild_state_is_high_risk_by_content(self) -> None:
        findings = detect_risk(
            ["refactor-state.json"],
            '+ "type": "rebuild"',
            self.config,
        )
        self.assertTrue(
            any(
                item.trigger == "refactor branch, worktree, or cutover operation"
                for item in findings
            )
        )

    def test_review_record_is_excluded_from_diff_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(
                ["git", "config", "user.email", "test@example.com"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Test"],
                cwd=root,
                check=True,
            )
            source = root / "app.py"
            source.write_text("value = 1\n", encoding="utf-8")
            subprocess.run(["git", "add", "app.py"], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-qm", "base"],
                cwd=root,
                check=True,
            )
            source.write_text("value = 2\n", encoding="utf-8")
            review = root / "reviews" / "change.json"
            review.parent.mkdir()
            review.write_text('{"diff_sha256":"first"}\n', encoding="utf-8")
            files = changed_files(root)
            first = canonical_diff_sha256(
                root,
                files,
                excluded_files={"reviews/change.json"},
            )
            review.write_text('{"diff_sha256":"second"}\n', encoding="utf-8")
            second = canonical_diff_sha256(
                root,
                changed_files(root),
                excluded_files={"reviews/change.json"},
            )
        self.assertEqual(first, second)

    def test_oversized_untracked_files_stop_review(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            boundary = root / "boundary.bin"
            boundary.write_bytes(b"x" * MAX_UNTRACKED_REVIEW_BYTES)
            boundary_hash = canonical_diff_sha256(root, changed_files(root))
            self.assertEqual(len(boundary_hash), 64)

            first = root / "first.bin"
            second = root / "second.bin"
            first.write_bytes(b"x" * (MAX_UNTRACKED_REVIEW_BYTES + 1))
            second.write_bytes(b"x" * (MAX_UNTRACKED_REVIEW_BYTES + 2))
            with self.assertRaises(RuntimeError) as context:
                canonical_diff_sha256(root, changed_files(root))

        message = str(context.exception)
        self.assertIn("first.bin", message)
        self.assertIn("second.bin", message)
        self.assertNotIn("boundary.bin", message)


if __name__ == "__main__":
    unittest.main()
