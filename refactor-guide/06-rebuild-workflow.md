# Step 6: Rebuild Workflow

> Part of the [Refactor Guide](INDEX.md). Load only this file when rebuilding slice by slice.

---

## Purpose

Each slice follows the standard Get Started Phases A-J workflow (see `getting-started/04-per-slice-workflow.md`). The A-J workflow is UNCHANGED. The refactor adds context, not new phases.

This file documents the small additions that layer on top of the standard workflow during a refactor rebuild.

---

## The Standard Workflow Is the Workflow

Phases A through J are the same as any Get Started project:

- **Phase A** — CTO plans the slice
- **Phase B** — QA Lead writes test specs (Gherkin scenarios)
- **Phase C** — Dev implements
- **Phase D-I** — Review, testing, refinement
- **Phase J** — Gate check, slice completion

Do not invent new phases. Do not skip phases. The refactor rebuild succeeds because it uses the same disciplined workflow as a greenfield project.

---

## Refactor-Specific Additions

The following additions layer onto the standard workflow at specific points:

### Before Phase A: Read Old Code

Before the CTO begins planning a slice, read the relevant old code from the reference branch to understand context for this slice.

- Open the reference branch worktree (path is in CLAUDE.md refactor addendum)
- Read the files that correspond to the features being rebuilt in this slice
- Understand what the old code does, how it handles edge cases, what its dependencies are
- This is READ-ONLY. Never modify the reference branch.

The purpose is context, not copying. The rebuild should produce better code, not a clone.

### During Phase B: Start from Chunked Per-Slice Gherkin

Use the **chunked per-slice Gherkin** from Step 4 Pass 2 as the starting point for test specs in this slice.

- The per-slice `.feature` files in `features/` contain scenarios already scoped to this slice (produced during Step 4 Pass 2 chunking)
- Pull the scenarios from the relevant `features/slice-NNN-*.feature` file into the QA Lead's Phase B work
- The QA Lead may refine, split, merge, or rewrite these scenarios — the extraction is a starting point, not a locked spec
- If the user flagged bugs during Gherkin extraction (Step 4), the corrected behavior is already reflected in the chunked scenarios
- Do NOT use the broad behavior spec (`refactor/gherkin/broad-behavior-spec.md`) directly — that is the raw extraction output before chunking

### After Phase J: Comparative Metrics Check

After a slice passes its Phase J gate, record comparative metrics — old vs. new:

- **File lengths** — are the new files shorter or more focused?
- **Test coverage** — does the new code have better coverage?
- **Coupling** — are dependencies cleaner?

Record these in `refactor/comparative-metrics.md` (use `COMPARATIVE-METRICS-TEMPLATE.md` from `refactor/templates/`). The format is per-slice: which slice, what was measured, old value, new value.

### After Phase J: Update Behavior Coverage Matrix

After each slice completes, update `refactor/behavior-coverage-matrix.md`:

- Mark which behaviors from the broad behavior spec are now covered by the rebuilt code
- Note any behaviors that were intentionally dropped (with the user's approval)
- Note any new behaviors added that did not exist in the old codebase

---

## What the Matrix Tracks

The Behavior Coverage Matrix tracks CORRECT behaviors, not old behaviors blindly. If the user flagged a bug during Gherkin extraction (Step 4), the corrected behavior is what gets tracked. The matrix answers the question: "Have we rebuilt everything the user wants in the new system?"

This means:

- Old bugs that were flagged are tracked as their corrected versions
- Features the user chose to drop are marked as intentionally excluded
- New features the user requested are tracked alongside the old ones

---

## Refactor Gate Check

In addition to the standard Get Started `gate_check.py` (which validates Phases A-J), the following refactor-specific checks must pass after each slice's Phase J:

1. **Comparative metrics recorded** — `refactor/comparative-metrics.md` has an entry for this slice
2. **Behavior coverage updated** — `refactor/behavior-coverage-matrix.md` has been updated to reflect behaviors covered by this slice
3. **Per-slice Gherkin accounted for** — every scenario in this slice's `features/slice-NNN-*.feature` file either passes or has been explicitly deferred with justification

These checks are manual (the CTO verifies before marking the slice complete). If any check fails, the slice is not complete — go back and address the gap before proceeding.

At rebuild completion (before cutover):

4. **Behavior Coverage Matrix = 100%** — all intended behaviors covered
5. **No unreviewed Gherkin** — every extracted scenario has been classified (CORRECT/WRONG/DROP)

---

## Quality Verification

Standard QA already handles quality verification through the Get Started workflow:

- **Peer Review** — every slice gets peer reviewed
- **QA Swarm** — test coverage validation
- **Whiskey Team** — adversarial review
- **Red Team** — security and edge case review

These are not refactor-specific. They are the standard Get Started quality gates. The only refactor-specific additions are the comparative metrics and behavior coverage tracking described above.

---

## Outcome

After each slice:

- The slice has passed all standard A-J gates
- Comparative metrics are recorded in `refactor/comparative-metrics.md`
- Behavior Coverage Matrix is updated in `refactor/behavior-coverage-matrix.md`
- The rebuild progresses one slice at a time until all slices are complete, then proceed to Step 7
