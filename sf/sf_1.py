
#!/bin/python3

import math
import os
import random
import re
import sys

import functools

def solution(people):
    print(people)
    vote_count = {}

    max_vote = 0

    for person in people:
        votes = vote_count.setdefault(person, 0)
        votes += 1
        vote_count[person] = votes

        if votes > max_vote:
            max_vote = votes

    people = []
    for p, v in vote_count.items():
        if v == max_vote:
            people.append(p)

    if len(people) == 1:
        return people[0]
    else:
        sorted_people = sorted(people)
        return sorted_people[-1]


def solve(reader, _solution):
    n = int(reader())
    people = []

    index = 0
    while index < n:
        people.append(reader().strip())
        index += 1

    return _solution(people)


def solve_std_in():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = solve(lambda: input(), solution)

    fptr.write(str(result) + '\n')
    fptr.close()


def solve_from_file(file):
    with open(file, 'r') as f:
        result = solve(lambda: f.readline(), solution)
        print(result)


if __name__ == '__main__':
    solve_from_file("sf1.txt")
