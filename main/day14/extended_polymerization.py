from collections import Counter


def solve(x, num_steps) -> int:
    template, rules = x
    counts = Counter(zip(template, template[1:]))
    for _ in range(num_steps):
        counts = take_turn(counts, rules)
    occurrences = find_occurrences(counts)
    return max(occurrences.values()) - min(occurrences.values())


def take_turn(counts, rules):
    updated_counts = {}
    for pair, occurrences in counts.items():
        new_middle = rules[pair[0] + pair[1]]
        left_pair = pair[0] + new_middle
        right_pair = new_middle + pair[1]
        updated_counts[left_pair] = updated_counts.get(left_pair, 0) + occurrences
        updated_counts[right_pair] = updated_counts.get(right_pair, 0) + occurrences
    return updated_counts


def find_occurrences(counts):
    single_keys = {}
    for pair, occurrences in counts.items():
        single_keys[pair[1]] = single_keys.get(pair[1], 0) + occurrences
    return single_keys
