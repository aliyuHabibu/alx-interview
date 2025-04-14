#!/bin/env python3
"""
Module to get the minimum multiple
of a given number
"""


def check_min_multi(min_mult, num, minOp):
    """
    Function to return the
    gotten multiple and the decided
    minimum operation counted
    """
    if num % 2 == 0:
        return min_mult, minOp
    else:
        minOp += 1
        return min_mult, minOp
