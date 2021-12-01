import os
from pathlib import Path

from main.day01.sonar_sweep import solve_pairs, solve_sliding


def test_two_simple():
    assert solve_pairs(read_input("data/test_input.txt")) == 7


def test_two_real():
    assert solve_pairs(read_input("data/input.txt")) == 1529


def test_three_simple():
    assert solve_sliding(read_input("data/test_input.txt")) == 5


def test_three_real():
    assert solve_sliding(read_input("data/input.txt")) == 1567


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
