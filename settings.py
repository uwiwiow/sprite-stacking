import pygame as pg
import os
import json

vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1600, 900)

if os.path.exists("res.txt"):
    with open("res.txt", 'r') as f:
        RES = WIDTH, HEIGHT = json.load(f)
        RES = WIDTH, HEIGHT = vec2(WIDTH, HEIGHT)

CENTER = H_WIDTH, H_HEIGHT = RES // 2
TILE_SIZE = 250

PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015

BG_COLOR = 'olivedrab'
NUM_ANGLES = 30  # multiple of 360 -> 24, 30, 36, 40, 45, 60, 72, 90, 120, 180

if os.path.exists("angles.txt"):
    with open("angles.txt", 'r') as f:
        NUM_ANGLES = json.load(f)

# entity sprites settings
ENTITY_SPRITE_ATTRS = {
    'player': {
        'path': 'assets/entities/player/player.png',
        'mask_path': 'assets/entities/player/mask.png',
        'num_layers': 7,
        'scale': 0.35,
        'y_offset': 0,
    },
    'mage': {
        'path': 'assets/entities/player/mage.png',
        'mask_path': 'assets/entities/player/mask.png',
        'num_layers': 7,
        'scale': 0.35,
        'y_offset': 0,
    },
    'kitty': {
        'path': 'assets/entities/cats/kitty.png',
        'num_layers': 8,
        'scale': 0.8,
        'y_offset': 0,
    },
    'explosion': {
        'num_layers': 7,
        'scale': 1.0,
        'path': 'assets/entities/explosion/explosion.png',
        'y_offset': 50,
    },
    'bullet': {
        'num_layers': 1,
        'scale': 0.4,
        'path': 'assets/entities/bullet/bullet.png',
        'y_offset': 50,
    },
    'ice_bullet': {
        'num_layers': 1,
        'scale': 0.25,
        'path': 'assets/entities/bullet/ice_bullet.png',
        'y_offset': 50,
    },
    'life': {
        'num_layers': 7,
        'scale': 10,
        'path': 'assets/entities/life/lifebar.png',
        'y_offset': 0,
    },
    'arrows': {
        'num_layers': 24,
        'scale': 5,
        'path': 'assets/entities/controlls/arrows.png',
        'y_offset': 0,
    },
    'wasd': {
        'num_layers': 21,
        'scale': 5,
        'path': 'assets/entities/controlls/wasd.png',
        'y_offset': 0,
    },
    'energy': {
        'num_layers': 7,
        'scale': 10,
        'path': 'assets/entities/energy/energy_bar.png',
        'y_offset': 0,
    },
}

# stacked sprites settings
STACKED_SPRITE_ATTRS = {
    'sphere': {
        'path': 'assets/stacked_sprites/sphere.png',
        'num_layers': 13,
        'scale': 10,
        'y_offset': 0,
        'mask_layer': 4,
    },
    'pancake': {
        'path': 'assets/stacked_sprites/pancake.png',
        'num_layers': 11,
        'scale': 7,
        'y_offset': 0,
        'mask_layer': 4,
    },
    'cup': {
        'path': 'assets/stacked_sprites/cup.png',
        'num_layers': 13,
        'scale': 8,
        'y_offset': 10,
    },
    'crate': {
        'path': 'assets/stacked_sprites/crate.png',
        'num_layers': 16,
        'scale': 5,
        'y_offset': 10,
    },
    'grass': {
        'path': 'assets/stacked_sprites/grass.png',
        'num_layers': 11,
        'scale': 7,
        'y_offset': 20,
        'outline': False,
    },
    'blue_tree': {
        'path': 'assets/stacked_sprites/blue_tree.png',
        'num_layers': 43,
        'scale': 8,
        'y_offset': -130,
        'transparency': True,
        'mask_layer': 3,
    },
    'car': {
        'path': 'assets/stacked_sprites/car.png',
        'num_layers': 9,
        'scale': 10,
        'y_offset': 10,
    },
    'tank': {
        'path': 'assets/stacked_sprites/tank.png',
        'num_layers': 17,
        'scale': 8,
        'y_offset': 0,
        'mask_layer': 4,
    },
}
