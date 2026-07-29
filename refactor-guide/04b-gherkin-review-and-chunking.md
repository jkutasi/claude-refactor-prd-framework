# Step 4b: Approve Behavior and Bind Executable Checks

## User Decisions

Classify each observed behavior:

- `PRESERVE`: retain it.
- `CORRECT`: replace a defect with approved behavior.
- `DROP`: intentionally remove it.
- `UNKNOWN`: collect more evidence.

`CORRECT` and `DROP` require explicit user approval recorded beside the behavior.
High-risk behavior decisions also require independent frontier review.

## Executable Parity

Map intended behaviors to commands that actually execute:

- unit, integration, contract, browser, migration, or smoke tests;
- controlled before/after probes;
- data reconciliation queries;
- operational log or metric checks.

Gherkin counts as executable only when the state file records a runner command and
the corresponding step bindings exist. Otherwise it remains useful specification.

Update the behavior coverage matrix with the behavior ID, decision, increment,
executable command, result, confidence, and approval evidence.

Set `refactor-state.json` to `baseline`, provide the inventory path and at least one
parity command, then run the state checker.

Next: [Step 5](05-bootstrap-rebuild.md)
