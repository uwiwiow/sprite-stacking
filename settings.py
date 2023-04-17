import pygame as pg

vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1600, 900)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
TILE_SIZE = 250

PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015

BG_COLOR = 'olivedrab'
NUM_ANGLES = 24  # multiple of 360 -> 24, 30, 36, 40, 45, 60, 72, 90, 120, 180

# entity sprites settings
ENTITY_SPRITE_ATTRS = {
    'player': {
        'path': 'assets/entities/player/player.png',
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
}

# stacked sprites settings
STACKED_SPRITE_ATTRS = {
    'chr_knight': {
        'path': 'assets/stacked_sprites/chr_knight.png',
        'num_layers': 15,
        'scale': 6,
        'y_offset': -40,
    },
    'hearth': {
        'path': 'assets/stacked_sprites/hearth.png',
        'num_layers': 200,
        'scale': 1,
        'y_offset': 0,
    },
    'car': {
        'path': 'assets/stacked_sprites/car.png',
        'num_layers': 9,
        'scale': 10,
        'y_offset': -15,
    },
    'blue_tree': {
        'path': 'assets/stacked_sprites/blue_tree.png',
        'num_layers': 43,
        'scale': 8,
        'y_offset': -170,
    },
    'crate': {
        'path': 'assets/stacked_sprites/crate.png',
        'num_layers': 16,
        'scale': 10,
        'y_offset': -80,
    },
    'cup': {
        'path': 'assets/stacked_sprites/cup.png',
        'num_layers': 13,
        'scale': 1,
        'y_offset': 0,
    },
    'grass': {
        'path': 'assets/stacked_sprites/grass.png',
        'num_layers': 11,
        'scale': 7,
        'y_offset': -10,
        'outline': False,
    },
    'grass1': {
        'path': 'assets/stacked_sprites/grass1.png',
        'num_layers': 10,
        'scale': 7,
        'y_offset': -15,
        'outline': False,
    },
    'pancake': {
        'path': 'assets/stacked_sprites/pancake.png',
        'num_layers': 11,
        'scale': 1,
        'y_offset': 0,
    },
    'pink_tree': {
        'path': 'assets/stacked_sprites/pink_tree.png',
        'num_layers': 43,
        'scale': 1,
        'y_offset': 0,
    },
    'sphere': {
        'path': 'assets/stacked_sprites/sphere.png',
        'num_layers': 13,
        'scale': 1,
        'y_offset': 0,
    },
    'tank': {
        'path': 'assets/stacked_sprites/tank.png',
        'num_layers': 17,
        'scale': 8,
        'y_offset': -50,
    },
    'tree': {
        'path': 'assets/stacked_sprites/tree.png',
        'num_layers': 8,
        'scale': 15,
        'y_offset': 0,
    },
    'trunk': {
        'path': 'assets/stacked_sprites/trunk.png',
        'num_layers': 50,
        'scale': 1,
        'y_offset': 0,
    },
}
