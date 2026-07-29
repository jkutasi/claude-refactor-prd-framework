# Behavior Inventory — {PROJECT_NAME}

Gherkin is optional human-readable specification. It is executable only when a
runner command and step bindings are recorded.

## Behavior

- ID: B-{NNN}
- Feature: {feature}
- Source: {passing test/probe/telemetry/code/user}
- Source reference: {path, command, trace, or ticket}
- Confidence: {HIGH/MEDIUM/LOW}
- Risk: {normal/high}
- Decision: {PRESERVE/CORRECT/DROP/UNKNOWN}
- User approval evidence for CORRECT or DROP: {reference/N/A}
- Executable parity command: {command/NONE}

```gherkin
Feature: {capability}

  Scenario: {observed behavior}
    Given {context}
    When {action}
    Then {observable result}
```

## Side Effects

- Data writes: {details}
- Permissions: {details}
- External services: {details}
- Background work: {details}
- Error behavior: {details}

LOW confidence and UNKNOWN behavior block destructive decisions until resolved.
