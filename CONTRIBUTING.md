# Contributing

Thanks for helping improve Ouroboros.

## Development workflow

1. Create a focused branch from `main`.
2. Keep changes small and testable.
3. Add or update tests for behavioral changes.
4. Run `ruff check .` and `pytest` locally.
5. Open a pull request describing the motivation, behavior change, and validation evidence.

## Design expectations

Changes to the recursive improvement loop should preserve three properties:

- **Observability:** decisions and state transitions are inspectable.
- **Comparability:** baseline and challenger results are evaluated consistently.
- **Reversibility:** promoted changes can be traced and rolled back.

For changes that expand agent capabilities, include stronger validation and explicit guardrails.
