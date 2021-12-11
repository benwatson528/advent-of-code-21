def solve(grid) -> int:
    num_flashes = 0
    for _ in range(100):
        flashed = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (y, x) in flashed:
                    continue
                elif grid[y][x] == 9:
                    grid[y][x] = 0
                    flashed.append((y, x))
                    flashed = bloom(grid, y, x, flashed)
                else:
                    grid[y][x] += 1
        num_flashes += len(flashed)
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
        if (new_y, new_x) in flashed or new_y < 0 or new_x < 0 or new_y >= len(grid) or new_x >= len(grid[new_y]):
            continue
        elif grid[new_y][new_x] == 9:
            grid[new_y][new_x] = 0
            flashed.append((new_y, new_x))
            flashed = bloom(grid, new_y, new_x, flashed)
        else:
            grid[new_y][new_x] += 1

    return flashed
