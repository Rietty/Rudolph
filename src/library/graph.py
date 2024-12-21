# Graph helper library for common graph operations used in problems.
import networkx as nx
from loguru import logger as log

from library.grid import Grid


class Graph:
    """Graph class for common graph operations. Uses NetworkX as the underlying graph library."""

    def __init__(self, directed=False):
        """Initialize the Graph object with a directed or undirected graph.

        Args:
            directed (bool, optional): Indicates if edges are directed or not. Defaults to False.
        """
        self._graph = nx.DiGraph() if directed else nx.Graph()

    def __getattr__(self, name):
        if hasattr(self._graph, name):
            return getattr(self._graph, name)
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def get(self):
        """Return the underlying NetworkX graph object.

        Returns:
            nx.Graph or nx.DiGraph: The underlying NetworkX graph object.
        """
        return self._graph

    def populate_from_grid[
        T
    ](
        self,
        grid: Grid,
        allowed: list[T] = None,
        blocked: list[T] = None,
        function: callable = None,
    ) -> None:
        for r in range(grid.width):
            for c in range(grid.height):
                if grid[r][c] in blocked:
                    continue
                for dr, dc in grid.get_neighbours(r, c):
                    if allowed is None or grid[dr][dc] in allowed:
                        if function:
                            if function(grid[r][c], grid[dr][dc]):
                                self.add_edge((r, c), (dr, dc))
                        else:
                            self.add_edge((r, c), (dr, dc))

    def __repr__(self):
        return f"{self._graph}"
