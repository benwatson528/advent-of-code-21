import json
import os
from pathlib import Path

from main.day18.snailfish import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 4140


def test_real():
    assert solve(read_input("data/input.txt")) == 3486


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(json.loads(line))
    return lines
