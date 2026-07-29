# Step 4a: Build the Behavior Baseline

## Purpose

Record observed behavior before changing it. A written scenario is a specification,
not proof that the system behaves that way.

## Evidence Sources

Prefer evidence in this order:

1. passing executable tests;
2. captured API/UI/CLI behavior from a safe environment;
3. production telemetry and support evidence;
4. code-path inspection;
5. stakeholder description.

For each behavior record source, confidence, data sensitivity, risk, and whether an
executable parity command exists. Low-confidence or implicit behavior remains
`UNKNOWN`.

Use `gherkin-templates/BEHAVIOR-EXTRACTION-TEMPLATE.md` when human-readable scenarios
help. Do not imply they execute unless a test runner and bindings are recorded.

## Safety

- Sanitize sensitive production data.
- Apply provider/retention policy before sharing code or evidence.
- Do not reproduce known unsafe behavior merely because it exists.
- Do not silently omit background jobs, permission rules, error behavior, or data
  side effects.

Next: [Step 4b](04b-gherkin-review-and-chunking.md)
