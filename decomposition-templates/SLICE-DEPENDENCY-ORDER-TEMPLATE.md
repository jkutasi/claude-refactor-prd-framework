# Increment Dependency Order — {PROJECT_NAME}

> Filename retained for compatibility.

| Order | Increment | Depends On | Can Run in Parallel | Risk | Reason |
|---:|---|---|---|---|---|
| 1 | R-001 | None | {IDs/No} | {normal/high} | {reason} |

## Dependency Rules

- Prefer vertical, independently verifiable increments.
- Separate schema expansion, data movement, application switching, and cleanup.
- Do not run parallel writers on overlapping paths or migration state.
- High-risk predecessors must have independent frontier sign-off before dependents
  integrate.

## Recovery Points

| After Increment | Recovery Reference | Rollback Command | Demonstrated |
|---|---|---|---|
| R-001 | {commit/flag/deploy} | {command} | {yes/evidence} |
