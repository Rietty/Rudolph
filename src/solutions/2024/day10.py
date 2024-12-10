import logging

import networkx as nx

from utils.decorators import benchmark

log = logging.getLogger(__name__)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@benchmark
def part_a[T](data: T) -> int:
    start_nodes = [node for node in data.nodes if data.nodes[node]["weight"] == 0]
    end_nodes = [node for node in data.nodes if data.nodes[node]["weight"] == 9]

    count = 0
    for start in start_nodes:
        for end in end_nodes:
            if nx.has_path(data, start, end):
                count += 1

    return count


@benchmark
def part_b[T](data: T) -> int:
    start_nodes = [node for node in data.nodes if data.nodes[node]["weight"] == 0]
    end_nodes = [node for node in data.nodes if data.nodes[node]["weight"] == 9]

    paths = []
    for start in start_nodes:
        for end in end_nodes:
            paths.extend(nx.all_simple_paths(data, start, end))

    return len(paths)


def parse[T](data: str) -> T:
    graph = nx.DiGraph()
    grid = [list(map(int, line)) for line in data.splitlines()]

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            graph.add_node((x, y), weight=grid[x][y])
            for dx, dy in DIRECTIONS:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x]):
                    graph.add_node((x + dx, y + dy), weight=grid[x + dx][y + dy])
                    if grid[x][y] + 1 == grid[x + dx][y + dy]:
                        graph.add_edge((x, y), (x + dx, y + dy))

    return graph


test_data_a = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

test_data_b = test_data_a
