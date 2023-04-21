import os.path
import sys
from button import Button
from image import Image
from main import App
import pygame as pg
import json

pg.init()

if not os.path.exists("data"):
    # Si el directorio no existe, crearlo
    os.makedirs("data")

vec2 = pg.math.Vector2
RES = WIDTH, HEIGHT = vec2(1600, 900)

if os.path.exists("data/res.txt"):
    with open("data/res.txt", 'r') as f:
        RES = WIDTH, HEIGHT = json.load(f)

SCREEN = pg.display.set_mode(RES)
pg.display.set_caption("Wizardry Warriors")
pygame_icon = pg.image.load("assets/interface/icon.png")
pg.display.set_icon(pygame_icon)

BG = pg.image.load("assets/interface/Background.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/interface/font.ttf", size)


def choose_character():
    while True:

        SCREEN.blit(BG, (0, 0))
        chose_mouse_pos = pg.mouse.get_pos()

        options_text = get_font(int(WIDTH * 72) // 1920).render("CHOOSE A CHARACTER", True, "Black")
        options_rect = options_text.get_rect(center=(WIDTH // 2, 100))
        SCREEN.blit(options_text, options_rect)

        warrior = Image(image=pg.image.load("assets/entities/warrior/row-1-column-1.png"),
                        pos=(WIDTH // 4, HEIGHT // 2))
        wizard = Image(image=pg.image.load("assets/entities/wizard/row-1-column-1.png"),
                       pos=(WIDTH - WIDTH // 4, HEIGHT // 2))

        for button in [warrior, wizard]:
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if warrior.check_for_input(chose_mouse_pos):
                    character('player')
                    play()
                if wizard.check_for_input(chose_mouse_pos):
                    character('mage')
                    play()

        pg.display.update()


def character(character):

    if character == 'player':
        save = ["player", "bullet", "assets/entities/warrior/row-1-column-1.png"]

    if character == 'mage':
        save = ["mage", "ice_bullet", "assets/entities/wizard/row-1-column-1.png"]

    with open("data/ch.txt", 'w') as f:
        json.dump(save, f)


def play():
    app = App()
    app.run()


def options():
    real = False  # display para el texto si cambia resolucion
    while True:
        SCREEN.blit(BG, (0, 0))
        options_mouse_pos = pg.mouse.get_pos()

        options_text = get_font(int(WIDTH * 72) // 1920).render("SET RESOLUTION", True, "Black")
        options_rect = options_text.get_rect(center=(WIDTH//2, 100))
        SCREEN.blit(options_text, options_rect)

        options_text_af = get_font(int(WIDTH * 36) // 1920).render("RESET TO APPLY CHANGES", True, "red")
        options_rect_af = options_text.get_rect(center=(WIDTH // 2, 50))

        if real:
            SCREEN.blit(options_text_af, options_rect_af)

        options_back = Button(image=None, pos=(250, HEIGHT - 100),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="White")

        hd_button = Button(image=None, pos=(WIDTH // 3, (HEIGHT // 2) - 150),
                              text_input="1280 x 720", font=get_font(56), base_color="Black", hovering_color="White")

        wxga_button = Button(image=None, pos=(WIDTH // 3, (HEIGHT // 2) - 50),
                              text_input="1366 x 768", font=get_font(56), base_color="Black", hovering_color="White")

        hdp_button = Button(image=None, pos=(WIDTH // 3, (HEIGHT // 2) + 50),
                              text_input="1600 x 900", font=get_font(56), base_color="Black", hovering_color="White")

        fhd_button = Button(image=None, pos=(WIDTH // 3, (HEIGHT // 2) + 150),
                              text_input="1920 x 1080", font=get_font(56), base_color="Black", hovering_color="White")

        set30_button = Button(image=None, pos=((WIDTH // 3) * 2.2, (HEIGHT // 2) - 150),
                           text_input="30", font=get_font(56), base_color="Black", hovering_color="White")

        set90_button = Button(image=None, pos=((WIDTH // 3) * 2.2, (HEIGHT // 2) - 50),
                             text_input="90", font=get_font(56), base_color="Black", hovering_color="White")

        set180_button = Button(image=None, pos=((WIDTH // 3) * 2.2, (HEIGHT // 2) + 50),
                            text_input="180", font=get_font(56), base_color="Black", hovering_color="White")

        set360_button = Button(image=None, pos=((WIDTH // 3) * 2.2, (HEIGHT // 2) + 150),
                            text_input="360", font=get_font(56), base_color="Black", hovering_color="White")

        reset_button = Button(image=None, pos=((WIDTH // 4) * 3, HEIGHT - 100),
                               text_input="RESET CONFIGURATION", font=get_font(36), base_color="Black", hovering_color="yellow")

        delete_all_button = Button(image=None, pos=((WIDTH // 4) * 3, HEIGHT - 50),
                               text_input="DELETE ALL DATA", font=get_font(36), base_color="Black", hovering_color="red")

        for button in [options_back, hd_button, wxga_button, hdp_button, fhd_button,
                       set30_button, set90_button,set180_button, set360_button,
                       reset_button, delete_all_button]:
            button.change_color(options_mouse_pos)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if options_back.check_for_input(options_mouse_pos):
                    main_menu()
                if hd_button.check_for_input(options_mouse_pos):
                    change_res(RES, (1280, 720))
                    real = True  # display para el texto si cambia resolucion
                if wxga_button.check_for_input(options_mouse_pos):
                    change_res(RES, (1366, 768))
                    real = True
                if hdp_button.check_for_input(options_mouse_pos):
                    change_res(RES, (1600, 900))
                    real = True
                if fhd_button.check_for_input(options_mouse_pos):
                    change_res(RES, (1920, 1080))
                    real = True
                if set30_button.check_for_input(options_mouse_pos):
                    change_angles(30)
                    real = True
                if set90_button.check_for_input(options_mouse_pos):
                    change_angles(90)
                    real = True
                if set180_button.check_for_input(options_mouse_pos):
                    change_angles(180)
                    real = True
                if reset_button.check_for_input(options_mouse_pos):
                    files_to_delete = ["data/res.txt", "data/angles.txt", "data/ch.txt", "data/time.txt"]
                    for file in files_to_delete:
                        if os.path.exists(file):
                            os.remove(file)
                    real = True
                if delete_all_button.check_for_input(options_mouse_pos):
                    files_to_delete = ["data/res.txt", "data/angles.txt", "data/ch.txt", "data/time.txt",
                                       "data/cache30.pickle", "data/cache90.pickle",
                                       "data/cache180.pickle", "data/cache360.pickle"]
                    for file in files_to_delete:
                        if os.path.exists(file):
                            os.remove(file)
                    real = True

        pg.display.update()


def change_res(old_res: vec2, new_res: vec2):
    old_res = new_res

    with open("data/res.txt", 'w') as f:
        json.dump(old_res, f)

def change_angles(opc):

    with open("data/angles.txt", 'w') as f:
        json.dump(opc, f)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        menu_mouse_pos = pg.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#d6c352")

        menu_rect = menu_text.get_rect(center=(WIDTH // 2, 100))

        play_button = Button(image=pg.image.load("assets/interface/Play Rect.png"), pos=(WIDTH//2, (250 * HEIGHT)//720),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pg.image.load("assets/interface/Options Rect.png"), pos=(WIDTH//2, (400*HEIGHT)//720),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pg.image.load("assets/interface/Quit Rect.png"), pos=(WIDTH // 2, (550 * HEIGHT) // 720),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    choose_character()
                if options_button.check_for_input(menu_mouse_pos):
                    options()
                if quit_button.check_for_input(menu_mouse_pos):
                    pg.quit()
                    sys.exit()

        pg.display.update()


main_menu()
