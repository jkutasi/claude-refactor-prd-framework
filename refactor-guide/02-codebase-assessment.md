# Step 2: Codebase Assessment

> Part of the [Refactor Guide](INDEX.md). Load only this file when assessing the existing codebase.

---

## Purpose

Understand the old codebase completely before changing anything. The assessment produces structured artifacts that every subsequent step depends on. This is forensic analysis, not planning — you are documenting what exists, not what you want to build.

---

## Context Window Protection is CRITICAL

A full codebase cannot fit in a single agent's context window. Attempting to read everything in one pass leads to truncation, hallucination, and missed details. The assessment uses a strict sub-agent hierarchy to keep each agent's scope narrow and its output compact.

---

## 2.1 Agent Hierarchy

The **CTO agent** spawns a **Codebase Assessment sub-agent**. The Assessment sub-agent does NOT read the entire codebase itself. Instead, it spawns focused sub-agents that each read a narrow scope, produce a structured summary, and die.

```
CTO
  -> Codebase Assessment Sub-Agent
       -> Structural Scan Sub-Agent (first, always)
       -> Module Analysis Sub-Agent (one per area, based on partition plan)
       -> Module Analysis Sub-Agent
       -> Module Analysis Sub-Agent
       -> ... (as many as needed)
     <- Synthesizes all summaries into 5 artifacts
  <- Reports back to CTO and dies
```

---

## 2.2 First Sub-Agent: Structural Scan

The Assessment sub-agent spawns a **Structural Scan sub-agent** first. This agent:

1. Reads the file tree of the old code (via the worktree path in `REFACTOR_CONFIG.md`)
2. Counts lines per file and per directory
3. Identifies entry points (main files, route handlers, exported APIs)
4. Identifies folder boundaries (where one module/area ends and another begins)
5. Produces a **partition plan** — a list of scoped areas, each small enough for a single sub-agent to read completely

The partition plan determines how the remaining work is divided. Each partition should be small enough that a sub-agent can read every file in that partition without exceeding context limits.

**Output:** A partition plan document listing each area, its files, approximate line count, and entry points.

---

## 2.3 Subsequent Sub-Agents: Module Analysis

Based on the partition plan, the Assessment sub-agent spawns **one sub-agent per area**. Each module analysis sub-agent:

1. Reads only the files in its assigned partition (narrow scope)
2. Produces a structured summary covering:
   - What this module does (purpose, responsibilities)
   - Public interface (exports, APIs, entry points)
   - Internal structure (key functions, classes, patterns)
   - Dependencies (what it imports, what imports it)
   - Data models (schemas, types, database tables)
   - Business logic locations (where the rules live)
   - Test coverage (what's tested, what's not)
   - Fragility indicators (tight coupling, global state, magic numbers, complex conditionals)
   - Infrastructure concerns (environment variables, external services, configuration)
3. Dies after producing its summary

Each summary stays compact — structured, not narrative. Bullet points and tables, not paragraphs.

**Summary size budget:** Each module summary must stay under 200 lines. If a module requires more detail, split it into sub-partitions and spawn additional sub-agents. The Assessment sub-agent's synthesis step (§2.4) receives all summaries at once — if total summary volume exceeds 1500 lines, the Assessment sub-agent must summarize in two passes: first group summaries by area, then synthesize groups into artifacts.

---

## 2.4 Synthesis: Five Artifacts

The Assessment sub-agent collects all module summaries and synthesizes them into five artifacts. Each artifact uses its corresponding template from `refactor/templates/` (deployed during Step 1.5).

### Artifact 1: Codebase Inventory
**Template:** `CODEBASE-INVENTORY-TEMPLATE.md`

Complete inventory of every file, module, and component. What exists, where it lives, how big it is. The map of the territory.

### Artifact 2: Feature Map
**Template:** `FEATURE-MAP-TEMPLATE.md`

What the project does from the user's perspective. Every feature, capability, and user-facing behavior, mapped to the code that implements it.

### Artifact 3: Dependency Graph
**Template:** `DEPENDENCY-GRAPH-TEMPLATE.md`

How modules depend on each other. Internal dependencies (module A imports module B) and external dependencies (third-party packages, APIs, services). Identifies dependency direction, circular dependencies, and coupling hotspots.

### Artifact 4: Tech Debt Catalog
**Template:** `TECH-DEBT-CATALOG-TEMPLATE.md`

Known problems, anti-patterns, workarounds, and fragile areas. This is not a judgment — it is a catalog of what will need attention during the rebuild. Includes: deprecated APIs, known bugs, performance bottlenecks, security concerns, dead code, inconsistent patterns.

### Artifact 5: Risk Assessment
**Template:** `RISK-ASSESSMENT-TEMPLATE.md`

What could go wrong during the rebuild. Areas with poor test coverage, complex business logic that is hard to verify, integrations with external systems, data migration concerns, areas where behavior is implicit rather than explicit.

---

## 2.5 Questions the Assessment Answers

When the five artifacts are complete, they should collectively answer:

- **What does this project do?** (Feature Map)
- **How is it structured?** (Codebase Inventory)
- **What are the dependencies?** (Dependency Graph)
- **Where is the business logic?** (Feature Map + Codebase Inventory)
- **What's tested?** (Codebase Inventory + Risk Assessment)
- **What's fragile?** (Tech Debt Catalog + Risk Assessment)
- **What's the data model?** (Codebase Inventory + Dependency Graph)
- **What's the infrastructure?** (Codebase Inventory + Dependency Graph)

If any question cannot be answered from the artifacts, the assessment is incomplete. Go back and fill the gaps.

---

## 2.6 Completion

1. All five artifacts are saved to `refactor/assessment/` in the project workspace
2. The Assessment sub-agent reports completion to the CTO agent
3. The Assessment sub-agent dies
4. The CTO agent reviews the artifacts for completeness before proceeding to Step 3

---

## Artifact Output Paths

```
refactor/assessment/
  codebase-inventory.md
  feature-map.md
  dependency-graph.md
  tech-debt-catalog.md
  risk-assessment.md
```

---

**Previous step:** [Step 1: Setup Reference Branch](01-setup-reference-branch.md)
**Next step:** [Step 3: Feature Decomposition](03-feature-decomposition.md)
