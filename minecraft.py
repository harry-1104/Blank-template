from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white cube',
            color = color.color(random.randint(0, 225), random.uniform(.9, 1.0)),
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            
            if key == 'right mouse down':
                destroy(self)

for x in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
