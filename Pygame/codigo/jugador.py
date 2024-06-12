import pygame
from configuraciones import *

class Jugador(pygame.sprite.Sprite):
    
    def __init__(self,pos,grupos,obstaculos):
        super().__init__(grupos)
        self.image = pygame.image.load('./graficos/Jugador1.png')
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.vector2()


        self.velocidad = 5

        self.obstaculos = obstaculos


    def ingresoTecla(self):

        tecla = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.direction.y = -1 #subir
        elif teclas [pygame.K:DOWN]:
            self.direction.y = 1 #bajar
        else:
            self.direction.y = 0


        if teclas [pygame.K_RIGHT]:
            self.direction.x = 1 #DERECHA
        elif teclas[pygame.K_LEFT]:
            self.direction.x = -1 #IZQUIERDA
        else:
            self.direction.x = 0


    def update(self):
        delf.ingresoTeclas()
        self.mover(self.velocidad)


    def mover(self,velocidad):
        if self.direction.magnitude() != 0:
            self.direction = self.derection.normalize()
            
        self.rect.x += self.direction.x * velocidad
        self.colision('horizontal')

        self.rect.y += self.direction.y * velocidad
        self.colision('vertical')
        

    def colision(self,direccion):
        if direccion == 'horizontal':
            for sprite in self.obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direccion == 'vertical':
            for sprite in self.obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
