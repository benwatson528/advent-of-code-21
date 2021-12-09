from math import prod


def solve_low_points(grid) -> int:
    return sum(grid[y][x] + 1 for (y, x) in find_low_points(grid))


def solve_basins(grid) -> int:
    low_points = find_low_points(grid)
    basins = []
    for low_point in low_points:
        basin_locations = set()
        basin_locations.add(low_point)
        basins.append(solve_basins_rec(grid, low_point, set(), basin_locations))
    basins.sort(key=lambda x: len(x))
    return prod(len(x) for x in basins[-3:])


def solve_basins_rec(grid, current, visited, basin_locations):
    (y, x) = current
    for new_y, new_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if 0 <= new_y < len(grid) \
                and 0 <= new_x < len(grid[new_y]) \
                and (new_y, new_x) not in visited \
                and grid[new_y][new_x] > grid[y][x] \
                and grid[new_y][new_x] != 9:
            visited.add(current)
            basin_locations.add((new_y, new_x))
            solve_basins_rec(grid, (new_y, new_x), visited, basin_locations)
    return basin_locations


def find_low_points(grid):
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current = grid[y][x]
            above = grid[y - 1][x] if y >= 1 else 10
            below = grid[y + 1][x] if y <= len(grid) - 2 else 10
            left = grid[y][x - 1] if x >= 1 else 10
            right = grid[y][x + 1] if x <= len(grid[y]) - 2 else 10
            if current < above and current < below and current < left and current < right:
                low_points.append((y, x))
    return low_points
