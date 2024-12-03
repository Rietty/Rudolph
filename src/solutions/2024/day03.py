import logging
import re

from utils.decorators import benchmark

log = logging.getLogger(__name__)


@benchmark
def part_a[T](data: T) -> int:
    # Parse out only the numbers with format of mul(x,y) where x and y are integers of size 1 to 3 digits.
    # Multiply x*y and sum all the results.
    # Return the sum.
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return sum([int(x) * int(y) for x, y in regex.findall(data)])


@benchmark
def part_b[T](data: T) -> int:
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


def parse[T](data: str) -> T:
    return data


test_data_a = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

test_data_b = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
