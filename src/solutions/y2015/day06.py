from dataclasses import dataclass

from utils.decorators import benchmark


@dataclass
class Instruction:
    op: str
    x1: int
    y1: int
    x2: int
    y2: int


@benchmark
def part_a(data: list[Instruction]) -> int:
    grid: list[list[int]] = [[0] * 1000 for _ in range(1000)]
    for d in data:
        n = d.x2 - d.x1 + 1
        s = slice(d.x1, d.x2 + 1)
        for y in range(d.y1, d.y2 + 1):
            row = grid[y]
            match d.op:
                case "toggle":
                    row[s] = [1 - v for v in row[s]]
                case "on":
                    row[s] = [1] * n
                case "off":
                    row[s] = [0] * n
                case _:
                    pass
    return sum(map(sum, grid))


@benchmark
def part_b(data: list[Instruction]) -> int:
    grid: list[list[int]] = [[0] * 1000 for _ in range(1000)]
    for d in data:
        s = slice(d.x1, d.x2 + 1)
        for y in range(d.y1, d.y2 + 1):
            row = grid[y]
            match d.op:
                case "toggle":
                    row[s] = [v + 2 for v in row[s]]
                case "on":
                    row[s] = [v + 1 for v in row[s]]
                case "off":
                    row[s] = [max(0, v - 1) for v in row[s]]
    return sum(map(sum, grid))


@benchmark
def parse(data: str) -> list[Instruction]:
    out = []
    for line in data.splitlines():
        op, a, _, b = line.replace("turn ", "").split()
        x1, y1 = map(int, a.split(","))
        x2, y2 = map(int, b.split(","))
        out.append(Instruction(op, x1, y1, x2, y2))
    return out


test_data_a = """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""

test_data_b = test_data_a
