from pgzrun import *
from sprite_groups import SpriteGroup
from random import randint
WIDTH = 750
HEIGHT = 750
targets = SpriteGroup()
crosshair = Actor("crosshair")
for i in range(25):
    target = Actor("target")
    target.pos = randint(0, WIDTH), randint(0, HEIGHT)
    targets.AddSprite(target)
def draw():
    screen.fill("#00FFFF")
    targets.draw()
    crosshair.draw()
def on_mouse_down():
    for i in targets.sprites:
        if i.colliderect(crosshair):
            targets.DeleteSprite(i)
def on_mouse_move(pos):
    crosshair.pos = pos
go()