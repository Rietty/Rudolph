import re

from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a(data: str) -> int:
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return sum([int(x) * int(y) for x, y in regex.findall(data)])


@benchmark
def part_b(data: str) -> int:
    mul = re.compile(r"mul\((\d+),(\d+)\)")
    control = re.compile(r"do\(\)|don't\(\)")

    active = True
    total_sum = 0

    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    for match in matches:
        if control.match(match):
            if match == "don't()":
                active = False
            elif match == "do()":
                active = True
        elif active:
            mul_match = mul.match(match)
            if mul_match:
                x, y = map(int, mul_match.groups())
                total_sum += x * y

    return total_sum


@benchmark
def parse(data: str) -> str:
    return data


test_data_a = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

test_data_b = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
