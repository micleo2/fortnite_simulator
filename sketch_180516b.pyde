from bus import Bus
from player import Player

WIDTH = 600
HEIGHT = 800
COLS = 100
ROWS = 100
cell_width = WIDTH / COLS
cell_height = HEIGHT / ROWS
z_off = 0

def setup():
    global WIDTH
    global HEIGHT
    global islandBus
    global player
    global target
    islandBus = Bus(WIDTH, HEIGHT)
    target = PVector(500, 300, 0)
    player = Player(target, islandBus)
    size(WIDTH, HEIGHT)

def draw():
    background(255, 255, 255)
    global z_off
    global islandBus
    islandBus.draw()
    player.draw()
    player.update()
    fill(0, 255, 0)
    noStroke()
    ellipse(target.x, target.y, 15, 15)
    
