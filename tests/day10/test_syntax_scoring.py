import os
from pathlib import Path

from main.day10.syntax_scoring import solve_invalid, solve_corrupted


def test_invalid_simple():
    assert solve_invalid(read_input("data/test_input.txt")) == 26397


def test_invalid_real():
    assert solve_invalid(read_input("data/input.txt")) == 415953


def test_corrupted_simple():
    assert solve_corrupted(read_input("data/test_input.txt")) == 288957


def test_corrupted_real():
    assert solve_corrupted(read_input("data/input.txt")) == 2292863731


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
