import re
from dataclasses import dataclass

from utils.decorators import benchmark

ABBA = re.compile(r"(.)(?!\1)(.)\2\1")
ABA = re.compile(r"(?=((.)(?!\2)(.)\2))", re.DOTALL)


def has_abba(s: str) -> bool:
    return ABBA.search(s) is not None


def find_aba_bab(s1: str, s2: str) -> list[tuple[str, str]]:
    pairs = []
    for m in ABA.finditer(s1):
        _, a, b = m.groups()
        bab = f"{b}{a}{b}"
        if bab in s2:
            pairs.append((f"{a}{b}{a}", bab))
    return pairs


def has_aba_bab(s1: str, s2: str) -> bool:
    return bool(find_aba_bab(s1, s2))


@dataclass
class IP:
    address: str
    cleaned: str
    hypernets: list[str]


@benchmark
def part_a(data: list[IP]) -> int:
    count: int = 0
    for line in data:
        is_valid: bool = True
        if has_abba(line.cleaned):
            for hn in line.hypernets:
                if has_abba(hn):
                    is_valid = False
            count += 1 if is_valid else 0
    return count


@benchmark
def part_b(data: list[IP]) -> int:
    count: int = 0
    for line in data:
        for hn in line.hypernets:
            if has_aba_bab(line.cleaned, hn):
                count += 1
                break
    return count


@benchmark
def parse(data: str) -> list[IP]:
    ips: list[IP] = []
    for line in data.splitlines():
        matches = re.findall(r"\[(.*?)\]", line)
        cleaned = re.sub(r"\[.*?\]", "-", line)
        ips.append(IP(line, cleaned, matches))
    return ips


test_data_a = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""

test_data_b = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
"""
