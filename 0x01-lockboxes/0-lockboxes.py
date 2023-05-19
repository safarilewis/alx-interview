#!/usr/bin/python3
"""
You are given a list of lists named boxes.
Each box is numbered sequentially from 0 to n - 1

In each list in box is a given set of numbers,
one of the numbers might be the key to the next box.
A key with the same number as a box opens that box
"""


def canUnlockAll(boxes) -> bool:
    '''Function that checks if all boxes can be opened'''
    check = 1
    position = 0
    keys = []
    for box in boxes:
        for item in box:
            keys.append(item)
    while position < len(boxes):
        for key in keys:
            if key == position:
                value = True
                position = position + 1
            else: value = False
    return value
