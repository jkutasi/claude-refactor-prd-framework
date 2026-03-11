# Step 3: Slice 0 Bootstrap (Create EVERYTHING Before Writing Code)

> Part of the [Getting Started](INDEX.md) roadmap. Load only this file when working on creating Slice 0 infrastructure.

> **Refactor projects:** Slice 0 bootstrap happens in the **rebuild branch**, not from an empty workspace. The old code is on the read-only reference branch. This bootstrap creates the Get Started framework infrastructure alongside the rebuild. See `refactor-guide/05-bootstrap-rebuild.md` for how assessment and decomposition outputs feed into this step.

Slice 0 creates every file, directory, skill, template, and script so that when Slice 1 starts, the infrastructure for compliance already exists. The CTO loads ONE subdocument at a time for each step.

### 3a. Create CLAUDE.md Contract

> Load `contract-templates/CLAUDE-MD-TEMPLATE.md` (core, ~90 lines) and customize for your project.
> Also load and deploy the extracted templates referenced by CLAUDE.md:
> - `contract-templates/AGENT-TEAMS-TEMPLATE.md` — team roster, sub-agent catalog, MCP architecture
> - `contract-templates/ARTICLES-INDEX-TEMPLATE.md` — articles 1-34 quick reference
> - `contract-templates/PER-SLICE-WORKFLOW-TEMPLATE.md` — Phases A-J with gates and checklists
> - `contract-templates/articles/` directory — one file per article, loaded on demand

The core contract contains:
- CTO role definition (Delegate Mode, never writes code)
- Nuclear Rules with verification gates
- Load-on-demand pointers to Agent Teams, Articles, Per-Slice Workflow, and Security

The articles appendix contains the full definitions of Articles 1-34 (code authorship, peer review, QA, Red Team, Professor Review, Whiskey Team, UX Sense Check, Test-First Specification Protocol, Test Peer Review, User Scope Confirmation, Code Architecture Standards). Agents load it on demand when they need a specific article's details.

**Path mapping:** Template files use `HYPHEN-TEMPLATE.md` naming (e.g., `ARCHITECTURE-STANDARDS-TEMPLATE.md`). When customized for your project, deploy to `contracts/` with underscore naming (e.g., `contracts/ARCHITECTURE_STANDARDS.md`). The articles directory copies as-is: `contract-templates/articles/` → `contracts/articles/`.

### 3b. Create Contract Documents

Load and customize each:
- `contract-templates/CONTRIBUTING-TEMPLATE.md` — Code authorship, naming, commit convention
- `contract-templates/SECURITY-TEMPLATE.md` — API keys, OWASP, access levels
- `contract-templates/DATA-CONTRACT-TEMPLATE.md` — Schemas, versioning, migration
- `contract-templates/ARCHITECTURE-STANDARDS-TEMPLATE.md` — Feature-based architecture, layer separation, 150-line limit, observability, error wrapping (Article 20)
- `contract-templates/TESTING-PYRAMID-TEMPLATE.md` — Test pyramid, coverage, Gherkin, edge cases
- `contract-templates/TESTING-PROCEDURES-TEMPLATE.md` — Test-first protocol, peer review, QA procedures
- `contract-templates/TESTING-GATES-TEMPLATE.md` — Defect resolution, browser testing, gate checklist

### 3c. Create Agent Skill Files

Load and customize each from `skill-templates/`:

**Core teammates:**
- `cto-orchestrator.md` — CTO lead skill file
- `coder-backend.md` — Backend coder
- `coder-frontend.md` — Frontend coder

**Peer reviewers:**
- `reviewer-gemini.md`, `reviewer-openai.md`, `reviewer-grok.md`

**QA team (all report to QA Lead):**
- `qa-lead.md` — QA Lead coordinator
- `qa-stats.md`, `qa-code-quality.md`, `qa-data-integrity.md`, `qa-security.md`, `qa-uiux-browser.md`
- `qa-manager.md` — QA findings synthesizer
- `red-team-reviewer.md` — 10 attack dimensions, pre-build gate
- `whiskey-team-adversarial-qa.md` — Adversarial QA + implicit regression + Goal Achievement Test
- `ux-sense-check.md` — Persona-based UX browser testing (3 generic personas)

