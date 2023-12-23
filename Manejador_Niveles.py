from Nivel_1 import *
from Nivel_2 import *
from Nivel_3 import *

class Manejador_Niveles:
    def __init__(self, pantalla):

        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

    def get_nivel(self, nombre_nivel):

        return self.niveles[nombre_nivel](self._slave)