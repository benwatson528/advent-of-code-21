uniques = {2: 1, 4: 4, 3: 7, 7: 8}


def solve_unique(records) -> int:
    counter = 0
    for record in records:
        _, output = record
        for o in output:
            if len(o) in (2, 4, 3, 7):
                counter += 1
    return counter


def solve_decode(x) -> int:
    total_output = 0
    for signals, output in x:
        found = find_unique_choices(signals)
        # Find 3 (it's got 1 + 3)
        for potential in filter(lambda l: len(l) == 5, signals):
            if len(set(potential) - set(found[1])) == 3 and potential not in found.values():
                found[3] = potential
                break
        # Find 9 (it's got 3 + 1)
        for potential in filter(lambda l: len(l) == 6, signals):
            if len(set(potential) - set(found[3])) == 1 and potential not in found.values():
                found[9] = potential
                break
        # Find 5 (it's got 9 - 1)
        for potential in filter(lambda l: len(l) == 5, signals):
            if len(set(found[9]) - set(potential)) == 1 and potential not in found.values():
                found[5] = potential
                break
        # Find 6 (it's got 5 + 1)
        for potential in filter(lambda l: len(l) == 6, signals):
            if len(set(potential) - set(found[5])) == 1 and potential not in found.values():
                found[6] = potential
                break
        # Find 0 (it's the only remaining 6)
        for potential in filter(lambda l: len(l) == 6, signals):
            if potential not in found.values():
                found[0] = potential
        # Find 2 (it's the only remaining 5)
        for potential in filter(lambda l: len(l) == 5, signals):
            if potential not in found.values():
                found[2] = potential
        current_output = ''
        for o in output:
            for k, v in found.items():
                if set(o) == set(v):
                    current_output += str(k)
                    break
        total_output += int(current_output)
    return total_output


def find_unique_choices(signals):
    found = {}
    for signal in signals:
        if len(signal) in uniques.keys():
            found[uniques[len(signal)]] = signal
    return found
