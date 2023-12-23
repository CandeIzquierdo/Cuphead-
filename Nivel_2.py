import pygame
from Nivel import *


class NivelDos(Nivel):
    def __init__(self, pantalla):

        self.direccion_plataforma = 1
        self.velocidad_plataforma = 4

        # Configuración Ventana Pygame

        self.intro_level()

        self.music_level_2()

        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load(r"Plataform Game\Ambiente\fondo nivel 2.jpg")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        pygame.display.set_caption("Cuphead")

        ICONO = pygame.image.load(r"Plataform Game\Ambiente\icono.png")
        pygame.display.set_icon(ICONO)

        EXIT = pygame.image.load(r"Plataform Game\Ambiente\exit.png")

        personaje = Personaje(diccionario, (100, 100), 20,600, 5)

        # Configuración Plataformas

        piso = crear_plataforma(ANCHO, 10, 0, 10, True)
        piso["rectangulo"].top = personaje.rectangulo_principal.bottom

        plataforma_tronco = crear_plataforma(450, 100, 520, 670, True, r"Plataform Game\Ambiente\tronco1.png")
        plataforma_hongo = crear_plataforma(150, 100,  1050, 600, True, r"Plataform Game\Ambiente\plataforma.png")
        plataforma_tierra = crear_plataforma(300, 110, 1320, 250, True, r"Plataform Game\Ambiente\plataforma2.png")
        plataforma_tierra2 = crear_plataforma(180, 110, 670, 250, True, r"Plataform Game\Ambiente\plataforma2.png")
        plataforma_tierra3 = crear_plataforma(300, 110, 50, 250, True, r"Plataform Game\Ambiente\plataforma2.png")

        lista_plataformas = [piso, plataforma_tronco, plataforma_hongo, plataforma_tierra, plataforma_tierra2, plataforma_tierra3]

        # Configuración Enemigos

        hongo = {
            "animacion_izquierda": Hongo,
            "animacion_derecha": None,
            "animacion_muere": Hongo_dead,
            "pos_x": 300,
            "pos_y": 660,
            "puede_moverse": False
        }

        bellota = {
            "animacion_izquierda": Bellota_walk,
            "animacion_derecha": Bellota_walk_right,
            "animacion_muere": Bellota_dead,
            "pos_x": 1480,
            "pos_y": 70,
            "puede_moverse": True
        }

        bellota2 = {
            "animacion_izquierda": Bellota_walk,
            "animacion_derecha": Bellota_walk_right,
            "animacion_muere": Bellota_dead,
            "pos_x": 770,
            "pos_y": 70,
            "puede_moverse": True
        }

        daisy = {
            "animacion_izquierda": Daisy_walk,
            "animacion_derecha": Daisy_walk_right,
            "animacion_muere": Daisy_dead,
            "pos_x": 170,
            "pos_y": 80,
            "puede_moverse": True
        }

        lista_datos_enemigos = [hongo, bellota, bellota2, daisy]

        lista_enemigos = Enemigo.crear_lista(lista_datos_enemigos, personaje)

        boss = []

        reloj = None

        # Configuración Items

        posiciones_monedas = [(580,580), (715,580), (850,580), (370,80), (470,50), (570,80), (1380,160)]
        lista_monedas = Items.crear_lista_monedas(posiciones_monedas)

        posiciones_vidas = [(1500, 180)]
        lista_vidas = Items.crear_lista_vidas(posiciones_vidas)

        posiciones_trampas = [(705,500)]
        lista_trampas = Trampa.crear_lista_trampas(posiciones_trampas)

        # Configuración Plataformas

        pantalla.blit(EXIT, (800, 800))
        # pantalla.blit(plataforma_hongo1["imagen"], plataforma_hongo1["rectangulo"])
        # pantalla.blit(plataforma_tierra["imagen"], plataforma_tierra["rectangulo"])
        # pantalla.blit(plataforma_tierra2["imagen"], plataforma_tierra2["rectangulo"])
        
        super().__init__(pantalla, personaje, lista_plataformas, lista_enemigos, lista_monedas, lista_vidas, lista_trampas, boss, fondo, reloj)

    # Configuración Plataforma Movible

    def mover_plataforma(self):
        
        plataforma_hongo1 = self.plataformas[2] 

        plataforma_hongo1["rectangulo"].y += self.velocidad_plataforma * self.direccion_plataforma

        if plataforma_hongo1["rectangulo"].y <= 120:  
            self.direccion_plataforma = 1 
        elif plataforma_hongo1["rectangulo"].y >= 660: 
            self.direccion_plataforma = -1 

    def intro_level(self):

        pygame.mixer.init()
        sonido_your_up = pygame.mixer.Sound(r"Plataform Game\Sonidos\YOUR_UP!.mp3")
        sonido_your_up.set_volume(0.2)
        sonido_your_up.play()

    def music_level_2(self):
        
        pygame.mixer.init()
        music_level_2 = pygame.mixer.Sound(r"Plataform Game\Sonidos\Cuphead OST - Threatin' Zeppelin [Music].wav")
        music_level_2.set_volume(0.2)
        music_level_2.play()