from dataclasses import dataclass


@dataclass(frozen=True)
class Instruction:
    on: bool
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int
