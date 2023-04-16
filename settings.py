import pygame as pg

vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1600, 900)
CENTER = H_WIDTH, H_HEIGHT = RES // 2

BG_COLOR = (20, 30, 46)

# stacked sprites settings
STACKED_SPRITE_ATTRS = {
    'chr_knight': {
        'path': 'assets/stacked_sprites/chr_knight.png',
        'num_layers': 15,
        'scale': 18,
    },
    'hearth': {
        'path': 'assets/stacked_sprites/hearth.png',
        'num_layers': 200,
        'scale': 1,
    },
    'car': {
        'path': 'assets/stacked_sprites/car.png',
        'num_layers': 14,
        'scale': 15,
    },
}
