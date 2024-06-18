#!/usr/bin/python3
"""
Prime game module
"""


def is_winner(x, nums):
    """
    a function to determine the winner of the prime game.
    """

    def primes_up_to(n):
        """
        Generate all prime numbers up to n using the Sieve of Eratosthenes.
        """
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return [p for p in range(2, n + 1) if sieve[p]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = primes_up_to(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
