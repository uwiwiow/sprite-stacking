import sys
from settings import *
from cache import Cache
from player import Player
from scene import Scene


class App:
    def __init__(self):
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0.01
        # user events
        self.anim_trigger = False
        self.anim_event = pg.USEREVENT + 0
        pg.time.set_timer(self.anim_event, 100)
        self.life_trigger = False
        self.life_event = pg.USEREVENT + 1
        self.energy_trigger = False
        self.energy_event = pg.USEREVENT + 2
        self.alimentar_trigger = False
        self.alimentar_event = pg.USEREVENT + 3
        # groups
        self.main_group = pg.sprite.LayeredUpdates()
        self.collision_group = pg.sprite.Group()
        self.collision_target = pg.sprite.Group()
        self.transparent_objects = []
        # game objects
        self.cache = Cache()
        if os.path.exists("ch.txt"):
            with open("ch.txt", 'r') as f:
                character = json.load(f)
        self.player = Player(self, energia=60, name=character[0], bulletname=character[1])
        self.scene = Scene(self)

    def update(self):
        self.scene.update()
        self.main_group.update()
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
        self.delta_time = self.clock.tick()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.main_group.draw(self.screen)
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.life_trigger = False
        self.energy_trigger = False
        self.alimentar_trigger = False
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif e.type == self.anim_event:
                self.anim_trigger = True
            elif e.type == self.life_event:
                self.life_trigger = True
            elif e.type == self.energy_event:
                self.energy_trigger = True
            elif e.type == self.alimentar_event:
                self.alimentar_trigger = True
            elif e.type == pg.KEYDOWN:
                self.player.single_fire(event=e)
                self.player.alimentarse(event=e)

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        try:
            pg.mixer.music.load("assets/interface/music.wav")
            pg.mixer.music.play(100, 0, 2000)
        except FileNotFoundError:
            print("No se encontro el archivo")
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
