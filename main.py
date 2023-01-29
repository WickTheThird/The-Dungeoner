import pygame, sys

# import settings and debug
from resource_path import debug
from settings import *
from player.player import *
from levels.level import *

# import main menu
from menu import MainMenu

#import game related stuff

class Game:
    def __init__(self):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.mouse_motion  = (0, 0)
        self.mouse_click = False

        # key press events
        self.keys = []

        #main menu
        self.menu = MainMenu()
        self.image = 1

        # player
        self.player = Player()
        self.player_img = 0
        
        # the level
        self.the_level = LevelBase()

        # colors
        self.dark_green = (12, 14, 0)
        self.light_green = (200, 207, 165)

        # declaring col defaults
        self.lvl = None
        self.settings = None
        self.resources = None
        self.quit = None

        # the player
        self.player = Player()

    def run(self):
        #name of game
        pygame.display.set_caption('The Doungeoner')
        icon_image = pygame.image.load('graphics/icons/icon.webp')
        pygame.display.set_icon(icon_image)

        #main loop
        while True:
            for event in pygame.event.get():

                # key events
                self.keys = pygame.key.get_pressed()

                if event.type == pygame.MOUSEMOTION:
                    self.mouse_motion = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click = True
                else:
                    self.mouse_click = False

                state = self.menu.buttons(self.mouse_motion, self.mouse_click)
                self.lvl, self.settings, self.resources, self.quit = state[0], state[1], state[2], state[3]

                if event.type == pygame.QUIT or self.quit == True or self.keys[K_l]:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.light_green)

            # main menu
            if self.lvl is not True:
                if self.image > 50:
                    self.image = 1

                self.image = self.menu.run(self.screen, self.image)

            # player level
            if self.lvl is True:
                if self.player_img > 3:
                    self.player_img = 0

                self.player_img = self.the_level.run(self.screen, self.keys, self.player_img)

            # end of events
            self.image += 1
            self.player_img += 1
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
