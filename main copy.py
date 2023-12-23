import pygame, sys
from pygame.locals import *
from animaciones import * 
from Class_Personaje import *
from modo import *
from Class_Enemigo import *
from Class_Disparo import *
from Class_Items import *
from Nivel_1 import *
from Nivel_2 import *
from Nivel_3 import *
from Material_UI.GUI_form_prueba import *
from Class_Presentacion import *
from Nivel import *

pygame.init()

# Configuración Ventana Pygame

ANCHO = 1700
ALTO = 950
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

FONDO_PRESENTACION = pygame.image.load(r"Plataform Game\Ambiente\fondo_interfaz.jpg")
FONDO_PRESENTACION = pygame.transform.scale(FONDO_PRESENTACION, (ANCHO, ALTO))

reloj = pygame.time.Clock()
FPS = 30

# Bucle

pygame.mixer.init()
pygame.mixer.music.load(r"Plataform Game\Sonidos\Intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

presentacion = Presentacion(PANTALLA)
mostrar_presentacion = True

while mostrar_presentacion:
    reloj.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if presentacion.verificar_tecla_enter(pygame.event.get()):
        mostrar_presentacion = False

    presentacion.mostrar_presentacion()

    pygame.display.flip()

form_principal = FormPrueba(PANTALLA, 60, 160, 500, 650, "gray", "white", 5, True)

while True:
    reloj.tick(FPS)

    PANTALLA.blit(FONDO_PRESENTACION, (0,0))

    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    form_principal.update(eventos)

    pygame.display.update()