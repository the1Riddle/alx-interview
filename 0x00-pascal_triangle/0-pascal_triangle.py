#!/usr/bin/python3
""" pascal triangle written in python
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        mylist = [1]
        """if its the first digit then use"""
        if i == 0:
            """mylist as the first digit"""
            triangle.append(mylist)
            continue
        else:
            """get the last row"""
            prev_row = triangle[-1]
            for j in range(1, i):
                nex = prev_row[j - 1] + prev_row[j]
                mylist.append(nex)
        """append 1 at the end of the list"""
        mylist.append(1)
        """the first digit should always be mylist"""
        triangle.append(mylist)

    return triangle
