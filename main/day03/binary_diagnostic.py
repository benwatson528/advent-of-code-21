import operator
from collections import Counter


def solve(l) -> int:
    gamma = build_binary(l, operator.gt)
    epsilon = build_binary(l, operator.lt)

    return int(gamma, 2) * int(epsilon, 2)


def build_binary(l, relate):
    binary = ""
    for col in list(map(list, zip(*l))):
        counter = Counter(col)
        binary += str(1) if relate(counter['1'], counter['0']) else str(0)
    return binary
