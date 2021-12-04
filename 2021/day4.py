import numpy as np

with open("input4") as file:
    xs = None
    boards = []
    board = np.zeros((2, 5, 5), dtype=int)
    row = 5
    for i, l in enumerate(file):
        if i == 0:
            xs = [int(e) for e in l.strip().split(",")]
        elif row < 5:
            for j, c in enumerate(l.strip().split()):
                board[0, row, j] = int(c)
            row += 1
        else:
            boards.append(board)
            board = np.zeros((2, 5, 5), dtype=int)
            row = 0
    boards.append(board)
    del boards[0]
n_players = len(boards)
for x in xs:
    for ib, board in reversed(list(enumerate(boards))):
        board[1, board[0, :, :] == x] = 1
        if any(5 in board[1].sum(axis=a) for a in [0, 1]):
            if len(boards) in [1, n_players] and False:
                print(x * board[0, board[1, :, :] == 0].sum())
            del boards[ib]
