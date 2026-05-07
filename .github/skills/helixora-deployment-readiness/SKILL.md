---
name: helixora-deployment-readiness
description: "Prepare Helixora AI for reliable deployment and operations. Use for environment readiness, configuration review, release safety, secrets and config hygiene, operational checklists, rollback planning, and production best practices."
user-invocable: true
---

# Helixora Deployment Readiness

## When to Use

- Prepare the system for staging or production deployment
- Review environment and configuration safety
- Improve release readiness and rollback planning
- Check secrets, config, and runtime assumptions
- Add operational checklists for reliable launches
- Reduce production risk before shipping healthcare workflows

## Readiness Areas

- environment parity
- configuration validation
- secret and credential handling
- dependency and migration readiness
- rollout and rollback planning
- health checks and alert readiness
- operational ownership and runbooks

## Procedure

1. Identify required environments, dependencies, and runtime services.
2. Review config values for safety, defaults, and secret separation.
3. Check startup assumptions, migrations, background workers, and scheduled jobs.
4. Ensure health endpoints, alerts, and dashboards exist for critical workflows.
5. Verify failure and rollback paths are documented and practical.
6. Review deployment impact on data integrity and recommendation continuity.
7. Validate release readiness for regulated, high-trust features.
8. Produce a checklist for pre-deploy and post-deploy verification.

## Helixora-Specific Readiness Checks

- recommendation workflows fail safely under degraded dependencies
- protected configs are never committed or exposed
- observability covers release-critical medical workflows
- data migrations preserve traceability and audit requirements
- clinician-facing features degrade predictably if AI or data subsystems fail

## Deliverables

- deployment readiness findings
- release checklist
- config and secret hygiene recommendations
- operational gaps and risks
- rollback and verification suggestions

## Best Practices

- prefer explicit config validation at startup
- separate secrets from code and non-sensitive config
- make rollback easy and tested
- verify critical workflows after every release
- treat deployment as an operational capability, not a one-time step
