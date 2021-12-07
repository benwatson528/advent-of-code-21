import os
from pathlib import Path

from main.day07.the_treachery_of_whales import solve_constant_burn, solve_increasing_burn


def test_constant_burn_simple():
    assert solve_constant_burn(read_input("data/test_input.txt")) == 37


def test_constant_burn_real():
    assert solve_constant_burn(read_input("data/input.txt")) == 349812


def test_increasing_burn_simple():
    assert solve_increasing_burn(read_input("data/test_input.txt")) == 168


def test_increasing_burn_real():
    assert solve_increasing_burn(read_input("data/input.txt")) == 99763899


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return list(map(int, f.readline().strip('\n').split(',')))
