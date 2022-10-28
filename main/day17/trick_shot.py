import itertools

from day17.Bounds import Bounds


def solve(bounds: Bounds) -> int:
    max_y = float('-inf')
    for starting_v in itertools.product(range(100), range(0, 1000)):
        y = move((0, 0), starting_v, bounds, float('-inf'), 0, False)
        max_y = y if y is not None and y > max_y else max_y
    return max_y


def move(current, velocity, bounds, overall_max_y, i, hit_target):
    if is_in_target_area(current, bounds):
        return overall_max_y
    else:
        if i == 500:
            return None
        new_position = (current[0] + velocity[0], current[1] + velocity[1])
        new_velocity = update_velocity(velocity)
        return move(new_position, new_velocity, bounds, max(current[1], overall_max_y), i + 1, hit_target)


def update_velocity(velocity):
    velocity_x = velocity[0]
    if velocity_x != 0:
        velocity_x = velocity_x - 1 if velocity_x > 0 else velocity_x + 1
    new_velocity = (velocity_x, velocity[1] - 1)
    return new_velocity


def is_in_target_area(current, bounds):
    return bounds.min_x <= current[0] <= bounds.max_x and bounds.min_y <= current[1] <= bounds.max_y
