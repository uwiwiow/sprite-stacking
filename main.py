import sys
from settings import *
from cache import Cache
from player import Player
from scene import Scene
from button import Button
from image import Image


class App:
    def __init__(self):
        self.run_app = True
        self.blur_surface = None
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
        self.win_event = pg.USEREVENT + 4
        # groups
        self.main_group = pg.sprite.LayeredUpdates()
        self.collision_group = pg.sprite.Group()
        self.collision_target = pg.sprite.Group()
        self.transparent_objects = []
        # game objects
        self.cache = Cache()
        if os.path.exists("ch.txt"):
            with open("ch.txt", 'r') as f:
                self.character = json.load(f)
        self.player = Player(self, energia=60, name=self.character[0], bulletname=self.character[1])
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
            elif e.type == self.win_event:
                # set blur
                screen_surface = pg.display.get_surface()
                blur_surface = pg.Surface((self.screen.get_width(), self.screen.get_height()))
                blur_surface.blit(screen_surface, (0, 0))
                blur_surface = pg.transform.smoothscale(blur_surface, (10, 10))
                blur_surface = pg.transform.smoothscale(blur_surface, (WIDTH, HEIGHT))
                blur_surface.set_alpha(128)
                self.blur_surface = blur_surface

                self.run_app = False
            elif e.type == pg.KEYDOWN:
                self.player.single_fire(event=e)
                self.player.alimentarse(event=e)

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def get_font(self, size):
        return pg.font.Font("assets/interface/font.ttf", size)

    def run(self):
        try:  # try load music
            pg.mixer.music.load("assets/interface/music.wav")
            pg.mixer.music.play(100, 0, 4000)
        except FileNotFoundError:
            print("No se encontro el archivo")
        while self.run_app:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()
        while True:
            mouse_pos = pg.mouse.get_pos()
            self.screen.blit(self.blur_surface, (0, 0))
            pg.mouse.set_visible(True)

            menu_text = self.get_font(100).render("YOU HAVE WON", True, "#d6c352")
            menu_rect = menu_text.get_rect(center=(WIDTH // 2, 100))
            self.screen.blit(menu_text, menu_rect)

            replay_button = Button(image=pg.image.load("assets/interface/Options Rect.png"),
                                   pos=(WIDTH // 3, (300 * HEIGHT) // 720),
                                   text_input="CONTINUE", font=self.get_font(75), base_color="#d7fcd4",
                                   hovering_color="White")

            quit_button = Button(image=pg.image.load("assets/interface/Quit Rect.png"),
                                 pos=(WIDTH // 3, (500 * HEIGHT) // 720),
                                 text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4",
                                 hovering_color="White")

            char = self.get_font(48).render("CHARACTER", True, "#4F76D6")
            char_rect = char.get_rect(center=((WIDTH // 4) * 3, (250 * HEIGHT) // 720))
            self.screen.blit(char, char_rect)

            char = Image(image=pg.image.load(self.character[2]),
                         pos=((WIDTH // 4) * 3, (450 * HEIGHT) // 720))

            self.timer = self.time

            timepass = self.get_font(36).render(str(self.timer), True, "#4F76D6")
            timepass_rect = timepass.get_rect(center=((WIDTH // 4) * 3, (650 * HEIGHT) // 720))
            self.screen.blit(timepass, timepass_rect)

            char.update(self.screen)

            for button in [replay_button, quit_button]:
                button.change_color(mouse_pos)
                button.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if replay_button.check_for_input(mouse_pos):
                        self.run_app = True
                        pg.mouse.set_visible(True)
                        self.run()
                    if quit_button.check_for_input(mouse_pos):
                        pg.quit()
                        sys.exit()

            pg.display.update()


if __name__ == '__main__':
    app = App()
    app.run()
