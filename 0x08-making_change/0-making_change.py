#!/usr/bin/python3
"""
    A function to determine the fewest number of coins needed to meet
    a given amount total, when the coins are of different values.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """
    Initialize the dp array with a high value for each amount
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """
    If dp[total] is still infinity, return -1 indicating no solution
    """
    return dp[total] if dp[total] != float('inf') else -1
