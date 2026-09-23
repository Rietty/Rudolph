import operator
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache

from utils.decorators import benchmark

MASK = 0xFFFF

OPS: dict[str, Callable[..., int]] = {
    "SET": lambda a: a,
    "NOT": lambda a: ~a,
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}

type Operand = int | str


@dataclass
class Gate:
    op: str
    args: tuple[Operand, ...]


def operand(tok: str) -> Operand:
    return int(tok) if tok.isdigit() else tok


def parse_line(line: str) -> tuple[str, Gate]:
    lhs, dest = line.split(" -> ")
    match lhs.split():
        case [a]:
            return dest, Gate("SET", (operand(a),))
        case ["NOT", a]:
            return dest, Gate("NOT", (operand(a),))
        case [a, ("AND" | "OR" | "LSHIFT" | "RSHIFT") as op, b]:
            return dest, Gate(op, (operand(a), operand(b)))
        case _:
            raise ValueError(f"Unrecognized instruction: {line!r}")


@benchmark
def part_a(data: dict[str, Gate]) -> int:
    @cache
    def signal(operand: Operand) -> int:
        if isinstance(operand, int):
            return operand
        gate = data[operand]
        return OPS[gate.op](*map(signal, gate.args)) & MASK

    return signal("a")


@benchmark
def part_b(data: dict[str, Gate]) -> int:
    a = part_a(data)
    return part_a(data | {"b": Gate("SET", (a,))})


@benchmark
def parse(data: str) -> dict[str, Gate]:
    return dict(parse_line(line) for line in data.splitlines())


test_data_a = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

test_data_b = test_data_a
