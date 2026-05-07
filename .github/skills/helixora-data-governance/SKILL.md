---
name: helixora-data-governance
description: "Establish data governance for Helixora AI across patient data handling, data quality, lineage, retention, consent, de-identification, and compliant data lifecycle practices. Use for healthcare data policy, dataset review, storage rules, and governance controls."
user-invocable: true
---

# Helixora Data Governance

## When to Use

- Define how patient and genomic data should be handled
- Improve data quality, lineage, and traceability
- Review retention, deletion, and consent-sensitive workflows
- Separate identifiable, de-identified, and derived datasets
- Add governance rules for AI training, inference, and analytics data
- Reduce compliance and operational risk around healthcare data

## Governance Focus Areas

- data classification
- lineage and provenance
- consent-aware processing
- retention and deletion rules
- de-identification and minimization
- dataset access controls
- auditability of data movement
- schema quality and stewardship

## Procedure

1. Identify data classes and sensitivity levels.
2. Map where data enters, moves, transforms, and is stored.
3. Define ownership and stewardship for each dataset.
4. Separate operational, analytical, and AI-specific data uses.
5. Review whether retention and deletion rules are explicit.
6. Check if consent and intended use affect downstream processing.
7. Recommend governance controls that are enforceable in code and operations.
8. Document high-risk gaps in lineage, quality, or access.

## Helixora-Specific Governance Needs

- clear handling of genomic and treatment recommendation artifacts
- separation of identifiable patient records from derived analytical outputs
- explicit rules for prompt inputs and model-generated outputs
- quality checks for medically relevant fields
- audit trails for data export, sharing, and transformation

## Deliverables

- governance findings
- recommended data classifications
- retention and handling guidelines
- lineage and ownership suggestions
- control recommendations for sensitive datasets

## Best Practices

- collect only what is needed
- keep lineage explicit
- separate data by sensitivity and purpose
- automate retention and deletion where possible
- make consent and intended use visible to downstream systems
