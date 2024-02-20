from ursina import *

from fpc import CustomFpc
from utils import generate_floor

app = Ursina()

generate_floor(Vec3(0, 0, 0))

player = CustomFpc(position=(10, 1, 0))

# Set the background color to simulate a sky
window.color = color.rgb(135, 206, 235)  # RGB values for sky blue

# Set camera rotation to look at the center of the skybox.
camera.rotation = (0, 0, 0)

app.run()