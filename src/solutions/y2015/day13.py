from dataclasses import dataclass
from itertools import permutations

from utils.decorators import benchmark


@dataclass
class SeatingRule:
    a: str
    b: str
    happiness: int
    delta: int


def get_people(rules: list[SeatingRule]) -> set[str]:
    return {p for r in rules for p in (r.a, r.b)}


def happiness_lookup(rules: list[SeatingRule]) -> dict[tuple[str, str], int]:
    return {(r.a, r.b): r.delta * r.happiness for r in rules}


def total_happiness(
    arrangement: tuple[str, ...], lookup: dict[tuple[str, str], int]
) -> int:
    pairs = zip(arrangement, arrangement[1:] + arrangement[:1])
    return sum(lookup.get((a, b), 0) + lookup.get((b, a), 0) for a, b in pairs)


def get_best_score(data: list[SeatingRule]) -> float:
    people = get_people(data)
    lookup = happiness_lookup(data)
    best_score = float("-inf")
    for perm in permutations(people):
        best_score = max(best_score, total_happiness(perm, lookup))
    return best_score


@benchmark
def part_a(data: list[SeatingRule]) -> float:
    return get_best_score(data)


@benchmark
def part_b(data: list[SeatingRule]) -> float:
    people = get_people(data)
    for p in people:
        data.append(SeatingRule("self", p, 0, 1))
        data.append(SeatingRule(p, "self", 0, 1))
    return get_best_score(data)


@benchmark
def parse(data: str) -> list[SeatingRule]:
    rules: list[SeatingRule] = []
    for line in data.splitlines():
        a, _, gl, amount, _, _, _, _, _, _, b = line.split()
        b = b.strip(".")
        delta = 1 if gl == "gain" else -1
        rules.append(SeatingRule(a, b, int(amount), delta))
    return rules


test_data_a = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""

test_data_b = test_data_a
