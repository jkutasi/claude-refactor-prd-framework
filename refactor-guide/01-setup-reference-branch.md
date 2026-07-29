# Step 1: Preserve the Baseline

## Outcome

Create an immutable recovery point and a verified read-only worktree before changing
behavior.

## Record the Snapshot

Start from a clean working tree. Record the full commit SHA, create an annotated tag,
and push the tag/reference branch if the remote is part of the recovery plan.

```text
git status --short
git rev-parse HEAD
git tag -a refactor/baseline-YYYY-MM-DD -m "Refactor baseline"
git branch reference/old-code
git worktree add ../project-reference reference/old-code
git worktree list
```

Do not run these examples blindly. Resolve and verify the intended repository,
branch, tag, and absolute worktree path first.

## Verify Read-Only Reference

- The recorded commit matches the tag and reference branch.
- The worktree contains the expected application and test files.
- No writer owns the reference worktree.
- Recovery from the snapshot has been demonstrated safely.

Copy `refactor-state.example.json` to `refactor-state.json`, set `stage` to
`snapshot`, complete the snapshot fields, then run:

```text
python scripts/check_refactor_state.py
```

## Working Strategy

Do not create a rebuild branch yet. Step 3 decides the strategy.

- Incremental work will use a branch derived from the existing code. It is not a
  clean-room branch.
- A full rebuild needs explicit user approval and a separate worktree/rollback plan.

Next: [Step 2](02-codebase-assessment.md)
