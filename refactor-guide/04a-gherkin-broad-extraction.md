# Step 4a: Gherkin Broad Extraction

> Part of the [Refactor Guide](INDEX.md). Load this file for Pass 1 of Gherkin extraction. For Pass 2 (user review + chunking), load [04b-gherkin-review-and-chunking.md](04b-gherkin-review-and-chunking.md).

---

## Purpose

Extract the old system's actual behavior as Gherkin scenarios. These scenarios become the definitive regression test for the rebuild — if the new code passes them, it correctly implements the intended behavior. No separate "functional regression tester" agent is needed. The Gherkin IS the spec.

---

## Agent Hierarchy

The **CTO agent** spawns a **Gherkin Extraction sub-agent**. The Extraction sub-agent spawns its own **focused sub-agents** per slice or module to keep context windows narrow.

```
CTO
  -> Gherkin Extraction Sub-Agent
       -> Pass 1 Sub-Agent (per module/area — reads old code, writes broad Gherkin)
       -> Pass 1 Sub-Agent
       -> ...
     <- Collects broad Gherkin, presents for user review
     (User review happens here — see 04b)
       -> Pass 2 Sub-Agent (per slice — chunks reviewed Gherkin into per-slice scenarios)
       -> Pass 2 Sub-Agent
       -> ...
     <- Produces final chunked Gherkin
  <- Reports back to CTO and dies
```

---

## Pass 1: Broad Extraction

Sub-agents read the old code area by area (using the partition plan from Step 2 and the worktree path from `REFACTOR_CONFIG.md`) and document **CURRENT behavior** as Gherkin scenarios.

### What Pass 1 captures

This is forensic, not aspirational. Document what the code **actually does** — including quirks, edge cases, and behaviors that might be bugs. If the code sends a 500 error when the user submits an empty form, write a Gherkin scenario for that. If there is a race condition that sometimes double-charges a customer, document it.

### Sources for extraction

1. **Existing tests** — translate existing test assertions into Gherkin. Tests are the most reliable source of intended behavior.
2. **Code paths** — trace each user action through the code. Every conditional branch is a potential scenario. Follow the happy path first, then error paths, then edge cases.
3. **UI behavior** — what the user sees, what they can click, what happens when they do. Form validations, error messages, success states, loading states.
4. **Error handling** — what happens when things go wrong. Invalid input, missing data, network failures, permission denials, timeout scenarios.
5. **Edge cases** — boundary values, empty states, maximum limits, concurrent operations, null/undefined handling.

### Extraction Reliability and Limitations

LLM-based Gherkin extraction is not infallible. Be aware of these limitations:

- **Spaghetti code with no tests:** Extraction will produce LOW confidence scenarios. These MUST be flagged for explicit user review — do not default them to CORRECT.
- **Implicit behavior:** Code with global state mutations, side effects buried in middleware, or framework magic (Rails callbacks, Spring AOP, Django signals) may have behaviors that are not discoverable by reading code alone. The Risk Assessment from Step 2 should flag these areas. For HIGH-risk implicit behavior areas, the user should manually describe expected behaviors rather than relying on extraction.
- **Obfuscated or generated code:** If code is minified, transpiled, or generated, extract Gherkin from the source (pre-build) version if available. If no readable source exists, extract from user-observable behavior (UI, API responses) rather than code paths.
- **What if extraction misses something?** Missed behaviors will surface during the rebuild when users test the new system and notice missing functionality. At that point, add new Gherkin scenarios to the relevant slice's `.feature` file and rebuild. The Behavior Coverage Matrix should be updated to track the newly discovered behavior.

Apply the Numbered Step Rule: scenarios with 3+ steps must include `# Step N/M` comments.

### Template

Use `BEHAVIOR-EXTRACTION-TEMPLATE.md` from `refactor/templates/` for structuring each sub-agent's output.

### Output

Broad extraction saved to `refactor/gherkin/broad-behavior-spec.md`. This is a single consolidated document containing all extracted Gherkin from all sub-agents, organized by module/area.

---

**Previous step:** [Step 3: Feature Decomposition](03-feature-decomposition.md)
**Next step:** [Step 4b: User Review & Chunking](04b-gherkin-review-and-chunking.md)
