#!/usr/bin/python3

"""
    Module to get the pascal triangle of a
    given number
"""


def pascal_triangle(n):
    """
        Function to get the list of each of
        pascal triangle of a given number
    """
    my_lists = []
    for i in range(n):
        my_lists.append([])
        x = 0
        while (x <= i):
            if (x == 0):
                my_lists[i].append(1)
            elif (x == 1):
                my_lists[i].append(i)
            elif (x == i - 1):
                my_lists[i].append(i)
            elif (x == i):
                my_lists[i].append(1)
            else:
                my_lists[i].append(my_lists[i - 1][x] + my_lists[i - 1][x - 1])
            x += 1
        i += 1
    return (my_lists)
