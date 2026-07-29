# Feature-to-Increment Map — {PROJECT_NAME}

> Filename retained for compatibility. An increment is a small, reversible refactor
> outcome; it is not tied to a legacy workflow phase.

| Increment | Outcome | Existing Paths | Allowed New/Changed Paths | Behaviors | Data Effect | Risk | Verification | Rollback |
|---|---|---|---|---|---|---|---|---|
| R-001 | {outcome} | {paths} | {paths} | {IDs} | {none/details} | {normal/high} | {commands} | {command} |

## Strategy

- Type: {incremental/rebuild}
- Rationale: {evidence}
- User approval required: {yes/no}
- Approval evidence: {reference}

## Behavior Decisions

| Behavior ID | Decision | Reason | User Approval | Executable Check |
|---|---|---|---|---|
| B-001 | PRESERVE | {reason} | N/A | {command} |

`CORRECT` and `DROP` decisions require explicit user approval.

## Boundaries

- One writer/worktree per active increment.
- Non-overlapping path ownership.
- Compatibility or feature-flag plan: {details}
- Dependencies that must land first: {IDs}
