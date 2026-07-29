# Behavior-to-Increment Map — {PROJECT_NAME}

| Behavior ID | Decision | Increment | Specification File | Executable Command | Status |
|---|---|---|---|---|---|
| B-001 | PRESERVE | R-001 | {path/NONE} | {command/NONE} | {planned/passing} |

## Rules

- Map every intended behavior to exactly one owning increment.
- Record cross-increment dependencies explicitly.
- A `.feature` file without a working runner and bindings is specification, not a
  passing test.
- `CORRECT` and `DROP` require user approval evidence.
- UNKNOWN behavior stays unimplemented until evidence resolves it.
