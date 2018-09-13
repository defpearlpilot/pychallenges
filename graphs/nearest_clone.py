#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


class Node(object):
    def __init__(self, number, color):
        self.number = number
        self.color = color

        self.edges = {}


def find_shortest(graph_nodes, graph_from, graph_to, ids, val):
    nodes = dict(((n + 1, Node(n + 1, c)) for n, c in enumerate(ids)))

    for from_id, to_id in zip(graph_from, graph_to):
        node_from = nodes[from_id]
        node_to = nodes[to_id]
        node_from.edges[to_id] = node_to

    print("FOO")
    return 4
    # solve here


def input_from_file():
    with open('graph.txt', 'r') as f:
        return input_from(lambda: f.readline())


def input_from_std_in():
    return input_from(lambda: input())


def input_from(reader):
    graph_nodes, graph_edges = map(int, reader().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, reader().split())

    ids = list(map(int, reader().rstrip().split()))

    val = int(reader())

    return graph_nodes, graph_from, graph_to, ids, val


if __name__ == '__main__':
    graph_nodes, graph_from, graph_to, ids, val = input_from_file()

    print(graph_nodes)
    ans = find_shortest(graph_nodes, graph_from, graph_to, ids, val)


