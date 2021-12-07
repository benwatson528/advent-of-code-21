import sys


def solve_constant_burn(crabs) -> int:
    min_fuel = sys.maxsize
    for i in range(min(crabs), max(crabs) + 1):
        min_fuel = min(min_fuel, sum(abs(crab - i) for crab in crabs))
    return min_fuel


def solve_increasing_burn(crabs) -> int:
    min_fuel = sys.maxsize
    for i in range(min(crabs), max(crabs) + 1):
        total_moved = 0
        for crab in crabs:
            distance = abs(crab - i)
            total_moved += (distance * (distance + 1)) / 2
        min_fuel = min(min_fuel, total_moved)
    return min_fuel
