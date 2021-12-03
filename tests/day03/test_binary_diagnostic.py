import os
from pathlib import Path

from main.day03.binary_diagnostic import solve_power_consumption, solve_life_support


def test_power_consumption_simple():
    assert solve_power_consumption(read_input("data/test_input.txt")) == 198


def test_power_consumption_real():
    assert solve_power_consumption(read_input("data/input.txt")) == 3882564


def test_life_support_simple():
    assert solve_life_support(read_input("data/test_input.txt")) == 230


def test_life_support_real():
    assert solve_life_support(read_input("data/input.txt")) == 3385170


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
