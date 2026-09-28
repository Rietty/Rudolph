# Grid implementation that can be useful for various problems.

from collections.abc import Callable
from typing import Iterator

from library.constants import Cardinals, Ordinals


class Grid[T]:
    """Grid class to represent a two-dimensional grid of values."""

    def __init__(self, grid: list[list[T]]) -> None:
        """Create a grid object from a list of lists.

        Args:
            grid (list[list[T]]): List of lists to create the grid from.
        """
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def get_neighbours(
        self, r: int, c: int, diagonals: bool = False
    ) -> list[tuple[int, int]]:
        """Obtain the neighbours of a cell at a given row, col in the grid. Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[tuple[int, int]]: List of coordinates of the neighbours of the cell.
        """
        neighbours: list[tuple[int, int]] = []

        for dr, dc in Cardinals:
            nr, nc = r + dr, c + dc
            if 0 <= nc < self.width and 0 <= nr < self.height:
                neighbours.append((nr, nc))

        if diagonals:
            for dr, dc in Ordinals:
                nr, nc = r + dr, c + dc
                if 0 <= nc < self.width and 0 <= nr < self.height:
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
    ) -> list[list[tuple[int, int]]]:
        """Get the values of the neighbours of a cell at a given row, col in the grid.  Always from clockwise starting from the top.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            scaling (int): How far to go in each direction.
            diagonals (bool, optional): If we should include diagonals of the cell. Defaults to False.

        Returns:
            list[list[T]]: List of the values of the neighbours of the cell.
        """
        rays: list[list[tuple[int, int]]] = []

        for dr, dc in Cardinals:
            ray: list[tuple[int, int]] = []
            for i in range(1, scaling + 1):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nc < self.width and 0 <= nr < self.height:
                    ray.append((nr, nc))
            rays.append(ray)

        if diagonals:
            for dr, dc in Ordinals:
                ray = []
                for i in range(1, scaling + 1):
                    nr, nc = r + dr * i, c + dc * i
                    if 0 <= nc < self.width and 0 <= nr < self.height:
                        ray.append((nr, nc))
                rays.append(ray)

        return rays

    def get_neighbour_ray_values(
        self, r: int, c: int, scaling: int, diagonals: bool = False
    ) -> list[list[T]]:
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

    def get_region(self, r: int, c: int, s: int) -> list[list[tuple[int, int]]]:
        """Get the region of the grid around a given row, col in the grid. Of size s x s. So if s = 3, it will return a 3x3 grid around the cell.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            s (int): Size of the region.

        Returns:
            list[list[T]]: List of the coordinates of the region.
        """
        region: list[list[tuple[int, int]]] = []
        half_s = s // 2
        for i in range(r - half_s, r + half_s + 1):
            row: list[tuple[int, int]] = []
            for j in range(c - half_s, c + half_s + 1):
                if 0 <= i < self.height and 0 <= j < self.width:
                    row.append((i, j))  # Append coordinates
            region.append(row)
        return region

    def get_region_values(self, r: int, c: int, s: int) -> list[list[T]]:
        """Get the values of the region of the grid around a given row, col in the grid. Of size s x s. So if s = 3, it will return a 3x3 grid around the cell.

        Args:
            r (int): Row of the cell.
            c (int): Column of the cell.
            s (int): Size of the region.

        Returns:
            list[list[T]]: List of the values of the region.
        """
        return [[self.grid[i][j] for i, j in row] for row in self.get_region(r, c, s)]

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

    def rotate_row(self, row: int, shift: int) -> None:
        """Rotate a row horizontally with wraparound.

        A positive shift moves values to the right, a negative shift
        moves them to the left.

        Args:
            row (int): Index of the row to rotate.
            shift (int): Number of positions to shift by.

        Raises:
            IndexError: If the row index is out of range.
        """
        if not 0 <= row < self.height:
            raise IndexError(f"Row {row} out of range for height {self.height}")

        shift %= self.width
        if shift:
            current = self.grid[row]
            self.grid[row] = current[-shift:] + current[:-shift]

    def rotate_column(self, col: int, shift: int) -> None:
        """Rotate a column vertically with wraparound.

        A positive shift moves values down, a negative shift moves them up.

        Args:
            col (int): Index of the column to rotate.
            shift (int): Number of positions to shift by.

        Raises:
            IndexError: If the column index is out of range.
        """
        if not 0 <= col < self.width:
            raise IndexError(f"Column {col} out of range for width {self.width}")

        shift %= self.height
        if shift:
            values = [self.grid[r][col] for r in range(self.height)]
            values = values[-shift:] + values[:-shift]
            for r, value in enumerate(values):
                self.grid[r][col] = value

    def count(self, value: T) -> int:
        """Count how many cells equal a given value.

        Args:
            value (T): The value to look for.

        Returns:
            int: Number of cells equal to value.
        """
        return sum(row.count(value) for row in self.grid)

    def count_type(self, type_: type | tuple[type, ...]) -> int:
        """Count how many cells are an instance of the given type(s).

        Args:
            type_ (type | tuple[type, ...]): Type or tuple of types to match.

        Returns:
            int: Number of cells that are instances of type_.
        """
        return sum(isinstance(cell, type_) for row in self.grid for cell in row)

    def count_if(self, predicate: Callable[[T], bool]) -> int:
        """Count how many cells satisfy a predicate.

        Args:
            predicate (Callable[[T], bool]): Function returning True for cells to count.

        Returns:
            int: Number of cells for which predicate returned True.
        """
        return sum(predicate(cell) for row in self.grid for cell in row)

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

    def __repr__(self) -> str:
        """String representation of the grid.

        Returns:
            str: String representation of the grid.
        """
        return "\n".join(["".join([str(cell) for cell in row]) for row in self.grid])

    def __iter__(self) -> Iterator[list[T]]:
        """Iterator implementation for the grid.

        Returns:
            Iterator[list[T]]: An iterator that gives rows of the grid.
        """
        return iter(self.grid)
