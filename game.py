import os
import math
import pyglet
from pyglet.window import key, Window
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.gl import glClearColor
from pyglet.graphics import draw
from pyglet import app
from random import randint






class Source(pyglet.sprite.Sprite):

    def __init__(self, image, x=0, y=0, batch=None):

        super(Source, self).__init__(image, x, y, batch=batch)
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
            
        if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):

            box.dy = 0
            box.dx = (force_x + box.dx) * 0.97

            
        else:

            box.dy += force_y
            box.dx = force_x + box.dx


        if abs(force_x) >= 0 and abs(force_x) < 1:

            source.image = (box_image)

            
        elif abs(force_x) >= 1  and abs(force_x) < 2:

            source.image = (box_image_off)


        elif abs(force_x) >= 2 and abs(force_x) < 3:

            source.image = (box_image_left)


        elif abs(force_x) >= 3 and abs(force_x) < 4:

            source.image = (box_image_right)


        elif abs(force_x) >= 4:

            source.image = (box_image_on)






class Line(pyglet.sprite.Sprite):
    
    def __init__(self, image, x=0, y=0, batch=None):

        super(Line, self).__init__(image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.mass = 500000


        
    def dist_vec_to(self, target):

        dx = abs(target.x - self.x)
        dy = abs(target.y - self.y)


        
    def force_on(self, target):

        status = self.dist_vec_to(target)
        return (status)


    
    def update (self, dt):

        source = self.force_on(box)
        print(source)           


        
                

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
        self.superjump=False
        self.thrust = 430.0




    def update(self, dt):

            if self.jump:
                
                if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):
                    
                    self.dy = 0

                    
                else:

                    self.dy += self.thrust * dt

                    
                self.image = player_image_up

                    
            elif self.superjump:
                
                if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):
                    
                    self.y += 300
                    self.dy = 0

                    
                self.image = player_image_up

                    
            elif self.duck:
                
                if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):

                    self.dy = 0

                    
                else:

                    self.dy -= self.thrust * dt

                    
                self.image = player_image_down
                    
                
            elif self.right:

                if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):

                    self.dx += (self.thrust * dt * 0.97)

                    
                else:

                    self.dx += self.thrust * dt

                    
                self.image = player_image_right

                
            elif self.left:

                if (lower_bound <= box.y <= upper_bound) and (left_bound <= box.x <= right_bound):

                    self.dx -= (self.thrust * dt * 0.97)

                    
                else:

                    self.dx -= self.thrust * dt

                    
                self.image = player_image_left


            else:

                self.image = player_image_on

                
            self.x += self.dx * dt
            self.y += self.dy * dt

            self.x = wrap(self.x, win.width)
            self.y = wrap(self.y, win.height)






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




def update(dt):

    box.update(dt)
    source.update(dt)
    line.update(dt)




pyglet.resource.reindex()
glClearColor(.1, .045, .06, 0.0) 
pyglet.clock.schedule_interval(update, 1/120.0)
    
win = Window(width=None, height=None, caption=None, resizable=False, style=None, fullscreen=True, visible=True, vsync=True, file_drops=False, display=None, screen=None, config=None, context=None, mode=None)
          
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
player_image_on = pyglet.resource.image('player_on.png')
center_anchor(player_image_on)
player_image_right = pyglet.resource.image('player_right.png')
center_anchor(player_image_right)
player_image_left = pyglet.resource.image('player_left.png')
center_anchor(player_image_left)
player_image_up = pyglet.resource.image('player_up.png')
center_anchor(player_image_up)
player_image_down = pyglet.resource.image('player_down.png')
center_anchor(player_image_down)
line_image = pyglet.resource.image('face_1.png')
center_anchor(line_image)
left_bound = center_x - 500
right_bound = center_x + 500
lower_bound = center_y + 102.5 + (65 / 2) - 10
upper_bound = center_y + 102.5 + (65 / 2) + 10

box = Box(box_image,x=center_x + 640, y=center_y, dx=0, dy=0)

source = Source(box_image, center_x, center_y + 45, None)

line = Line(line_image, center_x, center_y+100, None)






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


    if symbol == key.A:

        box.superjump = True






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


    if symbol == key.A:

        box.superjump = False






@win.event

def on_draw():

    win.clear() # ... call the clear() method of the Window constructor instance named 'win'
    box.draw() # ... call the draw() method of the Ship constructor (subclass of Sprite, a submodule of sprite,) instance named 'ship'
    #label.draw() # ... call the draw() method of the label instance of the Label constructor, a class of submodule text of module pyglet.
    source.draw()
    line.draw()






app.run()
