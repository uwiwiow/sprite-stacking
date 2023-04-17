from stacked_sprite import *
from random import uniform
from entity import Entity

P = 'player'
K = 'kitty'  # entity
A, B, C, D, E, F = 'crate', 'tank', 'blue_tree', 'car', 'grass', 'grass1'

MAP = [
    [0, 0, 0, 0, K, 0, 0, 0, 0],
    [0, C, C, C, F, C, C, 0, 0],
    [0, C, E, 0, 0, E, F, C, 0],
    [C, F, B, E, C, B, B, C, 0],
    [C, E, 0, 0, P, F, E, C, 0],
    [C, 0, F, A, 0, D, C, C, 0],
    [0, C, E, 0, 0, 0, C, C, 0],
    [0, C, C, 0, E, F, C, C, 0],
    [0, 0, 0, C, C, C, C, 0, 0]
]

MAP_SIZE = MAP_WIDTH, MAP_HEIGHT = vec2(len(MAP), len(MAP[0]))
MAP_CENTER = MAP_SIZE / 2

class Scene:
    def __init__(self, app):
        self.app = app
        self.load_scene()

    def load_scene(self):
        rand_rot = lambda: uniform(0, 360)
        rand_pos = lambda pos: pos + vec2(uniform(-0.25, 0.25))

        for j, row in enumerate(MAP):
            for i, name in enumerate(row):
                pos = vec2(i, j) + vec2(0.5)
                if name == 'player':
                    self.app.player.offset = pos * TILE_SIZE
                elif name == 'kitty':
                    Entity(self.app, name=name, pos=pos)
                elif name == 'blue_tree':
                    TrnsStackedSprites(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())
                elif name == 'crate':
                    TrnsStackedSprites(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())
                elif name:
                    StackedSprite(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())

    def get_closest_object_to_player(self):
        closest = sorted(self.app.transparent_objects, key=lambda e: e.dist_to_player)
        closest[0].alpha_trigger = True
        closest[1].alpha_trigger = True

    def update(self):
        self.get_closest_object_to_player()




















