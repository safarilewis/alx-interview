#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    '''Returns a list of ints representing pascal's triangle'''
    for i in range(0, n + 1):
        row = []
        tri = []
        new_row = []
        new_row = [j > 0 and j < i - 1 and i > 2 and row[j-1] +
                   row[j] or 1 for j in range(0, i)]
        row = new_row
        tri += [new_row]
    return tri
