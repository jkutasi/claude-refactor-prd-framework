# Gherkin Chunking — {PROJECT_NAME}

> **Purpose:** Break broad Gherkin scenarios from Pass 1 into per-slice scenarios that match the Feature Decomposition from Step 3. This is Pass 2 of the Gherkin Extraction step.

## Chunking Process

For each slice in the Feature-to-Slice Map:

1. Identify which broad scenarios from Pass 1 relate to this slice's concern
2. Extract the relevant scenarios and narrow them to this slice's scope
3. If a broad scenario spans multiple slices, split it — each slice gets the portion relevant to its business rule
4. Add detail: since slices are narrower than original features, the per-slice Gherkin should be more specific (concrete values, explicit edge cases)
5. Apply user classifications: CORRECT scenarios replicate as-is, WRONG scenarios use corrected Gherkin, DROP scenarios are excluded

When chunking broad scenarios into per-slice scenarios, preserve `# Step N/M` comments. Re-number from 1/M for each chunked scenario.

## Slice {N}: {SLICE_NAME}

**Business rule:** {one-sentence business rule from decomposition}
**Source feature:** {old feature name}
**Source scenarios:** {list of broad scenarios this slice draws from}

### Chunked Scenarios

```gherkin
Feature: {SLICE_NAME}

  Scenario: {Specific scenario for this slice's business rule}
    Given {precondition scoped to this slice}
    When {action scoped to this slice}
    Then {outcome verifiable with concrete input/output}

  Scenario: {Edge case for this business rule}
    Given {edge case precondition}
    When {action}
    Then {expected outcome}

  Scenario: {Error case for this business rule}
    Given {precondition that leads to error}
    When {action}
    Then {expected error handling}
```

### Behavior Changes in This Slice

| Original Behavior | New Behavior | Classification | Reason |
|-------------------|-------------|----------------|--------|
| {what old code did} | {what new code will do} | WRONG → CORRECTED | {why} |
| {dropped behavior} | N/A | DROP | {why} |

---

## Output

- Per-slice `.feature` files saved to `features/slice-N-{name}.feature`
- Follow Get Started Gherkin conventions (see `gherkin-examples.md` in the framework's `examples/` directory — deployed to `refactor/templates/` during Step 1.5 if needed)
- Each file is self-contained — a slice's Gherkin should be understandable without reading other slices
