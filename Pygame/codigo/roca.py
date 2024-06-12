import pygame
from configuraciones import *

class Roca(pygame.sprite.Sprite):
    
    def __init__(self,pos,grupos):
        super().__init__(grupos)
        self.image = pygame.image.load('./graficos/Roca1.png')
        self.rect = self.image.get_rect(topleft = pos)