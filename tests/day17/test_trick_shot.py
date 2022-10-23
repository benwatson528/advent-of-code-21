import os
from pathlib import Path

from main.day17.trick_shot import solve


def test_simple():
    assert solve("target area: x=20..30, y=-10..-5") == 0


def test_real():
    assert solve("target area: x=128..160, y=-142..-88") == 0

