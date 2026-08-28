# Ouroboros

> **A harness for recursive self-improvement.**

Ouroboros is an evaluation-driven harness for building agents that can inspect, propose, test, and promote improvements to themselves under explicit guardrails.

The project is organized around a controlled recursive loop:

```text
Execute → Observe → Evaluate → Reflect → Mutate → Validate → Promote / Rollback
```

## Why Ouroboros?

The ouroboros is a symbol of recursion and self-reference. The project mark is intentionally designed to also resemble the letter **Q** while remaining visibly an ouroboros.

## Design principles

- **Evaluation before promotion** — no change is accepted without measurable evidence.
- **Rollback by default** — regressions should be cheap to reverse.
- **Trace everything** — every proposal, evaluation, and decision should be inspectable.
- **Model-agnostic** — adapters should work across model providers and agent frameworks.
- **Composable** — runners, evaluators, mutators, gates, and memory should be independently replaceable.
- **Safe recursion** — recursion depth, budgets, capabilities, and promotion criteria must be bounded.

## Architecture

```text
Agent / Candidate
      │
      ▼
    Runner
      │
      ▼
    Trace
      │
      ▼
  Evaluator
      │
      ▼
  Reflector
      │
      ▼
   Mutator
      │
      ▼
  Validator
      │
      ▼
     Gate ───────► Promote
      │
      └──────────► Rollback
```

## Status

Ouroboros is currently in early development. The first milestone is a minimal, provider-agnostic improvement loop with deterministic evals and explicit promotion gates.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Roadmap

1. Core loop contracts and typed traces
2. Pluggable evaluator interface
3. Reflection and mutation strategies
4. Regression-aware promotion gate
5. Persistent experiment memory
6. Provider and agent-framework adapters
7. Benchmark harness and experiment dashboard

## License

MIT
