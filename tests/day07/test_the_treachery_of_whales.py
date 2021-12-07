import os
from pathlib import Path

from main.day07.the_treachery_of_whales import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 37


def test_real():
    assert solve(read_input("data/input.txt")) == 3


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return list(map(int, f.readline().strip('\n').split(',')))
