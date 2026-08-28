"""Minimal orchestration loop for evaluation-driven recursive improvement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .core import Candidate, Evaluation, GateDecision, Trace


class Runner(Protocol):
    def run(self, candidate: Candidate, input_data: object) -> Trace: ...


class Evaluator(Protocol):
    def evaluate(self, trace: Trace) -> Evaluation: ...


class Reflector(Protocol):
    def reflect(self, candidate: Candidate, trace: Trace, evaluation: Evaluation) -> str: ...


class Mutator(Protocol):
    def mutate(self, candidate: Candidate, reflection: str) -> Candidate: ...


class Gate(Protocol):
    def decide(self, baseline: Evaluation, challenger: Evaluation) -> GateDecision: ...


@dataclass(slots=True)
class ImprovementLoop:
    """One bounded improvement cycle: execute, evaluate, mutate, validate, gate."""

    runner: Runner
    evaluator: Evaluator
    reflector: Reflector
    mutator: Mutator
    gate: Gate

    def step(self, candidate: Candidate, input_data: object) -> tuple[Candidate, GateDecision]:
        baseline_trace = self.runner.run(candidate, input_data)
        baseline_eval = self.evaluator.evaluate(baseline_trace)

        reflection = self.reflector.reflect(candidate, baseline_trace, baseline_eval)
        challenger = self.mutator.mutate(candidate, reflection)

        challenger_trace = self.runner.run(challenger, input_data)
        challenger_eval = self.evaluator.evaluate(challenger_trace)
        decision = self.gate.decide(baseline_eval, challenger_eval)

        return (challenger if decision.promote else candidate, decision)
