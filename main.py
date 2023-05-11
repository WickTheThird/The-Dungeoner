import pygame
import sys
from resource_path import debug
from settings import *
from player.player import Player
from map_gen.level import LevelBase
from map_gen.map_level import Map
from menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.map = Map(width=100, height=100, scale=2, octaves=5)
        self.scale = 16
        self.mapX = 0
        self.mapY = 0
        self.level = LevelBase()

    def move(self, dx, dy):
        self.mapX += dx
        self.mapY -= dy

    def change_scale(self, delta):
        self.scale += delta

    def run(self):
        pygame.display.set_caption('The Doungeoner')

        key_actions = {
            pygame.K_w: (lambda: self.move(0, 10)),
            pygame.K_s: (lambda: self.move(0, -10)),
            pygame.K_a: (lambda: self.move(-10, 0)),
            pygame.K_d: (lambda: self.move(10, 0)),
            pygame.K_m: (lambda: self.change_scale(5)),
            pygame.K_n: (lambda: self.change_scale(-5)),
        }

        while True:
            self.screen.fill((0, 0, 0))  # Clear the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_l):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key in key_actions:
                    key_actions[event.key]()

            self.map.draw_map(self.screen, self.mapX, self.mapY, self.scale)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
