import pygame
from Nivel import *
from Class_Boss import *
from animaciones import *


class NivelTres(Nivel):
    def __init__(self, pantalla):

        self.desplazamiento_vertical = 1  
        self.direccion_plataforma = 1  
        self.movimiento_actual = 0  
        self.movimiento_total = 450

        # Configuración Ventana Pygame

        self.intro_level()

        self.music_level_3()

        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load(r"Plataform Game\Ambiente\fondo nivel 3.jpg")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        pygame.display.set_caption("Cuphead")

        ICONO = pygame.image.load(r"Plataform Game\Ambiente\icono.png")
        pygame.display.set_icon(ICONO)

        personaje = Personaje(diccionario, (100, 100), 120,680, 5)

        # Configuración Plataformas

        piso = crear_plataforma(ANCHO, 10, 0, 890, True)
        # piso["rectangulo"].top = personaje.rectangulo_principal.bottom

        plataforma_nube = crear_plataforma(200, 80, 740, 350, True, r"Plataform Game\Ambiente\cloud_01.png")
        plataforma_nube2 = crear_plataforma(200, 80, 650, 680, True, r"Plataform Game\Ambiente\cloud_02.png")
        plataforma_nube3 = crear_plataforma(200, 80, 400, 500, True, r"Plataform Game\Ambiente\cloud_01.png")
        plataforma_nube4 = crear_plataforma(200, 80, 50, 350, True, r"Plataform Game\Ambiente\cloud_02.png")
        plataforma_nube5 = crear_plataforma(200, 80, 120, 680, True, r"Plataform Game\Ambiente\cloud_02.png")
        plataforma_nube6 = crear_plataforma(200, 80, 390, 220, True, r"Plataform Game\Ambiente\cloud_03.png")

        self.plataformas_nube = [
        plataforma_nube,
        plataforma_nube2,
        plataforma_nube3,
        plataforma_nube4,
        plataforma_nube5,
        plataforma_nube6
        ]

        lista_plataformas = [piso, plataforma_nube, plataforma_nube2, plataforma_nube3, plataforma_nube4, plataforma_nube5, plataforma_nube6]

        # Configuración Enemigos

        lista_datos_enemigos = []
        lista_enemigos = Enemigo.crear_lista(lista_datos_enemigos, personaje)

        # Configuración BOSS
        boss_data = [
            {
                "animacion_vuela": Grim_Matchstick_fly,
                "animacion_muere": Bellota_dead,
                "animacion_ataque1": Grim_Matchstick_attack_1,
                "pos_x": 1050,
                "pos_y": 250,
            }
        ]

        boss = Boss.crear_lista_boss(boss_data, personaje, Pink_Rings, Green_Rings)

        reloj = None

        # Configuración Items

        posiciones_monedas = [(300,300), (620,300), (300,600), (620,600)]
        lista_monedas = Items.crear_lista_monedas(posiciones_monedas)
        posiciones_vidas = [(450,130)]
        lista_vidas = Items.crear_lista_vidas(posiciones_vidas)
        lista_trampas = []

        super().__init__(pantalla, personaje, lista_plataformas, lista_enemigos, lista_monedas, lista_vidas, lista_trampas, boss, fondo, reloj)

    # Configuración Plataforma Movible

    def mover_plataforma(self):

        for plataforma in self.plataformas_nube:
            plataforma["rectangulo"].y += self.desplazamiento_vertical * self.direccion_plataforma
            self.movimiento_actual += (self.desplazamiento_vertical)

        if self.movimiento_actual >= self.movimiento_total:
            self.movimiento_actual = 0
            self.direccion_plataforma *= -1 

    def intro_level(self):

        pygame.mixer.init()
        sonido_wallop = pygame.mixer.Sound(r"Plataform Game\Sonidos\WALLOP.mp3")
        sonido_wallop.set_volume(0.2)
        sonido_wallop.play()

    def music_level_3(self):
        
        pygame.mixer.init()
        music_level_3 = pygame.mixer.Sound(r"Plataform Game\Sonidos\Cuphead OST - Fiery Frolic [Music].wav")
        music_level_3.set_volume(0.2)
        music_level_3.play()