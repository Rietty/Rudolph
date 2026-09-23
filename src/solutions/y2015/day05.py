import re

from utils.decorators import benchmark


def has_min_vowels(text: str, n: int = 3) -> bool:
    return sum(c in "aeiou" for c in text.lower()) >= n


def contains_any(text: str, needles: list[str]) -> bool:
    return any(s in text for s in needles)


def has_double_letter(text: str) -> bool:
    return any(a == b and a.isalpha() for a, b in zip(text, text[1:]))


def has_repeated_pair(text: str) -> bool:
    return bool(re.search(r"(..).*\1", text))


def has_sandwich(text: str) -> bool:
    return bool(re.search(r"(.).\1", text))


def is_nice(s: str) -> bool:
    if (
        has_min_vowels(s, 3)
        and has_double_letter(s)
        and not contains_any(s, ["ab", "cd", "pq", "xy"])
    ):
        return True
    return False


def is_also_nice(s: str) -> bool:
    if has_repeated_pair(s) and has_sandwich(s):
        return True
    return False


@benchmark
def part_a(data: list[str]) -> int:
    return sum(is_nice(d) for d in data)


@benchmark
def part_b(data: list[str]) -> int:
    return sum(is_also_nice(d) for d in data)


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


test_data_a = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""

test_data_b = test_data_a
