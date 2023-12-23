import pygame

class Presentacion:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = pygame.image.load(r"Plataform Game\Ambiente\fondo_presentacion.png")
        self.fondo = pygame.transform.scale(self.fondo, (pantalla.get_width(), pantalla.get_height()))

        self.cuphead = pygame.image.load(r"Plataform Game\Ambiente\cuphead_title_screen_0001.png")

        self.texto = pygame.image.load(r"Plataform Game\Ambiente\enter.png")

    def mostrar_presentacion(self):

        self.pantalla.blit(self.fondo, (0, 0))

        self.pantalla.blit(self.cuphead, (680, 300))

        self.pantalla.blit(self.texto, (650, 870))

    def verificar_tecla_enter(self, eventos):

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:

                return True 

            return False