import ast

from utils.decorators import benchmark

type Pair = tuple[str, str]


@benchmark
def part_a(data: list[Pair]) -> int:
    return sum(len(raw) - len(s) for raw, s in data)


@benchmark
def part_b(data: list[Pair]) -> int:
    return sum(2 + raw.count('"') + raw.count("\\") for raw, _ in data)


@benchmark
def parse(data: str) -> list[Pair]:
    lines = [line for line in data.splitlines() if line.strip()]
    return [(line, ast.literal_eval(line)) for line in lines]


test_data_a = """""
"abc"
"aaa\"aaa"
"\x27"
"""

test_data_b = test_data_a
