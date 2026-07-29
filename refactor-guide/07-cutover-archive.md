# Step 7: Cut Over, Monitor, and Archive

Cutover is high-risk. Use `cutover-templates/CUTOVER-CHECKLIST-TEMPLATE.md`.

## Preconditions

- intended behaviors are accounted for;
- executable parity and project checks pass;
- approved corrections/removals are recorded;
- data reconciliation passes or is not applicable;
- deployment and smoke checks are defined;
- rollback is rehearsed in a safe environment;
- monitoring window and owner are recorded;
- the user explicitly approves cutover.

Set `refactor-state.json` to `cutover` and run the state checker. Independent
frontier sign-off must bind to the exact diff and raw evidence.

## Execution

Follow the project-specific cutover plan. Stop on unexpected state. Failed deploy,
smoke, parity, reconciliation, or critical monitoring triggers rollback unless the
user explicitly directs otherwise.

Do not remove a worktree, branch, migration path, compatibility layer, or archive
until its exact target is resolved and verified. Prefer recoverable moves and keep
the immutable snapshot/reference branch.

## Monitoring and Completion

Monitor for the recorded window. Compare errors, latency, data integrity, business
signals, and user-reported behavior with the baseline. Close the refactor only after
monitoring passes.

Archive temporary assessment and planning artifacts when useful, but keep durable
behavior decisions, migrations, rollback evidence, and high-risk review records.
