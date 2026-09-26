from dataclasses import dataclass

from utils.decorators import benchmark


@dataclass
class Sue:
    id: int
    properties: dict[str, int]


TARGET = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

GREATER_THAN = {"cats", "trees"}
FEWER_THAN = {"pomeranians", "goldfish"}


def matches(sue: Sue, target: dict[str, int]) -> bool:
    return all(target[key] == value for key, value in sue.properties.items())


def matches_with_restraints(sue: Sue, target: dict[str, int]) -> bool:
    return all(
        value > target[key]
        if key in GREATER_THAN
        else value < target[key]
        if key in FEWER_THAN
        else value == target[key]
        for key, value in sue.properties.items()
    )


@benchmark
def part_a(data: list[Sue]) -> int:
    match = next((s for s in data if matches(s, TARGET)), None)
    return match.id if match is not None else 0


@benchmark
def part_b(data: list[Sue]) -> int:
    match = next((s for s in data if matches_with_restraints(s, TARGET)), None)
    return match.id if match is not None else 0


@benchmark
def parse(data: str) -> list[Sue]:
    sues: list[Sue] = []

    for line in data.splitlines():
        if not line.strip():
            continue
        header, _, rest = line.partition(":")
        sue_id = int(header.split()[1])
        attrs = {
            key.strip(): int(val)
            for key, val in (item.split(":") for item in rest.split(","))
        }
        sues.append(Sue(id=sue_id, properties=attrs))

    return sues


test_data_a = """Sue 1: cars: 9, akitas: 3, goldfish: 0
"""

test_data_b = test_data_a
