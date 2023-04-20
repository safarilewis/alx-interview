#!/usr/bin/python3
'''Checks if a number is a valid utf8 encoding'''


def validUTF8(data) -> bool:
    '''Checks numbers in data and returns True if all are valid utf8'''
    count = 0
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