**Support:**
- `researcher.md`, `documentation-scribe.md`
- `relay-mcp-pattern.md` — Duplicate once per MCP server

### 3d. Create Review Artifact Templates

Copy from `review-templates/` into your project's `reviews/` directory:
- `TEST-SPEC-TEMPLATE.md` -- Gherkin audit + test specification (Article 17)
- `TEST-REVIEW-TEMPLATE.md` -- Test code peer review (Article 18)
- `PEER-REVIEW-TEMPLATE.md`
- `QA-SWARM-TEMPLATE.md`
- `RED-TEAM-REVIEW-TEMPLATE.md`
- `WHISKEY-TEAM-TEMPLATE.md`
- `UX-SENSE-CHECK-TEMPLATE.md`

### 3e. Create Gate Check Script

Copy `examples/gate_check.py` to your project root. This script mechanically verifies ALL artifacts exist before allowing the next slice.

### 3f. Create Supporting Infrastructure

- `PROJECT.md` — Full architecture + implementation details (source of truth)
- `DOCS_MAP.md` — Documentation index (every agent reads this first)
- `AGENT_REGISTRY.md` — Who does what (use `reference/agent-registry-template.md`)
- `config/default.yaml` + `config/CONFIG_SCHEMA.md` (use `reference/config-schema-template.md`)
- Create directories: `features/`, `tests/integration/`, `src/shared/errors/`, `src/shared/logging/`, `src/shared/middleware/`, `output/`, `diary/`, `slices/`, `learnings/`
- Initialize `diary/PROJECT_DIARY.md`
- Initialize `learnings/` files (one per domain: QA, BUILD, REVIEW, UX)
- Set up Husky pre-push hooks to run lint + type check on every push. See Article 23 for configuration.
- Set up `.env` with API keys for peer review models

### 3g. Install Observability Stack (MANDATORY — do not skip)

Three tools must be installed and working before any feature code is written:

**Sentry** — error tracking. Every error that occurs in the app — frontend or backend — gets captured automatically and appears in the Sentry dashboard. This is how we know what broke during QA: after every QA run, the CTO checks Sentry for new errors. No errors slipping through silently.

**Pino** (Node.js/TypeScript) or **structlog** (Python) — structured logger. Instead of scattered `console.log` statements that disappear, every log message is a structured JSON entry that Sentry can read. All code uses this shared logger — no raw `console.log` or `print()` anywhere.

**Ruff** (Python projects only) — linter. Automatically catches code quality issues before anything gets pushed. Wired into Husky pre-push hooks so bad Python code is blocked at the gate.

**Install steps (agent executes these):**

| Language | Packages to install |
|----------|-------------------|
| Node.js / TypeScript | `npm install pino pino-sentry-transport @sentry/node` |
| Python | `pip install structlog sentry-sdk ruff` + add to `requirements.txt` / `pyproject.toml` |
| Browser / SPA (frontend) | `npm install @sentry/browser` |

After installing:
1. Create `src/shared/logging/logger.{EXT}` — the single shared logger the whole codebase imports. It connects Pino/structlog to Sentry so errors flow through automatically.
2. Add `SENTRY_DSN` and `SENTRY_ENVIRONMENT` to `.env` using the project's Sentry credentials.
3. Send one test error through the logger and confirm it appears in the Sentry dashboard. If it doesn't show up, fix the connection before proceeding.

**Gate:** Do NOT start Slice 1 until Sentry is receiving errors. An error tracker configured "later" never gets configured.

### 3h. Set Up Persistence

Use plain Markdown files in `learnings/` for cross-session knowledge persistence:
- `learnings/QA_LEARNINGS.md` — QA patterns and findings
- `learnings/BUILD_LEARNINGS.md` — Build and deployment patterns
- `learnings/REVIEW_LEARNINGS.md` — Review patterns and common issues
- `learnings/UX_LEARNINGS.md` — UX patterns and user feedback
