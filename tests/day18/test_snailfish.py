import json
import os
from pathlib import Path

from main.day18.snailfish import solve, solve_max_magnitude


def test_part_1_simple():
    assert solve(read_input("data/test_input.txt")) == 4140


def test_part_1_real():
    assert solve(read_input("data/input.txt")) == 3486


def test_part_2_simple():
    assert solve_max_magnitude(read_input("data/test_input.txt")) == 3993


def test_part_2_real():
    assert solve_max_magnitude(read_input("data/input.txt")) == 4747


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(json.loads(line))
    return lines
