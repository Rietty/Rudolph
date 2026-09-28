from dataclasses import dataclass

from library.grid import Grid
from utils.decorators import benchmark


@dataclass
class Operation:
    pass


@dataclass
class Rotate(Operation):
    rotation: int = 0
    index: int = 0
    shift: int = 0


@dataclass
class Create(Operation):
    sx: int = 0
    sy: int = 0


@dataclass
class Instruction:
    op: Operation


def lights_on(grid: Grid[str], dx: int, dy: int) -> Grid[str]:
    for r in range(dx):
        for c in range(dy):
            grid[c][r] = "#"
    return grid


def process_instructions(data: list[Instruction], grid: Grid[str]) -> Grid[str]:
    for instruction in data:
        match instruction.op:
            case Rotate(rotation=r, index=i, shift=s):
                if r == 1:
                    grid.rotate_row(i, s)
                else:
                    grid.rotate_column(i, s)
            case Create(sx=x, sy=y):
                grid = lights_on(grid, x, y)
            case _:
                raise TypeError(f"unknown operation: {instruction.op!r}")
    return grid


@benchmark
def part_a(data: list[Instruction]) -> int:
    grid: Grid[str] = Grid([["." for _ in range(50)] for _ in range(6)])
    grid = process_instructions(data, grid)
    return grid.count("#")


@benchmark
def part_b(data: list[Instruction]) -> str:
    grid: Grid[str] = Grid([["." for _ in range(50)] for _ in range(6)])
    grid = process_instructions(data, grid)
    print(grid)
    return ""


@benchmark
def parse(data: str) -> list[Instruction]:
    instructions: list[Instruction] = []
    for line in data.splitlines():
        words = line.split()
        match words[0]:
            case "rect":
                d = words[1].split("x")
                instructions.append(Instruction(Create(sx=int(d[0]), sy=int(d[1]))))
            case "rotate":
                rotation = 1 if words[1] == "row" else 0
                index = int(words[2].split("=")[1])
                shift = int(words[4])
                instructions.append(
                    Instruction(Rotate(rotation=rotation, index=index, shift=shift))
                )
    return instructions


test_data_a = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""

test_data_b = test_data_a
