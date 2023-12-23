import pygame, sys
from animaciones import * 
from Class_Personaje import *
from modo import *
from Class_Enemigo import *
from Class_Disparo import *
from Class_Items import *
from funciones import mostrar_cronometro, actualizar_cronometro

pygame.init()

# Configuración Ventana Pygame

ANCHO = 1650
ALTO = 900
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Cuphead")

ICONO = pygame.image.load(r"Plataform Game\Ambiente\icono.png")
pygame.display.set_icon(ICONO)

EXIT = pygame.image.load(r"Plataform Game\Ambiente\exit.png")

FONDO = pygame.image.load(r"Plataform Game\Ambiente\fondo4.jpg")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))

BOX_AZUL = pygame.image.load(r"Plataform Game\Ambiente\box_blue.PNG")
BOX_AZUL = pygame.transform.scale(BOX_AZUL, (180,60))

ICONO_VIDA = pygame.image.load(r"Plataform Game\Items\cubo_azucar.png")
ICONO_VIDA = pygame.transform.scale(ICONO_VIDA, (60,45))

reloj = pygame.time.Clock()
FPS = 30

Cuphead = Personaje(diccionario, (100, 100), 380,600, 5)

# Configuración Plataformas

piso = crear_plataforma(ANCHO, 10, 0, 890, True)
piso["rectangulo"].top = Cuphead.rectangulo_principal.bottom

plataforma_hongo1 = crear_plataforma(150, 100, 740, 180, True, r"Plataform Game\Ambiente\plataforma.png")
plataforma_tierra = crear_plataforma(350, 120, 100, 280, True, r"Plataform Game\Ambiente\plataforma5.png")
plataforma_tierra2 = crear_plataforma(350, 120, 1200, 280, True, r"Plataform Game\Ambiente\plataforma5.png")

plataformas = [piso, plataforma_hongo1, plataforma_tierra, plataforma_tierra2]

# Configuración Plataforma Movible

direccion_plataforma = 1
velocidad_plataforma = 4

# Configuración Disparo

bandera_disparo = False
tiempo_ultimo_disparo = 0

# Configuración Enemigos

lista_enemigos = Enemigo.crear_lista(piso, Cuphead)

# Configuración Items

posiciones_monedas = [(160,180), (320,180), (1270,180), (1440,180), (790,180), (790,300), (790,60)]
lista_monedas = Items.crear_lista_monedas(posiciones_monedas)
posiciones_vidas = [(30,30)]
lista_vidas = Items.crear_lista_vidas(posiciones_vidas)

# Configuración Cronómetro

tiempo_inicial = pygame.time.get_ticks()
duracion_total = 90 * 1000

# Bucle

bandera = True
while bandera:
    reloj.tick(FPS)

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_restante = max((duracion_total - tiempo_transcurrido) // 1000, 0)

    if tiempo_restante <= 0:
        bandera = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    if bandera:
        keys = pygame.key.get_pressed()

        # MOVIMIENTO / QUIETO
    if keys[pygame.K_a]:
        Cuphead.que_hace = "izquierda"
        bandera_disparo = True
    elif keys[pygame.K_d]:
        Cuphead.que_hace = "derecha"
        bandera_disparo = True
    else:
        Cuphead.que_hace = "quieto"
        bandera_disparo = True

        # SALTO
    if keys[pygame.K_SPACE]:
        Cuphead.que_hace = "salta"
        bandera_disparo = True

        # DISPARO
    if bandera_disparo == True and keys[pygame.K_f]:

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_ultimo_disparo >= 100:
            Cuphead.lanzar_proyectil()

            for enemigo in lista_enemigos:
                enemigo.verificar_colision_disparo(Cuphead.lista_proyectiles)
            bandera_disparo = False
            tiempo_ultimo_disparo = tiempo_actual

        # PLATAFORMA MOVIBLE
    plataforma_hongo1["rectangulo"].y += velocidad_plataforma * direccion_plataforma

    # Verifico si la plataforma llega a ciertos límites para cambiar la dirección
    if plataforma_hongo1["rectangulo"].y <= 120:  # Límite superior
        direccion_plataforma = 1  # Cambia la dirección hacia abajo
    elif plataforma_hongo1["rectangulo"].y >= 660:  # Límite inferior
        direccion_plataforma = -1  # Cambia la dirección hacia arriba

    Cuphead.rectangulo_principal.y += 15 # Hago esto con la intencion de que el bottom de Cuphead no "flote" en las plataformas, ya que
                                        # debido a su animación constante "flota", por lo tanto, hago que su rect 'Y' incremente 15 valores más.

    PANTALLA.blit(FONDO, (0,0))
    PANTALLA.blit(BOX_AZUL, (720,0))
    PANTALLA.blit(BOX_AZUL, (10,0))
    PANTALLA.blit(BOX_AZUL, (1450,0))
    PANTALLA.blit(ICONO_VIDA, (1480, 5))
    Cuphead.colocar_vidas_pantalla(PANTALLA)
    mostrar_cronometro(tiempo_restante // 60, tiempo_restante % 60, PANTALLA)
    PANTALLA.blit(EXIT, (1500, 600))
    PANTALLA.blit(plataforma_hongo1["imagen"], plataforma_hongo1["rectangulo"])
    PANTALLA.blit(plataforma_tierra["imagen"], plataforma_tierra["rectangulo"])
    PANTALLA.blit(plataforma_tierra2["imagen"], plataforma_tierra2["rectangulo"])

    for moneda in lista_monedas:
        moneda.animar(PANTALLA)

    for enemigo in lista_enemigos:
        if not enemigo.esta_muriendo and not enemigo.esta_muerto:
            enemigo.actualizar(PANTALLA)

    for enemigo in lista_enemigos:
        if enemigo.esta_muerto:
            enemigo.animar(PANTALLA)
            lista_enemigos.remove(enemigo)
            del enemigo
            break

    Cuphead.actualizar(PANTALLA, plataformas)
    Cuphead.verificar_colision_monedas(PANTALLA, lista_monedas)
    Cuphead.verificar_colision_vidas(lista_vidas)
    rectangulos_cuphead = Cuphead.obtener_rectangulos_cuphead()
    Cuphead.actualizar_proyectiles(PANTALLA)
    Cuphead.verificar_colision_enemigo(PANTALLA, lista_enemigos)
    Cuphead.verificar_daño_enemigos(lista_enemigos)

    if get_mode() == True:

        Items.dibujar_rectangulo_monedas(lista_monedas, PANTALLA)

        Personaje.dibujar_rectangulos_cuphead(Cuphead, PANTALLA)
        
        dibujar_rectangulos_plataformas(plataformas, PANTALLA)

        Enemigo.dibujar_rectangulos_enemigos(lista_enemigos, PANTALLA)

    pygame.display.update()