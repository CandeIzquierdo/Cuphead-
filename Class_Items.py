from animaciones import *

class Items:
    def __init__(self, animaciones, pos_x, pos_y):
        self.animaciones = animaciones
        self.rectangulo = self.animaciones["gira"][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.animacion_actual = self.animaciones["gira"]
        self.frame_actual = 0

    def animar(self, pantalla):

        self.frame_actual = (self.frame_actual + 1) % len(self.animacion_actual)
        pantalla.blit(self.animacion_actual[self.frame_actual], self.rectangulo)

    @staticmethod
    def crear_lista_monedas(posiciones):

        diccionario_monedas = {}
        diccionario_monedas["gira"] = Coins

        lista_monedas = []
        for pos_x, pos_y in posiciones:
            nueva_moneda = Items(diccionario_monedas, pos_x, pos_y)
            lista_monedas.append(nueva_moneda)

        return lista_monedas

    def dibujar_rectangulo_monedas(lista_monedas, pantalla):

        for moneda in lista_monedas:
            pygame.draw.rect(pantalla, "orange", moneda.rectangulo, 3)

    @staticmethod
    def crear_lista_vidas(posiciones):

        diccionario_vidas = {}
        diccionario_vidas["gira"] = Health

        lista_vidas = []
        for pos_x, pos_y in posiciones:
            vida_extra = Items(diccionario_vidas, pos_x, pos_y)
            lista_vidas.append(vida_extra)

        return lista_vidas

    def dibujar_rectangulo_vidas(lista_vidas, pantalla):

        for vida in lista_vidas:
            pygame.draw.rect(pantalla, "purple", vida.rectangulo, 3)