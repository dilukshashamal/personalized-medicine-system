---
name: helixora-medical-ai-guardrails
description: "Apply medical AI guardrails and high-trust best practices for Helixora AI. Use for treatment recommendation safety, explainability, clinician oversight, prompt safety, model output review, evidence-aware reasoning, bias reduction, and healthcare AI governance."
user-invocable: true
---

# Helixora Medical AI Guardrails

## When to Use

- Design or review AI recommendation workflows
- Improve treatment recommendation safety
- Add explainability and evidence-aware outputs
- Strengthen clinician-in-the-loop controls
- Review prompts, model behavior, and output constraints
- Reduce unsafe, overconfident, or low-quality AI behavior

## Objectives

- Keep AI recommendations bounded, reviewable, and explainable
- Ensure the system supports clinicians instead of replacing them
- Reduce hallucinations and unsafe recommendation patterns
- Improve traceability from inputs to outputs
- Align AI behavior with healthcare-grade governance expectations

## Procedure

1. Identify where AI is used: summarization, retrieval, ranking, recommendation generation, explanation generation.
2. Define the clinical risk level for each workflow.
3. Add explicit constraints for what the model may and may not do.
4. Require rationale and confidence framing for recommendation outputs.
5. Add fallback behavior for uncertainty, missing data, or low-confidence cases.
6. Ensure human review checkpoints exist before high-impact actions.
7. Review prompts and output schemas for ambiguity or overreach.
8. Recommend safer patterns for evidence grounding and result presentation.

## Guardrails for Helixora AI

- never present AI output as a final medical decision
- clearly distinguish evidence, inference, and suggestion
- surface uncertainty and missing-data limitations
- prefer structured outputs for treatment suggestions and rationales
- capture clinician review or override actions
- avoid unsupported claims of efficacy or safety
- maintain boundaries around intended use

## Deliverables

- guardrail recommendations
- safer prompt/output design guidance
- clinician oversight checkpoints
- explainability requirements
- validation criteria for high-stakes recommendation flows

## Best Practices

- make uncertainty visible
- require structured, reviewable outputs
- keep evidence links or rationale paths where possible
- fail safely on incomplete data
- use narrow, domain-scoped prompts rather than open-ended generation
