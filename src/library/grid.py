# Grid implementation that can be useful for various problems.
from loguru import logger as log

from library.constants import Cardinals, Ordinals


class Grid[T]:
    """Grid class to represent a two-dimensional grid of values."""

    def __init__(self, grid: list[list[T]]) -> None:
        """Create a grid object from a list of lists.

        Args:
            grid (list[list[T]]): List of lists to create the grid from.
        """
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])

    def get_neighbours(
        self, r: int, c: int, diagonals: bool = False
    ) -> list[tuple[int, int]]:
        """Obtains the neighbours of a cell at a given row, col in the grid. Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[tuple[int, int]]: List of coordinates of the neighbours of the cell.
        """
        neighbours = []

        for dr, dc in Cardinals:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.width and 0 <= nc < self.height:
                neighbours.append((nr, nc))

        if diagonals:
            for dr, dc in Ordinals:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.width and 0 <= nc < self.height:
                    neighbours.append((nr, nc))

        return neighbours

    def get_neighbour_values(self, r: int, c: int, diagonals: bool = False) -> list[T]:
        """Get the values of the neighbours of a cell at a given row, col in the grid.  Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[T]: List of the values of the neighbours of the cell.
        """
        return [self.grid[nr][nc] for nr, nc in self.get_neighbours(r, c, diagonals)]

    def get_neighbour_rays(
        self, r: int, c: int, scaling: int, diagonals: bool = False
    ) -> list[list[T]]:
        """Get the values of the neighbours of a cell at a given row, col in the grid.  Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            scaling (int): How far to go in each direction.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[list[T]]: List of the values of the neighbours of the cell.
        """
        rays = []

        for dr, dc in Cardinals:
            ray = []
            for i in range(1, scaling + 1):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < self.width and 0 <= nc < self.height:
                    ray.append((nr, nc))
            rays.append(ray)

        if diagonals:
            for dr, dc in Ordinals:
                ray = []
                for i in range(1, scaling + 1):
                    nr, nc = r + dr * i, c + dc * i
                    if 0 <= nr < self.width and 0 <= nc < self.height:
                        ray.append((nr, nc))
                rays.append(ray)

        return rays

    def get_neighbour_ray_values(
        self, r: int, c: int, scaling: int, diagonals: bool = False
    ) -> list[T]:
        """Get the values of the neighbours of a cell at a given row, col in the grid.  Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            scaling (int): How far to go in each direction.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[T]: List of the values of the neighbours of the cell.
        """
        return [
            [self.grid[nr][nc] for nr, nc in ray]
            for ray in self.get_neighbour_rays(r, c, scaling, diagonals)
        ]

    def find_value(self, value: T, skip: int = 0) -> tuple[int, int]:
        """Find the first occurrence of a value in the grid.

        Args:
            value (T): Value to find in the grid.
            skip (int): Number of occurrences to skip.

        Returns:
            tuple[int, int]: Row and column of the value in the grid.
        """
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == value:
                    if skip == 0:
                        return i, j
                    skip -= 1

        return -1, -1  # Not found

    def width(self) -> int:
        """Width of the grid.

        Returns:
            int: Width of the grid.
        """
        return len(self.grid)

    def height(self) -> int:
        """Height of the grid.

        Returns:
            int: Height of the grid.
        """
        return len(self.grid[0])

    def __getitem__(self, row: int) -> list[T]:
        """Get the value at a given row in the grid.

        Args:
            row (int): Row of the grid.

        Returns:
            list[T]: List of values at the given row.
        """
        return self.grid[row]

    def __setitem__(self, row: int, value: list[T]) -> None:
        """Set the value at a given row in the grid.

        Args:
            row (int): Row of the grid.
            value (list[T]): Value to set at the given row.
        """
        self.grid[row] = value

    def __repr__(self):
        """String representation of the grid.

        Returns:
            str: String representation of the grid.
        """
        return "\n".join(["".join([str(cell) for cell in row]) for row in self.grid])
