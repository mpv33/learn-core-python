"""Shared agent types."""

from dataclasses import dataclass, field


@dataclass
class AgentStep:
    agent: str
    action: str
    detail: str
    output: str = ""


@dataclass
class AgentResult:
    agent: str
    answer: str
    sources: list[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
