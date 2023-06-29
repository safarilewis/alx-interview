#!/usr/bin/python3
"""Prime Game Module"""


def find_prime(n):
    """Find Prime Numbers"""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """Determines winner of Prime Game with x rounds"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        prime = find_prime(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
