import typing
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce

from loguru import logger as log

from utils.decorators import benchmark

WIDTH: typing.Final[int] = 101
HEIGHT: typing.Final[int] = 103

type Position = tuple[int, int]
type Velocity = tuple[int, int]
type Robots = list[Robot]


@dataclass
class Robot:
    position: Position
    velocity: Velocity

    def tick(self):
        x, y = self.position
        x += self.velocity[0]
        y += self.velocity[1]
        x = x % WIDTH
        y = y % HEIGHT
        self.position = (x, y)


def is_tree(robots: Robots) -> bool:
    robots_map = defaultdict(lambda: 0)

    for robot in robots:
        x, y = robot.position
        robots_map[x * WIDTH + y] += 1

    if any(value > 1 for value in robots_map.values()):
        return False

    return True


@benchmark
def part_a[T](data: T) -> int:
    for _ in range(100):
        for robot in data:
            robot.tick()

    counts = [0, 0, 0, 0]

    for robot in data:
        x, y = robot.position
        if x == (WIDTH // 2) or y == (HEIGHT // 2):
            continue
        quadrant = (x > (WIDTH // 2)) + 2 * (y > (HEIGHT // 2))
        counts[quadrant] += 1

    return reduce(lambda x, y: x * y, counts)


@benchmark
def part_b[T](data: T) -> int:
    seconds = 0
    while not is_tree(data):
        for robot in data:
            robot.tick()
        seconds += 1
    return seconds


@benchmark
def parse[T](data: str) -> T:
    robots = []
    for line in data.splitlines():
        parts = line.split()
        position = tuple(map(int, parts[0][2:].split(",")))
        velocity = tuple(map(int, parts[1][2:].split(",")))
        robots.append(Robot(position, velocity))
    return robots


test_data_a = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

test_data_b = test_data_a
