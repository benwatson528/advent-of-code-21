def solve_bingo(x, first_winner) -> int:
    called_numbers, boards = x
    winners = []
    for called_number in called_numbers:
        boards = update_boards(called_number, boards)
        for winner in check_boards(boards, winners):
            if winner not in winners:
                winners.append(winner)
                if first_winner or len(winners) == len(boards):
                    return int(called_number) * sum_board(boards[winner])


def update_boards(called_number, boards):
    for board in boards:
        for row in board:
            for index, value in enumerate(row):
                if value == called_number:
                    row[index] = '*'
    return boards


def check_boards(boards, winners):
    new_winners = []
    for idx, board in enumerate(boards):
        if idx in winners or idx in new_winners:
            continue
        if len(list(filter(lambda r: r.count('*') != len(r), board))) != len(board):
            new_winners.append(idx)
            continue
        for i in range(len(board)):
            if len([row[i] for row in board if row[i] == '*']) == len(board[0]):
                new_winners.append(idx)
    return new_winners


def sum_board(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            total += int(board[i][j]) if board[i][j] != '*' else 0
    return total
