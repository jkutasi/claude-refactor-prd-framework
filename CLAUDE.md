# Claude Project Instructions

Read and follow [WORKFLOW.md](WORKFLOW.md) and
[REFACTOR_WORKFLOW.md](REFACTOR_WORKFLOW.md). The refactor rules may not override
the shared workflow.

The default orchestrator is Claude Fable 5. Sonnet and Haiku are workers only.
Do not recreate the retired phase-based QA workflow.

Before changing files:

1. Classify the change as normal or high-risk using `workflow.config.json`.
2. Apply the provider data policy.
3. State acceptance criteria and verification commands.

Before delivery, run:

```text
python scripts/gate_check.py --change-id <id> --orchestrator fable
```

Use `--orchestrator sol` only when GPT-5.6 Sol is the active orchestrator.
