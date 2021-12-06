def solve(fish, num_turns) -> int:
    return len( progress_fish_rec(fish, 0, num_turns))


def progress_fish_rec(fish, current, end):
    if current == end:
        return fish
    else:
        new_fish = []
        for f in fish:
            if f - 1 == -1:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(f - 1)

        return progress_fish_rec(new_fish, current + 1, end)
