# Step 1: Setup Reference Branch

> Part of the [Refactor Guide](INDEX.md). Load only this file when setting up the reference branch.

---

## Purpose

Before any refactoring begins, you need two things accessible simultaneously: the old code (as a living, read-only spec) and a clean workspace for the rebuild. Git worktrees make this possible without copying files or juggling branches manually.

---

## 1.1 Tag and Branch the Old Code

Tag the current state so you can always find it, then create a named branch that agents can read from.

```bash
# Tag the current commit for permanent reference
git tag reference/old-code-snapshot

# Create the reference branch from the current state
git branch reference/old-code

# Verify the branch exists
git branch -a | grep reference
```

**The `reference/old-code` branch is READ-ONLY. It is never modified.** It is the living spec. Agents can read it but never write to it. No commits, no amendments, no "quick fixes." If you need to annotate the old code, do it in assessment artifacts, not on this branch.

---

## 1.2 Create the Rebuild Branch

Create a clean branch where all new work will happen.

```bash
# Create the rebuild branch from the same starting point
git checkout -b rebuild/main
```

This is your working branch. All refactored code lands here.

---

## 1.3 Set Up Git Worktree

Git worktree lets you have both branches checked out on the filesystem at the same time. Agents working on the rebuild can read the old code without switching branches.

```bash
# From the project root (on the rebuild/main branch), add a worktree for the reference branch
git worktree add ../project-reference reference/old-code

# Verify both are accessible
ls ../project-reference   # Old code, read-only
ls .                      # Rebuild workspace
```

You now have two directories:
- **Project root** (current directory) — the rebuild workspace on `rebuild/main`
- **`../project-reference`** — the old code on `reference/old-code`, read-only

Choose a worktree path that makes sense for your project layout. The path above is an example — adjust as needed.

---

## 1.4 Create REFACTOR_CONFIG.md

Create a configuration file at the root of the rebuild workspace so that every agent and every step knows where things live. This file is the single source of truth for refactor paths.

Create `REFACTOR_CONFIG.md` in the project root with the following structure:

```markdown
# Refactor Configuration

## Branches
- **Reference branch:** `reference/old-code`
- **Rebuild branch:** `rebuild/main`

## Paths
- **Worktree path (old code):** `../project-reference`
- **Old code root:** `../project-reference/src` (adjust to your project)
- **Rebuild workspace:** `.` (current project root)
- **Assessment output:** `refactor/assessment/`
- **Decomposition output:** `refactor/decomposition/`
- **Gherkin output (broad):** `refactor/gherkin/`
- **Gherkin output (chunked):** `features/`

## Status
- [ ] Step 1: Reference branch setup
- [ ] Step 2: Codebase assessment
- [ ] Step 3: Feature decomposition
- [ ] Step 4: Gherkin extraction
```

Update the paths to match your actual project structure.

---

## 1.5 Deploy Refactor Scaffolding

Copy the assessment and decomposition templates into the project workspace so agents can reference them during subsequent steps. These are temporary — they get used during the refactor process and removed when complete.

Templates to deploy into the rebuild workspace:

- `CODEBASE-INVENTORY-TEMPLATE.md`
- `FEATURE-MAP-TEMPLATE.md`
- `DEPENDENCY-GRAPH-TEMPLATE.md`
- `TECH-DEBT-CATALOG-TEMPLATE.md`
- `RISK-ASSESSMENT-TEMPLATE.md`
- `FEATURE-TO-SLICE-MAP-TEMPLATE.md`
- `SLICE-DEPENDENCY-ORDER-TEMPLATE.md`
- `BEHAVIOR-EXTRACTION-TEMPLATE.md`
- `GHERKIN-CHUNKING-TEMPLATE.md`
- `BEHAVIOR-COVERAGE-MATRIX-TEMPLATE.md`
- `COMPARATIVE-METRICS-TEMPLATE.md`
- `CUTOVER-CHECKLIST-TEMPLATE.md`

Place these in a `refactor/templates/` directory in the rebuild workspace. Agents will reference them by path during Steps 2-4.

```bash
mkdir -p refactor/templates refactor/assessment refactor/decomposition refactor/gherkin

# Copy from the framework repo's template directories into refactor/templates/
# Adjust the source path to wherever you cloned the refactor framework repo
FRAMEWORK_REPO="/path/to/claude-refactor-prd-framework"

cp "$FRAMEWORK_REPO"/assessment-templates/*.md refactor/templates/
cp "$FRAMEWORK_REPO"/decomposition-templates/*.md refactor/templates/
cp "$FRAMEWORK_REPO"/gherkin-templates/*.md refactor/templates/
cp "$FRAMEWORK_REPO"/regression-templates/*.md refactor/templates/
cp "$FRAMEWORK_REPO"/cutover-templates/*.md refactor/templates/
```

---

## 1.6 Verify Setup

Before proceeding to Step 2, confirm:

1. `reference/old-code` branch exists and contains the complete old codebase
2. `rebuild/main` branch exists and is your current checkout
3. The worktree is accessible and contains the old code at the expected path
4. `REFACTOR_CONFIG.md` exists at the project root with correct paths
5. Templates are deployed to `refactor/templates/`

```bash
# Quick verification
git branch | grep reference/old-code
git branch | grep rebuild/main
ls ../project-reference
cat REFACTOR_CONFIG.md
ls refactor/templates/
```

---

## Critical Rule

**The reference branch is NEVER modified.** It is the living spec. Every subsequent step reads from it to understand the old system. If you modify it, you lose the ground truth. Agents can read it freely — they must never write to it, commit to it, or check it out in the main workspace.

---

**Next step:** [Step 2: Codebase Assessment](02-codebase-assessment.md)
