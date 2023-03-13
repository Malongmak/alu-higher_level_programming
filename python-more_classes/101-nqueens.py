#!/usr/bin/python3
import sys

def is_valid(board, row, col, n):
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
        if row+i < n and col+i < n and board[row+i][col+i] == 1:
            return False
        if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 1:
            return False
        if row-i >= 0 and col+i < n and board[row-i][col+i] == 1:
            return False
        if row+i < n and col-i >= 0 and board[row+i][col-i] == 1:
            return False
    return True

def nqueens_helper(board, col, n, solutions):
    if col == n:
        solutions.append(board.copy())
        return
    for row in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            nqueens_helper(board, col+1, n, solutions)
            board[row][col] = 0

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    nqueens_helper(board, 0, n, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

