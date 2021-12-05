def solve(lines) -> int:
    max_x, max_y = find_grid_bounds(lines)
    grid = [[0 for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1)]
    draw_horizontal_lines(lines, grid)
    draw_vertical_lines(lines, grid)
    return find_most_dangerous(grid)


def find_grid_bounds(lines):
    max_x = max(lines, key=lambda l: max(l.x1, l.x2))
    max_y = max(lines, key=lambda l: max(l.y1, l.y2))
    return max(max_x.x1, max_x.x2), max(max_y.y1, max_y.y2)


def draw_horizontal_lines(lines, grid):
    horizontal_lines = filter(lambda l: l.y1 == l.y2, lines)
    for l in horizontal_lines:
        for x in range(min(l.x1, l.x2), max(l.x1, l.x2) + 1):
            grid[x][l.y1] += 1


def draw_vertical_lines(lines, grid):
    vertical_lines = filter(lambda l: l.x1 == l.x2, lines)
    for l in vertical_lines:
        for y in range(min(l.y1, l.y2), max(l.y1, l.y2) + 1):
            grid[l.x1][y] += 1


def find_most_dangerous(grid):
    most_dangerous = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] > 1:
                most_dangerous += 1
    return most_dangerous
