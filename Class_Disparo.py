import pygame
from animaciones import *

class Disparo:
    def __init__(self, x, y, direccion):
        self.superficie = pygame.image.load(r"Plataform Game\Cuphead_Img\Cuphead_shoot.png")
        self.superficie = pygame.transform.scale(self.superficie, (70, 20))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion
        self.girado = False

    def actualizar(self, pantalla):

        if self.direccion == "derecha" or self.direccion == "dispara":
            self.rectangulo.x += 10

            if self.girado:
                self.superficie = pygame.transform.flip(self.superficie, True, False)
                self.girado = False

        elif self.direccion == "izquierda" or self.direccion == "dispara_izquierda":
            self.rectangulo.x -= 10

            if not self.girado:
                self.superficie = pygame.transform.flip(self.superficie, True, False)
                self.girado = True

        pantalla.blit(self.superficie, self.rectangulo)
