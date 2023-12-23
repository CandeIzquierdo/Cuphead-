import pygame
from Nivel import *
from sonidos import *


class NivelUno(Nivel):
    def __init__(self, pantalla):

        self.direccion_plataforma = 1
        self.velocidad_plataforma = 4

        # Configuración Ventana Pygame

        self.intro_level()

        self.music_level_1()

        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load(r"Plataform Game\Ambiente\fondo nivel 1.jpg")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        pygame.display.set_caption("Cuphead")

        ICONO = pygame.image.load(r"Plataform Game\Ambiente\icono.png")
        pygame.display.set_icon(ICONO)

        EXIT = pygame.image.load(r"Plataform Game\Ambiente\exit.png")

        personaje = Personaje(diccionario, (100, 100), 380,600, 5)

        # Configuración Plataformas

        piso = crear_plataforma(ANCHO, 10, 0, 890, True)
        piso["rectangulo"].top = personaje.rectangulo_principal.bottom

        plataforma_hongo1 = crear_plataforma(150, 100, 740, 180, True, r"Plataform Game\Ambiente\plataforma.png")
        plataforma_tierra = crear_plataforma(350, 120, 100, 280, True, r"Plataform Game\Ambiente\plataforma2.png")
        plataforma_tierra2 = crear_plataforma(350, 120, 1200, 280, True, r"Plataform Game\Ambiente\plataforma2.png")

        lista_plataformas = [piso, plataforma_hongo1, plataforma_tierra, plataforma_tierra2]

        # Configuración Enemigos

        blueberry = {
            "animacion_izquierda": Blueberry_walk,
            "animacion_derecha": Blueberry_walk_right,
            "animacion_muere": Blueberry_dead,
            "pos_x": 1300,
            "pos_y": 660,
            "puede_moverse": True  # Aquí se establece si puede moverse o no
        }

        daisy = {
            "animacion_izquierda": Daisy_walk,
            "animacion_derecha": Daisy_walk_right,
            "animacion_muere": Daisy_dead,
            "pos_x": 230,
            "pos_y": 100,
            "puede_moverse": True  # Este enemigo no se moverá
        }

        daisy2 = {
            "animacion_izquierda": Daisy_walk,
            "animacion_derecha": Daisy_walk_right,
            "animacion_muere": Daisy_dead,
            "pos_x": 1400,
            "pos_y": 100,
            "puede_moverse": True  # Este enemigo sí se moverá
        }

        lista_datos_enemigos = [blueberry, daisy, daisy2]
        lista_enemigos = Enemigo.crear_lista(lista_datos_enemigos, personaje)

        # lista_enemigos = Enemigo.crear_lista(piso, personaje)

        boss = []

        reloj = None
        
        # Configuración Items

        posiciones_monedas = [(160,180), (320,180), (1270,180), (1440,180), (790,180), (790,300), (790,60)]
        lista_monedas = Items.crear_lista_monedas(posiciones_monedas)
        posiciones_vidas = []
        lista_vidas = Items.crear_lista_vidas(posiciones_vidas)
        lista_trampas = []

        # Configuración Plataformas

        pantalla.blit(EXIT, (1500, 600))
        pantalla.blit(plataforma_hongo1["imagen"], plataforma_hongo1["rectangulo"])
        pantalla.blit(plataforma_tierra["imagen"], plataforma_tierra["rectangulo"])
        pantalla.blit(plataforma_tierra2["imagen"], plataforma_tierra2["rectangulo"])

        super().__init__(pantalla, personaje, lista_plataformas, lista_enemigos, lista_monedas, lista_vidas, lista_trampas, boss, fondo, reloj)

    # Configuración Plataforma Movible

    def mover_plataforma(self):

        plataforma_hongo1 = self.plataformas[1] 

        plataforma_hongo1["rectangulo"].y += self.velocidad_plataforma * self.direccion_plataforma

        if plataforma_hongo1["rectangulo"].y <= 120:  
            self.direccion_plataforma = 1 
        elif plataforma_hongo1["rectangulo"].y >= 660: 
            self.direccion_plataforma = -1 

    def intro_level(self):

        pygame.mixer.init()
        sonido_now_go = pygame.mixer.Sound(r"Plataform Game\Sonidos\NOW_GO!.mp3")
        sonido_now_go.set_volume(0.3)
        sonido_now_go.play()

    def music_level_1(self):
        
        pygame.mixer.init()
        music_level_1 = pygame.mixer.Sound(r"Plataform Game\Sonidos\Cuphead OST - Forest Follies [Music].wav")
        music_level_1.set_volume(0.2)
        music_level_1.play()
