from dataclasses import dataclass

from utils.decorators import benchmark


@dataclass
class Reindeer:
    name: str
    velocity: int
    flight_time: int
    rest_time: int
    distance: int = 0
    phase_time: int = 0
    traveling: bool = True
    points: int = 0


def race(data: list[Reindeer], time: int) -> list[Reindeer]:
    for t in range(2503):
        for r in data:
            match r.traveling:
                case True:
                    r.distance += r.velocity
                    r.phase_time += 1
                    if r.phase_time == r.flight_time:
                        r.phase_time = 0
                        r.traveling = not r.traveling
                case False:
                    r.phase_time += 1
                    if r.phase_time == r.rest_time:
                        r.phase_time = 0
                        r.traveling = not r.traveling
        furthest = max(r.distance for r in data)
        for r in data:
            if r.distance == furthest:
                r.points += 1
    return data


@benchmark
def part_a(data: list[Reindeer]) -> int:
    return max(r.distance for r in race(data, 2503))


@benchmark
def part_b(data: list[Reindeer]) -> int:
    return max(r.points for r in race(data, 2503))


@benchmark
def parse(data: str) -> list[Reindeer]:
    reindeer: list[Reindeer] = []
    for line in data.splitlines():
        info = line.split()
        reindeer.append(Reindeer(info[0], int(info[3]), int(info[6]), int(info[13])))
    return reindeer


test_data_a = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

test_data_b = test_data_a
