from pyglet.window import key
from pyglet.window import Window
from pyglet import app
from pyglet.sprite import Sprite
from pyglet.text import Label
import pyglet
import os
import math
from random import randint
from pyglet.gl import glClearColor
from pyglet.graphics import draw


############################################################################################################################################################
#  Screen being used is 2736 x 1824
#
############################################################################################################################################################


win = Window(width=None, height=None, caption=None, resizable=False, style=None, fullscreen=True, visible=True, vsync=True, file_drops=False, display=None, screen=None, config=None, context=None, mode=None)


pyglet.resource.reindex()



def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2



def wrap(value, width):
    if width == 0:
        return 0
    if value > width:
        value -= width
    if value < 0:
        value += width
    return value



class Ground(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Ground, self).__init__(image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.mass = 5000000

        
    def dist_vec_to(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        sqr_distance = dx**2 + dy**2
        distance = math.sqrt(sqr_distance)

        angle = math.acos(float(dx) / distance)
        if dy < 0:
            angle = 2*math.pi - angle
        return (distance, angle)

    def force_on(self, target):
        G = 3
        distance, angle = self.dist_vec_to(target)
        return ((-G * self.mass) / (distance ** 2), angle)

    def update (self, dt):
            force, angle = self.force_on(box)
            force_x = force * math.cos(angle) * dt
            force_y = force * math.sin(angle) * dt
            box.dx += force_x
            box.dy += force_y

            print(force_x)
        
            
            if abs(force_x) >= 0 and abs(force_x) < 3:
                ground.image = (box_image)
            elif abs(force_x) >= 3  and abs(force_x) < 5:
                ground.image = (box_image_off)
            elif abs(force_x) >= 5 and abs(force_x) < 10:
                ground.image = (box_image_left)
            elif abs(force_x) >= 10 and abs(force_x) < 30:
                ground.image = (box_image_right)
            elif abs(force_x) >= 30:
                ground.image = (box_image_on)
               




class Line(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Line, self).__init__(image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.mass = 5000000
        
    def dist_vec_to(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        sqr_distance = dx**2 + dy**2
        distance = math.sqrt(sqr_distance)

        angle = math.acos(float(dx) / distance)
        if dy < 0:
            angle = 2*math.pi - angle
        return (distance, angle)

    def force_on(self, target):
        G = 1
        distance, angle = self.dist_vec_to(target)
        return ((-G * self.mass) / (distance ** 2), angle)

    def update (self, dt):
            force, angle = self.force_on(box)
            force_x = force * math.cos(angle) * dt
            force_y = force * math.sin(angle) * dt
            box.dx += force_x
            box.dy += force_y

            print(force_x)
                    
            if abs(force_x) >= 0 and abs(force_x) < 3:
                ground.image = (box_image)
            elif abs(force_x) >= 3  and abs(force_x) < 5:
                ground.image = (box_image_off)
            elif abs(force_x) >= 5 and abs(force_x) < 10:
                ground.image = (box_image_left)
            elif abs(force_x) >= 10 and abs(force_x) < 30:
                ground.image = (box_image_right)
            elif abs(force_x) >= 30:
                ground.image = (box_image_on)



                

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
            self.thrust = 200.0

        def update(self, dt):
            
            if self.jump:
                self.dy += self.thrust * dt
                self.image = box_image_off
            elif self.duck:
                self.dy -= self.thrust * dt
                self.image = box_image_off
            elif self.right:
                self.x += self.thrust * dt
                self.image = box_image_off
            elif self.left:
                self.x -= self.thrust * dt
                self.image = box_image_off
            else:
                self.image = box_image

            self.x += self.dx * dt
            self.y += self.dy * dt

            self.x = wrap(self.x, win.width)
            self.y = wrap(self.y, win.height)




            
center_x = int(win.width/2)
center_y = int(win.height/2)
width = int(win.width)
height = int(win.height)
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
line_image = pyglet.resource.image('line_orange.png')
center_anchor(line_image)

#label = Label("hello, world.", font_name='Times New Roman',font_size=96, x=center_x, y=center_y, anchor_x='center', anchor_y='center')

box = Box(box_image,x=center_x + 640, y=center_y, dx=0, dy=0)

ground = Ground(box_image, center_x, center_y, None)

line = Line(line_image, center_x, center_y+100, None)




def update(dt):
    box.update(dt)
    ground.update(dt)
    line.update(dt)
    


pyglet.clock.schedule_interval(update, 1/4.0)



@win.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        box.jump = True
    if symbol == key.RIGHT:
        box.right = True
    if symbol == key.LEFT:
        box.left = True
    if symbol == key.DOWN:
        box.duck = True


        
@win.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        box.jump = False
    if symbol == key.RIGHT:
        box.right = False
    if symbol == key.LEFT:
        box.left = False
    if symbol == key.DOWN:
        box.duck = False
        

        
glClearColor(.1, .045, .06, 0.0) 



@win.event
def on_draw():
    win.clear() # ... call the clear() method of the Window constructor instance named 'win'
    box.draw() # ... call the draw() method of the Ship constructor (subclass of Sprite, a submodule of sprite,) instance named 'ship'
    #label.draw() # ... call the draw() method of the label instance of the Label constructor, a class of submodule text of module pyglet.
    ground.draw()
    line.draw()


    
print(width)
print(height)



app.run()
