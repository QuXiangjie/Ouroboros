"""Ouroboros: a harness for recursive self-improvement."""

from .core import Candidate, Evaluation, GateDecision, Trace
from .loop import ImprovementLoop

__all__ = [
    "Candidate",
    "Evaluation",
    "GateDecision",
    "Trace",
    "ImprovementLoop",
]

__version__ = "0.1.0"
