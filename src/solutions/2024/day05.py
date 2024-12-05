import logging
import networkx as nx
from typing import List

from utils.decorators import benchmark

log = logging.getLogger(__name__)


def path_exists(graph: nx.DiGraph, path: List[int]) -> bool:
    return all(graph.has_edge(path[i], path[i + 1]) for i in range(len(path) - 1))


@benchmark
def part_a[T](data: T) -> int:
    graph, updates = data

    return sum(
        update[len(update) // 2] for update in updates if path_exists(graph, update)
    )


@benchmark
def part_b[T](data: T) -> int:
    graph, updates = data

    fixed_incorrect = []
    for update in updates:
        if not path_exists(graph, update):
            subgraph = graph.subgraph(update)
            fixed_incorrect.append(list(nx.topological_sort(subgraph)))

    return sum(update[len(update) // 2] for update in fixed_incorrect)


def parse[T](data: str) -> T:
    rules, updates = data.split("\n\n")

    rules = [tuple(map(int, rule.split("|"))) for rule in rules.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]

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

test_data_b = """47|53
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
