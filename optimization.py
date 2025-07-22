import numpy as np

def my_checker_board(n: int):
    board = np.array()
    for row in n:
        if n % 2 == 0:
            add = np.array([0 if row % 2 == 0 else 1])
        else:
            add = np.array([1 if row % 2 == 0 else 0])
        board = np.vstack(board, add)
        print(board)

my_checker_board(10)