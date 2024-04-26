"""
Conga_Line.py
Brianna Brost
2/10/23
Creates a conga line of circles that follow the mouse and each other.
"""
from random import random
import dudraw
from dudraw import Color
#creates sprite and makes it follow mouse and makes other circles follow the one before it
class Sprite:
    # gives initial (x,y) positions, initial target (x,y) radius and gives circles a random color
    def __init__(self, x_pos:float, y_pos:float, x_target:float, y_target:float, r=0.01):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_target = x_target
        self.y_target = y_target
        self.radius = r
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))
    def __str__(self):
        # returns position and target
        return f'{self.x_pos}, {self.y_pos}, {self.x_target}, {self.y_target}'
    def move(self):
        # moves sprites
        self.x_pos += (self.x_target - self.x_pos)*0.15
        self.y_pos += (self.y_target - self.y_pos)*0.15
    def set_target(self, x, y):
        # sets the target for sprite
        self.x_target = x
        self.y_target = y
    def draw(self):
        # draws
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_pos, self.y_pos, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_pos, self.y_pos, self.radius)
    def random_color(self):
        # gives rando color
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))
sprite_list = []
# creates list of sprites
for i in range(10):
    if i == 0:
        sprite_list.append(Sprite(random(), random(), dudraw.mouse_x(), dudraw.mouse_y()))
    else:
        sprite_list.append(Sprite(random(), random(), sprite_list[i-1].x_pos, sprite_list[i-1].y_pos))
key = ''
while key != 'q':
    #advances sprites to new position
    for sprite in sprite_list:
        sprite.move()
    #sets target of sprite equal to the mouse or cicle in front of it
    for i in range(len(sprite_list)):
        if i == 0:
            sprite_list[i].set_target(dudraw.mouse_x(), dudraw.mouse_y())
        else:
            sprite_list[i].set_target(sprite_list[i-1].x_pos, sprite_list[i-1].y_pos)
    #draw the frame, refreshes background and redraws circles
    dudraw.clear()
    for sprite in sprite_list:
        sprite.draw()
    #detect any key presses to quit program and add sprites
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
    if key == 'n':
        # adds sprite when press n
        sprite_list.append(Sprite(random(), random(), sprite_list[-1].x_pos, sprite_list[-1].y_pos))
        key = ''
    dudraw.show(50)
