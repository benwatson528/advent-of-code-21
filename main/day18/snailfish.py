import json
import math
import re


def solve(fishes) -> int:
    current = fishes[0]
    for i in range(1, len(fishes)):
        added = [current] + [fishes[i]]
        previous = json.loads("[]")
        transformed = added
        while transformed != previous:
            previous = transformed
            transformed = json.loads(transform(transformed))
        current = transformed
    return calculate_magnitude(current)


def transform(fish):
    fish_str = json.dumps(fish).replace(" ", "")
    fish = fish_str
    depth = 0
    i = 0
    while i < len(fish_str):
        c = fish_str[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

        if depth == 5 and c.isnumeric():  # we've found the start of a pair
            fish = prep_explode(fish_str, i)
            return fish
        i += 1

    i = 0
    is_in_number = False
    start_idx = -1
    fish = prep_split(fish, fish_str, i, is_in_number, start_idx)
    return fish


def prep_split(fish, fish_str, i, is_in_number, start_idx):
    while i < len(fish_str):
        c = fish_str[i]
        if is_in_number:
            if not c.isnumeric():
                is_in_number = False
                end_idx = i
                num = int(fish_str[start_idx:end_idx])
                if num >= 10:
                    fish = split(fish_str, start_idx, end_idx, num)
                    break
        elif c.isnumeric():
            is_in_number = True
            start_idx = i
        i += 1
    return fish


def prep_explode(fish_str, i):
    first_elem_start_idx = i
    while fish_str[i].isnumeric():
        i += 1
    first_elem_end_idx = i
    i += 1
    second_elem_start_idx = i
    while fish_str[i].isnumeric():
        i += 1
    second_elem_end_idx = i
    return explode(fish_str[:first_elem_start_idx - 1], fish_str[first_elem_start_idx:first_elem_end_idx],
                   fish_str[second_elem_start_idx:second_elem_end_idx], fish_str[second_elem_end_idx + 1:])


def explode(left, first_elem, second_elem, right):
    left_neighbour_idxs = [m.span() for m in re.finditer(r'\d+', left)]
    if left_neighbour_idxs:
        left_neighbour = left[left_neighbour_idxs[-1][0]:left_neighbour_idxs[-1][1]]
        new_left = str(int(left_neighbour) + int(first_elem))
        new_before = left[:left_neighbour_idxs[-1][0]] + new_left + left[left_neighbour_idxs[-1][1]:]
    else:
        new_before = left

    right_neighbour_idxs = [m.span() for m in re.finditer(r'\d+', right)]
    if right_neighbour_idxs:
        right_neighbour = right[right_neighbour_idxs[0][0]:right_neighbour_idxs[0][1]]
        new_right = str(int(right_neighbour) + int(second_elem))
        new_after = right[:right_neighbour_idxs[0][0]] + new_right + right[right_neighbour_idxs[0][1]:]
    else:
        new_after = right

    final = new_before + '0' + new_after
    return final


def split(fish, start_idx, end_idx, num):
    left = num // 2
    right = math.ceil(num / 2)
    return fish[:start_idx] + f"[{left},{right}]" + fish[end_idx:]


def calculate_magnitude(fish):
    def rec(left, right):
        total = 0
        total += 3 * rec(left[0], left[1]) if isinstance(left, list) else 3 * left
        total += 2 * rec(right[0], right[1]) if isinstance(right, list) else 2 * right
        return total

    return rec(fish[0], fish[1])
