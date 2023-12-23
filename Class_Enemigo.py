from animaciones import *
from Class_Disparo import *
from Class_Personaje import *
from sonidos import *

class Enemigo:
    def __init__(self, animaciones, personaje, pos_x=0, pos_y=0, puede_moverse=False):
        self.animaciones = animaciones
        self.rectangulo = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["izquierda"]
        self.mira_izquierda = True

        self.pasos_izquierda = 25
        self.pasos_derecha = 25

        self.esta_muerto = False
        self.esta_muriendo = False

        self.personaje = personaje

        self.puede_moverse = puede_moverse

    def avanzar(self):

        if self.puede_moverse:
            
            if self.mira_izquierda:
                self.animacion_actual = self.animaciones["izquierda"]
                self.rectangulo.x -= 6
                self.pasos_izquierda -= 1
                if self.pasos_izquierda == 0:
                    self.mira_izquierda = False
                    self.pasos_derecha = 25
            elif not self.mira_izquierda:
                self.animacion_actual = self.animaciones["derecha"]
                self.rectangulo.x += 6
                self.pasos_derecha -= 1
                if self.pasos_derecha == 0:
                    self.mira_izquierda = True
                    self.pasos_izquierda = 25

    def animar(self, pantalla):

        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos +=1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

    def actualizar(self, pantalla):

        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar()

    @staticmethod
    def crear_lista(datos_enemigos, personaje):

        lista_enemigos = []
        for datos in datos_enemigos:
            animaciones_enemigo = {
                "izquierda": datos["animacion_izquierda"],
                "derecha": datos["animacion_derecha"],
                "muere": datos["animacion_muere"]
            }
            
            nuevo_enemigo = Enemigo(animaciones_enemigo, personaje, datos["pos_x"], datos["pos_y"], datos["puede_moverse"])
            lista_enemigos.append(nuevo_enemigo)

        return lista_enemigos

    def obtener_rectangulos_enemigos(self):
        
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

    def dibujar_rectangulos_enemigos(lista_enemigos, pantalla):

        for enemigo in lista_enemigos:
            pygame.draw.rect(pantalla, "red", enemigo.rectangulo, 3)

            rectangulos_enemigo = enemigo.obtener_rectangulos_enemigos()
            pygame.draw.rect(pantalla, "red", rectangulos_enemigo["bottom"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos_enemigo["top"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos_enemigo["left"], 3)
            pygame.draw.rect(pantalla, "red", rectangulos_enemigo["right"], 3)

    def verificar_colision_disparo(self, lista_proyectiles_personaje):

        for disparo in self.personaje.lista_proyectiles:

            if self.rectangulo.colliderect(disparo.rectangulo):
                cuphead_parry()
                self.animacion_actual = self.animaciones["muere"]
                self.esta_muriendo = True
                self.personaje.score += 100
                self.esta_muerto = True
                
    # @staticmethod
    # def crear_lista(piso, personaje):
    #     diccionario_enemigo = {}
    #     diccionario_enemigo["izquierda"] = Blueberry_walk
    #     diccionario_enemigo["derecha"] = Blueberry_walk_right
    #     diccionario_enemigo["muere"] = Blueberry_dead
    #     blueberry = Enemigo(diccionario_enemigo, personaje)
    #     blueberry.rectangulo.bottom = piso["rectangulo"].top

    #     d = {"muerte": diccionario_enemigo["muere"]}

    #     diccionario_enemigo2 = {}
    #     diccionario_enemigo2["izquierda"] = Daisy_walk
    #     diccionario_enemigo2["derecha"] = Daisy_walk_right
    #     diccionario_enemigo2["muere"] = Daisy_dead
    #     daisy = Enemigo(diccionario_enemigo2, personaje)
    #     daisy2 = Enemigo(diccionario_enemigo2, personaje)
    #     daisy.rectangulo.x = 230
    #     daisy.rectangulo.y = 100
    #     daisy2.rectangulo.x = 1400
    #     daisy2.rectangulo.y = 100

    #     lista_enemigos = [blueberry, daisy, daisy2]

    #     return lista_enemigos