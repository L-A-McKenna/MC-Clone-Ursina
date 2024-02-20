from ursina import held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

__all__ = (
    "CustomFpc",
)

class CustomFpc(FirstPersonController):

    def input(self, key):
        if held_keys["left shift"]:
            self.speed = 10
        else:
            self.speed = 5

        return super().input(key)