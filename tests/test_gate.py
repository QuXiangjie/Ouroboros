from ouroboros.core import Evaluation
from ouroboros.gates import MinimumImprovementGate


def test_promotes_when_delta_clears_threshold() -> None:
    gate = MinimumImprovementGate(min_delta=0.05)
    baseline = Evaluation(score=0.70)
    challenger = Evaluation(score=0.76)

    decision = gate.decide(baseline, challenger)

    assert decision.promote is True


def test_rejects_regression() -> None:
    gate = MinimumImprovementGate(min_delta=0.01)
    baseline = Evaluation(score=0.80)
    challenger = Evaluation(score=0.79)

    decision = gate.decide(baseline, challenger)

    assert decision.promote is False
