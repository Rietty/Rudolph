"""Defined constants to be used."""

from enum import Enum
from typing import Final

# The cardinal and ordinal directions
Cardinals: Final = [
    (-1, 0),  # North
    (0, 1),  # East
    (1, 0),  # South
    (0, -1),  # West
]

Ordinals: Final = [
    (-1, 1),  # North East
    (1, 1),  # South East
    (1, -1),  # South West
    (-1, -1),  # North West
]
