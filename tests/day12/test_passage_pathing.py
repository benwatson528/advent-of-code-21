import os
from pathlib import Path

from main.day12.passage_pathing import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 10


def test_real():
    assert solve(read_input("data/input.txt")) == 5212


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n').split('-'))
        return lines
