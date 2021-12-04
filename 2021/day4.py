import numpy as np


def get_input():
    with open("input4") as file:
        x = None
        boards = []
        board = np.zeros((2, 5, 5), dtype=int)
        row = 5
        for i, l in enumerate(file):
            if i == 0:
                x = [int(e) for e in l.strip().split(",")]
            elif row < 5:
                for j, c in enumerate(l.strip().split()):
                    board[0, row, j] = int(c)
                row += 1
            else:
                boards.append(board)
                board = np.zeros((2, 5, 5), dtype=int)
                row = 0
        boards.append(board)
        return x, boards[1:]


if __name__ == "__main__":
    xs, boards = get_input()
    n_players = len(boards)
    for x in xs:
        for ib, board in reversed(list(enumerate(boards))):
            board[1, board[0, :, :] == x] = 1
            if any(5 in board[1].sum(axis=a) for a in [0, 1]):
                if len(boards) in [1, n_players]:
                    print(x * board[0, board[1, :, :] == 0].sum())
                del boards[ib]
