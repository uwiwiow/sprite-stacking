from settings import *
import os
import pickle


class Cache:
    def __init__(self):
        if os.path.exists("cache.pickle"):

            with open("cache.pickle", "rb") as f:
                self.stacked_sprite_cache = pickle.load(f)
                for key, value in self.stacked_sprite_cache.items():
                    for angle, array_surface in value['rotated_sprites'].items():
                        value['rotated_sprites'][angle] = pg.surfarray.make_surface(array_surface)
                        image = value['rotated_sprites'][angle]
                        image.set_colorkey((77, 55, 29))

            self.viewing_angle = 360 // NUM_ANGLES
            self.entity_sprite_cache = {}
            self.get_entity_sprite_cache()

        else:
            self.stacked_sprite_cache = {}
            self.stacked_sprite_cache_save = {}
            self.entity_sprite_cache = {}
            self.viewing_angle = 360 // NUM_ANGLES
            self.outline_thickness = 5
            self.get_stacked_sprite_cache()
            self.get_entity_sprite_cache()
            with open("cache.pickle", "wb") as f:
                pickle.dump(self.stacked_sprite_cache_save, f)

    def get_entity_sprite_cache(self):
        for sprite_name in ENTITY_SPRITE_ATTRS:
            self.entity_sprite_cache[sprite_name] = {
                'images': None,
            }
            attrs = ENTITY_SPRITE_ATTRS[sprite_name]
            images = self.get_layer_array(attrs)
            self.entity_sprite_cache[sprite_name]['images'] = images

    def get_stacked_sprite_cache(self):
        for obj_name in STACKED_SPRITE_ATTRS:
            self.stacked_sprite_cache[obj_name] = {
                'rotated_sprites': {},
            }
            self.stacked_sprite_cache_save[obj_name] = {
                'rotated_sprites': {},
            }
            attrs = STACKED_SPRITE_ATTRS[obj_name]
            layer_array = self.get_layer_array(attrs)
            self.run_prerender(obj_name, layer_array, attrs)

    def run_prerender(self, obj_name, layer_array, attrs):
        outline = attrs.get('outline', True)

        for angle in range(NUM_ANGLES):
            surf = pg.Surface(layer_array[0].get_size())
            surf = pg.transform.rotate(surf, angle * self.viewing_angle)
            sprite_surf = pg.Surface([surf.get_width(), surf.get_height()
                                      + attrs['num_layers'] * attrs['scale']])
            sprite_surf.fill((77, 55, 29))
            sprite_surf.set_colorkey((77, 55, 29))

            for ind, layer in enumerate(layer_array):
                layer = pg.transform.rotate(layer, angle * self.viewing_angle)
                sprite_surf.blit(layer, (0, ind * attrs['scale']))

            # get outline
            if outline:
                outline_coords = pg.mask.from_surface(sprite_surf).outline()
                pg.draw.polygon(sprite_surf, 'black', outline_coords, self.outline_thickness)

            image = pg.transform.flip(sprite_surf, flip_x=True, flip_y=True)
            array_surface = pg.surfarray.array3d(image)
            self.stacked_sprite_cache[obj_name]['rotated_sprites'][angle] = image
            self.stacked_sprite_cache_save[obj_name]['rotated_sprites'][angle] = array_surface

    def get_layer_array(self, attrs):
        # load sprite sheet
        sprite_sheet = pg.image.load(attrs['path']).convert_alpha()
        # scaling
        sprite_sheet = pg.transform.scale(sprite_sheet,
                                          vec2(sprite_sheet.get_size()) * attrs['scale'])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        sprite_height = sheet_height // attrs['num_layers']
        # new height to prevent error
        sheet_height = sprite_height * attrs['num_layers']
        # get sprites
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface((0, y, sheet_width, sprite_height))
            layer_array.append(sprite)
        return layer_array[::-1]
