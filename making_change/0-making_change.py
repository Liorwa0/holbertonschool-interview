#!/usr/bin/python3
"""
Module for makeChange function.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [0] + [total + 1] * total
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    return dp[total] if dp[total] <= total else -1
