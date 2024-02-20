from ursina import *

__all__ = (
    "Voxel",
)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='white_cube', color=color.white):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = texture,
            color = color,
            origin_y = 0.5,
            collider = 'box'
        )

    def input(self, key):

        if self.hovered:
            if key == 'left mouse down':
                # prevent placing a block on top of another block
                voxel_position = self.position + mouse.normal

                if not any(voxel.position == voxel_position for voxel in scene.entities):
                    Voxel(position = voxel_position, texture = "./assets/grass.png")

            elif key == "right mouse down":
                destroy(self)