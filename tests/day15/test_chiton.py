import os
from pathlib import Path

from main.day15.chiton import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 40


def test_real():
    assert solve(read_input("data/input.txt")) == 389  # not 384, 389


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(list(map(int, line.strip('\n'))))
        return lines
