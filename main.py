from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
"""
Define a pixel class

Set parent to scene and model to cube so that it becomes a button
"""


class Pixel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime

        )
    """
    Overrided method of class Button,
    Left mouse button click: Construct a cube
    Right mouse button click: Destroy a cube
    @:param key: Left mouse down or right mouse down
    """
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                pixel = Pixel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


for z in range(8):
    for x in range(8):
        pixel = Pixel(position=(x, 0, z))

player = FirstPersonController()
app.run()
