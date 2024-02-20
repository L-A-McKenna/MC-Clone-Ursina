from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ursina import Vec3

from voxel import Voxel

__all__ = (
    "generate_floor",
)

def generate_floor(position: Vec3):

    for x in range(11):
        for z in range(11):
            Voxel(
                position = (position.x + x, position.y, position.z + z)
            )