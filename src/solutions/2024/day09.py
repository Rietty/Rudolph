import logging
from dataclasses import dataclass
from typing import List

from utils.decorators import benchmark

log = logging.getLogger(__name__)


@dataclass
class Block:
    id: int  # Block ID, -1 for free space
    type: bool  # True for file, False for free space


def parse_disk_map(disk_map: str) -> List[Block]:
    blocks = []
    is_file = True
    block_id = 0

    for char in disk_map:
        length = int(char)
        if is_file:
            for _ in range(length):
                blocks.append(Block(id=block_id, type=True))
            block_id += 1
        else:
            for _ in range(length):
                blocks.append(Block(id=-1, type=False))
        is_file = not is_file

    return blocks


def compact_disk(blocks: List[Block]) -> None:
    left, right = 0, len(blocks) - 1

    while left < right:
        while left < len(blocks) and blocks[left].type:
            left += 1

        while right >= 0 and not blocks[right].type:
            right -= 1

        if left < right:
            blocks[left], blocks[right] = blocks[right], blocks[left]
            left += 1
            right -= 1


def calculate_checksum(blocks: List[Block]) -> int:
    checksum = 0
    for i, block in enumerate(blocks):
        if block.type:
            checksum += i * block.id
    return checksum


@benchmark
def part_a(data: str) -> int:
    disk_map = parse_disk_map(data)
    compact_disk(disk_map)
    return calculate_checksum(disk_map)


@benchmark
def part_b(data: str) -> int:
    return 0


def parse[T](data: str) -> T:
    return data.strip()


test_data_a = """2333133121414131402"""

test_data_b = test_data_a
