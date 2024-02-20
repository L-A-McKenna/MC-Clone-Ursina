from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', texture='ground_texture.png', scale=(100, 1, 100), color=color.green.tint(-0.2), collider='box')
player = FirstPersonController(position=(10, 1, 0))

# Set the background color to simulate a sky
window.color = color.rgb(135, 206, 235)  # RGB values for sky blue

# Block textures for selection
block_textures = ['white_cube', 'brick', 'grass', 'stone']

# Function to spawn a block on top of the ground
def spawn_block():
    block = Entity(model='cube', texture='block_texture.png', scale=(1, 1, 1), position=(0, 2, 0), collider='box')  # Adjusted position
    return block


# Current block index
current_block_index = 0

# HUD text for block selection
hud_text = Text(text=f'Current Block: {block_textures[current_block_index]}', position=(-0.8, 0.4), scale=0.05, origin=(0, 0), color=color.white)

# Hand entity to display the current block
hand = Entity(parent=camera.ui, model='cube', texture=block_textures[current_block_index], scale=(0.2, 0.2, 0.2), position=(0.8, -0.4))

def input(key):
    global current_block_index

    if key == 'left mouse down':
        block_texture = block_textures[current_block_index]
        block = Voxel(position=player.position + player.forward, texture=block_texture)

    if key == 'right mouse down':
        voxel_position = player.position + player.forward
        destroy_voxel(voxel_position)

    # Change block selection with number keys (1-4)
    if key.isdigit() and 1 <= int(key) <= len(block_textures):
        current_block_index = int(key) - 1
        update_hud_text()
        update_hand_texture()

def update_hud_text():
    hud_text.text = f'Current Block: {block_textures[current_block_index]}'

def update_hand_texture():
    hand.texture = block_textures[current_block_index]

def destroy_voxel(position):
    for voxel in scene.entities:
        if voxel.position == position:
            destroy(voxel)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='white_cube', color=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,
            color=color,
            origin_y=0.5,
            collider='box'
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # prevent placing a block on top of another block
                voxel_position = self.position + mouse.normal
                if not any(voxel.position == voxel_position for voxel in scene.entities):
                    block_texture = block_textures[current_block_index]
                    Voxel(position=voxel_position, texture=block_texture)

# Handle mouse scroll to change block selection
def update():
    global current_block_index

    scroll = held_keys['scroll']
    if scroll:
        current_block_index += int(scroll)
        current_block_index = clamp(current_block_index, 0, len(block_textures) - 1)
        update_hud_text()
        update_hand_texture()

# Create a skybox entity
skybox = Entity(model='cube', texture='skybox.jpeg', scale=(500, 500, 500))

# Set camera rotation to look at the center of the skybox
camera.rotation = (0, 0, 0)

def update():
    # Rotate the skybox to create an animation effect
    skybox.rotation_y += 0.5 * time.dt

# Create a house entity
house = Entity(model='cube', texture='house.png', scale=(2, 2, 2), position=(20, 1, 20), collider='box')

# Create a roof for the house
roof = Entity(model='pyramid', texture='roof.png', scale=(2.2, 1, 2.2), position=(20, 3, 20), collider='box')

# Create a NPC Entity
npc = Entity(model='cube', texture='cow.jpeg', scale=(1, 2, 1), collider='box')

def update():
    # Move the NPC randomly
    npc.x += random.uniform(-0.1, 0.1)  # Adjust the range based on your preference
    npc.z += random.uniform(-0.1, 0.1)



app.run()

def update():
    # Rotate the house to create an animation effect
    house.rotation_y += 1 * time.dt

    # Rotate the skybox to create a wraparound effect
    skybox.rotation_y += 0.1 * time.dt

app.run()