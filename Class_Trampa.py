import pygame
from animaciones import *

class Trampa:
    def __init__(self, animaciones, pos_x, pos_y):
        self.animaciones = animaciones
        self.rectangulo = self.animaciones["gira"][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.animacion_actual = self.animaciones["gira"]
        self.frame_actual = 0
        self.velocidad = 5
        self.direccion = 1


    def animar(self, pantalla):

        self.frame_actual = (self.frame_actual + 1) % len(self.animacion_actual)
        pantalla.blit(self.animacion_actual[self.frame_actual], self.rectangulo)

    def mover(self):

        self.rectangulo.y += self.velocidad * self.direccion

        if self.rectangulo.y <= 350:
            self.direccion = 1
        elif self.rectangulo.y >= 590:
            self.direccion = -1

    @staticmethod
    def crear_lista_trampas(posiciones):

        diccionario_trampas = {}
        diccionario_trampas["gira"] = Pink_spiker

        lista_trampas = []
        for pos_x, pos_y in posiciones:
            nueva_moneda = Trampa(diccionario_trampas, pos_x, pos_y)
            lista_trampas.append(nueva_moneda)

        return lista_trampas

    def obtener_rectangulos_trampa(self):

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

    def dibujar_rectangulo_trampa(lista_trampas, pantalla):

        for trampa in lista_trampas:
            pygame.draw.rect(pantalla, "pink", trampa.rectangulo, 3)

            rectangulos_enemigo = trampa.obtener_rectangulos_trampa()
            pygame.draw.rect(pantalla, "pink", rectangulos_enemigo["bottom"], 3)
            pygame.draw.rect(pantalla, "pink", rectangulos_enemigo["top"], 3)
            pygame.draw.rect(pantalla, "pink", rectangulos_enemigo["left"], 3)
            pygame.draw.rect(pantalla, "pink", rectangulos_enemigo["right"], 3)