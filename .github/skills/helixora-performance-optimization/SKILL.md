---
name: helixora-performance-optimization
description: "Optimize Helixora AI performance, reliability, and cost efficiency. Use for latency reduction, AI inference efficiency, query optimization, caching strategy, background job tuning, concurrency control, scalability review, and resource usage improvements."
user-invocable: true
---

# Helixora Performance Optimization

## When to Use

- Reduce slow API or UI interactions
- Improve AI recommendation latency
- Optimize data processing and storage access
- Reduce infrastructure cost for compute-heavy workflows
- Tune background jobs and queue-based processing
- Improve scalability under growing patient and clinician workloads

## Optimization Areas

- API response time
- database/query efficiency
- model invocation overhead
- caching strategy
- batching and asynchronous workflows
- queue and worker throughput
- memory and CPU efficiency
- network call reduction

## Procedure

1. Identify the slowest user-facing and background workflows.
2. Measure bottlenecks before proposing fixes.
3. Separate compute-bound, I/O-bound, and model-bound costs.
4. Review repeated queries, redundant transformations, and chatty integrations.
5. Add caching where correctness and freshness rules allow it.
6. Move non-critical work out of request paths when possible.
7. Validate reliability and correctness after optimization.
8. Prefer maintainable performance improvements over fragile micro-optimizations.

## Helixora-Specific Optimization Targets

- genomic data parsing and normalization
- recommendation generation pipeline latency
- retrieval and summarization overhead
- clinician dashboard load performance
- patient timeline/history aggregation
- batch analysis workflows for research cohorts

## Deliverables

- identified bottlenecks
- prioritized optimization plan
- code-level and architecture-level suggestions
- expected performance impact
- validation approach after changes

## Best Practices

- benchmark first
- optimize highest-value paths first
- protect correctness and explainability
- define latency budgets for critical workflows
- use caching carefully in regulated domains
