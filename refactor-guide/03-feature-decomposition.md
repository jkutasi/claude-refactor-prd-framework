# Step 3: Feature Decomposition

> Part of the [Refactor Guide](INDEX.md). Load only this file when decomposing features into slices.

---

## Purpose

Break the old system's features into vertical slices small enough to build, test, and verify independently. The decomposition transforms a monolithic understanding of the old system into an ordered build plan for the new one.

---

## 3.1 List All Features from the Assessment

Start with the Feature Map produced in Step 2 (`refactor/assessment/feature-map.md`). Every feature identified during assessment becomes an input to decomposition. Nothing is skipped — even features flagged for removal need to appear so their removal is an explicit, tracked decision.

---

## 3.2 Identify Concerns per Feature

For each feature, identify its constituent concerns:

- **Layers:** UI, API, business logic, data access, infrastructure
- **Data:** What data does this feature read, write, transform?
- **User Actions:** What can the user do? What triggers what?
- **Side Effects:** Emails sent, webhooks fired, logs written, external APIs called
- **Shared Dependencies:** Auth checks, permission gates, rate limiting, caching

This concern breakdown reveals where a single "feature" is actually multiple independent pieces of work.

---

## 3.3 Apply Decomposition Rules

Apply the Get Started decomposition rules (Article 29) to break each feature into slices:

1. **Single concern** — each slice does one thing
2. **Vertical** — each slice cuts through all necessary layers (not a "backend slice" and a "frontend slice")
3. **Independent** — each slice can be built and tested without other incomplete slices
4. **Small** — if a slice feels like it will take more than one focused session, it is too big

One old feature may become 2-10+ slices. This is expected. A complex feature with multiple user actions, multiple data models, and multiple edge cases will decompose into many slices.

---

## Slice Sizing Principle

A vertical slice = the smallest unit of work where the business rule it implements can be stated in one sentence and verified with a concrete input/output pair.

### Too Small
Cannot state a meaningful business rule. The output is meaningless without adjacent context.

**Concrete test:** If you need to mock/stub the thing this slice depends on to test it, and the mock is more complex than the code, it is too small — merge it with its dependency.

### Too Big
Multiple business rules are bundled together. You find yourself saying "and" when describing what the slice does.

### Right Size
One statable business rule, one verifiable input/output pair.

### Example

**Business rule:** "Gold tier customers get 15% off shipping on orders over $100."

- **Input:** (Gold tier customer, $150 order)
- **Output:** 15% shipping discount applied

This is one slice. The shipping rate lookup is a separate slice. The order total calculation that combines item prices, shipping, and discounts is another slice. Each has its own statable rule and verifiable pair.

### Non-Business-Rule Slices

Not all slices are business-rule slices. For infrastructure, UI, and integration slices, the sizing rule adapts:

- **Infrastructure** (auth setup, DB connection, logging pipeline): One statable capability with a verifiable outcome. "The application connects to PostgreSQL and runs migrations on startup" — verifiable by checking that tables exist after boot.
- **UI** (layout, navigation, component shells): One statable capability with a verifiable outcome. "The sidebar navigation renders all top-level routes and highlights the active page" — verifiable by checking rendered output.
- **Integration** (webhook handler, third-party API client): One statable capability with a verifiable outcome. "The Stripe webhook handler processes `payment_intent.succeeded` events and updates order status" — verifiable with a test payload.

---

## 3.4 Map Old Features to New Slices

Produce a mapping from every old feature to its new slices using the `FEATURE-TO-SLICE-MAP-TEMPLATE.md` template. The map must be exhaustive — every behavior in the old system is either mapped to a slice or explicitly marked as dropped.

---

## 3.5 Determine Rebuild Order

Slices are sequential, not nested. They have dependencies (build order) but are not inside each other. Like bricks, not Russian dolls.

The dependency graph determines build sequence:

1. Identify which slices depend on which other slices
2. Slices with no dependencies come first (foundation slices — typically infrastructure and data model setup)
3. Slices that depend only on completed slices come next
4. Continue until all slices are ordered

Use the `SLICE-DEPENDENCY-ORDER-TEMPLATE.md` template to produce the ordered build plan.

No circular dependencies between slices. If two slices appear to depend on each other, resolve using one of these strategies:

1. **Interface extraction:** Define a shared interface (types, contracts) as an infrastructure slice that both depend on. Neither depends on the other — both depend on the interface. Example: Auth and User both depend on a `UserIdentity` interface slice.
2. **Event decoupling:** If A calls B and B calls A, introduce an event/message interface slice. A publishes events, B subscribes (and vice versa). The event contract slice comes first, then A and B can be built independently.
3. **Merge:** If the circular dependency is genuine and cannot be decoupled, merge the two slices into one. This is a last resort — it means the original decomposition cut too aggressively. A merged slice that violates the sizing principle is better than a circular dependency that cannot be resolved.
4. **Stub-first:** Build slice A first with a stub for the B dependency. Build slice B. Then update slice A to use the real B. The stub is a temporary measure, not a permanent mock.

---

## 3.6 Peer Review the Decomposition

Before the user reviews, submit the decomposition to peer review with 3+ external models. The specific question for reviewers:

**"Can any of these slices be broken down further while still satisfying the slice sizing principle?"**

Reviewers should also check for:
- Slices that bundle multiple business rules
- Slices that are too small (mocks more complex than code)
- Missing slices (behaviors in the old system not covered)
- Dependency ordering errors (slice depends on something that comes later)
- Slices that are not truly vertical (backend-only or frontend-only)

Incorporate reviewer feedback before presenting to the user.

---

## 3.7 User Review and Approval

Present the complete decomposition to the user:
- Feature-to-slice map (every old feature mapped to new slices)
- Ordered build plan (dependency-driven sequence)
- Any features marked for removal (explicit, not accidental)

The user reviews, adjusts, and approves. No building begins until the slice plan is approved.

---

## Templates Used

- `FEATURE-TO-SLICE-MAP-TEMPLATE.md` — maps old features to new slices
- `SLICE-DEPENDENCY-ORDER-TEMPLATE.md` — ordered build sequence with dependencies

---

## Artifact Output Paths

```
refactor/decomposition/
  feature-to-slice-map.md
  slice-dependency-order.md
```

---

**Previous step:** [Step 2: Codebase Assessment](02-codebase-assessment.md)
**Next step:** [Step 4a: Gherkin Broad Extraction](04a-gherkin-broad-extraction.md)
