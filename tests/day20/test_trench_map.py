import os
from pathlib import Path

from main.day20.trench_map import solve


def test_2_steps_simple():
    algorithm, input_image = read_input("data/test_input.txt")
    assert solve(algorithm, input_image, 2) == 35


def test_2_steps_real():
    algorithm, input_image = read_input("data/input.txt")
    assert solve(algorithm, input_image, 2) == 5395


def test_50_steps_simple():
    algorithm, input_image = read_input("data/test_input.txt")
    assert solve(algorithm, input_image, 50) == 3351


def test_50_steps_real():
    algorithm, input_image = read_input("data/input.txt")
    assert solve(algorithm, input_image, 50) == 5395


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        algorithm = f.readline().strip('\n')
        f.readline()

        input_image = []
        for line in f.readlines():
            input_image.append(line.strip('\n'))
        return algorithm, input_image
