import itertools

import networkx as nx
from loguru import logger as log

from utils.decorators import benchmark

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_graph[T](data: T) -> list[nx.Graph, tuple[int, int], tuple[int, int]]:
    graph = nx.Graph()
    start, end = None, None
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "#":
                continue

            # Add all nodes
            graph.add_node((x, y))

            # For start and end, we save the node as well to pass out.
            if data[x][y] == "S":
                start = (x, y)
            elif data[x][y] == "E":
                end = (x, y)

            # Add all edges that are not walls
            for dx, dy in DIRECTIONS:
                if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]):
                    if data[x + dx][y + dy] != "#":
                        graph.add_edge((x, y), (x + dx, y + dy))

    return graph, start, end


# Possible cheats are all the points within a specific (manhattan) distance.
def get_possible_cheats(size: int) -> list[tuple[int, int, int]]:
    return [
        (x, y, abs(x) + abs(y))
        for x, y in itertools.product(range(-(size + 1), size + 2), repeat=2)
        if abs(x) + abs(y) <= size
    ]


# Count the number of good cheats.
def count_good_cheats(
    graph: nx.Graph,
    start: tuple[int, int],
    end: tuple[int, int],
    max_cheat_distance: int,
) -> int:
    source_path_lengths = nx.single_source_shortest_path_length(graph, start)
    target_path_lengths = nx.single_source_shortest_path_length(graph, end)

    # Get the path length from the source to the end.
    original_length = source_path_lengths[end]

    # For each possible cheat, for every node in the graph, we do the following:
    # 1. Get all possible nodes that are within the cheat distance and in the graph.
    # 2. Look up the shortest path from the source to the node and from the node to the target.
    # 3. Add them together, plus the manhattan distance from the node to the target.
    # 4. If the difference between the original path and the new path is greater than 100, we count it as a good cheat.
    good_cheats = 0

    for cheat_x, cheat_y, cheat_distance in get_possible_cheats(max_cheat_distance):
        for node in graph.nodes:
            x, y = node
            cheat_node = (x + cheat_x, y + cheat_y)
            if cheat_node in graph.nodes:
                new_length = (
                    source_path_lengths[node]
                    + target_path_lengths[cheat_node]
                    + cheat_distance
                )

                if original_length - new_length >= 100:
                    good_cheats += 1

    return good_cheats


@benchmark
def part_a[T](data: T) -> int:
    graph, start, end = get_graph(data)
    return count_good_cheats(graph, start, end, 2)


@benchmark
def part_b[T](data: T) -> int:
    graph, start, end = get_graph(data)
    return count_good_cheats(graph, start, end, 20)


@benchmark
def parse[T](data: str) -> T:
    return [list(line) for line in data.splitlines()]


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
