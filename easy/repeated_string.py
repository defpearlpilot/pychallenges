#!/bin/python3

import math
import os
import random
import re
import sys
import functools


# Complete the repeatedString function below.
def repeatedString(s, n):
    def count_a(_s):
        return functools.reduce(lambda a, c: a + 1 if c == 'a' else a, _s, 0)

    s_len = len(s)
    a_count = count_a(s)

    repeats = n // s_len
    remaining = n - (repeats * s_len)

    sub_s = s[:remaining]
    remaining_a = count_a(sub_s)

    return (a_count * repeats) + remaining_a


def solve(reader, solution):
    s = reader().strip()

    n = int(reader())

    return solution(s, n)


def solve_std_in():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = solve(lambda: input(), repeatedString)

    fptr.write(str(result) + '\n')
    fptr.close()


def solve_from_file(file):
    with open(file, 'r') as f:
        result = solve(lambda: f.readline(), repeatedString)
        print(result)


if __name__ == '__main__':
    solve_from_file("repeated_string.txt")