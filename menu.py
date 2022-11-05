import pygame, sys
from pygame.locals import *
from screeninfo import get_monitors

# The purpose of this file is to make a main menu available

class MainMenu:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()

        # path to background images
        self.background_path = 'graphics/background_main'

        # text font
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # screen size
        self.height = get_monitors()[0].height
        self.width = get_monitors()[0].width

        # title
        self.title = pygame.image.load('graphics/background_main/title.png').convert_alpha()

        # declaring the text
        self.play = self.font.render('Play', True, (20, 39, 56))
        self.settings = self.font.render('Settings', True, (20, 39, 56))
        self.resources = self.font.render('Resources', True, (20, 39, 56))
        self.quit = self.font.render('Quit', True, (20, 39, 56))

        # declaring collision state
        self.col_main = False
        self.col_settings = False
        self.col_resources = False
        self.col_quit = False

        # clicking on the buttons
        self.play_state = None
        self.settings_state = None
        self.resources_state = None
        self.quit_state = None

    def background(self, image=1):

        # main menu main animation
        main_path = 'graphics/background_main/castle/'
        file_name = "castle-" + str(image) + ".tiff"

        image = pygame.image.load(main_path + file_name).convert_alpha()
        image = pygame.transform.scale(image, (self.width, self.height))

        return image

    def buttons(self, mouse_motion, mouse_click):
        
        # mouse_pos rect
        mouse_rect = pygame.Rect(mouse_motion[0], mouse_motion[1], 16, 16)

        # making the buttons for play, setting, resources, quit
        self.main_gem = pygame.image.load('graphics/items/gems/serafil/long_serafil_gem.png').convert_alpha()
        self.main_gem = pygame.transform.scale(self.main_gem, (180, 110))

        self.hover_gem = pygame.image.load('graphics/items/gems/thradil/long_thrandil_gem.png').convert_alpha()
        self.hover_gem = pygame.transform.scale(self.hover_gem, (180, 110))

        self.quit_gem = pygame.image.load('graphics/items/gems/sardul/long_sardul_gem.png').convert_alpha()
        self.quit_gem = pygame.transform.scale(self.quit_gem, (180, 110))

        # creating Rectangles in order to detect collisions
        play_gem_rect = pygame.Rect(self.width / 2 - 89, self.height / 2 - 140, 180, 110)
        settings_gem_rect = pygame.Rect(self.width / 2 - 89, self.height / 2 - 20, 180, 110)
        resources_gem_rect = pygame.Rect(self.width / 2 - 89, self.height / 2 + 100, 180, 110)
        quit_gem_rect = pygame.Rect(self.width / 2 - 89, self.height / 2 + 220, 180, 110)

        # detecting colosion
        if pygame.Rect.colliderect(mouse_rect, settings_gem_rect) and mouse_click:
            self.col_settings = True
            self.settings_state = True
        elif pygame.Rect.colliderect(mouse_rect, settings_gem_rect):
            self.col_settings = True
        else:
            self.col_settings = False

        if pygame.Rect.colliderect(mouse_rect, resources_gem_rect) and mouse_click:
            self.col_resources = True
            self.resources_state = True
        elif pygame.Rect.colliderect(mouse_rect, resources_gem_rect):
            self.col_resources = True
        else:
            self.col_resources = False

        if pygame.Rect.colliderect(mouse_rect, play_gem_rect) and mouse_click:
            self.col_main = True
            self.play_state = True
        elif pygame.Rect.colliderect(mouse_rect, play_gem_rect):
            self.col_main = True
        else:
            self.col_main = False

        if pygame.Rect.colliderect(mouse_rect, quit_gem_rect) and mouse_click:
            self.col_quit = True
            self.quit_state = True
        elif pygame.Rect.colliderect(mouse_rect, quit_gem_rect):
            self.col_quit = True
        else:
            self.col_quit = False

        return [self.play_state, self.settings_state, self.resources_state, self.quit_state]

    def run(self, screen, image=1):

        # running the background animation
        self.clock.tick(15)
        screen.blit(self.background(image), (0, 0))

        # the buttons...
        if self.col_main:
            screen.blit(self.hover_gem, (self.width / 2 - 89, self.height / 2 - 140))
        else:
            screen.blit(self.main_gem, (self.width / 2 - 89, self.height / 2 - 140))

        if self.col_settings:
            screen.blit(self.hover_gem, (self.width / 2 - 89, self.height / 2 - 20))
        else:
            screen.blit(self.main_gem, (self.width / 2 - 89, self.height / 2 - 20))
        
        if self.col_resources:
            screen.blit(self.hover_gem, (self.width / 2 - 89, self.height / 2 + 100))
        else:
            screen.blit(self.main_gem, (self.width / 2 - 89, self.height / 2 + 100))
        
        if self.col_quit:
            screen.blit(self.quit_gem, (self.width / 2 - 89, self.height / 2 + 220))
        else:
            screen.blit(self.main_gem, (self.width / 2 - 89, self.height / 2 + 220))

        screen.blit(self.title, (70, 100))
        screen.blit(self.play, (self.width / 2 - 35, self.height / 2 - 100))
        screen.blit(self.settings, (self.width / 2 - 65, self.height / 2 + 20))
        screen.blit(self.resources, (self.width / 2 - 80, self.height / 2 + 140))
        screen.blit(self.quit, (self.width / 2 - 35, self.height / 2 + 260))

        return image

# Some variable testing

if __name__ == '__main__':

    """
    menu = MainMenu()
    print(menu.screen)
    """

    pass
