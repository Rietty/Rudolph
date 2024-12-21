from collections import deque
from dataclasses import dataclass

from loguru import logger as log

from utils.decorators import benchmark


@dataclass
class Block:
    id: int  # Block ID, -1 for free space
    type: bool  # True for file, False for free space

    # Print blocks by having a `.` for free space and `#` for files.
    def __repr__(self) -> str:
        return f"{self.id}" if self.type else "."


def defragment_disk(blocks: list[Block]) -> None:
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


def super_defragment_disk(blocks: list[Block]) -> None:
    # Keep track of all the file blocks.
    file_blocks: deque[tuple[int, int, int]] = deque()

    # Go through the blocks using pointers to keep track of the size of the same type of blocks and their starting index to add to the deques.
    left, right = 0, 0
    while right < len(blocks):
        while (
            right < len(blocks)
            and blocks[right].type == blocks[left].type
            and blocks[right].id == blocks[left].id
        ):
            right += 1

        if blocks[left].type:
            file_blocks.append((left, right - left, blocks[left].id))

        left = right

    # Keep track of where we are in the current blocks list and we iterate until file_blocks is empty.
    while file_blocks:
        # Start from the index 0 of the blocks list.
        left, right = 0, 0

        # Pop the first element from the file_blocks list.
        start, size, block_id = file_blocks.pop()

        while blocks[left].type:
            left += 1

        right = left

        while not blocks[right].type:
            right += 1

        # Calculate the size of the free space.
        free_space = right - left

        log.debug(f"Free space is from {left} to {right} with size {free_space}")

        # Check if the free space is enough to fit the file.
        if free_space >= size:
            # If the free space is enough, take the block info we popped, and use it to set the next size blocks to the file with correct id.
            for i in range(start, start + size):
                blocks[left + i - start] = Block(id=block_id, type=True)

            left += size
        else:
            continue

        log.debug("Blocks: %s", "".join(map(str, blocks)))


def calculate_checksum(blocks: list[Block]) -> int:
    checksum = 0
    for i, block in enumerate(blocks):
        if block.type:
            checksum += i * block.id
    return checksum


@benchmark
def part_a(data: list[Block]) -> int:
    defragment_disk(data)  # No return as we simply modify the list in place.
    return calculate_checksum(data)


@benchmark
def part_b(data: list[Block]) -> int:
    super_defragment_disk(data)  # No return as we simply modify the list in place.
    return calculate_checksum(data)


@benchmark
def parse(data: str) -> list[Block]:
    blocks = []
    is_file = True
    block_id = 0

    for char in data.strip():
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


test_data_a = """2333133121414131402"""

test_data_b = test_data_a
