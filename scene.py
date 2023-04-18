from stacked_sprite import *
from random import uniform
from entity import Entity

P = 'player'
L = 'life'
A = 'arrows'
W = 'wasd'
K = 'kitty'  # entity
I = 'energy'
B, C, D, E, F, G, H = 'tank', 'blue_tree', 'car', 'grass', 'crate', 'cup', 'pancake'
S = 'sphere'  # transform object

MAP = [
    [C, E, C, E, B, C, E, C, C, E, C, E, C, E],
    [E, C, C, C, 0, C, C, 0, E, 0, C, C, C, C],
    [C, C, 0, 0, I, L, E, C, 0, C, 0, H, 0, C],
    [C, 0, 0, E, P, K, 0, C, C, 0, 0, 0, 0, C],
    [C, E, 0, A, C, E, 0, E, 0, 0, F, E, 0, C],
    [C, 0, W, 0, E, D, E, S, 0, F, 0, 0, C, C],
    [C, C, E, 0, 0, 0, E, 0, E, 0, 0, B, C, E],
    [C, C, C, 0, E, 0, C, C, 0, G, E, C, 0, C],
    [E, C, C, C, C, C, C, C, C, C, C, C, E, C],
]

MAP_SIZE = MAP_WIDTH, MAP_HEIGHT = vec2(len(MAP), len(MAP[0]))
MAP_CENTER = MAP_SIZE / 2

class Scene:
    def __init__(self, app):
        self.app = app
        self.transform_objects = []
        self.move_life = 0
        self.move_energy = 0
        self.life_pos = 0
        self.player_pos = 0
        self.load_scene()

    def load_scene(self):
        rand_rot = lambda: uniform(0, 360)
        rand_pos = lambda pos: pos + vec2(uniform(-0.25, 0.25))

        for j, row in enumerate(MAP):
            for i, name in enumerate(row):
                pos = vec2(i, j) + vec2(0.5)
                if name == 'player':
                    self.app.player.offset = pos * TILE_SIZE
                    self.player_pos = self.app.player.offset
                elif name == 'kitty':
                    Entity(self.app, name=name, pos=pos, collision=True)
                    self.life_pos = vec2(pos) * TILE_SIZE
                elif name == 'life':
                    obj = Entity(self.app, name=name, pos=pos, collision=False)
                    self.move_life = obj
                elif name == 'energy':
                    obj = Entity(self.app, name=name, pos=pos, collision=False)
                    self.move_energy = obj
                elif name == 'wasd':
                    Entity(self.app, name=name, pos=pos, collision=False)
                elif name == 'arrows':
                    Entity(self.app, name=name, pos=pos, collision=False)
                elif name == 'blue_tree':
                    TrnspStackedSprite(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())
                elif name == 'grass':
                    StackedSprite(self.app, name=name, pos=rand_pos(pos), rot=rand_rot(),
                                  collision=False)
                elif name == 'sphere':
                    obj = StackedSprite(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())
                    self.transform_objects.append(obj)
                elif name:
                    StackedSprite(self.app, name=name, pos=rand_pos(pos), rot=rand_rot())

    def get_closest_object_to_player(self):
        closest = sorted(self.app.transparent_objects, key=lambda e: e.dist_to_player)
        closest[0].alpha_trigger = True
        closest[1].alpha_trigger = True

    def transform(self):
        for obj in self.transform_objects:
            obj.rot = 30 * self.app.time

    def update(self):
        self.get_closest_object_to_player()
        self.transform()
        self.move_ui()

    def move_ui(self):
        self.move_life.pos = self.life_pos
        self.move_energy.pos = self.player_pos
















