# Claude Refactor PRD Framework

A structured rebuild framework for refactoring existing projects using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) with [Agent Teams](https://docs.anthropic.com/en/docs/claude-code/agent-teams). It defines the assessment, decomposition, and rebuild process for taking an existing codebase and restructuring it into the [Get Started PRD Framework](https://github.com/jkutasi/claude-get-started-prd-framework) methodology.

## What This Is

This is **temporary scaffolding** for rebuilding an existing project. You give Claude Code the URL to this repo alongside your existing project and tell it to refactor. The CTO follows the refactor guide to assess the old codebase, decompose features into narrow vertical slices, extract behavior specs, then rebuild from scratch using the Get Started framework.

Once the rebuild is complete, the refactor scaffolding gets archived and the project runs on the standard Get Started framework going forward. Claude never reads refactor context again after cutover.

> **Building a new project from scratch?** Use the [Get Started Framework](https://github.com/jkutasi/claude-get-started-prd-framework) directly. This repo is for existing projects that need fundamental restructuring.

## How It Differs from Get Started

| Aspect | Get Started | Refactor |
|--------|------------|----------|
| Starting point | Empty workspace | Existing codebase |
| First step | Planning (what to build) | Assessment (what exists) |
| Old code | N/A | Preserved on read-only reference branch |
| Slice decomposition | Design from scratch | Decompose existing features into narrower slices |
| Gherkin source | Written from requirements | Extracted from old code behavior, then chunked per slice |
| QA | Standard (does it work?) | Standard + comparative metrics (is it better than before?) |
| Framework lifecycle | Permanent | Temporary — archived after rebuild complete |

## Quick Start

1. **Open** your existing project in Claude Code
2. **Give Claude** the URL to this repo: `https://github.com/jkutasi/claude-refactor-prd-framework`
3. **Tell it** to refactor the project according to these guidelines
4. **Follow** `refactor-guide/INDEX.md` — the 7-step sequential roadmap

## The Refactor Journey (7 Steps)

| Step | Name | What Happens |
|------|------|-------------|
| **1** | Setup Reference Branch | Preserve old code on read-only branch, create rebuild worktree |
| **2** | Codebase Assessment | Analyze old code: features, patterns, dependencies, debt, risks |
| **3** | Feature Decomposition | Break old features into narrowest possible vertical slices |
| **4** | Gherkin Extraction | Extract old behavior as scenarios, chunk per slice, user reviews |
| **5** | Bootstrap Rebuild | Deploy Get Started framework in rebuild branch, run Slice 0 |
| **6** | Rebuild Workflow | Rebuild slice by slice using standard Get Started Phases A-J |
| **7** | Cutover & Archive | Archive refactor scaffolding, project becomes standard Get Started |

## Per-Slice Workflow (Phases A–J)

Every vertical slice follows this mandatory sequence during the rebuild:

| Phase | Name | What Happens |
|-------|------|-------------|
| **A** | Preparation | CTO reviews requirements, researcher gathers docs |
| **A.5** | Doc Bootstrap + Diagrams | Slice 0: docs + high-level diagrams. Slices 1+: per-slice diagrams |
| **A.6** | User Scope Confirmation | User reviews and approves slice scope before Red Team and tests |
| **A.7** | Red Team Pre-Build | Adversarial review of the user-confirmed plan before any code is written |
| **B** | Test Specification | B.1: Gherkin audit. B.2: Test-writer agents write all tests (must be RED). B.3: Test peer review |
| **C** | Implementation | Coder agents write code until all tests from Phase B pass |
| **D** | Self-Reflection | Each coder re-reads their own code as a reviewer |
| **E** | Peer Review | 3+ independent external models review in parallel (+ Greptile if configured) |
| **F** | QA Swarm | Standard QA + Whiskey Team + UX Sense Check in parallel |
| **G** | Autonomous Fix Verification | Autonomous Defect Resolution Protocol — QA agents fix inline, CTO verifies + handles escalations |
| **H** | Regression | Full regression check + implicit behavior regression (6 categories) |
| **I** | Documentation | Scribe updates all affected docs |
| **I.5** | User Delivery | CTO presents DONE slice to user with all QA results — user only sees fully-vetted work |
| **J** | Gate Check | Mechanical verification that all artifacts exist |
| **Post-Push** | Post-Push Verification | Check error tracker, deployment logs, and Greptile after every push |

## Repository Structure

```
.
├── refactor-guide/                      # The refactor roadmap — start here
│   ├── INDEX.md                        # Document map (what to load per phase)
│   ├── 01-setup-reference-branch.md   # Preserve old code, create worktree
│   ├── 02-codebase-assessment.md      # Analyze existing codebase
│   ├── 03-feature-decomposition.md    # Break features into narrow slices
│   ├── 04a-gherkin-broad-extraction.md # Pass 1: extract behavior from old code
│   ├── 04b-gherkin-review-and-chunking.md # User review + Pass 2: chunk per slice
│   ├── 05-bootstrap-rebuild.md        # Deploy Get Started framework
│   ├── 06-rebuild-workflow.md         # Slice-by-slice rebuild
│   └── 07-cutover-archive.md          # Archive scaffolding, finalize
│
├── assessment-templates/                # Templates for analyzing old codebase
│   ├── CODEBASE-INVENTORY-TEMPLATE.md
│   ├── FEATURE-MAP-TEMPLATE.md
│   ├── DEPENDENCY-GRAPH-TEMPLATE.md
│   ├── TECH-DEBT-CATALOG-TEMPLATE.md
│   └── RISK-ASSESSMENT-TEMPLATE.md
│
├── decomposition-templates/             # Breaking old features into slices
│   ├── FEATURE-TO-SLICE-MAP-TEMPLATE.md
│   └── SLICE-DEPENDENCY-ORDER-TEMPLATE.md
│
├── gherkin-templates/                   # Extracting and chunking Gherkin
│   ├── BEHAVIOR-EXTRACTION-TEMPLATE.md
│   └── GHERKIN-CHUNKING-TEMPLATE.md
│
├── regression-templates/                # Tracking correct behavior coverage
│   ├── BEHAVIOR-COVERAGE-MATRIX-TEMPLATE.md
│   └── COMPARATIVE-METRICS-TEMPLATE.md
│
├── cutover-templates/                   # Final switchover checklist
│   └── CUTOVER-CHECKLIST-TEMPLATE.md
│
├── getting-started/                     # Get Started framework content (copied)
├── contract-templates/                  # Contract templates (copied, some adapted)
├── skill-templates/                     # Agent skill definitions (copied)
├── review-templates/                    # Review artifact templates (copied)
├── examples/                            # Reference examples (copied)
└── reference/                           # Supporting reference docs (copied)
```

## Key Concepts

- **Temporary Scaffolding**: The refactor framework guides the rebuild, then gets archived. After cutover, the project is a standard Get Started project.
- **Reference Branch**: Old code preserved on a read-only branch. Agents can read it for context but never modify it.
- **Behavior Coverage Matrix**: Tracks which correct behaviors from the old code are now covered by rebuilt slices. Rebuild is not complete until all intended behaviors are covered.
- **Slice Sizing Principle**: A slice = one statable business rule with a concrete input/output pair. Too small = can't state a meaningful rule. Too big = multiple rules bundled.
- **Comparative Metrics**: After each slice, compare old vs. new metrics (file lengths, coverage, coupling) to verify the rebuild is actually improving structure.

## Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- Agent Teams enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- API keys for peer review models (at least 3 of: Gemini, OpenAI/Codex, Grok/xAI, Greptile)
- [OpenAI Codex CLI](https://developers.openai.com/codex) installed (`npm install -g @openai/codex`)
- [Greptile](https://www.greptile.com) API key (optional — adds codebase-aware 4th reviewer)
- `agent-browser` (Vercel) available for browser-based QA testing

## License

Private — for internal team use only.
