#!/bin/python3

import math
import os
import random
import re
import sys
import functools


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_colors = {}
    for sock_color in ar:
        sock_count = sock_colors.setdefault(sock_color, 0.0)
        sock_colors[sock_color] = sock_count + 0.5

    return functools.reduce(lambda x, y: x + y,
                            [math.floor(count) for count in sock_colors.values()])


def solve(reader, sockMerchant):
    n = int(reader())

    ar = list(map(int, reader().rstrip().split()))

    return sockMerchant(n, ar)


def solve_std_in():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = solve(lambda: input(), sockMerchant)

    fptr.write(str(result) + '\n')
    fptr.close()


def solve_from_file(file):
    with open(file, 'r') as f:
        result = solve(lambda: f.readline(), sockMerchant)
        print(result)


if __name__ == '__main__':
    solve_from_file("sock_input.txt")
