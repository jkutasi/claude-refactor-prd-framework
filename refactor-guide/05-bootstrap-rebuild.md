# Step 5: Prepare the Refactor Workspace

The filename is retained for compatibility; a full rebuild is not assumed.

## Incremental Strategy

Create a normal working branch or separate worktree derived from the existing code.
Describe it accurately as old-code-derived. Confirm the baseline reference remains
read-only and assign one writer per worktree.

Customize:

- `workflow.config.json` checks, risk patterns, limits, and provider policy;
- `refactor-state.json` current increment and rollback command;
- project-native test, lint, build, migration, smoke, and monitoring commands.

Run every command locally before relying on CI.

## Full-Rebuild Strategy

Do not create an orphan branch or remove existing files from this guide. Use a
project-specific high-risk plan that has:

- explicit user approval;
- separate verified worktree;
- coexistence and data-migration plan;
- rollback to the immutable snapshot;
- independent frontier plan approval.

## Ready Check

The workspace is ready when ownership is non-overlapping, the reference is immutable,
checks execute, refactor state passes, and rollback has been demonstrated.

Next: [Step 6](06-rebuild-workflow.md)
