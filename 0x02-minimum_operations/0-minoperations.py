#!/usr/bin/python3

"""
    a functions that calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    given a number n
"""


def minOperations(n: int) -> int:
    """
        the method that calculates the fewest number of operations
    """
    i: int = 0

    if n <= 1:
        return (0)
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return (minOperations(n // i) + i)
        return (n)

