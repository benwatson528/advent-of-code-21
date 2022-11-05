from collections import Counter


def solve(algorithm, input_image_list, steps) -> int:
    input_image = image_to_set(input_image_list)
    print_image(input_image)
    for step in range(steps):
        input_image = generate_image(algorithm, input_image, step)
    return len(input_image)


def image_to_set(input_image):
    s = set()
    for i in range(len(input_image)):
        for j in range((len(input_image[i]))):
            if input_image[i][j] == '#':
                s.add((i, j))
    return s


def generate_image(algorithm, input_image, step):
    output_image = set()
    min_x = min(x[0] for x in input_image)
    min_y = min(y[1] for y in input_image)
    max_x = max(x[0] for x in input_image)
    max_y = max(y[1] for y in input_image)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            surroundings = get_surroundings(input_image, x, y, step)
            decimal = grid_to_decimal(surroundings)
            new_value = algorithm[decimal]
            if new_value == '#':
                output_image.add((x, y))
    print_image(output_image)
    return output_image


def get_surroundings(input_image, centre_x, centre_y, step):
    # each time we expand by one in each direction, so we just need to trim the excess
    infinite_value = '#' if step % 2 == 0 else '.'
    grid = []
    for i in [-1, 0, 1]:
        row = []
        for j in [-1, 0, 1]:
            row.append('#' if (centre_x + i, centre_y + j) in input_image else '.')
        grid.append(row)
    return grid


def grid_to_decimal(grid):
    binary = ''.join(['0' if item == '.' else '1' for sublist in grid for item in sublist])
    return int(binary, 2)


def print_image(image):
    min_x = min(x[0] for x in image)
    min_y = min(y[1] for y in image)
    max_x = max(x[0] for x in image)
    max_y = max(y[1] for y in image)
    print()
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            print('#' if (x, y) in image else '.', end='')
        print()
