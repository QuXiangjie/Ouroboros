"""Core value objects used by the Ouroboros improvement loop."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class Candidate:
    """A versioned agent configuration eligible for evaluation and promotion."""

    id: str
    payload: Mapping[str, Any]
    parent_id: str | None = None
    generation: int = 0


@dataclass(frozen=True, slots=True)
class Trace:
    """Observable execution evidence produced by running a candidate."""

    candidate_id: str
    input: Any
    output: Any
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class Evaluation:
    """A normalized score plus supporting metrics for a candidate run."""

    score: float
    metrics: Mapping[str, float] = field(default_factory=dict)
    notes: str = ""


@dataclass(frozen=True, slots=True)
class GateDecision:
    """The promotion gate's decision for a proposed candidate."""

    promote: bool
    reason: str
