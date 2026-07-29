# Risk Assessment — {PROJECT_NAME}

## Risk Register

| ID | Risk | Trigger | Likelihood | Impact | Detection | Mitigation | Rollback | Owner |
|---|---|---|---|---|---|---|---|---|
| R-001 | {risk} | {trigger} | {H/M/L} | {H/M/L} | {check} | {action} | {method} | {owner} |

Cover at least:

- implicit or untested behavior;
- authentication, permissions, secrets, and private data;
- money or financial calculations;
- schema, production data, queues, caches, and files;
- public APIs and external dependencies;
- deployment, monitoring, recovery, and support operations.

## Data and Schema

| Store | Current Contract | Proposed Effect | Compatibility Window | Reconciliation | Recovery |
|---|---|---|---|---|---|
| {store} | {schema/format} | {effect} | {window} | {command} | {method} |

Use expand/migrate/switch/contract sequencing when possible. Never schedule
irreversible cleanup before the new path is verified and rollback is no longer needed.

## Unknowns

| Area | Why Unknown | Risk if Wrong | Evidence Needed | Owner |
|---|---|---|---|---|
| {area} | {reason} | {impact} | {next step} | {owner} |

Unknown high-impact behavior blocks destructive strategy or cutover decisions.
