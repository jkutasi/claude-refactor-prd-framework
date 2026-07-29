# Refactor Guide

Read `WORKFLOW.md` and `REFACTOR_WORKFLOW.md` first. Load only the current step.

| Step | File | Outcome |
|---|---|---|
| 1 | [01-setup-reference-branch.md](01-setup-reference-branch.md) | Immutable snapshot and verified reference worktree |
| 2 | [02-codebase-assessment.md](02-codebase-assessment.md) | Evidence-based inventory, dependency, debt, and risk maps |
| 3 | [03-feature-decomposition.md](03-feature-decomposition.md) | User-approved strategy and reversible increment order |
| 4a | [04a-gherkin-broad-extraction.md](04a-gherkin-broad-extraction.md) | Observed behavior inventory with confidence and sources |
| 4b | [04b-gherkin-review-and-chunking.md](04b-gherkin-review-and-chunking.md) | User decisions and executable parity mapping |
| 5 | [05-bootstrap-rebuild.md](05-bootstrap-rebuild.md) | Safe working branch/worktree and configured checks |
| 6 | [06-rebuild-workflow.md](06-rebuild-workflow.md) | Small verified refactor increments |
| 7 | [07-cutover-archive.md](07-cutover-archive.md) | Approved cutover, monitoring, rollback, and archive |

The filenames for steps 5 and 6 are retained for compatibility. Their workflow is
incremental-first; a full rebuild is never assumed.
