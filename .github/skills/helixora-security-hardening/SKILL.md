---
name: helixora-security-hardening
description: "Harden Helixora AI for healthcare-grade security, privacy, and secure coding practices. Use for threat review, patient-data protection, auth/authz, secrets handling, dependency risk reduction, API hardening, secure defaults, and remediation planning."
user-invocable: true
---

# Helixora Security Hardening

## When to Use

- Review security posture of the codebase
- Protect patient and genomic data
- Improve authentication and authorization design
- Harden APIs, services, and storage access
- Reduce vulnerabilities in dependencies and configuration
- Add secure coding and privacy-preserving patterns

## Security Focus Areas

- authentication and session management
- role-based or attribute-based access control
- encryption in transit and at rest
- secure secret storage and rotation
- audit logging for access to sensitive operations
- secure input validation and output encoding
- dependency and supply-chain hygiene
- least-privilege infrastructure and service permissions

## Procedure

1. Identify sensitive assets: patient data, genomic data, treatment plans, clinician actions, tokens, secrets.
2. Review entry points: APIs, forms, uploads, admin tools, model prompts, integrations.
3. Check for missing validation, overexposed endpoints, and insecure defaults.
4. Review how secrets, keys, and environment variables are handled.
5. Verify access controls for patient-specific workflows.
6. Review data retention and logging to avoid leaking regulated data.
7. Recommend fixes with severity and implementation order.
8. Prefer secure-by-default refactors over patchwork mitigations.

## Helixora-Specific Guardrails

- Never expose raw PHI/PII unnecessarily in logs or traces
- Avoid placing sensitive data in prompts unless required and controlled
- Mask or tokenize patient identifiers where possible
- Keep recommendation review and approval actions auditable
- Ensure every sensitive operation has an accountable actor or service identity

## Deliverables

- prioritized security findings
- concrete code/config fixes
- secure architecture recommendations
- privacy and compliance-sensitive logging guidance
- follow-up validation checklist

## Best Practices

- deny by default
- validate all inputs
- minimize sensitive data movement
- rotate and isolate secrets
- apply least privilege everywhere
- treat AI inputs and outputs as security-sensitive surfaces
