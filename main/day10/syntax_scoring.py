from math import floor

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
scoring_table = {'(': 1, '[': 2, '{': 3, '<': 4}


def solve_invalid(lines) -> int:
    invalid_counter = {')': 0, ']': 0, '}': 0, '>': 0}

    for line in lines:
        invalid_bracket = find_invalid(line)
        if invalid_bracket is not None:
            invalid_counter[invalid_bracket] += 1
    return calculate_total_error(invalid_counter)


def solve_corrupted(lines) -> int:
    scores = [fix_line(x) for x in filter(lambda x: find_invalid(x) is None, lines)]
    return sorted(scores)[floor(len(scores) / 2)]


def fix_line(line):
    stack = []
    for c in line:
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            stack.pop()

    score = 0
    while len(stack) != 0:
        c = stack.pop()
        score *= 5
        score += scoring_table[c]
    return score


def find_invalid(line):
    stack = []
    for c in line:
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            popped = stack.pop()
            if brackets[popped] != c:
                return c


def calculate_total_error(invalid):
    total_error = 0
    for k, v in invalid.items():
        if k == ')':
            total_error += 3 * v
        elif k == ']':
            total_error += 57 * v
        elif k == '}':
            total_error += 1197 * v
        elif k == '>':
            total_error += 25137 * v
    return total_error
