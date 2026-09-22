from utils.decorators import benchmark


def deliver(data: list[str]) -> set[tuple[int, int]]:
    locations: set[tuple[int, int]] = set()
    x, y = 0, 0
    for d in data:
        locations.add((x, y))
        match d:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
            case _:
                pass
    locations.add((x, y))
    return locations


@benchmark
def part_a(data: list[str]) -> int:
    return len(deliver(data))


@benchmark
def part_b(data: list[str]) -> int:
    return len(deliver(data[0::2]) | deliver(data[1::2]))


@benchmark
def parse(data: str) -> list[str]:
    return [d for d in data.strip()]


test_data_a = """^>v<
"""

test_data_b = test_data_a
