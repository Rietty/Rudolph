from dataclasses import dataclass, replace

from utils.decorators import benchmark


@dataclass(frozen=True)
class State:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    shield_timer: int
    poison_timer: int
    recharge_timer: int


def castable_spells(state: State) -> list[tuple[str, int]]:
    spells: list[tuple[str, int]] = []

    if state.player_mana >= 53:
        spells.append(("mm", 53))

    if state.player_mana >= 73:
        spells.append(("dr", 73))

    if state.player_mana >= 113 and state.shield_timer == 0:
        spells.append(("sh", 113))

    if state.player_mana >= 173 and state.poison_timer == 0:
        spells.append(("po", 173))

    if state.player_mana >= 229 and state.recharge_timer == 0:
        spells.append(("re", 229))

    return spells


def boss_turn(state: State) -> State:
    state = apply_effects(state, False)
    if state.boss_hp <= 0:
        return state

    armor = 7 if state.shield_timer > 0 else 0
    damage = max(1, state.boss_damage - armor)
    return replace(state, player_hp=state.player_hp - damage)


def apply_effects(state: State, hard_mode: bool = False) -> State:
    boss_hp = state.boss_hp
    mana = state.player_mana
    player_hp = state.player_hp

    if hard_mode:
        player_hp -= 1

    if state.poison_timer > 0:
        boss_hp -= 3
    if state.recharge_timer > 0:
        mana += 101

    return replace(
        state,
        player_hp=player_hp,
        boss_hp=boss_hp,
        player_mana=mana,
        shield_timer=max(0, state.shield_timer - 1),
        poison_timer=max(0, state.poison_timer - 1),
        recharge_timer=max(0, state.recharge_timer - 1),
    )


def cast(state: State, spell: str) -> State:
    new_state: State  # declare the type once, up front
    match spell:
        case "mm":
            new_state = replace(
                state, boss_hp=state.boss_hp - 4, player_mana=state.player_mana - 53
            )
        case "dr":
            new_state = replace(
                state,
                boss_hp=state.boss_hp - 2,
                player_hp=state.player_hp + 2,
                player_mana=state.player_mana - 73,
            )
        case "sh":
            new_state = replace(
                state, shield_timer=6, player_mana=state.player_mana - 113
            )
        case "po":
            new_state = replace(
                state, poison_timer=6, player_mana=state.player_mana - 173
            )
        case "re":
            new_state = replace(
                state, recharge_timer=5, player_mana=state.player_mana - 223
            )
        case _:
            raise ValueError(f"Unknown spell: {spell}")
    return new_state


BEST: float = float("inf")


def battle(state: State, mana_spent: int, hard_mode: bool = False) -> None:
    global BEST

    if mana_spent >= BEST:
        return

    state = apply_effects(state, hard_mode)

    if state.player_hp <= 0:
        return

    if state.boss_hp <= 0:
        BEST = min(BEST, mana_spent)
        return

    for spell in castable_spells(state):
        cost = mana_spent + spell[1]
        if cost >= BEST:
            continue

        after_cast = cast(state, spell[0])
        after_boss = boss_turn(after_cast)

        if after_boss.boss_hp <= 0:
            BEST = min(BEST, cost)
            continue
        if after_boss.player_hp <= 0:
            continue

        battle(after_boss, cost, hard_mode)


@benchmark
def part_a(data: dict[str, int]) -> float:
    global BEST
    state = State(50, 500, data["hit points"], data["damage"], 0, 0, 0)
    battle(state, 0)
    return BEST


@benchmark
def part_b(data: dict[str, int]) -> float:
    global BEST
    state = State(50, 500, data["hit points"], data["damage"], 0, 0, 0)
    battle(state, 0, hard_mode=True)
    return BEST


@benchmark
def parse(data: str) -> dict[str, int]:
    boss: dict[str, int] = {}
    for line in data.splitlines():
        info = line.strip().split(":")
        boss[info[0].lower()] = int(info[1])
    return boss


test_data_a = """Hit Points: 13
Damage: 8
"""

test_data_b = test_data_a
