import os
from pathlib import Path

from main.day12.passage_pathing import solve_limited, solve_unlimited


def test_unlimited_simple():
    assert solve_unlimited(read_input("data/test_input.txt")) == 10


def test_unlimited_real():
    assert solve_unlimited(read_input("data/input.txt")) == 5212


def test_limited_simple():
    assert solve_limited(read_input("data/test_input.txt")) == 36


def test_limited_real():
    assert solve_limited(read_input("data/input.txt")) == 134862


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n').split('-'))
        return lines
