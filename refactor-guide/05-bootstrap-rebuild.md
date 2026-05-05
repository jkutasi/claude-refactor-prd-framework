# Step 5: Bootstrap Rebuild

> Part of the [Refactor Guide](INDEX.md). Load only this file when bootstrapping the rebuild branch.

---

## Purpose

This step deploys the Get Started framework into the rebuild branch and runs Slice 0. The rebuild branch starts clean — the Get Started contracts, skills, and review templates are deployed here, and the planning phase outputs are filled in using the assessment and decomposition results from earlier steps.

---

## Deploy the Get Started Framework

Copy the following from the Get Started template into the rebuild branch:

- **Contracts** — all contract files (nuclear rules, workflow contracts, role contracts)
- **Skills** — all skill files for CTO, Dev, QA Lead, etc.
- **Review Templates** — consolidated review files (`reviews/slice-{N}.md`), peer review, QA swarm, Red Team templates

These are deployed as-is. The refactor does not modify the Get Started framework — it uses it.

---

## Fill In Planning Phase Outputs

The Get Started framework expects certain planning artifacts to exist before Slice 0 runs. During a refactor rebuild, these come from the assessment and decomposition work done in Steps 2-3:

| Planning Artifact | Source |
|---|---|
| **User Story (Step 1a)** | Comes from the assessment (Step 2) — what the old project does, restated as a user story |
| **Tech Stack (Step 1b)** | Same as the old project, or upgraded — the user decides |
| **MCP Integrations (Step 1c)** | Same as Get Started — search for MCPs, configure in `.claude/settings.local.json` |
| **Architecture (Step 1d)** | Comes from the assessment dependency graph and inventory (Step 2) — restated as workspace layout and data flow |
| **Vertical Slices (Step 1e)** | Come directly from the decomposition output (Step 3) — the feature-to-slice map and slice dependency order |
| **Plan Peer Review (Step 1f)** | Same as Get Started — mandatory. The full plan goes through 3+ model peer review before any code |

The user may adjust any of these. The assessment and decomposition provide the starting point, not a locked-in plan.

---

## Run Slice 0 Bootstrap

Run Slice 0 Bootstrap as normal (see `getting-started/03-slice-0-bootstrap.md`). This creates:

- **CLAUDE.md** — project intelligence file
- **Contracts** — confirmed and in place
- **Skills** — confirmed and in place
- **Infrastructure** — project scaffolding, folder structure, CI/CD baseline

Everything in Slice 0 follows the standard Get Started process. The only refactor-specific addition is the CLAUDE.md Refactor Addendum below.

---

## Append the CLAUDE.md Refactor Addendum

After Slice 0 completes, append the following temporary section to CLAUDE.md:

```markdown
## REFACTOR ADDENDUM (TEMPORARY — Archive after rebuild complete)

### Reference Branch
- Branch: `reference/old-code`
- Worktree path: {PATH}
- Access: READ-ONLY. Never modify.

### Article 20h Override
During this refactor rebuild, Article 20h ("refactor only when touching a file") is
suspended. The entire project is being rebuilt from scratch. This override expires
when this addendum is removed at cutover.

### Comparative Metrics
After each slice's Phase J gate check, record old-vs-new metrics:
file lengths, test coverage, coupling. Track in refactor/comparative-metrics.md.

### Behavior Coverage Matrix
Track in refactor/behavior-coverage-matrix.md.
Rebuild not complete until all intended behaviors are covered.
```

This addendum is temporary. It is removed at cutover (Step 7).

---

## Note on the Article 20h Override

Article 20 §8 (in the Architecture Standards contract) says "refactor only when touching a file — do not rewrite entire codebase." This rule exists to prevent scope creep during normal development.

During a refactor rebuild, this rule is explicitly overridden. The entire point of the refactor journey is a structured rewrite. The CLAUDE.md addendum makes this override visible and temporary — every session sees it, and it is removed when the rebuild is complete. This is not a loophole; it is the designed mechanism for full rewrites.

---

## Outcome

After this step:

- The rebuild branch has the full Get Started framework deployed
- Slice 0 is complete — CLAUDE.md, contracts, skills, and infrastructure are in place
- The CLAUDE.md refactor addendum gives Claude the context it needs: where the old code lives, which rules are overridden, and what to track
- The project is ready for slice-by-slice rebuilding (Step 6)

---

**Previous step:** [Step 4b: Gherkin Review & Chunking](04b-gherkin-review-and-chunking.md)
**Next step:** [Step 6: Rebuild Workflow](06-rebuild-workflow.md)
