# Step 6: Implement Reversible Increments

The filename is retained for compatibility. Use the same lean normal/high-risk
workflow for each increment.

## Before Editing

- select one bounded increment;
- read the relevant reference code and evidence;
- confirm intended behavior and approved changes;
- set allowed paths and one writer per worktree;
- record verification and rollback commands;
- classify risk mechanically and by judgment.

## Normal Increment

Implement, run configured deterministic checks, compare results with acceptance
criteria and the behavior matrix, then deliver. Do not create an AI-review artifact.

## High-Risk Increment

The other frontier model reviews the plan. After implementation, run all normal and
targeted checks. The same non-author frontier reviewer controls exact-diff sign-off.
Unresolved disagreement goes to the user.

## Evidence

After each increment:

- run parity and regression commands;
- update behavior coverage;
- record data reconciliation if applicable;
- compare only metrics that matter to the project;
- demonstrate the rollback command safely;
- update `refactor-state.json`.

Metrics inform decisions; arbitrary file-count or line-count improvement is not a
completion requirement.

Next: [Step 7](07-cutover-archive.md)
