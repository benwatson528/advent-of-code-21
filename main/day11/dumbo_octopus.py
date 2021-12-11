def solve(grid, sync) -> int:
    num_flashes = 0
    for i in range(9999999 if sync else 100):
        flashed = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                flashed = evolve(grid, y, x, flashed)
        num_flashes += len(flashed)
        if all(item == 0 for sublist in grid for item in sublist):
            return i + 1
    return num_flashes


def bloom(grid, y, x, flashed):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return flashed
    for new_y, new_x in (
            (y + 1, x),
            (y - 1, x),
            (y, x + 1),
            (y, x - 1),
            (y + 1, x + 1),
            (y + 1, x - 1),
            (y - 1, x + 1),
            (y - 1, x - 1)):
        flashed = evolve(grid, new_y, new_x, flashed)
    return flashed


def evolve(grid, y, x, flashed):
    if (y, x) in flashed or y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return flashed
    elif grid[y][x] == 9:
        grid[y][x] = 0
        flashed.append((y, x))
        flashed = bloom(grid, y, x, flashed)
    else:
        grid[y][x] += 1
    return flashed
