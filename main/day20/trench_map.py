def solve(algorithm, input_image, steps) -> int:
    for _ in range(steps):
        input_image = generate_image(algorithm, input_image)
    return [pixel for sublist in input_image for pixel in sublist].count('#')


def generate_image(algorithm, input_image):
    output_image = []
    for x in range(-1, len(input_image) + 1):
        output_row = []
        for y in range(-1, len(input_image[0]) + 1):
            grid = get_grid(input_image, x, y)
            decimal = grid_to_decimal(grid)
            new_pixel = algorithm[decimal]
            output_row.append(new_pixel)
        output_image.append(output_row)
    return output_image


def get_grid(input_image, centre_x, centre_y):
    grid = []
    for i in [-1, 0, 1]:
        row = []
        for j in [-1, 0, 1]:
            if 0 <= centre_x + i < len(input_image) and 0 <= centre_y + j < len(input_image[i]):
                row.append(input_image[centre_x + i][centre_y + j])
            else:
                row.append('.')
        grid.append(row)
    return grid


def grid_to_decimal(grid):
    binary = ''.join(['0' if item == '.' else '1' for sublist in grid for item in sublist])
    return int(binary, 2)
