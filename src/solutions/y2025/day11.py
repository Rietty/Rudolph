from functools import lru_cache

import networkx as nx

from utils.decorators import benchmark


@lru_cache(maxsize=None)
def dfs(data: nx.DiGraph, src: str, target: str, first: str, second: str):
    if src == target:
        return (1, 0, 0, 0)

    A, B, C, D = map(
        sum, zip(*(dfs(data, s, target, first, second) for s in data.successors(src)))
    )

    if src == first:
        B, D, A, C = B + A, D + C, 0, 0
    elif src == second:
        C, D, A, B = C + A, D + B, 0, 0

    return (A, B, C, D)


@benchmark
def part_a(data: nx.DiGraph) -> int:
    return sum(1 for _ in nx.all_simple_paths(data, source="you", target="out"))


@benchmark
def part_b(data: nx.DiGraph) -> int:
    return dfs(data, "svr", "out", "dac", "fft")[3]


@benchmark
def parse(data: str) -> nx.DiGraph:
    G = nx.DiGraph()
    for line in data.strip().splitlines():
        node, neighbors = line.split(":")
        node = node.strip()
        neighbors = neighbors.strip().split()
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


test_data_a = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

test_data_b = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
