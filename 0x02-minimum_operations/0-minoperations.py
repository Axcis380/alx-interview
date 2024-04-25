#!/usr/bin/python3

"""
    Method that determines the number of minimum operations given n characters
"""


def minOperations(n):

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if remainder % now == 0:
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
