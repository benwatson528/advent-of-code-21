import os
from pathlib import Path

from main.day20.trench_map import solve


def test_simple():
    algorithm, input_image = read_input("data/test_input.txt")
    assert solve(algorithm, input_image, 2) == 35


def test_real():
    algorithm, input_image = read_input("data/input.txt")
    assert solve(algorithm, input_image, 2) == 5504 # 5504 too high


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        algorithm = f.readline().strip('\n')
        f.readline()

        input_image = []
        for line in f.readlines():
            input_image.append(line.strip('\n'))
        return algorithm, input_image
