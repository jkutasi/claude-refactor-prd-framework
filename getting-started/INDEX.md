# Getting Started — Index

> **Purpose:** This directory contains the project setup roadmap from the Get Started framework. For refactor projects, **start with `refactor-guide/INDEX.md` first** — it walks you through assessment, decomposition, and Gherkin extraction before you use these files.

## Refactor Projects: Start Here

| File | When to Load |
|------|-------------|
| [../refactor-guide/INDEX.md](../refactor-guide/INDEX.md) | **START HERE** — the refactor roadmap |

## Get Started Framework Content (Used During Rebuild)

Once you've completed the refactor assessment and decomposition (Steps 1-4), the rebuild phase uses these standard Get Started files:

| File | When to Load |
|------|-------------|
| [00-nuclear-rules.md](00-nuclear-rules.md) | Always — read first at every session |
| [01-planning-phase.md](01-planning-phase.md) | Step 5: Planning inputs come from assessment + decomposition output |
| [02-agent-teams.md](02-agent-teams.md) | Step 5: Setting up Agent Teams (includes refactor-phase sub-agents) |
| [03-slice-0-bootstrap.md](03-slice-0-bootstrap.md) | Step 5: Creating Slice 0 infrastructure in the rebuild branch (scaffolding: steps 3a–3f) |
| [03a-slice-0-bootstrap-tooling.md](03a-slice-0-bootstrap-tooling.md) | Step 5 (continued): Tooling install — Sentry SDK, Sentry CLI, structured logging, linter, MCP servers (steps 3g–3i) |
| [04-per-slice-workflow.md](04-per-slice-workflow.md) | Step 6: Running phases A–J for each slice (+ comparative metrics) |
| [04a-per-slice-workflow-phases-A-C.md](04a-per-slice-workflow-phases-A-C.md) | Step 6 detail: Phases A through C |
| [04b-per-slice-workflow-phases-E-POST-PUSH.md](04b-per-slice-workflow-phases-E-POST-PUSH.md) | Step 6 detail: Phases E through J + Post-Push |
| [05-browser-testing.md](05-browser-testing.md) | Step 6: Browser testing + session checklist |
| [06-appendix.md](06-appendix.md) | Reference: file structure + naming conventions |
| [sentry-automation.md](sentry-automation.md) | Sentry automation: relay-sentry MCP polling for F.5 + Post-Push |
| [skill-lifecycle-workflow.md](skill-lifecycle-workflow.md) | Skill management: find, create, promote, or combine skills |
| [skill-v2-creation-guide.md](skill-v2-creation-guide.md) | Step-by-step guide for building a SKILL.md in v2 format |

## Task Tracking

Every project uses `.taskmaster/` for durable task storage that survives across Claude sessions.

- **Skill:** `.claude/skills/task-manager/SKILL.md` — load at the start of every work session
- **Database:** `.taskmaster/tasks.json` — read this to see pending and in-progress tasks
- **Config:** `.taskmaster/config.json` — model role assignments

At every session start, load the `task-manager` skill and read `.taskmaster/tasks.json` BEFORE doing any work. Create tasks with `testStrategy` before writing code. See `.taskmaster/README.md` for schema details.
