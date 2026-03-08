# Step 7: Cutover & Archive

> Part of the [Refactor Guide](INDEX.md). Load only this file when the rebuild is complete.

---

## Purpose

The rebuild is done. This step verifies completeness, archives the refactor scaffolding, and transitions the project to a standard Get Started framework project. After cutover, Claude never reads refactor context again in future sessions.

Uses template: `CUTOVER-CHECKLIST-TEMPLATE.md`

---

## Cutover Criteria

ALL of the following must be true before cutover proceeds:

1. **All slices complete** — every slice in the rebuild has passed its Get Started A-J gates
2. **Behavior Coverage Matrix complete** — all intended behaviors are covered (checked in `refactor/behavior-coverage-matrix.md`)
3. **All Gherkin scenarios pass** — every scenario in the test suite passes
4. **User acceptance testing done** — the user has tested the rebuilt application and approved it
5. **Comparative metrics show improvement** — the new code is measurably better than the old: smaller files, better test coverage, less coupling (checked in `refactor/comparative-metrics.md`)
6. **Data migration complete (if applicable)** — if the Risk Assessment identified Medium/High data migration risk, the data migration slice has been executed and production data is compatible with the rebuilt schema

Do not proceed with cutover until all criteria are satisfied.

---

## Archive Steps

Once all cutover criteria are met, execute these steps in order:

### 1. Remove CLAUDE.md Refactor Addendum

Remove the `## REFACTOR ADDENDUM (TEMPORARY)` section from CLAUDE.md. This removes the reference branch pointer, the Article 20h override, and the comparative metrics and behavior coverage tracking instructions. Claude will no longer see refactor context in future sessions.

### 2. Move Refactor Scaffolding to Archive

Move all refactor-specific artifacts to `archive/refactor/`:

- `refactor/assessment/` — inventory, feature map, dependency graph, debt catalog, risk assessment
- `refactor/decomposition/` — feature-to-slice map, slice dependency order
- `refactor/gherkin/broad-behavior-spec.md` — the broad extraction (per-slice Gherkin stays in `features/`)
- `refactor/templates/` — framework templates deployed during Step 1.5
- `refactor/behavior-coverage-matrix.md`
- `refactor/comparative-metrics.md`
- `REFACTOR_CONFIG.md`

These are historical records. They document what was assessed, how the rebuild was planned, and what was tracked. They are not read during normal development.

### 3. Remove Reference Branch Worktree

```bash
git worktree remove {PATH_TO_WORKTREE}
```

The worktree is no longer needed. Removing it cleans up the working directory.

### 4. Keep the Reference Branch

Keep the `reference/old-code` branch. This is the strong default — do not delete it.

The branch serves as a historical record of what the old code looked like before the rebuild. It costs nothing to keep and provides value if anyone ever needs to understand the old system's behavior or trace a decision back to the original code.

### 5. Project Is Now Standard

The project is now a standard Get Started framework project. No special rules, no overrides, no refactor context. Future sessions follow the normal Get Started workflow.

---

## What Stays After Cutover

- **Standard CLAUDE.md** — without the refactor addendum
- **All Get Started contracts, skills, templates** — the framework that governs the project
- **Rebuilt code in feature-based folders** — the new codebase
- **Gherkin feature files in `features/`** — these are the test suite, they are permanent
- **All review artifacts from the rebuild** — peer review, QA swarm, Whiskey Team, Red Team records
- **`archive/refactor/`** — historical record of the refactor journey

---

## What's Gone After Cutover

- **CLAUDE.md refactor addendum** — removed, no longer needed
- **Active refactor scaffolding** — moved to `archive/refactor/`, no longer in active paths
- **Reference branch worktree** — removed from the filesystem
- **Refactor context in future sessions** — Claude never reads refactor-specific files again during normal development

---

## Abort / Partial Rollback

If the rebuild stalls or fails mid-stream, these are the options:

### Option 1: Pause and Resume Later

The rebuild branch preserves all completed slices. You can stop at any point and resume later. The reference branch, assessment artifacts, decomposition, and Gherkin files all persist. No work is lost.

### Option 2: Ship Partial Rebuild

If some slices are complete and provide standalone value, you can cutover with a partial rebuild:

1. Update the Behavior Coverage Matrix to reflect which behaviors are covered and which are deferred
2. Create follow-up slices for the uncovered behaviors (these become normal Get Started slices)
3. Run the standard cutover process for the completed portion
4. The deferred behaviors remain as planned work in the backlog

### Option 3: Abort and Revert to Old Code

If the rebuild is fundamentally wrong (bad decomposition, wrong architecture choice, misunderstood requirements):

1. Checkout the `reference/old-code` branch
2. Delete the `rebuild/main` branch
3. Remove the worktree
4. Archive whatever assessment/decomposition artifacts are salvageable to `archive/refactor/`
5. The old code is fully intact — the reference branch was never modified

### Re-Decomposition Mid-Rebuild

If slices 1-10 are done but the remaining decomposition is wrong:

1. Freeze the completed slices (they stay)
2. Re-run Step 3 (Feature Decomposition) for the remaining features only
3. Re-run Step 4 Pass 2 (Gherkin Chunking) for the new slices only
4. Continue rebuilding from the new slice plan

This is expected for large rebuilds. Discovery during implementation often reveals that the original decomposition needs adjustment.

---

## Outcome

The refactor journey is complete. The project has been rebuilt from scratch using the Get Started framework's disciplined slice-by-slice workflow. The old code is preserved as a historical reference. The new code is clean, tested, and governed by the same contracts and quality gates as any Get Started project.

---

**Previous step:** [Step 6: Rebuild Workflow](06-rebuild-workflow.md)
