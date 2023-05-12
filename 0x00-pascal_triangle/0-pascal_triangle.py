#!/usr/bin/python3
"""Pascal's Triangle"""
from math import factorial


def pascal_triangle(n):
    '''Returns a list of ints representing pascal's triangle'''

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(factorial(i)//(factorial(j)*factorial(i-j)))
        print(row)
        row = []
