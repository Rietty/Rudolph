from dataclasses import dataclass

from utils.decorators import benchmark


@dataclass
class Register:
    id: str
    value: float


@dataclass
class Instruction:
    op: str
    register: str
    offset: int = 0


def process_instruction(instruction: Instruction, a: Register, b: Register) -> int:
    register = a if instruction.register == "a" else b
    match instruction.op:
        case "hlf":
            register.value /= 2
        case "tpl":
            register.value *= 3
        case "inc":
            register.value += 1
        case "jmp":
            return instruction.offset
        case "jie":
            return instruction.offset if register.value % 2 == 0 else 1
        case "jio":
            return instruction.offset if register.value == 1 else 1
    return 1


@benchmark
def part_a(data: list[Instruction]) -> float:
    index: int = 0
    a: Register = Register("a", 0)
    b: Register = Register("b", 0)
    while index < len(data):
        index += process_instruction(data[index], a, b)
    return b.value


@benchmark
def part_b(data: list[Instruction]) -> float:
    index: int = 0
    a: Register = Register("a", 1)
    b: Register = Register("b", 0)
    while index < len(data):
        index += process_instruction(data[index], a, b)
    return b.value


@benchmark
def parse(data: str) -> list[Instruction]:
    instructions: list[Instruction] = []
    for line in data.splitlines():
        values = line.split()
        match values[0]:
            case "hlf":
                instructions.append(Instruction("hlf", values[1]))
            case "tpl":
                instructions.append(Instruction("tpl", values[1]))
            case "inc":
                instructions.append(Instruction("inc", values[1]))
            case "jmp":
                instructions.append(Instruction("jmp", "", int(values[1])))
            case "jie":
                instructions.append(
                    Instruction("jie", values[1].strip(","), int(values[2]))
                )
            case "jio":
                instructions.append(
                    Instruction("jio", values[1].strip(","), int(values[2]))
                )
    return instructions


test_data_a = """inc a
jio a, +2
tpl a
inc a
"""

test_data_b = test_data_a
