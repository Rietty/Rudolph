from __future__ import annotations

from itertools import permutations
from typing import Sequence

import networkx as nx

from utils.decorators import benchmark


def route_length(data: nx.DiGraph[str], path: Sequence[str]) -> int:
    return sum(data[u][v]["weight"] for u, v in zip(path, path[1:]))


@benchmark
def part_a(data: nx.DiGraph[str]) -> int:
    return min(route_length(data, p) for p in permutations(data.nodes))


@benchmark
def part_b(data: nx.DiGraph[str]) -> int:
    return max(route_length(data, p) for p in permutations(data.nodes))


@benchmark
def parse(data: str) -> nx.DiGraph[str]:
    graph: nx.DiGraph[str] = nx.DiGraph()
    for line in data.splitlines():
        route, _, dist = line.partition(" = ")
        src, _, dest = route.partition(" to ")
        graph.add_edge(src, dest, weight=int(dist))
        graph.add_edge(dest, src, weight=int(dist))
    return graph


test_data_a = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

test_data_b = test_data_a
