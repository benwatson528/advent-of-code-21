import os
from pathlib import Path

from main.day02.dive import solve_2d, solve_aim


def test_2d_simple():
    assert solve_2d(read_input("data/test_input.txt")) == 150


def test_2d_real():
    assert solve_2d(read_input("data/input.txt")) == 1990000


def test_aim_simple():
    assert solve_aim(read_input("data/test_input.txt")) == 900


def test_aim_real():
    assert solve_aim(read_input("data/input.txt")) == 1975421260


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n').split(' '))
        return lines
