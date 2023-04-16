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
        self.layer_array = self.get_layer_array()
        self.angle = 0

    def get_angle(self):
        self.angle = -math.degrees(self.app.time)

    def update(self):
        self.get_angle()
        self.get_image()

    def get_image(self):
        surf = pg.Surface(self.layer_array[0].get_size())
        surf = pg.transform.rotate(surf, self.angle)
        sprite_surf = pg.Surface([surf.get_width(), surf.get_height()
                                  + self.attrs['num_layers'] * self.attrs['scale']], pg.SRCALPHA)

        for ind, layer in enumerate(self.layer_array):
            layer = pg.transform.rotate(layer, self.angle)
            sprite_surf.blit(layer, (0, ind * self.attrs['scale']))

        self.image = pg.transform.flip(sprite_surf, flip_x=True, flip_y=True)
        self.rect = self.image.get_rect(center=self.pos + CENTER)

    def get_layer_array(self):
        # load sprite sheet
        sprite_sheet = pg.image.load(self.attrs['path']).convert_alpha()
        # scaling
        sprite_sheet = pg.transform.scale(sprite_sheet,
                                          vec2(sprite_sheet.get_size()) * self.attrs['scale'])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        sprite_height = sheet_height // self.attrs['num_layers']
        # new height to prevent error
        sheet_height = sprite_height * self.attrs['num_layers']
        # get sprites
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface((0, y, sheet_width, sprite_height))
            layer_array.append(sprite)
        return layer_array[::-1]
