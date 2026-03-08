# Tech Debt Catalog — {PROJECT_NAME}

Documents known issues, workarounds, and undocumented behavior. Produced during Step 2 (Codebase Assessment).

---

## Severity Levels

- **P0** — Security debt (hardcoded secrets, injection vectors)
- **P1** — Frequently-modified oversized files
- **P2** — Infrequently-modified violations
- **P3** — Cosmetic debt (naming, formatting)

---

## Debt Items

| ID | Category | Description | Files Affected | Severity | Notes |
|----|----------|-------------|---------------|----------|-------|
| TD-001 | {CATEGORY} | {DESCRIPTION} | {FILES} | {P0/P1/P2/P3} | {NOTES} |

### Categories

- Oversized Files (>150 lines)
- Missing Tests
- Lint Suppressions
- Dead Code
- Hardcoded Values
- Security Issues
- Architecture Violations
- Undocumented Behavior

---

## TODO/FIXME/HACK Comments Found

| File | Line | Comment | Type |
|------|------|---------|------|
| {FILE_PATH} | {LINE_NUMBER} | {COMMENT_TEXT} | {TODO/FIXME/HACK} |

---

## Suppression Directives Found

| File | Line | Directive | Reason |
|------|------|-----------|--------|
| {FILE_PATH} | {LINE_NUMBER} | {noqa/eslint-disable/type: ignore} | {REASON_IF_DOCUMENTED} |
