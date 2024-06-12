import pygame
from configuraciones import *
from roca import Roca
from jugador import Jugador

class Nivel():

    def __init__(self):

        self.personajes = Camara()
        self.obstaculos = pygame.sprite.Group()

        self.superficie = pygame.display.get_surface()
        
        for posFila, fila in enumerate(MUNDO):
            for posColumna, columna in enumerate(fila):
                x = posColumna * RECUADRO
                y = posFila * RECUADRO
                if columna == 'x':
                    Roca((x,y),[self.personajes,self.obstaculos])
                if columna == 'P':
                    self.jugador = Jugador((x,y),[self.personajes],self.obstaculos)

    def iniciarNivel(self):

        self.personajes.mostrarCamara(self.jugador)
        self.personajes.update()
    

class Camara(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.superficie = pygame.display.get_surface()
        self.desenfoque = pygame.math.Vector2()

    def mostrarCamara(self,jugador):

        self.desenfoque.x = jugador.rect.centerx - self.superficie.get_size()[0] //4
        self.desenfoque.y = jugador.rect.centery - self.superficie.get_size()[1] //4

        for sprite in self.sprites():
            desenfoqueTotal = sprite.rect.topleft - self.desenfoque
            self.superficie.blit(sprite.image,desenfoqueTotal)