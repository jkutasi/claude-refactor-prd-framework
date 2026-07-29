from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from check_refactor_contract import failures  # noqa: E402


class RefactorContractTests(unittest.TestCase):
    def test_current_template_passes(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        self.assertEqual(failures(repo_root), [])

    def test_retired_path_is_detected(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(dir=repo_root) as temp:
            retired = Path(temp) / "contract-templates"
            retired.mkdir()
            problems = failures(Path(temp), enforce_inventory=False)
        self.assertTrue(
            any("retired path still exists: contract-templates" in item for item in problems)
        )

    def test_unclassified_path_is_detected_in_template_mode(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        unexpected = repo_root / "unexpected-template-directory"
        try:
            unexpected.mkdir()
            problems = failures(repo_root, enforce_inventory=True)
        finally:
            unexpected.rmdir()
        self.assertTrue(any("unclassified top-level path" in item for item in problems))

    def test_project_mode_allows_application_directories(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        application = repo_root / "application-source"
        state = repo_root / "refactor-state.json"
        try:
            application.mkdir()
            state.write_text("{}\n", encoding="utf-8")
            problems = failures(repo_root)
        finally:
            state.unlink(missing_ok=True)
            application.rmdir()
        self.assertFalse(any("application-source" in item for item in problems))

    def test_template_mode_allows_gitignored_local_file(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        local_log = repo_root / "refactor-contract-local-test.log"
        try:
            local_log.write_text("local only\n", encoding="utf-8")
            problems = failures(repo_root, enforce_inventory=True)
        finally:
            local_log.unlink(missing_ok=True)
        self.assertFalse(any(local_log.name in item for item in problems))

    def test_project_mode_does_not_scan_project_readme_or_workflows(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflow = root / ".github" / "workflows" / "project.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text("# Phase A uses Gemini\n", encoding="utf-8")
            (root / "README.md").write_text(
                "This application integrates with Gemini.\n",
                encoding="utf-8",
            )
            problems = failures(root, enforce_inventory=False)
        self.assertFalse(any("README.md: contains" in item for item in problems))
        self.assertFalse(any("project.yml: contains" in item for item in problems))


if __name__ == "__main__":
    unittest.main()
