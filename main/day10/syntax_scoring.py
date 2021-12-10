def solve(lines) -> int:
    invalid = {')': 0, ']': 0, '}': 0, '>': 0}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for line in lines:
        stack = []
        for c in line:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                popped = stack.pop()
                if brackets[popped] != c:
                    invalid[c] += 1
                    break
    return calculate_total_error(invalid)


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
