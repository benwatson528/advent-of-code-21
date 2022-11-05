from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    score: int
    position: int
