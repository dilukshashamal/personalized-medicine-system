# Helixora AI Repository Instructions

## Project Context

- Helixora AI is a high-trust personalized medicine system.
- Prioritize patient safety, clinician oversight, explainability, privacy, and auditability.
- Treat all recommendation logic as decision support, not autonomous medical decision-making.

## Engineering Priorities

- Prefer clear, maintainable, modular code over clever shortcuts.
- Keep business and clinical logic out of controllers, routes, and UI layers.
- Use strong schemas and explicit validation at system boundaries.
- Design for observability, security, and testability from the start.
- Minimize coupling between AI orchestration, domain logic, and infrastructure code.

## Medical AI Guardrails

- Never frame AI outputs as final medical advice.
- Make uncertainty, assumptions, and missing-data limitations visible.
- Prefer structured outputs for recommendations, rationales, and review states.
- Ensure clinician review or override paths remain explicit and auditable.
- Avoid unsupported claims about efficacy, safety, or clinical certainty.

## Security and Privacy

- Do not expose secrets, tokens, PHI, PII, or genomic data in code, logs, tests, or examples.
- Prefer de-identified or synthetic test data.
- Apply least privilege to services, data access, and integrations.
- Avoid storing sensitive data in prompts, telemetry, or client-visible payloads unless explicitly required.

## Observability and Operations

- Prefer structured logs with correlation IDs.
- Add audit events for sensitive actions and recommendation lifecycle changes.
- Instrument critical workflows with metrics and traces.
- Ensure failures are diagnosable without leaking sensitive data.

## Quality Standards

- Add or update tests for meaningful behavior changes.
- Validate unhappy paths, low-confidence flows, and missing-data scenarios.
- Preserve backward-compatible contracts unless a breaking change is clearly intended.
- Document important architectural or safety tradeoffs in code comments or docs when needed.

## When Working in This Repo

- Use the Helixora skill files under `.github/skills/` when the task matches their domain.
- Recommend incremental improvements when requirements are ambiguous.
- Favor safe defaults and explicit constraints in every layer.
