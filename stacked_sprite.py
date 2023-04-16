from settings import *
import math


class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos):
        self.app = app
        self.name = name
        self.pos = vec2(pos)
        self.group = app.main_group
        super().__init__(self.group)

        self.attrs = STACKED_SPRITE_ATTRS[name]
        self.cache = app.cache.stacked_sprite_cache
        self.viewing_angle = app.cache.viewing_angle
        self.rotated_sprites = self.cache[name]['rotated_sprites']
        self.angle = 0

    def get_angle(self):
        self.angle = -math.degrees(self.app.time) // self.viewing_angle
        self.angle = int(self.angle % NUM_ANGLES)

    def update(self):
        self.get_angle()
        self.get_image()

    def get_image(self):
        self.image = self.rotated_sprites[self.angle]
        self.rect = self.image.get_rect(center=self.pos + CENTER)
