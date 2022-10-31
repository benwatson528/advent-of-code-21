import os
from pathlib import Path

from main.day19.beacon_scanner import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 0


def test_real():
    assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
