



from pyglet.window import key
from pyglet.window import Window # import Window constructor, a class from pyglet.window submodule
from pyglet import app
from pyglet.sprite import Sprite # import Sprite constructor, a class from pyglet.sprite submodule
from pyglet.text import Label # import Label constructor, a class from pyglet.text submodule
import pyglet
import os
import math



#pages 288 - 319 of Hello Python!





def wrap(value, width):
    if width == 0:
        return 0
    if value > width:
        value -= width
    if value < 0:
        value += width
    return value

def to_radians(degrees):
    return math.pi * degrees / 180.0



win = Window(width=None, height=None, caption=None, resizable=False, style=None, fullscreen=True, visible=True, vsync=True, file_drops=False, display=None, screen=None, config=None, context=None, mode=None) # call Window constructor to create a fullscreen window whose name is win

label = Label('Hello, world',
              font_name='Times New Roman',
              font_size=36,
              x=win.width//2, y=win.height//2,
              anchor_x='center', anchor_y='center')

pyglet.resource.reindex()

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

planet_image = pyglet.resource.image('mars.png')
center_anchor(planet_image)
ship_image_on = pyglet.resource.image('ship_on.png')
center_anchor(ship_image_on)
ship_image = pyglet.resource.image('ship.png')
center_anchor(ship_image)


"""
On classes: Planet is a subclass of pyglet.sprite.Sprite, which is a class of submodule pyglet.sprite.

"""

class Planet(Sprite):
    # ... create Planet constructor, a subclass of Sprite, a submodule of pyglet.sprite
    def __init__(self, image, x=0, y=0, batch=None):
        # ... define the constructor method '__init__' which is reserved method that python whose statements are used to create the data members of class 'Planet'.
        # ... sublass 'Planet' inherits the __init__ method of base class 'Sprite'.
        # ... so, objects of baseclass 'Sprite' such as 'planet' automatically
        # ... calls __init__ method of 'Sprite' at time of creation since
        # ... it is called by sub class 'Planet' __init__ constructor.
        # ... __init__ is also called "doubled underscores init" or "dunder init"
        # ... __init__ is invoked and used internally in Python, without being
        # ... required to be called explicitly by the object
        # ... "while giving the definition for an __init__(self) method, a default
        # ... parameter, named 'self' is always passed in its argument.
        # ... this self represents the object of the class itself.
        # ... like in any other method of a class, in case of __init__ also 'self'
        # ... is used as a dummy object variable for assigning values to
        # ... data members of an object
        # ... self is required as it refers to the instance of the class
        super(Planet, self).__init__(
            image, x, y, batch=batch)
        # ... the super() method        
        self.x = x
        self.y = y
        
""" example
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def show(self):
        print(self.name, " teaches", self.subject)
T = Teacher('Bobby Colson', "pyglet game")  #init is invoked here
T.show()
"""
"""
On __init__:
init method is inherited from OOP languages like C++.  It creates an object of the planet subclass of the pyglet.sprite.Sprite class.
super 

"""

"""
On super () method (from realpython.com's 'supercharge your classes with python super()'):
inheritance...

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width - width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

"""
center_x = int(win.width/2)
center_y = int(win.height/2)
planet = Planet(planet_image, center_x, center_y, None) # call Planet constructor to create a sprite whose name is planet


class Ship(Sprite):
    # ... create Ship constructor, a subclass of pyglet.sprite.Sprite
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
            self.rot_spd = 100.0
            self.rot_left = False
            self.rot_right = False
            self.engines = False

        def update(self, dt):
            self.image = ship_image
            if self.rot_left:
                self.rotation -= self.rot_spd * dt
            if self.rot_right:
                self.rotation += self.rot_spd * dt
            self.rotation = wrap(self.rotation, 360.) #wrap function

            if self.engines:
                self.image = ship_image_on
                rotation_x = math.cos(
                    to_radians(self.rotation))
                rotation_y = math.sin(
                    to_radians(-self.rotation))
                self.dx += self.thrust * rotation_x * dt
                self.dy += self.thrust * rotation_y * dt

            self.x += self.dx * dt
            self.y += self.dy * dt

            self.x = wrap(self.x, win.width)
            self.y = wrap(self.y, win.height)

def update(dt): # ... create a scheduled function called 'update' which accepts paramter 'dt' (delta time/change in time)
    ship.update(dt)
    
# ... call the update function twice a second.
pyglet.clock.schedule_interval(update, 1/2.0)

# ... create a ship instance of a Sprite object using the Ship constructor
ship = Ship(ship_image,
            x=center_x + 300, y=center_y,
            dx=0, dy=150, rotv=-90)

@win.event #Event handler which sets variables when keyboard is pressed
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        ship.rot_left = True
    if symbol == key.RIGHT:
        ship.rot_right = True
    if symbol == key.UP:
        ship.engines = True
        ship.jump = True

@win.event #Event handler which sets variables when keyboard is released
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        ship.rot_left = False
    if symbol == key.RIGHT:
        ship.rot_right = False
    if symbol == key.UP:
        ship.engines = False
        ship.jump = False

@win.event #Event handler which clears teh window, draws ship & planet when on_draw occurs 
def on_draw():
    # ... drawing code ....
    win.clear() # ... call the clear() method of the Window constructor instance named 'win'
    planet.draw() # ... call the draw() method of the Planet constrcutor (subclass of sprite) instance named 'planet'
    ship.draw() # ... call the draw() method of the Ship constructor (subclass of Sprite, a submodule of sprite,) instance named 'ship'
    label.draw() # ... call the draw() method of the label instance of the Label constructor, a class of submodule text of module pyglet.
    
app.run()
# ... call the run() method of the app constructor, a module of pyglet.
