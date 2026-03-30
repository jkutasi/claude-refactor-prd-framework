# Step 4b: Gherkin User Review & Chunking

> Part of the [Refactor Guide](INDEX.md). Load this file for user review and Pass 2 chunking. For Pass 1 (broad extraction), load [04a-gherkin-broad-extraction.md](04a-gherkin-broad-extraction.md).

---

## User Review

### Batching for Large Codebases

If the extraction produces more than ~30 scenarios, batch the review:

1. **Priority batching:** Present scenarios grouped by feature, highest-risk features first (use Risk Assessment from Step 2)
2. **Default classification:** Scenarios extracted from passing tests default to CORRECT unless the user overrides. Only scenarios with LOW confidence or extracted from code paths (not tests) require explicit review.
3. **Session limits:** Review no more than 20-30 scenarios per session. The Extraction sub-agent tracks review progress and resumes where the user left off.

For small codebases (<30 scenarios), review all at once.

Verify all multi-step scenarios include `# Step N/M` comments before approving.

The user reviews the extracted Gherkin and classifies every scenario into one of three categories:

### CORRECT — Replicate Exactly
The behavior is intentional and correct. The rebuilt system must pass this scenario exactly as written. No changes to the Gherkin.

### WRONG — Write Corrected Gherkin
The behavior is a bug or a bad pattern. The user writes (or directs the agent to write) corrected Gherkin that describes what the system **should** do. The old scenario is kept for reference (commented out or in an appendix) but the corrected version becomes the spec.

Example:
```gherkin
# OLD (bug): Empty form submission returns 500
# Scenario: Submit empty contact form
#   Given I am on the contact page
#   When I submit the form with no fields filled
#   Then I receive a 500 Internal Server Error

# CORRECTED: Empty form submission shows validation errors
Scenario: Submit empty contact form
  Given I am on the contact page
  When I submit the form with no fields filled
  Then I see validation errors for all required fields
  And no form submission is sent to the server
```

### DROP — Intentionally Removed
The behavior is being intentionally removed in the rebuild. Mark it clearly so its absence is a tracked decision, not an accidental omission.

```gherkin
# DROPPED: Legacy XML export — replaced by JSON API in rebuild
# Scenario: Export report as XML
#   ...
```

---

## Pass 2: Chunk into Per-Slice Scenarios

After user review, the Extraction sub-agent spawns **Pass 2 sub-agents** that break the reviewed Gherkin into per-slice scenarios matching the decomposition from Step 3.

### Why chunking is needed

The broad extraction is organized by module/area (matching the old code structure). The decomposition from Step 3 reorganized the system into vertical slices. A single broad scenario might span multiple slices, or a single slice might pull scenarios from multiple broad areas.

Pass 2 realigns the Gherkin to match the slice structure:

- Each slice gets its own Gherkin file
- Scenarios become more detailed and more numerous (a broad scenario covering a complex flow might split into 3-5 slice-level scenarios)
- Every slice has at least one scenario — if a slice has no Gherkin, either the extraction missed something or the slice is not needed

### Template

Use `GHERKIN-CHUNKING-TEMPLATE.md` from `refactor/templates/` for structuring the chunking process.

### Output

Chunked Gherkin files saved to `features/` directory — the standard Get Started location for feature specs. One `.feature` file per slice, named to match the slice identifier from the decomposition.

```
features/
  slice-001-db-connection.feature
  slice-002-user-model.feature
  slice-003-auth-login.feature
  slice-004-auth-registration.feature
  ...
```

---

## The Gherkin Files ARE the Regression Test

There is no separate regression testing step or agent. The Gherkin scenarios extracted in this step define the complete behavioral contract for the rebuilt system. If all scenarios pass, the rebuild is behaviorally equivalent to the old system (with user-approved corrections applied).

---

## Completion

1. Broad extraction saved to `refactor/gherkin/broad-behavior-spec.md`
2. User review completed — all scenarios classified as CORRECT, WRONG (corrected), or DROP
3. Chunked Gherkin saved to `features/` directory, one file per slice
4. The Gherkin Extraction sub-agent reports completion to the CTO agent
5. The Gherkin Extraction sub-agent dies

---

## Templates Used

- `BEHAVIOR-EXTRACTION-TEMPLATE.md` — structures broad extraction output per module
- `GHERKIN-CHUNKING-TEMPLATE.md` — structures the chunking from broad to per-slice

---

## Artifact Output Paths

```
refactor/gherkin/
  broad-behavior-spec.md

features/
  slice-001-*.feature
  slice-002-*.feature
  ...
```

---

**Previous step:** [Step 4a: Broad Extraction](04a-gherkin-broad-extraction.md)
**Next step:** [Step 5: Bootstrap Rebuild](05-bootstrap-rebuild.md)
