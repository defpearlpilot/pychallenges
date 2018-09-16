
#!/bin/python3

import math
import os
import random
import re
import sys
import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
import functools

url_template = "https://jsonmock.hackerrank.com/api/movies/search/?Title=%(title)s&page=%(page)s"


def fetch_page(substr, page):
    url = url_template % {"title": substr, "page": page}

    with urlopen(url) as response:
        return response.json()


def process_results(results):
    if results["data"] is None:
        return []

    listings = results["data"]
    return list(map(lambda entry: entry["Title"], listings))


def solution(substr):
    page = 1

    raw_results = []
    while True:
        results = fetch_page(substr, page)
        raw_results.extend(process_results(results))

        total_pages = results['total_pages']
        if total_pages == page:
            break

        page += 1

    results = sorted(raw_results)

    return results


def solve(reader, _solution):
    title = reader()

    return _solution(title)


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
    solve_from_file("sf2.txt")
