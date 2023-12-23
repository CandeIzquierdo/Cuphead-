from Class_Disparo import *
from animaciones import *
from Class_Enemigo import *
from Class_Items import *
from Class_Trampa import *
from sonidos import *

import pygame

class Personaje:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = animaciones
        self.rectangulo_principal = animaciones["quieto"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animacion_actual = self.animaciones["quieto"]
        self.mira_derecha = True # Orientación

        # Score

        self.score = 0

        # Vida

        self.vidas = 3

        # Salto

        self.desplazamiento_y = 0 
        self.potencia_salto = -32 
        self.limite_velocidad_salto = 32
        self.esta_saltando = False
        self.gravedad = 1 

        # Disparo

        self.lista_proyectiles = []

    def obtener_rectangulos_cuphead(self):

        diccionario = {}

        # Rectángulo bottom 
        diccionario["bottom"] = pygame.Rect(self.rectangulo_principal.left, self.rectangulo_principal.bottom - 10, self.rectangulo_principal.width, 10)
        # Rectángulo top 
        diccionario["top"] = pygame.Rect(self.rectangulo_principal.left, self.rectangulo_principal.top, self.rectangulo_principal.width, 10)
        # Rectángulo left 
        diccionario["left"] = pygame.Rect(self.rectangulo_principal.left, self.rectangulo_principal.top, 10, self.rectangulo_principal.height)
        # Rectángulo right 
        diccionario["right"] = pygame.Rect(self.rectangulo_principal.right - 10, self.rectangulo_principal.top, 10, self.rectangulo_principal.height)

        return diccionario
    
    def dibujar_rectangulos_cuphead(cuphead, pantalla):
        
        rectangulos = cuphead.obtener_rectangulos_cuphead()

        pygame.draw.rect(pantalla, "blue", rectangulos["bottom"], 3)
        pygame.draw.rect(pantalla, "blue", rectangulos["top"], 3)
        pygame.draw.rect(pantalla, "blue", rectangulos["left"], 3)
        pygame.draw.rect(pantalla, "blue", rectangulos["right"], 3)

    def detectar_colisiones_plataformas(self, plataformas):

        rect_personaje = self.obtener_rectangulos_cuphead()

        for pl in plataformas:
            
            if rect_personaje["right"].colliderect(pl["rectangulo"]):
                self.rectangulo_principal.right = pl["rectangulo"].left
                self.velocidad_x = 0

            if rect_personaje["left"].colliderect(pl["rectangulo"]):
                self.rectangulo_principal.left = pl["rectangulo"].right
                self.velocidad_x = 0

            if rect_personaje["bottom"].colliderect(pl["rectangulo"]):
                self.rectangulo_principal.bottom = pl["rectangulo"].top
                self.esta_saltando = False
                self.desplazamiento_y = 0

            if rect_personaje["top"].colliderect(pl["rectangulo"]):
                self.rectangulo_principal.top = pl["rectangulo"].bottom
                self.desplazamiento_y = 0

            # Manejar si el personaje está en una plataforma y no cae
            if rect_personaje["bottom"].colliderect(pl["rectangulo"]) and self.esta_saltando:
                self.esta_saltando = False
                self.desplazamiento_y = 0

    def caminar(self, pantalla):

        velocidad_actual = self.velocidad
        if self.mira_derecha == False:
            self.que_hace = "izquierda"
            velocidad_actual *= -3

        nueva_posicion = self.rectangulo_principal.x + velocidad_actual

        if nueva_posicion > 0 and nueva_posicion < (pantalla.get_width() - self.rectangulo_principal.width):
            self.rectangulo_principal.x += velocidad_actual + 4

    def saltar(self, pantalla, plataformas):
        
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for pl in plataformas:

            if self.rectangulo_principal.colliderect(pl["rectangulo"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.rectangulo_principal.bottom = pl["rectangulo"].top  
                break
            else:
                self.esta_saltando = True

    def animar(self, pantalla):

        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo * 2:
            self.contador_pasos = 0
        imagen_actual = self.contador_pasos // 2
        pantalla.blit(self.animacion_actual[imagen_actual], self.rectangulo_principal)
        self.contador_pasos += 1

    def actualizar(self, pantalla, plataformas):

        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.mira_derecha = True
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "izquierda":
                if not self.esta_saltando:
                    self.mira_derecha = False
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "quieto":
                if not self.esta_saltando:
                    if self.mira_derecha == True:
                        self.animacion_actual = self.animaciones["quieto"]
                        self.animar(pantalla)
                    else:
                        self.animacion_actual = self.animaciones["quieto_izquierda"]
                        self.animar(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    if self.mira_derecha == True:
                        self.animacion_actual = self.animaciones["salta"]
                    else:
                        self.animacion_actual = self.animaciones["salta_izquierda"]
            case "dispara":
                if not self.esta_saltando:
                    if self.mira_derecha == True:
                        self.animacion_actual = self.animaciones["dispara"]
                        self.animar(pantalla)
            case "dispara_izquierda":
                if not self.esta_saltando:
                    if self.mira_derecha == False:
                        self.animacion_actual = self.animaciones["dispara_izquierda"]
                        self.animar(pantalla)

                        
        self.saltar(pantalla, plataformas)
        self.actualizar_proyectiles(pantalla)

    def lanzar_proyectil(self):

        x = None
        margen = 47
        y = self.rectangulo_principal.centery + 30

        if self.mira_derecha:
            self.que_hace = "dispara"
            x = self.rectangulo_principal.right + 50 - margen
        else:
            self.que_hace = "dispara_izquierda"
            x = self.rectangulo_principal.left - 50 + margen

        if x is not None:
            self.lista_proyectiles.append(Disparo(x, y, self.que_hace))

    def actualizar_proyectiles(self, pantalla):

        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            p.actualizar(pantalla)
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1

    def verificar_colision_enemigo(self, pantalla, lista_enemigos):

        rect_personaje = self.obtener_rectangulos_cuphead()

        for enemigo in lista_enemigos:
            rect_enemigo = enemigo.obtener_rectangulos_enemigos()

            if rect_personaje["bottom"].colliderect(rect_enemigo["top"]):
                cuphead_parry()
                self.score += 100
                enemigo.animacion_actual = enemigo.animaciones["muere"]
                enemigo.animar(pantalla)
                enemigo.esta_muriendo = True

                enemigo.rectangulo.y += 10

    def verificar_colision_monedas(self, pantalla, lista_monedas):

        for moneda in lista_monedas:
            if moneda.rectangulo.colliderect(self.rectangulo_principal):
                player_pickup_coin()
                self.score += 100
                lista_monedas.remove(moneda)

        fuente = pygame.font.Font(r"Plataform Game\Bangers-Regular.ttf", 35)
        texto = fuente.render(f"SCORE: {self.score}", True, "white")
        pantalla.blit(texto, (28, 10))

    def perder_vida(self):
        
        self.vidas -= 1

    def verificar_colision_vidas(self, lista_vidas):

        for vida in lista_vidas:
            if self.rectangulo_principal.colliderect(vida.rectangulo):
                player_drink_coffee()
                self.vidas += 1
                lista_vidas.remove(vida)

    def verificar_daño_enemigos(self, lista_enemigos):

        rect_personaje = self.obtener_rectangulos_cuphead()

        for enemigo in lista_enemigos:
            rect_enemigo = enemigo.obtener_rectangulos_enemigos()

            if rect_personaje["right"].colliderect(rect_enemigo["left"]):
                player_damage()
                self.perder_vida()
            elif rect_personaje["left"].colliderect(rect_enemigo["right"]):
                player_damage()
                self.perder_vida()
            else:
                pass

    def colocar_vidas_pantalla(self, pantalla):

        fuente = pygame.font.Font(r"Plataform Game\Bangers-Regular.ttf", 35)
        texto = fuente.render(f"{self.vidas}", True, "white")
        pantalla.blit(texto, (1620, 20))

    def verificar_colision_trampas(self, lista_trampas):
        
        rect_personaje = self.obtener_rectangulos_cuphead()

        for trampa in lista_trampas:
            rect_trampa = trampa.obtener_rectangulos_trampa()

            if rect_personaje["top"].colliderect(rect_trampa["bottom"]):
                player_damage()
                self.perder_vida()
            else:
                pass

    def verificar_daño_arcosluz(self, lista_arcosluz):

        rect_personaje = self.obtener_rectangulos_cuphead()

        for arco_luz in lista_arcosluz:
            rect_arcosluz = arco_luz.obtener_rectangulos_arcosluz()

            if rect_personaje["right"].colliderect(rect_arcosluz["left"]):
                player_damage()
                self.perder_vida()
            else:
                pass