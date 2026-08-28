# Architecture

Ouroboros treats recursive self-improvement as a controlled experiment pipeline rather than an unconstrained self-modification loop.

## Core cycle

```text
Execute → Observe → Evaluate → Reflect → Mutate → Validate → Gate
                                                     │
                                   Promote ◄──────────┤
                                   Rollback ◄─────────┘
```

## Components

### Candidate
A versioned agent configuration. It may contain prompts, policies, tool selections, code references, model settings, or other mutable state.

### Runner
Executes a candidate against a task and produces a structured trace.

### Evaluator
Converts execution evidence into normalized scores and supporting metrics.

### Reflector
Produces a diagnosis of why the current candidate succeeded or failed.

### Mutator
Proposes a challenger candidate from the current candidate plus reflection evidence.

### Validator
Runs challenger candidates against evaluation and regression suites. In the initial implementation, validation is represented by re-running the evaluator; a dedicated validation abstraction will follow.

### Gate
Makes the final promotion decision. Gates should be deterministic where possible and should include regression constraints, minimum deltas, cost limits, and confidence thresholds.

### Memory
Stores experiment lineage, traces, evaluations, reflections, mutations, and promotion decisions so the system can learn from prior attempts without repeating failed strategies.

## Safety invariants

1. Every recursion is bounded by depth, time, token, and/or cost budgets.
2. A candidate cannot promote itself without an externalized gate decision.
3. Baseline and challenger evaluations must be comparable.
4. Promotion decisions must retain enough evidence for audit and rollback.
5. Capability expansion should require stricter gates than parameter or prompt changes.

## Near-term direction

The first implementation targets prompt/configuration-level improvement. Later layers may support tool creation, code mutation, memory optimization, and architecture search behind progressively stronger validation gates.
