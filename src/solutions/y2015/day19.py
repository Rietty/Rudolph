import random
from collections import defaultdict

from utils.decorators import benchmark

INPUT_STRING = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"


def all_replacements(molecule: str, mapping: dict[str, list[str]]) -> set[str]:
    results: set[str] = set()

    for key, values in mapping.items():
        start = 0
        while (idx := molecule.find(key, start)) != -1:
            for value in values:
                new_molecule = molecule[:idx] + value + molecule[idx + len(key) :]
                results.add(new_molecule)
            start = idx + 1

    return results


def fewest_steps(target: str, mapping: dict[str, list[str]]) -> int:
    rules = [(k, v) for k, values in mapping.items() for v in values]

    while True:
        molecule = target
        steps = 0
        rules_order = rules[:]
        random.shuffle(rules_order)

        while molecule != "e":
            for key, value in rules_order:
                if value in molecule:
                    molecule = molecule.replace(value, key, 1)
                    steps += 1
                    break
            else:
                break

        if molecule == "e":
            return steps


@benchmark
def part_a(data: dict[str, list[str]]) -> int:
    return len(all_replacements(INPUT_STRING, data))


@benchmark
def part_b(data: dict[str, list[str]]) -> int:
    return fewest_steps(INPUT_STRING, data)


@benchmark
def parse(data: str) -> dict[str, list[str]]:
    mapping: defaultdict[str, list[str]] = defaultdict(list)
    for line in data.splitlines()[:-2]:
        molecules = line.split(" => ")
        mapping[molecules[0]].append(molecules[1])
    return mapping


test_data_a = """H => HO
H => OH
O => HH
"""

test_data_b = test_data_a
