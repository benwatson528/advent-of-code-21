from dataclasses import dataclass

from day21.Player import Player


@dataclass(frozen=True)
class State:
    player_1: Player
    player_2: Player
