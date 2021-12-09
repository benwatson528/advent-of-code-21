import os
from pathlib import Path

from main.day09.smoke_basin import solve_low_points, solve_basins


def test_low_points_simple():
    assert solve_low_points(read_input("data/test_input.txt")) == 15


def test_low_points_real():
    assert solve_low_points(read_input("data/input.txt")) == 504


def test_basins_simple():
    assert solve_basins(read_input("data/test_input.txt")) == 1134


def test_basins_real():
    assert solve_basins(read_input("data/input.txt")) == 1558722


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(list(int(c) for c in line.strip('\n')))
        return lines
