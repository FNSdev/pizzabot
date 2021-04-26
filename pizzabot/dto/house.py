from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class House:
    x: int
    y: int
    id: str = field(default_factory=lambda: str(uuid4()))
