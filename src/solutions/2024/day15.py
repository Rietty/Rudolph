import typing

from loguru import logger as log

from utils.decorators import benchmark

type Coordinates = tuple[int, int]
type Location = tuple[Coordinates, str]
type Grid = list[list[str]]

WALL: typing.Final[str] = "#"
EMPTY: typing.Final[str] = "."
BOX: typing.Final[str] = "O"
ROBOT: typing.Final[str] = "@"


# Function to advance one instruction in the given direction.
def advance(
    grid: Grid, robot_pos: Coordinates, direction: str
) -> tuple[Grid, Coordinates]:
    direction_map: dict[str, Coordinates] = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    dx, dy = direction_map[direction]
    x, y = robot_pos
    target_x, target_y = x + dx, y + dy

    # Check boundaries
    if not (0 <= target_x < len(grid[0]) and 0 <= target_y < len(grid)):
        return grid, robot_pos  # Movement invalid

    target_cell = grid[target_y][target_x]

    if target_cell == WALL:
        return grid, robot_pos  # Robot can't move into a wall

    if target_cell == EMPTY:
        # Move robot
        grid[y][x], grid[target_y][target_x] = EMPTY, ROBOT
        return grid, (target_x, target_y)

    if target_cell == BOX:
        # Check the sequence of boxes
        box_positions = []
        bx, by = target_x, target_y
        while 0 <= bx < len(grid[0]) and 0 <= by < len(grid) and grid[by][bx] == BOX:
            box_positions.append((bx, by))
            bx += dx
            by += dy

        # bx and by now point to the cell after the last box in the sequence
        if not (0 <= bx < len(grid[0]) and 0 <= by < len(grid)):
            return grid, robot_pos  # Movement invalid

        if grid[by][bx] in {WALL, BOX}:
            return grid, robot_pos  # Can't push into a wall or another box

        # Move all boxes
        for bx, by in reversed(box_positions):
            grid[by][bx] = EMPTY
            grid[by + dy][bx + dx] = BOX

        # Move robot
        grid[y][x] = EMPTY
        grid[target_y][target_x] = ROBOT

        return grid, (target_x, target_y)

    return grid, robot_pos


# Print the grid.
def print_grid(grid: Grid):
    for row in grid:
        print("".join(row))


def scale_up_map(grid: Grid) -> Grid:
    new_grid = []
    for row in grid:
        scaled_row = []
        for cell in row:
            if cell == WALL:
                scaled_row.extend([WALL, WALL])
            elif cell == BOX:
                scaled_row.extend(["[", "]"])
            elif cell == EMPTY:
                scaled_row.extend([EMPTY, EMPTY])
            elif cell == ROBOT:
                scaled_row.extend([ROBOT, EMPTY])
        new_grid.append(scaled_row)
    return new_grid


@benchmark
def part_a[T](data: T) -> int:
    grid, directions = data

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ROBOT:
                robot_pos = (x, y)
                break

    for direction in directions:
        grid, robot_pos = advance(grid, robot_pos, direction)

    total_gps = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == BOX:
                gps_coord = 100 * y + x
                total_gps += gps_coord

    return total_gps


def advance_in_scaled_map(
    grid: Grid, robot_pos: Coordinates, direction: str
) -> tuple[Grid, Coordinates]:
    direction_map = {"^": (0, -1), "v": (0, 1), "<": (-2, 0), ">": (2, 0)}
    dx, dy = direction_map[direction]
    x, y = robot_pos
    target_x, target_y = x + dx, y + dy

    # Check boundaries
    if not (0 <= target_x < len(grid[0]) and 0 <= target_y < len(grid)):
        return grid, robot_pos  # Movement invalid

    target_cell = grid[target_y][target_x]

    if target_cell == WALL:
        return grid, robot_pos  # Robot can't move into a wall

    if target_cell == EMPTY:
        # Move robot
        grid[y][x], grid[target_y][target_x] = EMPTY, ROBOT
        return grid, (target_x, target_y)

    if target_cell == "[" and grid[target_y][target_x + 1] == "]":
        # Check the sequence of boxes
        box_positions = []
        bx, by = target_x, target_y
        while (
            0 <= bx < len(grid[0]) - 1
            and 0 <= by < len(grid)
            and grid[by][bx] == "["
            and grid[by][bx + 1] == "]"
        ):
            box_positions.append((bx, by))
            bx += dx
            by += dy

        # bx and by now point to the cell after the last box in the sequence
        if not (0 <= bx < len(grid[0]) - 1 and 0 <= by < len(grid)):
            return grid, robot_pos  # Movement invalid

        if grid[by][bx] in {WALL, "["}:
            return grid, robot_pos  # Can't push into a wall or another box

        # Move all boxes
        for bx, by in reversed(box_positions):
            grid[by][bx], grid[by][bx + 1] = EMPTY, EMPTY
            grid[by + dy][bx + dx], grid[by + dy][bx + dx + 1] = "[", "]"

        # Move robot
        grid[y][x] = EMPTY
        grid[target_y][target_x] = ROBOT

        return grid, (target_x, target_y)

    return grid, robot_pos


@benchmark
def part_b[T](data: T) -> int:
    grid, directions = data
    grid = scale_up_map(grid)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ROBOT:
                robot_pos = (x, y)
                break

    for direction in directions:
        grid, robot_pos = advance_in_scaled_map(grid, robot_pos, direction)

    print_grid(grid)

    total_gps = 0
    for y, row in enumerate(grid):
        for x in range(0, len(row), 2):
            if row[x] == "[" and row[x + 1] == "]":
                min_vertical_distance = min(y, len(grid) - y - 1)
                min_horizontal_distance = min(x // 2, (len(row) // 2) - (x // 2) - 1)
                gps_coord = 100 * min_vertical_distance + min_horizontal_distance
                total_gps += gps_coord
    return total_gps


@benchmark
def parse[T](data: str) -> T:
    # Parse the data in test_data_a into a grid (list of lists) and a list of directions.
    grid = []
    directions = []
    for line in data.splitlines():
        if line.startswith("#"):
            grid.append(list(line))
        elif not line.startswith("\n"):
            directions.extend(list(line))
    return grid, directions


test_data_a = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

test_data_b = test_data_a
