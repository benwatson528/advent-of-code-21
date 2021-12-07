def solve(crabs) -> int:
    min_fuel = 999999
    for i in range(min(crabs), max(crabs) + 1):
        fuel_cost = 0
        for crab in crabs:
            abs1 = abs(crab - i)
            fuel_cost += abs1
        min_fuel = min(min_fuel, fuel_cost)

    return min_fuel
