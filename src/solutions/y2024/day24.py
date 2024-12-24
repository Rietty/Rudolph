from collections import deque
from enum import Enum

from loguru import logger as log

from utils.decorators import benchmark


class Operation(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


@benchmark
def part_a(data: tuple[dict[str, int], deque[tuple[str, str, str, str]]]) -> int:
    wires, gates = data

    while gates:
        w1, op, w2, w3 = gates.popleft()

        if w1 not in wires or w2 not in wires:
            gates.append((w1, op, w2, w3))
            continue

        match op:
            case Operation.AND.value:
                wires[w3] = wires[w1] & wires[w2]
            case Operation.OR.value:
                wires[w3] = wires[w1] | wires[w2]
            case Operation.XOR.value:
                wires[w3] = wires[w1] ^ wires[w2]

    return int(
        "".join(
            map(
                str,
                [
                    wires[key]
                    for key in sorted(
                        (k for k in wires if k.startswith("z")),
                        key=lambda x: int(x[1:]),
                        reverse=True,
                    )
                ],
            )
        ),
        2,
    )


@benchmark
def part_b(data: tuple[dict[str, int], deque[tuple[str, str, str, str]]]) -> int:
    return 0


@benchmark
def parse(data: str) -> tuple[dict[str, int], deque[tuple[str, str, str, str]]]:
    wires, gates = data.split("\n\n")
    processed_wires: dict[str, int] = {}
    processed_gates: deque[tuple[str, str, str, str]] = deque()

    for wire in wires.splitlines():
        wire_name, wire_value = wire.split(": ")
        processed_wires[wire_name] = int(wire_value)

    for gate in gates.splitlines():
        w1, op, w2, _, w3 = gate.split()
        processed_gates.append((w1, op, w2, w3))

    return processed_wires, processed_gates


test_data_a = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

test_data_b = test_data_a
