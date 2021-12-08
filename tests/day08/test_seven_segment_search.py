import os
from pathlib import Path

from main.day08.seven_segment_search import solve_unique, solve_decode


def test_unique_simple():
    assert solve_unique(read_input("data/test_input.txt")) == 26


def test_unique_real():
    assert solve_unique(read_input("data/input.txt")) == 310


def test_decode_simple():
    assert solve_decode(read_input("data/test_input.txt")) == 61229


def test_decode_real():
    assert solve_decode(read_input("data/input.txt")) == 915941


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            signals, output = line.strip('\n').split(' | ')
            lines.append((signals.split(), output.split()))
        return lines
