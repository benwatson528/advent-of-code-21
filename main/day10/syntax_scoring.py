from math import floor

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}


def solve_invalid(lines) -> int:
    scoring_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        invalid_bracket = find_invalid(line)
        if invalid_bracket is not None:
            score += scoring_table.get(invalid_bracket)
    return score


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

    scoring_table = {'(': 1, '[': 2, '{': 3, '<': 4}
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
