#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    minimum_operations = 2
    while n > 1:
        while n % minimum_operations == 0:
            operations += minimum_operations
            n /= min_operations
        minimum_operations += 1
    return operations
