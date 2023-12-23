import pygame
from Class_Personaje import *

class ProyectilArcosLuz:
    def __init__(self, animacion_completa, pos_x, pos_y):
        self.animacion = animacion_completa
        self.frame_actual = 0 
        self.rectangulo = self.animacion[self.frame_actual].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = 8

    def mover(self):

        self.rectangulo.x -= self.velocidad

    def animar(self, pantalla):

        pantalla.blit(self.animacion[self.frame_actual], self.rectangulo)
        self.frame_actual = (self.frame_actual + 1) % len(self.animacion)

    def obtener_rectangulos_arcosluz(self):

        diccionario = {}

        # Rectángulo bottom 
        diccionario["bottom"] = pygame.Rect(self.rectangulo.left, self.rectangulo.bottom - 10, self.rectangulo.width, 10)
        # Rectángulo top 
        diccionario["top"] = pygame.Rect(self.rectangulo.left, self.rectangulo.top, self.rectangulo.width, 10)
        # Rectángulo left 
        diccionario["left"] = pygame.Rect(self.rectangulo.left, self.rectangulo.top, 10, self.rectangulo.height)
        # Rectángulo right 
        diccionario["right"] = pygame.Rect(self.rectangulo.right - 10, self.rectangulo.top, 10, self.rectangulo.height)

        return diccionario

    def dibujar_rectangulo_arcos_luz(arcosluz, pantalla):

        rectangulos = arcosluz.obtener_rectangulos_arcosluz()

        pygame.draw.rect(pantalla, "purple", rectangulos["bottom"], 3)
        pygame.draw.rect(pantalla, "purple", rectangulos["top"], 3)
        pygame.draw.rect(pantalla, "purple", rectangulos["left"], 3)
        pygame.draw.rect(pantalla, "purple", rectangulos["right"], 3)