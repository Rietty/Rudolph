import math
from enum import Enum

from loguru import logger as log

from utils.decorators import benchmark


class Instruction(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


def compute(registers: list[int], program: list[int]) -> list[int]:
    a, b, c = registers
    halt = False
    ip = 0
    res = []
    jump = False

    while not halt:
        try:
            ins, op = program[ip], program[ip + 1]
        except Exception:
            halt = True
            continue

        combo = op

        if op == 4:
            combo = a
        elif op == 5:
            combo = b
        elif op == 6:
            combo = c
        elif op >= 7:
            raise ValueError("Invalid!")

        match ins:
            case Instruction.ADV.value:
                a = math.trunc((a / (2**combo)))
            case Instruction.BXL.value:
                b = b ^ op
            case Instruction.BST.value:
                b = combo % 8
            case Instruction.JNZ.value:
                if a != 0:
                    ip = op
                    jump = True
            case Instruction.BXC.value:
                b = b ^ c
            case Instruction.OUT.value:
                res.append(combo % 8)
            case Instruction.BDV.value:
                b = math.trunc((a / (2**combo)))
            case Instruction.CDV.value:
                c = math.trunc((a / (2**combo)))

        if not jump:
            ip += 2

        jump = False

    return res


@benchmark
def part_a(data: tuple[list[int], list[int]]) -> str:
    registers, program = data
    return ",".join(map(str, compute(registers, program)))


@benchmark
def part_b(data: tuple[list[int], list[int]]) -> int:
    _, program = data
    current = 0

    for digit in range(len(program) - 1, -1, -1):
        for i in range(0, int(1e10)):
            candidate = current + (1 << (digit * 3)) * i
            output = compute([candidate, 0, 0], program)
            if output[digit:] == program[digit:]:
                current = candidate
                break

    return current


@benchmark
def parse(data: str) -> tuple[list[int], list[int]]:
    registers_str, program_str = data.split("\n\n")
    registers = [int(num) for line in registers_str.splitlines() for num in line.split(":") if num.strip().isdigit()]
    program = list(map(int, program_str.split(":")[1].split(",")))
    return registers, program


test_data_a = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

test_data_b = test_data_a
