def solve(fish, num_turns) -> int:
    states = [0] * 9
    for f in fish:
        states[f] += 1
    return sum(progress_fish_rec(states, 0, num_turns))


def progress_fish_rec(states, current_turn, num_turns):
    if current_turn == num_turns:
        return states
    else:
        new_states = [0] * 9
        for i in range(9):
            prev = (i + 1) % 9
            new_states[i] = states[prev]
            if i == 6:
                new_states[i] += states[0]
        return progress_fish_rec(new_states, current_turn + 1, num_turns)
