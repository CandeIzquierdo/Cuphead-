import pygame
from modo import *
from Class_Items import *
from Class_Personaje import *
from funciones import mostrar_cronometro
from Class_Enemigo import *
from animaciones import *
from Class_Trampa import *
from Class_Boss import *
from Class_Arcos_Luz import *
from Material_UI.GUI_form import *
from sonidos import *
from Material_UI.top_scores import *

class Nivel:
    def __init__(self, pantalla, personaje, lista_plataformas, lista_enemigos, lista_monedas, lista_vidas, lista_trampas, boss, fondo, reloj):
        self._slave = pantalla
        self.personaje = personaje
        self.plataformas = lista_plataformas
        self.enemigos = lista_enemigos
        self.monedas = lista_monedas
        self.vidas = lista_vidas
        self.trampas = lista_trampas
        self.boss = boss
        self.fondo = fondo
        self.bandera_disparo = False
        self.tiempo_ultimo_disparo = 0

        self.tiempo_inicial = pygame.time.get_ticks()
        self.duracion_total = 3 * 60 * 1000

        self.sonido_checkpoint = False

    def update(self, lista_eventos):

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

    def leer_inputs(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.personaje.que_hace = "izquierda"
            self.bandera_disparo = True
        elif keys[pygame.K_d]:
            self.personaje.que_hace = "derecha"
            self.bandera_disparo = True
        else:
            self.personaje.que_hace = "quieto"
            self.bandera_disparo = True

        if keys[pygame.K_SPACE]:
            self.player_jump()
            self.personaje.que_hace = "salta"
            self.bandera_disparo = True

        if self.bandera_disparo and keys[pygame.K_f]:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo >= 100:
                self.player_fire()
                self.personaje.lanzar_proyectil()
                self.bandera_disparo = False
                self.tiempo_ultimo_disparo = tiempo_actual

                for enemigo in self.enemigos:
                    enemigo.verificar_colision_disparo(self.personaje.lista_proyectiles)
                self.bandera_disparo = False
                self.tiempo_ultimo_disparo = tiempo_actual

    def dibujar_rectangulos(self):

        if get_mode() == True:

            Items.dibujar_rectangulo_monedas(self.monedas, self._slave)

            Items.dibujar_rectangulo_vidas(self.vidas, self._slave)

            Personaje.dibujar_rectangulos_cuphead(self.personaje, self._slave)
            
            dibujar_rectangulos_plataformas(self.plataformas, self._slave)

            Enemigo.dibujar_rectangulos_enemigos(self.enemigos, self._slave)

            Trampa.dibujar_rectangulo_trampa(self.trampas, self._slave)

            Boss.dibujar_rectangulos_boss(self.boss, self._slave)
            
            for boss in self.boss:
                boss.dibujar_rectangulo_ojos(self._slave)
                
                for arco_luz in boss.lista_proyectiles_arcos_luz:
                    arco_luz.dibujar_rectangulo_arcos_luz(self._slave)

    def actualizar(self):

        self._slave.blit(self.fondo, (0,0))

        ICONO_VIDA = pygame.image.load(r"Plataform Game\Items\coffee.png")
        ICONO_VIDA = pygame.transform.scale(ICONO_VIDA, (55,60))

        self._slave.blit(ICONO_VIDA, (1550, 5))

        for plataforma in self.plataformas[1:]:
            self._slave.blit(plataforma["imagen"], plataforma["rectangulo"])
        self.personaje.rectangulo_principal.y += 15 

        self.personaje.actualizar(self._slave, self.plataformas)

        rectangulos_cuphead = self.personaje.obtener_rectangulos_cuphead()
        self.personaje.actualizar_proyectiles(self._slave)
        self.personaje.verificar_colision_enemigo(self._slave, self.enemigos)
        self.personaje.verificar_daño_enemigos(self.enemigos)
        self.personaje.verificar_colision_trampas(self.trampas)

        self.personaje.verificar_colision_vidas(self.vidas)
        self.personaje.verificar_colision_monedas(self._slave, self.monedas)
        self.personaje.colocar_vidas_pantalla(self._slave)

        for moneda in self.monedas:
            moneda.animar(self._slave)

        for vida in self.vidas:
            vida.animar(self._slave)

        for trampa in self.trampas:
            trampa.mover()
            trampa.animar(self._slave)

        for enemigo in self.enemigos:
            if not enemigo.esta_muriendo and not enemigo.esta_muerto:
                enemigo.actualizar(self._slave)

        for enemigo in self.enemigos:
            if enemigo.esta_muerto:
                enemigo.animar(self._slave)
                self.enemigos.remove(enemigo)
                del enemigo
                break

        if self.boss is not None:
            for boss in self.boss:
                boss.actualizar(self._slave)
                if boss.esta_muerto:
                    boss.animar(self._slave)
                    self.boss.remove(boss)
                    del boss
                    break

                for arco_luz in boss.lista_proyectiles_arcos_luz:
                    arco_luz.mover()
                    arco_luz.animar(self._slave)
                
                proyectiles_boss_disparados = boss.lista_proyectiles_arcos_luz[:] 
                self.personaje.verificar_daño_arcosluz(proyectiles_boss_disparados)

    def actualizar_tiempo(self):

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        tiempo_restante = max((self.duracion_total - tiempo_transcurrido), 0)

        minutos = tiempo_restante // 60000
        segundos = (tiempo_restante % 60000) // 1000
        mostrar_cronometro(minutos, segundos, self._slave)

    def mostrar_cronometro(self, minutos, segundos):

        tiempo_formateado = f"Time: {minutos:02}:{segundos:02}"
        fuente = pygame.font.Font("Plataform Game\Bangers-Regular.ttf", 35)  
        texto_tiempo = fuente.render(tiempo_formateado, True, "white") 
        self._slave.blit(texto_tiempo, (740, 10))

    def player_death(self):
        
        pygame.mixer.init()
        sonido_death = pygame.mixer.Sound(r"Plataform Game\Sonidos\Death.mp3")
        sonido_death.set_volume(0.2)
        duracion_sonido = sonido_death.get_length() * 1000  # Duración en milisegundos
        sonido_death.play(maxtime=int(duracion_sonido))

    def verificar_tiempo_agotado(self):

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        return tiempo_transcurrido >= self.duracion_total

    def verificar_final_nivel(self):

        if len(self.monedas) == 0 and len(self.enemigos) == 0 and len(self.boss) == 0:
            EXIT = pygame.image.load(r"Plataform Game\Ambiente\exit.png")
            self._slave.blit(EXIT, (1500, 600))
            rectangulo_exit = EXIT.get_rect(topleft=(1500, 600))

            if self.personaje.rectangulo_principal.colliderect(rectangulo_exit):
                self.detener_musica()
                return True
        return False

    def verificar_game_over(self):

        if self.personaje.vidas <= 0 or self.verificar_tiempo_agotado():
            self.player_death()
            return True

    def player_jump(self):

        pygame.mixer.init()
        sonido_cuphead_jump = pygame.mixer.Sound(r"Plataform Game\Sonidos\Player_Jump.mp3")
        sonido_cuphead_jump.set_volume(0.4)
        sonido_cuphead_jump.play()

    def player_fire(self):

        pygame.mixer.init()
        sonido_cuphead_parry = pygame.mixer.Sound(r"Plataform Game\Sonidos\Player_Fire.mp3")
        sonido_cuphead_parry.set_volume(0.2)
        sonido_cuphead_parry.play()

    def checkpoint(self):

        pygame.mixer.init()
        sonido_checkpoint = pygame.mixer.Sound(r"Plataform Game\Sonidos\Checkpoint Sound.mp3")
        sonido_checkpoint.set_volume(0.3)
        sonido_checkpoint.play()

    def detener_musica(self):

        pygame.mixer.stop()

    def calcular_score(self):

        score = 0

        score += len(self.monedas) * 10
        
        score += len(self.enemigos) * 100
        
        score += len(self.boss) * 10

        return score

    def nivel_terminado(self):

        return self.verificar_final_nivel or self.verificar_game_over or self.verificar_tiempo_agotado