#!/bin/python3
"""
Module to get the minimum number of operations
to achieve a given number n
"""
check_min_multi = __import__('0-get_multi').check_min_multi


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only
    two operations in this file: Copy All and Paste.
    Given a number n, write a method that calculates the
    fewest number of operations needed to result
    in exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n == 0:
        return 0

    minOp, marker, incre = 1, 0, 1
    i = 1
    while i < n:
        if n > 5 and i > 1:
            if n % i == 0 and not marker:
                incre, minOp = check_min_multi(i, n, minOp)
                marker = 1
        else:
            incre = incre
        i += incre
        minOp += 1
    return minOp
