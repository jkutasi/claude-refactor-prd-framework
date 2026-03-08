# Cutover Checklist — {PROJECT_NAME}

> **Purpose:** Verify everything is complete before archiving refactor scaffolding. ALL items must be checked before proceeding with cutover.

## Pre-Cutover Gates

All must be true:

| Gate | Status | Evidence |
|------|--------|----------|
| All slices complete (passed Get Started A-J gates) | [ ] | gate_check.py PASS for all slices |
| Behavior Coverage Matrix = 100% | [ ] | refactor/behavior-coverage-matrix.md |
| All Gherkin scenarios pass | [ ] | Test suite output |
| User acceptance testing complete | [ ] | User confirmed |
| Comparative metrics show improvement | [ ] | refactor/comparative-metrics.md |
| Data migration complete (if applicable) | [ ] | Migration script tested, data verified |

## Cutover Steps

Execute in order:

### 1. Remove CLAUDE.md Refactor Addendum
- [ ] Open the project's `CLAUDE.md`
- [ ] Remove the `## REFACTOR ADDENDUM (TEMPORARY)` section entirely
- [ ] Verify CLAUDE.md reads as a standard Get Started contract

### 2. Archive Refactor Scaffolding
- [ ] Create `archive/refactor/` directory
- [ ] Move `refactor/assessment/` → `archive/refactor/assessment/`
- [ ] Move `refactor/decomposition/` → `archive/refactor/decomposition/`
- [ ] Move `refactor/gherkin/broad-behavior-spec.md` → `archive/refactor/`
- [ ] Move `refactor/templates/` → `archive/refactor/templates/`
- [ ] Move `refactor/behavior-coverage-matrix.md` → `archive/refactor/`
- [ ] Move `refactor/comparative-metrics.md` → `archive/refactor/`
- [ ] Move `REFACTOR_CONFIG.md` → `archive/refactor/`
- [ ] Remove empty `refactor/` directory

### 3. Remove Reference Branch Worktree
- [ ] Run: `git worktree remove {WORKTREE_PATH}`
- [ ] Verify worktree is removed: `git worktree list`

### 4. Keep Reference Branch
- [ ] Verify `reference/old-code` branch exists: `git branch -a`
- [ ] Do NOT delete this branch — it is the historical record

### 5. Final Verification
- [ ] Project runs correctly without any refactor scaffolding
- [ ] CLAUDE.md contains no refactor references
- [ ] No refactor-specific files outside `archive/refactor/`
- [ ] Standard Get Started gate_check.py passes
- [ ] Claude Code reads CLAUDE.md without encountering refactor context

## Post-Cutover

The project is now a standard Get Started framework project. Future development follows the standard Get Started per-slice workflow (Phases A-J). The refactor is complete.
