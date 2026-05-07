---
name: helixora-api-design
description: "Design and review Helixora AI APIs for clarity, safety, versioning, validation, and maintainability. Use for endpoint design, schema contracts, error handling, idempotency, clinician workflow APIs, and healthcare-grade backend best practices."
user-invocable: true
---

# Helixora API Design

## When to Use

- Design new APIs or review existing endpoints
- Improve request and response contracts
- Standardize validation and error handling
- Plan versioning and backward compatibility
- Build clinician, patient, or admin-facing backend interfaces
- Reduce ambiguity in healthcare and AI workflow integrations

## API Priorities

- explicit contracts
- strong validation
- safe defaults
- predictable errors
- versioned evolution
- permission-aware operations
- traceability for sensitive actions

## Procedure

1. Identify the domain action each endpoint represents.
2. Design schemas around domain concepts, not storage internals.
3. Validate required, optional, and derived fields explicitly.
4. Standardize error shapes and status code usage.
5. Define idempotency rules for write operations where relevant.
6. Ensure sensitive operations are authenticated, authorized, and auditable.
7. Keep recommendation generation and review endpoints semantically clear.
8. Prefer consistency across resources, naming, and pagination/filtering patterns.

## Helixora-Specific API Concerns

- patient-profile ingestion and updates
- genomic data submission and validation
- treatment recommendation generation and retrieval
- clinician review, approval, or override actions
- explanation and rationale payloads
- audit/event retrieval for regulated workflows

## Deliverables

- API structure recommendations
- schema and validation guidance
- endpoint naming and versioning suggestions
- error handling improvements
- risks in current API design

## Best Practices

- design around business meaning
- keep contracts stable and documented
- reject invalid inputs early
- avoid leaking internal implementation details
- ensure every sensitive mutation is attributable and reviewable
