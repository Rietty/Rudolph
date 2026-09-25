import json
from typing import Any, Iterator

from utils.decorators import benchmark


def find_numbers(obj: Any, bad_value: str = "") -> Iterator[Any]:
    if isinstance(obj, bool):
        return
    if isinstance(obj, (int, float)):
        yield obj
    elif isinstance(obj, dict):
        if bad_value in obj.values() and bad_value:
            return
        for v in obj.values():
            yield from find_numbers(v, bad_value)
    elif isinstance(obj, list):
        for v in obj:
            yield from find_numbers(v, bad_value)


@benchmark
def part_a(data: Any) -> int:
    return sum(find_numbers(data))


@benchmark
def part_b(data: Any) -> int:
    return sum(find_numbers(data, "red"))


@benchmark
def parse(data: str) -> Any:
    return json.loads(data)


test_data_a = """{"a":2,"b":4}
"""

test_data_b = test_data_a
