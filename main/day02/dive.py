def solve_2d(commands) -> int:
    horizontal = 0
    vertical = 0
    for line in commands:
        direction = line[0]
        magnitude = int(line[1])
        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            vertical += magnitude
        elif direction == "up":
            vertical -= magnitude

    return horizontal * vertical


def solve_aim(commands) -> int:
    horizontal = 0
    vertical = 0
    aim = 0
    for line in commands:
        direction = line[0]
        magnitude = int(line[1])
        if direction == "forward":
            horizontal += magnitude
            vertical += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude

    return horizontal * vertical
