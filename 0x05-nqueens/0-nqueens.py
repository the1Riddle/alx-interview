#!/usr/bin/python3
"""
A program that solves the n queens challenge.
"""
import sys


def is_safe(board: list, row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    for r in range(row):
        if board[r] == col or \
                board[r] - r == col - row or \
                board[r] + r == col + row:
            return False
    return True


def find_aplace(board, row, n, solutions):
    """
    Recursively find a safe place for a queen in the current row.
    """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            find_aplace(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n: int):
    """
    Solve the n queens problem for a given board size.
    """
    board = [-1] * n
    solutions = []
    find_aplace(board, 0, n, solutions)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions to the N-queens problem.
    """
    for sol in solutions:
        result = [[col, row] for row, col in enumerate(sol)]
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    # prints the results
    solution = nqueens(n)
    print_solutions(solution)
