#library
import pygame
from pygame.locals import *
import sys

#local

pygame.init()

#screen
screen = pygame.display.set_mode((1000, 800))

#title
pygame.display.set_caption("Nomad")
theme = pygame.image.load("wallpaper.jpeg")

#icon
icon = pygame.image.load("treasure-map.png")
pygame.display.set_icon(icon)

# colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0,255,255)

# fonts
font = pygame.font.Font('freesansbold.ttf', 32)

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
