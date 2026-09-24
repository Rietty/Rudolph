from itertools import groupby

from utils.decorators import benchmark


def increment(s: str) -> str:
    head = s.rstrip("z")  # everything up to the last non-'z'
    wrapped = "a" * (len(s) - len(head))  # each trailing 'z' becomes 'a'
    if not head:  # all z's (or empty): pure wrap
        return wrapped
    return head[:-1] + chr(ord(head[-1]) + 1) + wrapped


def has_straight_increase(text: str) -> bool:
    return any(
        ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c)
        for a, b, c in zip(text, text[1:], text[2:])
    )


def contains_any(text: str, needles: str) -> bool:
    return any(s in text for s in needles)


def has_two_double_letters(text: str) -> bool:
    pairs = sum(len(list(run)) // 2 for char, run in groupby(text) if char.isalpha())
    return pairs >= 2


@benchmark
def part_a(data: str) -> str:
    while True:
        data = increment(data)
        if has_straight_increase(data) and has_two_double_letters(data):
            if not contains_any(data, "iol"):
                return data


@benchmark
def part_b(data: str) -> str:
    return part_a(part_a(data))


@benchmark
def parse(data: str) -> str:
    return data.strip()


test_data_a = """abcdefgh
"""

test_data_b = test_data_a
