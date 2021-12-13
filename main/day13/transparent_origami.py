def solve(t, first_fold=False) -> int:
    hashes, folds = t[0], t[1]
    if first_fold:
        hashes = fold_paper(hashes, folds[0])
    else:
        for fold in folds:
            hashes = fold_paper(hashes, fold)
    # Uncomment to display the text answer for part 2
    # print_grid(hashes)
    return len(set(hashes))


def fold_paper(hashes, fold):
    fold_line = int(fold[1])
    return fold_y(fold_line, hashes) if fold[0] == 'y' else fold_x(fold_line, hashes)


def fold_y(fold_line, hashes):
    new_hashes = []
    for coord in hashes:
        if coord[1] < fold_line:
            new_hashes.append(coord)
        else:
            new_hashes.append((coord[0], fold_line - (coord[1] - fold_line)))
    return new_hashes


def fold_x(fold_line, hashes):
    new_hashes = []
    for coord in hashes:
        if coord[0] < fold_line:
            new_hashes.append(coord)
        else:
            new_hashes.append((fold_line - (coord[0] - fold_line), coord[1]))
    return new_hashes


def print_grid(hashes):
    max_x = max(c[0] for c in hashes)
    max_y = max(c[1] for c in hashes)
    print()
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in hashes:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()
