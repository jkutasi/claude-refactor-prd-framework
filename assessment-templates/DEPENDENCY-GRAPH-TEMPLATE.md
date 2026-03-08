# Dependency Graph — {PROJECT_NAME}

Documents external dependencies and internal coupling. Produced during Step 2 (Codebase Assessment).

---

## External Dependencies

| Package | Version | Purpose | Update Status | Risk |
|---------|---------|---------|---------------|------|
| {PACKAGE} | {VERSION} | {PURPOSE} | {Current/Outdated/Deprecated} | {LOW/MEDIUM/HIGH} |

---

## Internal Coupling

| Module A | Module B | Coupling Type | Strength |
|----------|----------|---------------|----------|
| {MODULE_A} | {MODULE_B} | {imports/shared state/shared DB table/event} | {Tight/Loose} |

---

## Shared State

- {GLOBAL_VARIABLE_OR_SINGLETON}: {DESCRIPTION_AND_WHICH_MODULES_USE_IT}
- {SHARED_CACHE}: {DESCRIPTION_AND_WHICH_MODULES_USE_IT}

---

## Database Coupling

| Module | Table | Access |
|--------|-------|--------|
| {MODULE} | {TABLE_NAME} | {Read/Write/Read+Write} |

---

## Dependency Diagram

```mermaid
graph TD
    {MODULE_A} --> {MODULE_B}
    {MODULE_A} --> {MODULE_C}
    {MODULE_B} --> {MODULE_D}
```
