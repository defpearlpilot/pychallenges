#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0

    index = 0
    max_index = len(c) - 1

    while index < max_index:
        for addend in (2, 1):
            new_index = index + addend
            if new_index <= max_index:
                item = c[new_index]
                if item == 0:
                    jumps += 1
                    index += addend
                    break

    return jumps


def solve(reader, solution):
    n = int(reader())

    c = list(map(int, reader().rstrip().split()))

    return solution(c)


def solve_std_in():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = solve(lambda: input(), jumpingOnClouds)

    fptr.write(str(result) + '\n')
    fptr.close()


def solve_from_file(file):
    with open(file, 'r') as f:
        result = solve(lambda: f.readline(), jumpingOnClouds)
        print(result)


if __name__ == '__main__':
    solve_from_file("jumping_clouds.txt")

