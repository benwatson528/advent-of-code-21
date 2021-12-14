import os
from pathlib import Path

from main.day14.extended_polymerization import solve


def test_ten_turns_simple():
    assert solve(read_input("data/test_input.txt"), 10) == 1588


def test_ten_turns_real():
    assert solve(read_input("data/input.txt"), 10) == 2584


def test_forty_turns_simple():
    assert solve(read_input("data/test_input.txt"), 40) == 2188189693529


def test_forty_turns_real():
    assert solve(read_input("data/input.txt"), 40) == 2584


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        template = f.readline().strip('\n')
        f.readline()
        rules = {}
        for line in f.readlines():
            split_line = line.strip('\n').split(' -> ')
            rules[split_line[0]] = split_line[1]
        return template, rules
