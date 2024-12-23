# Graph helper library for common graph operations used in problems.
from typing import Callable

import networkx as nx
from loguru import logger as log

from library.grid import Grid


def graph_from_grid[
    T
](
    grid: Grid,
    directed: bool = False,
    allowed: list[T] | None = None,
    blocked: list[T] | None = None,
    function: Callable | None = None,
) -> None:
    graph = nx.DiGraph() if directed else nx.Graph()

    for r in range(grid.width):
        for c in range(grid.height):
            if blocked and grid[r][c] in blocked:
                continue
            for dr, dc in grid.get_neighbours(r, c):
                if allowed is None or grid[dr][dc] in allowed:
                    if function:
                        if function(grid[r][c], grid[dr][dc]):
                            graph.add_edge((r, c), (dr, dc))
                    else:
                        graph.add_edge((r, c), (dr, dc))

    return graph
