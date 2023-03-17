#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
       for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j]:
            return False
       return True

def solve_nqueens(board, col):
    """Solve the N queens problem, starting at column col."""
    if col == len(board):
              print(board)
        return
    for row in range(len(board)):
        if is_safe(board, row, col):
                       board[row][col] = 1
            # Move to the next column
            solve_nqueens(board, col + 1)
                     board[row][col] = 0

if __name__ == '__main__':
      if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
  
    board = [[0] * n for i in range(n)]
    solve_nqueens(board, 0)
