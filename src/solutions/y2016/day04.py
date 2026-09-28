from collections import Counter
from dataclasses import dataclass
from string import ascii_lowercase as abc

from utils.decorators import benchmark


def shift(text: str, n: int) -> str:
    n %= 26
    table = str.maketrans(abc, abc[n:] + abc[:n])
    return text.translate(table)


@dataclass
class Room:
    name: str
    checksum: str
    sector: int


@benchmark
def part_a(data: list[Room]) -> int:
    sum: int = 0
    for room in data:
        counter = Counter(c for c in room.name if c.isalpha())
        top5 = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
        checksum = "".join(letter for letter, _ in top5)
        if checksum == room.checksum:
            sum += room.sector
    return sum


@benchmark
def part_b(data: list[Room]) -> int:
    for room in data:
        counter = Counter(c for c in room.name if c.isalpha())
        top5 = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
        checksum = "".join(letter for letter, _ in top5)
        if checksum == room.checksum:
            value = shift(room.name, room.sector)
            if value == "northpole-object-storage":
                return room.sector
    return 0


@benchmark
def parse(data: str) -> list[Room]:
    rooms: list[Room] = []
    for line in data.splitlines():
        head, checksum = line.rstrip("]").split("[")
        name, sector_id = head.rsplit("-", 1)
        rooms.append(Room(name, checksum, int(sector_id)))
    return rooms


test_data_a = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

test_data_b = test_data_a
