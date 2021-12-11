import os
from pathlib import Path

from main.day11.dumbo_octopus import solve


def test_turns_simple():
    assert solve(read_input("data/test_input.txt"), False) == 1656


def test_turns_real():
    assert solve(read_input("data/input.txt"), False) == 1688


def test_sync_simple():
    assert solve(read_input("data/test_input.txt"), True) == 195


def test_sync_real():
    assert solve(read_input("data/input.txt"), True) == 403


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(list(map(int, line.strip('\n'))))
        return lines
