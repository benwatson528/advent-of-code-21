import os
from pathlib import Path

from day05.Line import Line
from main.day05.hydrothermal_venture import solve


def test_straight_simple():
    assert solve(read_input("data/test_input.txt"), False) == 5


def test_straight_real():
    assert solve(read_input("data/input.txt"), False) == 6687


def test_diagonal_simple():
    assert solve(read_input("data/test_input.txt"), True) == 12


def test_diagonal_real():
    assert solve(read_input("data/input.txt"), True) == 19851


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            split_line = line.strip('\n').split(" -> ")
            x1, y1 = split_line[0].split(",")
            x2, y2 = split_line[1].split(",")
            lines.append(Line(int(x1), int(y1), int(x2), int(y2)))
        return lines
