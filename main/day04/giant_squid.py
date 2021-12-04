def solve_bingo(x) -> int:
    called_numbers, boards = x
    for called_number in called_numbers:
        boards = update_boards(called_number, boards)
        winner = check_boards(boards)
        if winner is not None:
            board = sum_board(boards[winner])
            return int(called_number) * board


def update_boards(called_number, boards):
    for board in boards:
        for row in board:
            for index, value in enumerate(row):
                if value == called_number:
                    row[index] = '*'
    return boards


def check_boards(boards):
    for idx, board in enumerate(boards):
        f = list(filter(lambda r: r.count('*') != len(r), board))
        if len(f) != len(board):
            return idx
        for i in range(len(board)):
            if len([row[i] for row in board]) != len(board[0]):
                return idx
    return None


def sum_board(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            total += int(board[i][j]) if board[i][j] != '*' else 0
    return total
