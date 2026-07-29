# Step 2: Assess the Existing Project

## Outcome

Produce enough evidence to choose a safe strategy without loading the whole codebase
into one model context.

## Scope the Scan

The frontier orchestrator owns synthesis. Bounded workers may inspect non-overlapping
areas and return compact evidence. Record ownership when multiple workers are used.

Start with a structural inventory:

- entry points, packages, routes, jobs, and public APIs;
- schemas, migrations, storage, and external services;
- authentication, permissions, money, secrets, and private data;
- test suites, fixtures, coverage, deploy, monitoring, and rollback paths;
- dependency direction, cycles, generated code, and high-change areas.

Then inspect bounded modules. Each result identifies files read, behavior observed,
dependencies, tests, risks, unknowns, and confidence. Do not turn assumptions into
requirements.

## Required Artifacts

Use the five files in `assessment-templates/`:

1. codebase inventory;
2. feature map;
3. dependency graph;
4. technical-debt catalog;
5. risk assessment.

Every high-risk or unknown area has an owner and a next evidence step. Apply provider
and retention policy before sending project content to any model.

## Completion

Assessment is complete when the artifacts collectively explain what the project does,
where behavior and data live, what is executable, what is fragile, and what remains
unknown. Unknowns block destructive strategy decisions.

Next: [Step 3](03-feature-decomposition.md)
