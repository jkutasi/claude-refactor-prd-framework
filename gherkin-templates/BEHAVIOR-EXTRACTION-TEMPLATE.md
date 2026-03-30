# Behavior Extraction — {PROJECT_NAME}

> **Purpose:** Document what the old code actually does as Gherkin scenarios. This is the broad extraction — Pass 1 of the Gherkin Extraction step. These scenarios describe CURRENT behavior, not desired behavior.

## Extraction Sources

For each feature in the Feature Map, extract behavior from:
1. Existing tests (translate to Gherkin)
2. Code paths (trace each user action through the code)
3. UI behavior (what the user sees and does)
4. Error handling (how the code handles failures)
5. Edge cases (boundary conditions the code handles or fails to handle)

For multi-step scenarios (3+ Given/When/Then/And lines), include `# Step N/M` comments on each line.

## Feature: {FEATURE_NAME}

**Old code location:** {file paths in reference branch}
**Extracted by:** {sub-agent ID}
**Confidence:** HIGH / MEDIUM / LOW

> LOW confidence means the extractor is unsure about the behavior. These scenarios MUST be flagged for user review.

### Happy Path Scenarios

```gherkin
Feature: {FEATURE_NAME}

  Scenario: {Descriptive name of the happy path}
    Given {precondition from old code}
    When {user action or trigger}
    Then {observable outcome}
    And {additional outcomes}
```

### Error Handling Scenarios

```gherkin
  Scenario: {What happens when X fails}
    Given {precondition}
    When {action that triggers error}
    Then {how the old code handles it}
```

### Edge Case Scenarios

```gherkin
  Scenario: {Boundary condition}
    Given {edge case precondition}
    When {action at boundary}
    Then {old code behavior at boundary}
```

### Undocumented / Implicit Behavior

```gherkin
  # CONFIDENCE: LOW — Behavior inferred from code, not documented or tested
  Scenario: {Implicit behavior discovered during extraction}
    Given {inferred precondition}
    When {action}
    Then {inferred outcome}
```

---

## User Review Checklist

After extraction, the user reviews each scenario and classifies it:

| Scenario | Classification | Notes |
|----------|---------------|-------|
| {scenario name} | CORRECT / WRONG / DROP | {if WRONG: what should it do instead} |

### Classifications

- **CORRECT:** Replicate this behavior exactly in the rebuild.
- **WRONG:** This is a bug or bad pattern. Write corrected Gherkin for what it SHOULD do. The corrected version goes into the per-slice Gherkin.
- **DROP:** This behavior is intentionally removed in the rebuild. Do not replicate.
