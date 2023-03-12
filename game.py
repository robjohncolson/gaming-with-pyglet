



from pyglet.window import key
import pyglet
import os




window = pyglet.window.Window(fullscreen=True)
pyglet.resource.reindex()

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

planet_image = pyglet.resource.image('mars.png')
center_anchor(planet_image)

class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Planet, self).__init__(
            image, x, y, batch=batch)
        self.x = x
        self.y = y


center_x = int(window.width/2)
center_y = int(window.height/2)
planet = Planet(planet_image, center_x, center_y, None)

ship_image = pyglet.resource.image('ship.png')
center_anchor(ship_image)
class Ship(pyglet.sprite.Sprite):
        def __init__(self, image, x=0, y=0,
                     dx=0, dy=0, rotv=0, batch=None):
            super(Ship, self).__init__(
                image, x, y, batch=batch)
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            self.rotation = rotv
            self.thrust = 200.0
            self.rot_spd = 100.
ship = Ship(ship_image,
            x=center_x + 300, y=center_y,
            dx=0, dy=150, rotv=-90)
@window.event
def on_draw():
    window.clear()
    planet.draw()
    ship.draw()
    
pyglet.app.run()






