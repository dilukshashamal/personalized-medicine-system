---
name: helixora-architecture-review
description: "Review and improve Helixora AI system architecture, service boundaries, data flow, maintainability, scalability, and engineering best practices. Use for system design review, refactoring guidance, module separation, technical debt reduction, backend/frontend/API structuring, and long-term maintainability planning."
user-invocable: true
---

# Helixora Architecture Review

## When to Use

- Review the overall system design
- Define clean boundaries between API, AI, data, and UI layers
- Reduce technical debt
- Improve maintainability and modularity
- Plan scalable healthcare platform architecture
- Standardize engineering best practices across the repository

## Goals

- Keep architecture modular and understandable
- Separate clinical logic, AI orchestration, data access, and presentation concerns
- Minimize coupling between services and modules
- Make future features easier to implement safely
- Support testing, auditing, and regulated-domain traceability

## Procedure

1. Identify the current application shape: API, frontend, data layer, AI workflows, background jobs, integrations.
2. Map responsibilities for each module and detect overlap.
3. Separate domain logic from framework-specific code.
4. Recommend stable contracts for APIs, events, and internal interfaces.
5. Ensure patient-data handling paths are explicit and traceable.
6. Check whether sensitive logic is isolated behind well-defined services.
7. Suggest refactors that improve readability, extensibility, and testability.
8. Document tradeoffs and propose incremental, low-risk improvements first.

## Architecture Priorities for Helixora AI

- Strong domain model for patient profile, genomic insights, treatment recommendation, and clinical review
- Explicit boundaries between recommendation generation and final clinician-facing output
- Clear handling for structured versus unstructured medical data
- Versioned schemas for high-trust healthcare workflows
- Explainability-friendly pipeline design
- Auditability for decisions and changes

## Output Expectations

When using this skill, provide:

- current-state findings
- architectural risks
- recommended structure changes
- quick wins vs longer-term improvements
- specific file/module suggestions when applicable

## Best Practices

- Prefer small, composable services
- Avoid business logic inside controllers, routes, or UI components
- Centralize validation and schema definitions
- Design for observability and security from the start
- Treat medical recommendation logic as a high-trust domain concern
