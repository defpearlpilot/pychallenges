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


class Edge(object):
    def __init__(self, distance, node):
        self.node = node
        self.distance = distance


class Node(object):
    def __init__(self, node_id, color):
        self.node_id = node_id
        self.color = color

        self.edges = {}


def find_shortest(graph_nodes, graph_from, graph_to, ids, val):
    node_map = {}
    color_map = {}

    for num, color in enumerate(ids):
        node_id = num + 1
        node = Node(node_id, color)
        node_map[node.node_id] = node

        color_list = color_map.setdefault(color, [])
        color_list.append(node)

    for from_id, to_id in zip(graph_from, graph_to):
        node_from = node_map[from_id]
        node_to = node_map[to_id]
        node_from.edges[to_id] = node_to



    return 4


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


