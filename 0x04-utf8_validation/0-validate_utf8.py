#!/usr/bin/python3
"""
    a function that determines if a given data set represens a valid
    UTF-8 encoding
"""


def validUTF8(data):
    """
    the method to implement the functionality
    """
    n_bytes = 0
    for num in data:
        if n_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            n_bytes -= 1
    return n_bytes == 0
