from loguru import logger as log
from enum import Enum
import math

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

    while not halt:
        try:
            ins, op = program[ip], program[ip + 1]
        except:
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
            raise ValueError(f"Operand value was {op} - Which is invalid!")

        match ins:
            case Instruction.ADV.value:
                a = math.trunc((a / (2**combo)))
                ip += 2
            case Instruction.BXL.value:
                b = b ^ op
                ip += 2
            case Instruction.BST.value:
                b = combo % 8
                ip += 2
            case Instruction.JNZ.value:
                if a != 0:
                    ip = op
                else:
                    ip += 2
            case Instruction.BXC.value:
                b = b ^ c
                ip += 2
            case Instruction.OUT.value:
                res.append(combo % 8)
                ip += 2
            case Instruction.BDV.value:
                b = math.trunc((a / (2**combo)))
                ip += 2
            case Instruction.CDV.value:
                c = math.trunc((a / (2**combo)))
                ip += 2

    return res


@benchmark
def part_a[T](data: T) -> str:
    registers, program = data
    return ",".join(map(str, compute(registers, program)))


@benchmark
def part_b[T](data: T) -> int:
    return 0


@benchmark
def parse[T](data: str) -> T:
    registers, program = data.split("\n\n")
    registers = [
        int(l)
        for line in registers.splitlines()
        for l in line.split(":")
        if l[1].isdigit()
    ]
    program = list(map(int, program.split(":")[1].split(",")))
    return registers, program


test_data_a = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

test_data_b = test_data_a
