from dataclasses import dataclass
from typing import Any, cast

from z3 import If, Int, Optimize, sat

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


def optimize(data: list[Ingredient], calorie_target: int | None) -> int:
    n = len(data)
    x = [Int(f"x_{i}") for i in range(n)]
    opt = Optimize()

    opt.add(sum(x) == TOTAL_TEASPOONS)
    for xi in x:
        opt.add(xi >= 0)

    if calorie_target is not None:
        total_calories = sum(ing.calories * xi for ing, xi in zip(data, x))
        opt.add(total_calories == calorie_target)

    property_values = []
    for prop in PROPERTIES:
        raw = sum(getattr(ing, prop) * xi for ing, xi in zip(data, x))
        clamped = If(raw >= 0, raw, 0)
        property_values.append(clamped)

    objective = property_values[0]
    for val in property_values[1:]:
        objective = objective * val

    handle = opt.maximize(objective)

    if opt.check() != sat:
        raise ValueError("no feasible ingredient mix satisfies the constraints")

    return int(cast(Any, handle.value()).as_long())


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
