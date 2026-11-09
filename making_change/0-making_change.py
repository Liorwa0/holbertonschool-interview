#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        count += temp
        total -= temp * coin
    if total != 0:
        return -1
    return count
