import pygame
import sys
from configuraciones import *
from nivel import Nivel


class Juego:
    
    #este metodo nos construlle la clase juego
    def __init__(self): # __ (son dos rayas al piso juntas )
        pygame.init()
        
        # SE CREA LA PANTALLA DE JUEGO CON EL ANCHO Y EL ALTO 
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        # SE PONE EL TITULOA LA VENTANA DE ESTA PANTALLA 
        pygame.display.set_caption('ECO-GUERRA')
        # crea el reloj:
        self.reloj = pygame.time.Clock()
         # crear veriable de nivel
        self.nivel = Nivel()
        
    def iniciarJuego(self):
        while True:
            for evento in pygame.event.get():
                #si se pulso la x para salir 
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    #si se pulso     la q para salir 
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            #mortrar la pantalla de fondo negro
            self.pantalla.fill('black')
            # iniciamos nivel 
            self.nivel.iniciarNivel()
            #que actualice la pantalla con los cambios
            pygame.display.update()
            # que el reloj empiece a contar
            self.reloj.tick(IPS)

if __name__ == '__main__':
    #hacer una variable que sea un juego
    jugar = Juego()
    
    jugar.iniciarJuego()
