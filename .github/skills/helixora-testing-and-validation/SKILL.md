---
name: helixora-testing-and-validation
description: "Test and validate Helixora AI across unit, integration, API, AI workflow, and safety-critical scenarios. Use for regression prevention, recommendation validation, schema testing, edge-case handling, and healthcare-grade quality checks."
user-invocable: true
---

# Helixora Testing and Validation

## When to Use

- Add or improve automated tests
- Validate high-risk healthcare workflows
- Prevent regressions in recommendation logic
- Verify schema contracts and API behavior
- Test clinician review and approval flows
- Evaluate AI-assisted outputs for safety and consistency

## Validation Layers

- unit tests for core domain logic
- integration tests for services and data flows
- API contract tests
- end-to-end tests for critical user journeys
- AI workflow validation for prompts, outputs, and failure handling
- regression suites for recommendation safety boundaries

## Procedure

1. Identify critical workflows and highest-risk failure modes.
2. Define expected behavior for normal, edge, and invalid inputs.
3. Add deterministic tests for core logic before relying on UI or model behavior.
4. Validate schemas, data transformations, and permission boundaries.
5. Add scenario-based tests for clinician review, override, and audit paths.
6. Test missing-data, low-confidence, and conflicting-data conditions.
7. Ensure failures are explicit, safe, and observable.
8. Prioritize repeatable automated tests over manual-only validation.

## Helixora-Specific Quality Gates

- no silent failures in treatment recommendation generation
- explainability fields present when recommendations are returned
- incomplete patient data handled safely
- clinician approval paths remain auditable
- unsafe or unsupported recommendation patterns are blocked or flagged
- patient identity and privacy boundaries are preserved in test fixtures

## Deliverables

- test strategy by layer
- recommended test cases
- gaps in coverage
- validation criteria for medical AI flows
- suggestions for test data design

## Best Practices

- test domain logic independently of frameworks
- keep fixtures realistic but de-identified
- cover unhappy paths deliberately
- validate contracts at module and API boundaries
- treat safety checks as first-class test targets
