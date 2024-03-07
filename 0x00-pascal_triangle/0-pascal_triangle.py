#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        mylist = [1]
        if i == 0:#if its the first digit then use
            triangle.append(mylist)#mylist as the first digit
            continue
        else:
            prev_row = triangle[-1]#get the last row
            for j in range(1, i):
                nex = prev_row[j -1] + prev_row[j]
                mylist.append(nex)
        mylist.append(1)#append 1 at the end of the list
        triangle.append(mylist)#the first digit should always be mylist

    return triangle
