# Risk Assessment — {PROJECT_NAME}

Identifies fragile areas and unknowns. Produced during Step 2 (Codebase Assessment).

---

## Risk Register

| ID | Risk | Category | Likelihood | Impact | Mitigation |
|----|------|----------|-----------|--------|------------|
| R-001 | {RISK_DESCRIPTION} | {CATEGORY} | {HIGH/MEDIUM/LOW} | {HIGH/MEDIUM/LOW} | {MITIGATION_STRATEGY} |

### Categories

- **Fragile code** — Frequently breaks
- **Untested code** — Zero coverage
- **Undocumented behavior** — No one knows why it works
- **External dependencies** — Third-party API changes
- **Data risks** — Migration complexity
- **Infrastructure risks** — Deployment coupling

---

## Data Migration Assessment

| Aspect | Current State | Rebuild Impact | Migration Strategy |
|--------|--------------|----------------|-------------------|
| **Database schema** | {DESCRIBE_CURRENT_SCHEMA} | {WHAT_CHANGES} | {HOW_TO_MIGRATE} |
| **Production data** | {VOLUME_AND_FORMAT} | {COMPATIBILITY} | {MIGRATION_PLAN} |
| **External data stores** | {CACHES_QUEUES_ETC} | {WHAT_CHANGES} | {HOW_TO_HANDLE} |
| **File storage** | {UPLOADS_ASSETS_ETC} | {PATH_CHANGES} | {MIGRATION_PLAN} |

### Data Migration Risk Level

- [ ] **None** — No persistent data (static site, CLI tool, etc.)
- [ ] **Low** — Schema unchanged, data compatible as-is
- [ ] **Medium** — Schema changes needed, migration script required
- [ ] **High** — Major schema redesign, data transformation required, rollback plan needed

> If Medium or High: create a dedicated data migration slice early in the rebuild sequence (Step 3 decomposition). Data migration is infrastructure — it should be one of the first slices built.

---

## Areas of Confidence

What is well-tested, well-documented, and stable:

- {AREA}: {WHY_IT_IS_STABLE}

---

## Unknown Areas

Parts of the codebase no one fully understands:

- {AREA}: {WHAT_IS_UNCLEAR}
