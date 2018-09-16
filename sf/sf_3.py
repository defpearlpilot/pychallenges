
#!/bin/python3

import math
import os
import random
import re
import sys


def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2  # return False
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def manipulate_generator(generator, n):
    # Enter your code here
    num_generated = 0

    while num_generated < n:
        next_int = next(generator)
        while is_prime(next_int):
            next_int = next(generator)

        num_generated += 1
        print(next_int)
        generator.send(next_int)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


def solve():
    total = 10
    gen = positive_integers_generator()
    manipulate_generator(gen, total)


if __name__ == '__main__':
    solve()
