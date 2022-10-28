from dataclasses import dataclass


@dataclass(frozen=True)
class Bounds:
    min_x: int
    max_x: int
    min_y: int
    max_y: int
