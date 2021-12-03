import operator
from collections import Counter


def solve_power_consumption(l) -> int:
    return int(build_binary(l, operator.gt), 2) * int(build_binary(l, operator.lt), 2)


def build_binary(l, op):
    return ''.join(str(1) if op(Counter(x)['1'], Counter(x)['0']) else str(0) for x in list(map(list, zip(*l))))


def solve_life_support(l) -> int:
    return int(solve_life_support_rec(l, operator.ge, 0), 2) * int(solve_life_support_rec(l, operator.lt, 0), 2)


def solve_life_support_rec(l, op, i):
    filtered = list(filter(lambda x: (x[i] == build_binary(l, op)[i]), l))
    return filtered[0] if len(filtered) == 1 else solve_life_support_rec(filtered, op, i + 1)
