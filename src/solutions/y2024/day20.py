import itertools

import networkx as nx
from loguru import logger as log

from library.graph import Graph
from library.grid import Grid
from utils.decorators import benchmark


# Possible cheats are all the points within a specific (manhattan) distance.
def get_possible_cheats(size: int) -> list[tuple[int, int, int]]:
    return [
        (x, y, abs(x) + abs(y))
        for x, y in itertools.product(range(-(size + 1), size + 2), repeat=2)
        if abs(x) + abs(y) <= size
    ]


# Count the number of good cheats.
def count_good_cheats(
    graph: Graph,
    start: tuple[int, int],
    end: tuple[int, int],
    max_cheat_distance: int,
) -> int:
    source_path_lengths = nx.single_source_shortest_path_length(graph.get(), start)

    original_length = source_path_lengths[end]
    good_cheats = 0

    for cheat_x, cheat_y, cheat_distance in get_possible_cheats(max_cheat_distance):
        for node in graph.nodes:
            x, y = node
            cheat_node = (x + cheat_x, y + cheat_y)
            if cheat_node in graph.nodes:
                new_length = (
                    source_path_lengths[node]
                    + (original_length - source_path_lengths[cheat_node])
                    + cheat_distance
                )

                if original_length - new_length >= 100:
                    good_cheats += 1

    return good_cheats


@benchmark
def part_a(data: tuple[Graph, tuple[int, int], tuple[int, int]]) -> int:
    graph, start, end = data
    return count_good_cheats(graph, start, end, 2)


@benchmark
def part_b(data: tuple[Graph, tuple[int, int], tuple[int, int]]) -> int:
    graph, start, end = data
    return count_good_cheats(graph, start, end, 20)


@benchmark
def parse(data: str) -> tuple[Graph, tuple[int, int], tuple[int, int]]:
    grid = Grid([list(line) for line in data.splitlines()])
    graph = Graph()
    graph.populate_from_grid(
        grid,
        allowed=[".", "S", "E"],
        blocked=["#"],
    )
    return graph, grid.find_value("S"), grid.find_value("E")


test_data_a = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

test_data_b = test_data_a
