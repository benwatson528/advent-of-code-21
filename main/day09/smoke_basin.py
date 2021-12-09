def solve(grid) -> int:
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current = grid[y][x]
            above = grid[y - 1][x] if y >= 1 else 10
            below = grid[y + 1][x] if y <= len(grid) - 2 else 10
            left = grid[y][x - 1] if x >= 1 else 10
            right = grid[y][x + 1] if x <= len(grid[y]) - 2 else 10
            if current < above and current < below and current < left and current < right:
                low_points.append(current)

    return sum(x + 1 for x in low_points)
