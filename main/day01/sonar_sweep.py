def solve_pairs(x) -> int:
    return sum(1 if b > a else 0 for a, b in zip(x, x[1:]))


def solve_sliding(x) -> int:
    return sum(1 if b + c + d > a + b + c else 0 for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))
