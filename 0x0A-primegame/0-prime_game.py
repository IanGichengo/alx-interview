#!/usr/bin/python3
"""
This module contains the isWinner function to determine the winner
of a game played between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the game played

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             Returns None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    # Precompute prime numbers for all rounds up to the maximum n
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    # Count the wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
