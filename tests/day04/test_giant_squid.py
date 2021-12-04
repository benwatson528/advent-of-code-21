import os
from pathlib import Path

from main.day04.giant_squid import solve_bingo


def test_winner_simple():
    assert solve_bingo(read_input("data/test_input.txt"), True) == 4512


def test_winner_real():
    assert solve_bingo(read_input("data/input.txt"), True) == 63552


def test_loser_simple():
    assert solve_bingo(read_input("data/test_input.txt"), False) == 1924


def test_loser_real():
    assert solve_bingo(read_input("data/input.txt"), False) == 9020


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        called_numbers = f.readline().strip('\n').split(',')
        f.readline()
        boards = []
        board = []
        for line in f.readlines():
            stripped_line = line.strip('\n')
            if not stripped_line:
                boards.append(board)
                board = []
            else:
                board.append(stripped_line.split())
        boards.append(board)
        return called_numbers, boards
