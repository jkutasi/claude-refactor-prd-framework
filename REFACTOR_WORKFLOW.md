# Refactor Workflow

This file adds refactor-specific rules to `WORKFLOW.md`. It cannot override the
shared model, privacy, risk, review, handoff, budget, or rollback policy.

## 1. Required State

Active refactors keep `refactor-state.json` at the repository root. Copy
`refactor-state.example.json`, replace every example value, and run:

```text
python scripts/check_refactor_state.py
```

The state advances only when the evidence for the declared stage passes.

## 2. Lifecycle

1. **Snapshot:** record the current commit and tag; create a verified, read-only
   reference worktree.
2. **Assess:** map features, dependencies, tests, data, operations, debt, and risk.
3. **Choose strategy:** incremental refactoring is the default. A full rebuild
   requires explicit user approval, rationale, failure modes, and rollback.
4. **Baseline behavior:** record intended behavior and executable parity commands.
   Gherkin is a specification unless a test runner executes its bindings.
5. **Implement increments:** use small path-bounded changes with an explicit
   rollback command and deterministic verification.
6. **Verify:** prove behavioral parity, approved changes, data reconciliation,
   operational readiness, and monitoring.
7. **Cut over and archive:** rehearse rollback, obtain user approval, execute the
   cutover, monitor, then archive temporary refactor artifacts.

## 3. Behavior Decisions

Observed behavior is evidence, not automatically a requirement.

- `PRESERVE`: retain the behavior.
- `CORRECT`: change a known defect; requires explicit user approval.
- `DROP`: intentionally remove behavior; requires explicit user approval.
- `UNKNOWN`: do not implement or remove until resolved.

Every decision identifies its source, confidence, owner, executable check if one
exists, and approving user statement where required.

## 4. Strategy

Prefer an incremental branch derived from the current code. Describe it accurately;
it is not a clean-room rebuild.

A full rebuild is high-risk. Do not create a clean/orphan rebuild branch or remove
existing code until the user approves the strategy and a safe, separate worktree
plan demonstrates recovery to the immutable snapshot.

## 5. High-Risk Refactor Work

In addition to shared triggers, treat these as high-risk:

- behavior correction or removal;
- authentication, permissions, money, private data, or cryptography;
- schema or data migration;
- public API or dependency-boundary change;
- branch, worktree, deployment, cutover, or archive operation;
- a full rebuild or irreversible replacement.

The other frontier model reviews original requirements, raw diff, raw verification,
data evidence, and rollback evidence. The non-author reviewer controls sign-off.

## 6. Cutover

Cutover requires:

- all applicable deterministic checks passing;
- intended behavior accounted for;
- executable parity checks passing;
- data reconciliation passing or recorded as not applicable;
- rollback rehearsed in a safe environment;
- monitoring window and owner recorded;
- explicit user approval.

Failure in verification, deployment, smoke checks, data reconciliation, or critical
runtime monitoring triggers rollback unless the user explicitly directs otherwise.
