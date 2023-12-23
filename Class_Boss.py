import pygame
from animaciones import *
from Class_Disparo import *
from Class_Personaje import *
from Class_Arcos_Luz import *
import random
from sonidos import *

class Boss:

    def __init__(self, animaciones, personaje, pos_x, pos_y, animacion_arco_rosa, animacion_arco_verde):
        self.animaciones = animaciones
        self.rectangulo = self.animaciones["vuela"][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["vuela"]
        self.personaje = personaje

        # Vida

        self.vida = 10000 # Con vida me refiero a que si recibe 10000 disparos MUERE
        self.colisiones_con_disparos = 0
        self.esta_muriendo = False
        self.esta_muerto = False

        # Fase Ataque 1

        self.animaciones_arco_rosa = animacion_arco_rosa
        self.animaciones_arco_verde = animacion_arco_verde

        self.ultimo_evento = pygame.time.get_ticks()
        self.lista_proyectiles_arcos_luz = []

    def animar(self, pantalla):

        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

    def actualizar(self, pantalla):

        if not self.esta_muerto:
            self.verificar_colision_disparo_boss(self.personaje.lista_proyectiles)
            self.animar(pantalla)
            self.primer_fase_ataque(pantalla)
            self.disparar_arcos_luz(pantalla)
            self.morir_boss()

    @staticmethod
    def crear_lista_boss(datos_boss, personaje, animacion_arco_rosa, animacion_arco_verde):

        lista_boss = []

        for datos in datos_boss:
            animaciones_boss = {
                "vuela": datos["animacion_vuela"],
                "muere": datos["animacion_muere"],
                "ataque1": datos["animacion_ataque1"]
            }
            
            nuevo_boss = Boss(animaciones_boss, personaje, datos["pos_x"], datos["pos_y"], animacion_arco_rosa, animacion_arco_verde)
            lista_boss.append(nuevo_boss)

        return lista_boss
    
    def morir_boss(self):

        if self.colisiones_con_disparos >= 10000:
            knockout()
            self.esta_muerto = True

    def verificar_colision_disparo_boss(self, lista_proyectiles_personaje):

        for disparo in lista_proyectiles_personaje:

            if self.rectangulo.colliderect(disparo.rectangulo):
                self.colisiones_con_disparos += 1
                if self.colisiones_con_disparos >= 10000:
                    self.animacion_actual = self.animaciones["muere"]
                    self.personaje.score += 1000
                    self.esta_muerto = True
                    self.animacion_actual = self.animaciones["muere"]

    def obtener_rectangulos_boss(self):

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
    
    def dibujar_rectangulos_boss(lista_boss, pantalla):
        
        for boss in lista_boss:
            pygame.draw.rect(pantalla, "red", boss.rectangulo, 3)
            rectangulos = boss.obtener_rectangulos_boss()

            pygame.draw.rect(pantalla, "red", rectangulos["bottom"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos["top"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos["left"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos["right"], 3)

    def obtener_rectangulo_ojos(self):

        ojos_width = 100
        ojos_height = 50
        ojos_x = 1150 
        ojos_y = 320 

        rectangulo_ojos = pygame.Rect(ojos_x, ojos_y, ojos_width, ojos_height)

        return rectangulo_ojos
    
    def dibujar_rectangulo_ojos(boss, pantalla):

        rect_ojos = boss.obtener_rectangulo_ojos()

        pygame.draw.rect(pantalla, "purple", rect_ojos, 3)

    def primer_fase_ataque(self, pantalla):

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.ultimo_evento

        if self.vida >= 0 and self.vida <= 10000:
            if tiempo_transcurrido >= 4000:
                self.ultimo_evento = tiempo_actual

                if self.animacion_actual == self.animaciones["vuela"]:
                    self.animacion_actual = self.animaciones["ataque1"]

                    arcos_disparados = self.disparar_arcos_luz(pantalla)
                    if arcos_disparados:
                        self.lista_proyectiles_arcos_luz.extend(arcos_disparados)
                        boss_shoot()
                else:
                    self.animacion_actual = self.animaciones["vuela"]

    def disparar_arcos_luz(self, pantalla):

        lista_arcosluz = []
        rect_ojos = self.obtener_rectangulo_ojos()

        posiciones = [
            (rect_ojos.left + 60, 350),
            (rect_ojos.centerx + 80, 300),
            (rect_ojos.right - 100, 400)
        ]

        for pos_x, pos_y in posiciones:

            if random.random() < 0.5:
                animacion_arco = self.animaciones_arco_rosa  
            else:
                animacion_arco = self.animaciones_arco_verde 

            nuevo_arco = ProyectilArcosLuz(animacion_arco, pos_x, pos_y)
            lista_arcosluz.append(nuevo_arco)

        return lista_arcosluz