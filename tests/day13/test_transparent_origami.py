import os
from pathlib import Path

from main.day13.transparent_origami import solve


def test_first_fold_simple():
    assert solve(read_input("data/test_input.txt"), first_fold=True) == 17


def test_first_fold_real():
    assert solve(read_input("data/input.txt"), first_fold=True) == 706


def test_full_simple():
    assert solve(read_input("data/test_input.txt"), first_fold=False) == 16


def test_full_real():
    assert solve(read_input("data/input.txt"), first_fold=False) == 95


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        coords = []
        folds = []
        for line in f:
            stripped = line.strip('\n')
            if len(stripped) == 0:
                continue
            elif stripped.startswith('fold'):
                fold_split = stripped.split('fold along ')[1]
                axis, pos = fold_split.split('=')[0], fold_split.split('=')[1]
                folds.append((axis, pos))
            else:
                x, y = stripped.split(',')[0], stripped.split(',')[1]
                coords.append((int(x), int(y)))
        return coords, folds
