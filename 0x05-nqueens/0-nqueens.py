#!/usr/bin/python3
"""
A program that solves the N-queens challenge.
"""
import sys
from typing import List


def is_safe(board: List[int], row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    for r in range(row):
        if board[r] == col or \
                board[r] - r == col - row or \
                board[r] + r == col + row:
            return False
    return True


def solve_nqueens(
        board: List[int], row: int, n: int, solutions: List[List[int]]
        ):
    """
    Recursively find a safe place for a queen in the current row.
    """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n: int) -> List[List[int]]:
    """
    Solve the N-queens problem for a given board size.
    """
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions


def print_solutions(solutions: List[List[int]]):
    """
    Print all solutions to the N-queens problem.
    """
    for solution in solutions:
        result = [[col, row] for row, col in enumerate(solution)]
        print(result)


def main():
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

    solutions = nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
