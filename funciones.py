import pygame
from pygame.locals import *

def actualizar_cronometro(tiempo_restante, tiempo_pasado):

    tiempo_restante -= tiempo_pasado  
    return tiempo_restante

def mostrar_cronometro(minutos, segundos, PANTALLA):

    tiempo_formateado = f"Time: {minutos:02}:{segundos:02}"
    fuente = pygame.font.Font("Plataform Game\Bangers-Regular.ttf", 35)  
    texto_tiempo = fuente.render(tiempo_formateado, True, "white") 
    PANTALLA.blit(texto_tiempo, (740, 10))