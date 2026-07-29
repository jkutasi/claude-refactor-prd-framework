# Refactor Existing Project Template

A lean AI-assisted workflow for safely improving an existing software project.
It mirrors the model routing and risk controls in the New Project template while
adding assessment, behavior-parity, migration, rollback, and cutover discipline.

## Model Roles

| Model | Role |
|---|---|
| Claude Fable 5 | Default orchestrator |
| GPT-5.6 Sol | Alternate orchestrator and independent frontier reviewer |
| Claude Sonnet 5 | Bounded implementation worker |
| Claude Haiku 4.5 | Mechanically verifiable utility worker |

Only Fable or Sol may orchestrate. Normal changes use deterministic checks without
AI peer review. High-risk changes use the other non-author frontier model.

## Refactor Principles

- Preserve an immutable snapshot before changing behavior.
- Prefer small, reversible improvements to a full rebuild.
- A full rebuild requires explicit user approval and a demonstrated rollback plan.
- Extract observed behavior, but do not mistake written Gherkin for an executable test.
- Require user approval before correcting or dropping existing behavior.
- Verify behavior, data, operations, and rollback before cutover.

## Start Here

1. Read [WORKFLOW.md](WORKFLOW.md) for shared model, privacy, risk, and review rules.
2. Read [REFACTOR_WORKFLOW.md](REFACTOR_WORKFLOW.md) for the refactor lifecycle.
3. Follow [refactor-guide/INDEX.md](refactor-guide/INDEX.md) one step at a time.
4. Customize [workflow.config.json](workflow.config.json) and copy
   [refactor-state.example.json](refactor-state.example.json) to
   `refactor-state.json`.
5. Run:

```text
python scripts/gate_check.py --change-id <id> --orchestrator fable
```

Use `--orchestrator sol` when Sol is active.

## Useful Refactor Assets

- `assessment-templates/`: inventory, feature, dependency, debt, and risk analysis.
- `decomposition-templates/`: bounded increment mapping and dependency order.
- `gherkin-templates/`: optional human-readable behavior specifications.
- `regression-templates/`: behavior coverage and comparative evidence.
- `cutover-templates/`: high-risk cutover and rollback checklist.
- `.claude/settings.json`: wires the short session-start routing reminder.

## Safety Defaults

- Incremental refactoring is the default strategy.
- Cutover, data migration, auth, infrastructure, and behavior removal are high-risk.
- Missing refactor-state evidence fails closed.
- Provider approval and retention policy are checked before repository content is sent.
- A refusal stops for user review; it is not silently retried through another provider.
