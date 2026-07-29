# Step 3: Choose Strategy and Decompose the Work

## Strategy Decision

Incremental refactoring is the default. Choose a full rebuild only when evidence shows
incremental change is less safe or materially less viable.

Record:

- strategy and rationale;
- failure modes and data risks;
- compatibility/coexistence plan;
- rollout and rollback approach;
- user approval evidence for a full rebuild.

Set `refactor-state.json` to `strategy`. A rebuild cannot pass the state checker
without explicit user approval.

## Build Reversible Increments

Map features to small end-to-end increments using `decomposition-templates/`.
Each increment includes:

- user-visible or operational outcome;
- allowed paths and dependency boundaries;
- behavior decisions and executable parity commands;
- data/schema effect;
- verification commands;
- rollout and rollback;
- predecessor dependencies.

Prefer increments that can ship independently behind compatibility adapters or
feature flags. Separate database expansion, data movement, application switching,
and cleanup when data is involved.

## Frontier Review

The other frontier model reviews the strategy only when the plan is high-risk. It
receives the original requirements, assessment evidence, decomposition, failure
modes, and rollback plan. The user resolves disagreement.

Next: [Step 4a](04a-gherkin-broad-extraction.md)
