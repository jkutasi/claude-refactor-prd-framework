# Codex Project Instructions

Read and follow [WORKFLOW.md](WORKFLOW.md) and
[REFACTOR_WORKFLOW.md](REFACTOR_WORKFLOW.md). The refactor rules may not override
the shared workflow.

Only GPT-5.6 Sol or Claude Fable 5 may orchestrate. When this repository is opened
with another model, operate only as a bounded worker and do not approve completion.
This file does not select Sol automatically; establish the active orchestrator under
the authority rules in `WORKFLOW.md`.

Before changing files:

1. Classify the change as normal or high-risk using `workflow.config.json`.
2. Apply the provider data policy.
3. State acceptance criteria and verification commands.

Before delivery, run:

```text
python scripts/gate_check.py --change-id <id> --orchestrator sol
```

Use `--orchestrator fable` only when Claude Fable 5 is the active orchestrator.
