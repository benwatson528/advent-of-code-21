from collections import Counter


def solve(x, num_steps) -> int:
    template, rules = x
    for _ in range(num_steps):
        template = take_turn(template, rules)
    counter = Counter(template)
    return max(counter.values()) - min(counter.values())


def take_turn(template, rules):
    updated_template = []
    for pair in list(zip(template, template[1:])):
        updated_template.append(pair[0])
        updated_template.append(rules[pair[0] + pair[1]])
    updated_template.append(template[-1])
    return updated_template
