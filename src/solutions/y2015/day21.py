from itertools import chain, combinations
from typing import Any, Iterator

from utils.decorators import benchmark

ITEM_SHOP = {
    "weapons": [
        {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
        {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
        {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
        {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
        {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
    ],
    "armor": [
        {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
        {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
        {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
        {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
        {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
    ],
    "rings": [
        {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
        {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
        {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
        {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
        {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
        {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
    ],
}


def generate_loadouts(shop: dict[str, list[dict[str, Any]]]) -> Iterator[Any]:
    weapon_choices = shop["weapons"]
    armor_choices = [None, *shop["armor"]]
    ring_choices = list(
        chain(
            combinations(shop["rings"], 0),
            combinations(shop["rings"], 1),
            combinations(shop["rings"], 2),
        )
    )

    for weapon in weapon_choices:
        for armor in armor_choices:
            for rings in ring_choices:
                equipped = [
                    item for item in (weapon, armor, *rings) if item is not None
                ]

                yield {
                    "cost": sum(item["cost"] for item in equipped),
                    "damage": sum(item["damage"] for item in equipped),
                    "armor": sum(item["armor"] for item in equipped),
                    "items": [item["name"] for item in equipped],
                }


def does_player_win(boss: dict[str, int], player: dict[str, int]) -> bool:
    player["hit points"] = 100
    while True:
        boss["hit points"] = boss["hit points"] - (player["damage"] - boss["armor"])

        if boss["hit points"] <= 0:
            return True

        player["hit points"] = player["hit points"] - (boss["damage"] - player["armor"])

        if player["hit points"] <= 0:
            return False


@benchmark
def part_a(data: dict[str, int]) -> int:
    min_cost: int = 10000
    for stats in generate_loadouts(ITEM_SHOP):
        if does_player_win(data.copy(), stats):
            min_cost = min(min_cost, stats["cost"])
    return min_cost


@benchmark
def part_b(data: dict[str, int]) -> int:
    max_cost: int = -10000
    for stats in generate_loadouts(ITEM_SHOP):
        if not does_player_win(data.copy(), stats):
            max_cost = max(max_cost, stats["cost"])
    return max_cost


@benchmark
def parse(data: str) -> dict[str, int]:
    boss: dict[str, int] = {}
    for line in data.splitlines():
        info = line.strip().split(":")
        boss[info[0].lower()] = int(info[1])
    return boss


test_data_a = """Hit Points: 12
Damage: 7
Armor: 2
"""

test_data_b = test_data_a
