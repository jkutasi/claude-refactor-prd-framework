# Comparative Metrics — {PROJECT_NAME}

> **Purpose:** Track old-vs-new metrics after each slice's Phase J. Updated per-slice to show measurable improvement across the rebuild.

## Summary

| Metric | Old Codebase | Current Rebuild | Trend |
|--------|-------------|-----------------|-------|
| Average file length (LOC) | {N} | {N} | ↓ / ↑ / = |
| Max file length (LOC) | {N} | {N} | ↓ / ↑ / = |
| Test coverage % | {N}% | {N}% | ↓ / ↑ / = |
| Total source files | {N} | {N} | ↓ / ↑ / = |
| Cross-module imports | {N} | {N} | ↓ / ↑ / = |

## Per-Slice Metrics

| Slice | Old Files Replaced | New Files | Old Avg LOC | New Avg LOC | Old Coverage | New Coverage | Notes |
|-------|-------------------|-----------|-------------|-------------|-------------|-------------|-------|
| Slice 1 | {files} | {files} | {N} | {N} | {N}% | {N}% | {notes} |

## How to Measure

- **File length:** Count non-blank, non-comment lines (use `gate_check.py` line counter or `wc -l` as approximation)
- **Test coverage:** Use the project's test runner coverage report (e.g., `pytest --cov`, `jest --coverage`)
- **Cross-module imports:** Count import statements that cross feature-folder boundaries. Fewer = less coupling.
- **Old baseline:** Measure from the reference branch worktree. The old baseline is measured once during Step 2 assessment and reused for all slices.

## Interpreting Results

- More files with shorter lengths is expected and good (feature-folder decomposition)
- Total LOC may increase (explicit error handling, types, logging) — this is fine if files stay under 150 lines
- Coverage should always improve (old untested code → new tested code)
- Cross-module imports should decrease (better encapsulation)

> **Cutover gate:** Comparative metrics must "show improvement" — this means the trend column should show improvement on the metrics that matter for this project. Not every metric must improve. If total files increased but average file length halved and coverage doubled, that is improvement.
