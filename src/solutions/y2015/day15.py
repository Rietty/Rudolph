from dataclasses import dataclass
from math import prod
from typing import Any, Iterator

from utils.decorators import benchmark


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavour: int
    texture: int
    calories: int


PROPERTIES = ["capacity", "durability", "flavour", "texture"]
TOTAL_TEASPOONS = 100


def generate_amounts(n: int, remaining: int) -> Iterator[Any]:
    if n == 1:
        yield (remaining,)
        return
    for amount in range(remaining + 1):
        for rest in generate_amounts(n - 1, remaining - amount):
            yield (amount, *rest)


def optimize(data: list[Ingredient], calorie_target: int | None) -> int:
    best = 0

    for amounts in generate_amounts(len(data), TOTAL_TEASPOONS):
        if calorie_target is not None:
            total_calories = sum(ing.calories * amt for ing, amt in zip(data, amounts))
            if total_calories != calorie_target:
                continue

        properties = [
            sum(getattr(ing, prop) * amt for ing, amt in zip(data, amounts))
            for prop in PROPERTIES
        ]
        if any(p <= 0 for p in properties):
            continue

        score = prod(properties)
        if score > best:
            best = score

    return best


@benchmark
def part_a(data: list[Ingredient]) -> int:
    return optimize(data=data, calorie_target=None)


@benchmark
def part_b(data: list[Ingredient]) -> int:
    return optimize(data=data, calorie_target=500)


@benchmark
def parse(data: str) -> list[Ingredient]:
    ingredients: list[Ingredient] = []
    for line in data.splitlines():
        info = line.split()
        ingredients.append(
            Ingredient(
                name=info[0][:-1],
                capacity=int(info[2].strip(",")),
                durability=int(info[4].strip(",")),
                flavour=int(info[6].strip(",")),
                texture=int(info[8].strip(",")),
                calories=int(info[10].strip(",")),
            )
        )
    return ingredients


test_data_a = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

test_data_b = test_data_a
