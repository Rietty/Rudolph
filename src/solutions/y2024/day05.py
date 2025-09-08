import networkx as nx
from loguru import logger as log

from utils.decorators import benchmark


def path_exists(graph: nx.DiGraph, path: list[int]) -> bool:
    return all(graph.has_edge(path[i], path[i + 1]) for i in range(len(path) - 1))


@benchmark
def part_a(data: tuple[nx.DiGraph, list[list[int]]]) -> int:
    graph, updates = data

    return sum(update[len(update) // 2] for update in updates if path_exists(graph, update))


@benchmark
def part_b(data: tuple[nx.DiGraph, list[list[int]]]) -> int:
    graph, updates = data
    fixed_incorrect = []

    for update in updates:
        if not path_exists(graph, update):
            subgraph = graph.subgraph(update)
            fixed_incorrect.append(list(nx.topological_sort(subgraph)))

    return sum(update[len(update) // 2] for update in fixed_incorrect)


@benchmark
def parse(data: str) -> tuple[nx.DiGraph, list[list[int]]]:
    r, u = data.split("\n\n")

    rules: list[tuple[int, ...]] = [tuple(map(int, rule.split("|"))) for rule in r.splitlines()]
    updates: list[list[int]] = [list(map(int, update.split(","))) for update in u.splitlines()]

    graph = nx.DiGraph()
    graph.add_edges_from(rules)

    return (graph, updates)


test_data_a = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

test_data_b = test_data_a
