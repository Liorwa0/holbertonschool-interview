#!/usr/bin/python3
"""
N Queens problem solver using Backtracking.
"""
import sys


def solve_nqueens(n):
    """
    Solves the N Queens puzzle and prints all solutions.
    """
    board = [-1] * n

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or \
               abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solution = [[r, board[r]] for r in range(n)]
            print(solution)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


def main():
    """
    Main function to parse arguments and trigger the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
