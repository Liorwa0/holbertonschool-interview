#!/usr/bin/python3
"""Find the overall winner of the prime game."""


def isWinner(x, nums):
    """Return the player who wins the most rounds, or None for a tie."""
    if x <= 0 or not nums:
        return None

    rounds = min(x, len(nums))
    highest = max(nums[:rounds])
    if highest < 2:
        return 'Ben'

    primes = [True] * (highest + 1)
    primes[0] = primes[1] = False

    for number in range(2, int(highest ** 0.5) + 1):
        if primes[number]:
            for multiple in range(number * number, highest + 1,
                                  number):
                primes[multiple] = False

    prime_counts = [0] * (highest + 1)
    for number in range(1, highest + 1):
        prime_counts[number] = prime_counts[number - 1] + primes[number]

    maria = 0
    ben = 0
    for n in nums[:rounds]:
        if prime_counts[n] % 2:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return 'Maria'
    if ben > maria:
        return 'Ben'
    return None
