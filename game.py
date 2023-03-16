

from pyglet.window import key
from pyglet.window import Window # import Window constructor, a class from pyglet.window submodule
from pyglet import app
from pyglet.sprite import Sprite # import Sprite constructor, a class from pyglet.sprite submodule
from pyglet.text import Label # import Label constructor, a class from pyglet.text submodule
import pyglet
import os
import math
from random import randint
from pyglet.gl import glClearColor
from pyglet.graphics import draw


win = Window(width=None, height=None, caption=None, resizable=False, style=None, fullscreen=True, visible=True, vsync=True, file_drops=False, display=None, screen=None, config=None, context=None, mode=None) # call Window constructor to create a fullscreen window whose name is win

pyglet.resource.reindex()



def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

box_image_on = pyglet.resource.image('box_on.png')
center_anchor(box_image_on)
box_image_right = pyglet.resource.image('box_right.png')
center_anchor(box_image_right)
box_image_left = pyglet.resource.image('box_left.png')
center_anchor(box_image_left)
box_image = pyglet.resource.image('box.png')
center_anchor(box_image)
box_image_off = pyglet.resource.image('box_off.png')
center_anchor(box_image_off)
center_x = int(win.width/2)
center_y = int(win.height/2)
width = int(win.width)
height = int(win.height)



def wrap(value, width):
    if width == 0:
        return 0
    if value > width:
        value -= width
    if value < 0:
        value += width
    return value


class Box(Sprite):
        def __init__(self, image, x=0, y=0,
                     dx=0, dy=0, rotv=0, batch=None):
            super(Box, self).__init__(
                image, x, y, batch=batch)
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            self.right = False
            self.jump = False
            self.left = False
            self.duck = False

        def update(self, dt):
            
            if self.jump:
                self.image = box_image_on
                self.y = 40 + self.y
                self.dy = 1 + self.dy
            elif self.duck:
                self.image = box_image_off
                self.dy = self.dy - 11
                self.y = self.y - 40
            elif self.right:
                self.image = box_image_right
                self.x = 240 + self.x
                self.dx = 1 + self.dx
            elif self.left:
                self.image = box_image_left
                self.x = self.x - 240
                self.dx = self.dx - 1
            else:
                self.image = box_image

            self.x += self.dx * dt
            self.x = wrap(self.x, win.width)
            self.y = self.y + (self.dy * dt - 9.8 * dt)
            self.y = wrap(self.y, win.height)


def update(dt): # ... create a scheduled function called 'update' which accepts paramter 'dt' (delta time/change in time)
    box.update(dt)
# ... call the update function twice per second.
pyglet.clock.schedule_interval(update, 1/4.0)

# ... create a 'box' instance of a Sprite object using the Box constructor
box = Box(box_image,
            x=center_x + 640, y=center_y,
            dx=0, dy=0)

@win.event #Event handler which sets variables when keyboard is pressed
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        box.jump = True
    if symbol == key.RIGHT:
        box.right = True
    if symbol == key.LEFT:
        box.left = True
    if symbol == key.DOWN:
        box.duck = True
  
@win.event #Event handler which sets variables when keyboard is released
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        box.jump = False
    if symbol == key.RIGHT:
        box.right = False
    if symbol == key.LEFT:
        box.left = False
    if symbol == key.DOWN:
        box.duck = False
        
label = Label("hello, world.", font_name='Times New Roman',
              font_size=96,
              x=center_x, y=center_y,
              anchor_x='center', anchor_y='center')

glClearColor(.1, .045, .06, 0.0) 
@win.event #Event handler which clears teh window, draws ship & planet when on_draw occurs 
def on_draw():
    # ... drawing code ....
    #win.clear() # ... call the clear() method of the Window constructor instance named 'win'
    box.draw() # ... call the draw() method of the Ship constructor (subclass of Sprite, a submodule of sprite,) instance named 'ship'
    label.draw() # ... call the draw() method of the label instance of the Label constructor, a class of submodule text of module pyglet.
    
app.run()
# ... call the run() method of the app constructor, a module of pyglet.
