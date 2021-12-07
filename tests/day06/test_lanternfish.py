import os
from pathlib import Path

from main.day06.lanternfish import solve


def test_80_simple():
    assert solve(read_input("data/test_input.txt"), 80) == 5934


def test_80_real():
    assert solve(read_input("data/input.txt"), 80) == 390923


def test_256_simple():
    assert solve(read_input("data/test_input.txt"), 256) == 26984457539


def test_256_real():
    assert solve(read_input("data/input.txt"), 256) == 1749945484935


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return list(map(int, f.readline().strip('\n').split(',')))
