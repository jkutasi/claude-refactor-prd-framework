# Behavior Coverage Matrix — {PROJECT_NAME}

> **Purpose:** Track which correct behaviors from the old code are covered by rebuilt slices. Updated after each slice completes Phase J. The rebuild is not complete until all intended behaviors are covered.

## Coverage Summary

| Total Intended Behaviors | Covered | Remaining | Coverage % |
|-------------------------:|--------:|----------:|-----------:|
| {N} | {N} | {N} | {N}% |

## Per-Feature Coverage

| Old Feature | Total Behaviors | Covered by Slices | Remaining | Status |
|-------------|----------------:|-------------------:|----------:|--------|
| {feature} | {N} | Slice 1, 3, 5 | {N} | IN_PROGRESS / COMPLETE |

## Per-Behavior Detail

| ID | Old Feature | Description | Classification | Covered by Slice | Gherkin Scenario | Status |
|----|-------------|-------------|----------------|-----------------|------------------|--------|
| BHV-001 | {feature} | {what it does} | CORRECT | Slice {N} | {scenario name} | COVERED |
| BHV-002 | {feature} | {what it does} | WRONG | Slice {N} | {corrected scenario} | COVERED (CORRECTED) |
| BHV-003 | {feature} | {what it does} | DROP | N/A | N/A | DROPPED |
| BHV-004 | {feature} | {what it does} | CORRECT | -- | -- | NOT_STARTED |

## Classification Legend

- **CORRECT:** Old behavior replicated exactly. Gherkin matches old code's behavior.
- **WRONG → CORRECTED:** Old behavior was a bug/bad pattern. Gherkin describes the corrected behavior.
- **DROP:** Old behavior intentionally removed. Not covered because it shouldn't exist.
- **COVERED:** New code passes the Gherkin scenario for this behavior.
- **NOT_STARTED:** No slice has been built for this behavior yet.

## New Behaviors (Not in Old System)

Behaviors added during the rebuild that did not exist in the old codebase:

| ID | Feature | Description | Added in Slice | Gherkin Scenario | Status |
|----|---------|-------------|---------------|------------------|--------|
| NEW-001 | {feature} | {what it does} | Slice {N} | {scenario name} | COVERED |

> New behaviors are tracked separately. They do not affect the old-behavior coverage percentage but must have their own Gherkin scenarios and passing tests.

---

## Notes

- Behaviors classified as DROP are excluded from the coverage percentage
- Coverage % = COVERED / (Total Intended - DROPPED) * 100
- The rebuild is complete when Coverage % = 100% AND all NEW behaviors have passing tests
- New behaviors (NEW-xxx) are tracked in the section above — they represent improvements over the old system
