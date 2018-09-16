
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valleys = 0
    maybe_valley = False

    for step in s:
        if step == 'D':
            level -= 1
            if level < 0:
                maybe_valley = True
        elif step == 'U':
            level += 1
            if level == 0 and maybe_valley:
                valleys += 1
                maybe_valley = False

    return valleys


def solve(reader, solution):
    n = int(reader())

    ar = reader()

    return solution(n, ar)


def solve_std_in():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = solve(lambda: input(), countingValleys)

    fptr.write(str(result) + '\n')
    fptr.close()


def solve_from_file(file):
    with open(file, 'r') as f:
        result = solve(lambda: f.readline(), countingValleys)
        print(result)


if __name__ == '__main__':
    solve_from_file("counting_valleys.txt")
