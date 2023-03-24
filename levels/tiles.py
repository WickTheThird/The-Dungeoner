import pygame
from pygame.locals import *

class Tiles:

    def __init__(self):
        self.graphicsPath = "../graphics/0x72_16x16DungeonTileset.v5/items"
        self.tiles = {}

    def background(self):
        tile = pygame.image.load(self.graphicsPath + "black.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def floorPlain(self):
        tile = pygame.image.load(self.graphicsPath + "floor_plain.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile

    def floorLight(self):
        tile = pygame.image.load(self.graphicsPath + "floor_light.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def floorMudE(self):
        tile = pygame.image.load(self.graphicsPath + "floor_mud_e.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def floorMudMid1(self):
        tile = pygame.image.load(self.graphicsPath + "floor_mud_mid_1.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def floorMudMid2(self):
        tile = pygame.image.load(self.graphicsPath + "floor_mud_mid_2.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def edgeE(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_e.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def edgeW(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_w.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile
    
    def edgeN(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_n.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile
    
    def edgeS(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_s.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile
    
    def edgeNE(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_ne.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile
    
    def edgeNW(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_nw.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))
        
        return tile 

    def edgeSE(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_se.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def edgeSW(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_sw.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

    def edgeSingle(self):
        tile = pygame.image.load(self.graphicsPath + "Edge_single.png").convert_alpha()
        tile = pygame.transform.scale(tile, (64, 64))

        return tile

