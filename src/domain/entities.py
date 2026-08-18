from dataclasses import dataclass


@dataclass
class Workplace:
    id: int
    name: str
    is_available: bool = True
