"""Default promotion gates."""

from __future__ import annotations

from dataclasses import dataclass

from .core import Evaluation, GateDecision


@dataclass(frozen=True, slots=True)
class MinimumImprovementGate:
    """Promote only when the challenger clears a minimum score delta."""

    min_delta: float = 0.0

    def decide(self, baseline: Evaluation, challenger: Evaluation) -> GateDecision:
        delta = challenger.score - baseline.score
        promote = delta >= self.min_delta
        reason = (
            f"challenger improved score by {delta:.4f} (required {self.min_delta:.4f})"
            if promote
            else f"challenger delta {delta:.4f} is below required {self.min_delta:.4f}"
        )
        return GateDecision(promote=promote, reason=reason)
