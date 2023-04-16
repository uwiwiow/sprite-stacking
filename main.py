import sys
from settings import *
from stacked_sprite import StackedSprite


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0.01
        # groups
        self.main_group = pg.sprite.Group()
        # scene
        StackedSprite(self, name='chr_knight', pos=(-H_WIDTH // 2, 0))
        StackedSprite(self, name='car', pos=(H_WIDTH // 2, 0))

    def update(self):
        self.main_group.update()
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
        self.delta_time = self.clock.tick()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.main_group.draw(self.screen)
        pg.display.flip()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
