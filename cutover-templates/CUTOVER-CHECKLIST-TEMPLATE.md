# Cutover Checklist — {PROJECT_NAME}

Cutover is high-risk and requires independent non-author frontier sign-off.

## Preconditions

- [ ] Original requirements and intended behaviors are accounted for.
- [ ] All applicable deterministic checks pass.
- [ ] Executable parity commands pass.
- [ ] CORRECT and DROP decisions have explicit user approval.
- [ ] Data reconciliation is PASS or NOT_REQUIRED.
- [ ] Deployment and smoke commands are recorded.
- [ ] Rollback has been rehearsed safely; evidence: {reference}.
- [ ] Monitoring window: {duration}; owner: {person/role}.
- [ ] User approved cutover; evidence: {reference}.
- [ ] Exact diff has independent frontier approval.

## Execution

| Order | Action | Command/Owner | Expected Result | Stop/Rollback Trigger |
|---:|---|---|---|---|
| 1 | {action} | {command/owner} | {result} | {trigger} |

Resolve and verify every destructive target before execution. Do not use unresolved
variables, broad directories, or implicit branch/worktree names.

## Monitoring

- [ ] Deploy/smoke checks pass.
- [ ] Critical logs and alerts remain clear.
- [ ] Data integrity checks pass.
- [ ] Business and user signals match expectations.

Any failed critical check triggers rollback unless the user explicitly directs
otherwise.

## Archive

- [ ] Keep the immutable tag/reference branch.
- [ ] Keep durable behavior, migration, rollback, and review records.
- [ ] Archive temporary analysis only after monitoring passes.
- [ ] Remove a worktree only after its exact path and clean state are verified.
