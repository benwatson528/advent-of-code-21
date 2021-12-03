import operator
from collections import Counter


def solve(l) -> int:
    return build_binary(l, operator.gt) * build_binary(l, operator.lt)


def build_binary(l, relate):
    return int(
        ''.join(str(1) if relate(Counter(x)['1'], Counter(x)['0']) else str(0) for x in list(map(list, zip(*l)))), 2)
