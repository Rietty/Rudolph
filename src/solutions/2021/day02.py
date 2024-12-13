from dataclasses import dataclass

from loguru import logger as log

from utils.decorators import benchmark


@dataclass
class Command:
    dir: str
    dist: int


@benchmark
def part_a[T](data: T) -> int:
    horizontal = 0
    depth = 0
    for command in data:
        if command.dir == "forward":
            horizontal += command.dist
        elif command.dir == "down":
            depth += command.dist
        elif command.dir == "up":
            depth -= command.dist
    return horizontal * depth


@benchmark
def part_b[T](data: T) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for command in data:
        if command.dir == "forward":
            horizontal += command.dist
            depth += aim * command.dist
        elif command.dir == "down":
            aim += command.dist
        elif command.dir == "up":
            aim -= command.dist
    return horizontal * depth


@benchmark
def parse[T](data: str) -> T:
    return list(
        map(
            lambda x: Command(x.split()[0], int(x.split()[1])),
            data.strip().splitlines(),
        )
    )


test_data_a = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

test_data_b = test_data_a
