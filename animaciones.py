import pygame

# FUNCIONES PARA IMÁGENES

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        imagen = pygame.transform.flip(imagen, flip_x, flip_y)
        lista_girada.append(imagen)

    return lista_girada

def escalar_imagenes(lista_animaciones, ancho, alto):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (ancho, alto))

    return lista_animaciones

# FUNCIONES CONSTRUCTORAS

def crear_plataforma(ancho, alto, x, y, es_visible, path=None):

    plataforma = {}

    if es_visible and path is not None:
        plataforma["imagen"] = pygame.image.load(path)
        plataforma["imagen"] = pygame.transform.scale(plataforma["imagen"], (ancho, alto))
    else:
        plataforma["imagen"] = pygame.Surface((ancho, alto))

    plataforma["rectangulo"] = plataforma["imagen"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma

def obtener_rectangulos_plataformas(plataforma):

    diccionario = {}

    # Rectángulo bottom 
    diccionario["bottom"] = pygame.Rect(plataforma["rectangulo"].left, plataforma["rectangulo"].bottom - 10, plataforma["rectangulo"].width, 10)
    # Rectángulo top 
    diccionario["top"] = pygame.Rect(plataforma["rectangulo"].left, plataforma["rectangulo"].top, plataforma["rectangulo"].width, 10)
    # Rectángulo left 
    diccionario["left"] = pygame.Rect(plataforma["rectangulo"].left, plataforma["rectangulo"].top, 10, plataforma["rectangulo"].height)
    # Rectángulo right 
    diccionario["right"] = pygame.Rect(plataforma["rectangulo"].right - 10, plataforma["rectangulo"].top, 10, plataforma["rectangulo"].height)

    return diccionario

def dibujar_rectangulos_plataformas(lista_plataformas, pantalla):

    for plataforma in lista_plataformas:
        pygame.draw.rect(pantalla, "black", plataforma["rectangulo"], 3)

        rectangulos_plataforma = obtener_rectangulos_plataformas(plataforma)
        pygame.draw.rect(pantalla, "yellow", rectangulos_plataforma["bottom"], 3)
        pygame.draw.rect(pantalla, "yellow", rectangulos_plataforma["top"], 3)
        pygame.draw.rect(pantalla, "yellow", rectangulos_plataforma["left"], 3)
        pygame.draw.rect(pantalla, "yellow", rectangulos_plataforma["right"], 3)

# ANIMACIONES

# Cuphead quieto DERECHA
Cuphead_idle = [pygame.image.load(r"Plataform Game\Cuphead_Img\0.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\1.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\2.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\3.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\4.png")]

# Cuphead quieto IZQUIERDA
Cuphead_idle_left = girar_imagenes(Cuphead_idle, True, False)

# Cuphead camina DERECHA
Cuphead_walk = [pygame.image.load(r"Plataform Game\Cuphead_Img\13.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\14.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\15.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\16.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\17.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\18.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\19.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\20.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\21.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\22.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\23.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\24.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\25.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\26.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\27.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\28.png")]

# Cuphead camina IZQUIERDA
Cuphead_walk_left = girar_imagenes(Cuphead_walk, True, False)

# Cuphead salta DERECHA
Cuphead_jump = [pygame.image.load(r"Plataform Game\Cuphead_Img\5.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\6.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\7.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\8.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\9.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\10.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\11.png"),
                pygame.image.load(r"Plataform Game\Cuphead_Img\12.png"),]

# Cuphead salta IZQUIERDA
Cuphead_jump_left = girar_imagenes(Cuphead_jump, True, False)

# Cuphead dispara DERECHA
Cuphead_idle_shoot = [pygame.image.load(r"Plataform Game\Cuphead_Img\31.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\32.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\33.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\34.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\35.png")]

# Cuphead dispara IZQUIERDA
Cuphead_idle_shoot_left = girar_imagenes(Cuphead_idle_shoot, True, False)

# Cuphead dispara camina
Cuphead_run_shoot = [pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_01.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_02.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_03.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_04.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_05.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_06.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_07.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_08.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_09.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_10.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_11.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_12.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_13.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_14.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_15.png"),
                    pygame.image.load(r"Plataform Game\Cuphead_Img\cuphead_run_shoot_16.png")]

# Cuphead dispara camina IZQUIERDA
Cuphead_run_shoot_left = girar_imagenes(Cuphead_run_shoot, True, False)

# Enemigo "Arándano Molesto" camina IZQUIERDA
Blueberry_walk = [pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_01.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_02.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_03.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_04.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_05.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_06.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_run_07.png")]

# Enemigo "Arándano Molesto" camina DERECHA
Blueberry_walk_right = girar_imagenes(Blueberry_walk, True, False)

# Enemigo "Arándano Molesto" MUERE
Blueberry_dead = [pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_01.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_02.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_03.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_04.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_05.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_06.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_07.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_08.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_09.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_10.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_11.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_12.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\blob_melt_13.png")]

# Enemigo "Margarita Molesta" camina IZQUIERDA
Daisy_walk = [pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_01.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_02.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_03.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_04.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_05.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_06.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_run_07.png")]

# Enemigo "Margarita Molesta" camina DERECHA
Daisy_walk_right = girar_imagenes(Daisy_walk, True, False)

# Enemigo "Margarita Molesta" MUERE
Daisy_dead = [pygame.image.load(r"Plataform Game\Enemigos_Img\daisy_explote.png")]

# Moneda
Coins = [pygame.image.load(r"Plataform Game\Items\1.png"),
        pygame.image.load(r"Plataform Game\Items\2.png"),
        pygame.image.load(r"Plataform Game\Items\3.png"),
        pygame.image.load(r"Plataform Game\Items\4.png"),
        pygame.image.load(r"Plataform Game\Items\5.png"),
        pygame.image.load(r"Plataform Game\Items\6.png"),
        pygame.image.load(r"Plataform Game\Items\7.png"),
        pygame.image.load(r"Plataform Game\Items\8.png"),
        pygame.image.load(r"Plataform Game\Items\9.png"),
        pygame.image.load(r"Plataform Game\Items\10.png"),
        pygame.image.load(r"Plataform Game\Items\11.png"),
        pygame.image.load(r"Plataform Game\Items\12.png"),
        pygame.image.load(r"Plataform Game\Items\13.png"),
        pygame.image.load(r"Plataform Game\Items\14.png"),
        pygame.image.load(r"Plataform Game\Items\15.png"),
        pygame.image.load(r"Plataform Game\Items\16.png")]

# Vida (Cubos de azúcar)
Health = [pygame.image.load(r"Plataform Game\Items\coffee.png")]
for i in range(len(Health)):
    Health[i] = pygame.transform.scale(Health[i], (60, 75))

# Trampa
Pink_spiker = [pygame.image.load(r"Plataform Game\Trampas\pink_spiker_01.png"),
            pygame.image.load(r"Plataform Game\Trampas\pink_spiker_02.png"),
            pygame.image.load(r"Plataform Game\Trampas\pink_spiker_03.png"),
            pygame.image.load(r"Plataform Game\Trampas\pink_spiker_04.png"),
            pygame.image.load(r"Plataform Game\Trampas\pink_spiker_05.png"),
            pygame.image.load(r"Plataform Game\Trampas\pink_spiker_06.png")]

# Enemigo "Hongo" QUIETO
Hongo = [pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_01.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_02.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_03.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_04.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_05.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_05.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_04.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_03.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_02.png"),
        pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_idle_01.png")]

# Enemigo "Hongo" MUERE
Hongo_dead = [pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_popout_01.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_popout_02.png"),
            pygame.image.load(r"Plataform Game\Enemigos_Img\mushroom_popout_03.png")]

# Enemigo "Bellota" IZQUIERDA
Bellota_walk = [pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0001.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0002.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0003.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0004.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0005.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0006.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0007.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0008.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0009.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0010.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\acorn_fly_0011.png")]

Bellota_walk_right = girar_imagenes(Bellota_walk, True, False)

# Enemigo "Bellota" MUERE
Bellota_dead = [pygame.image.load(r"Plataform Game\Enemigos_Img\puff_01.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\puff_02.png"),
                pygame.image.load(r"Plataform Game\Enemigos_Img\puff_03.png")]

# BOSS "Grim Matchstick" VUELA IZQUIERDA 
Grim_Matchstick_fly = [pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0001.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0002.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0003.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0004.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0005.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0006.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0007.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0008.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0009.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0010.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0011.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0012.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0013.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0014.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0015.png"),
                        pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_idle_0016.png")]

# BOSS "Grim Matchstick" ATAQUE FASE 1
Grim_Matchstick_attack_1 = [pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0001.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0002.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0003.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0004.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0005.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0006.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0007.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0008.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0009.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0010.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0011.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0012.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0013.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0014.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0015.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_peashot_idle_0016.png")]

# BOSS "Grim Matchstick" ARCOS DE LUZ ROSAS
Pink_Rings = [pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0001.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0002.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0003.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0004.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0005.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0006.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0007.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_pink_0008.png")]

# BOSS "Grim Matchstick" ARCOS DE LUZ VERDES
Green_Rings = [pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0001.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0002.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0003.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0004.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0005.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0006.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0007.png"),
            pygame.image.load(r"Plataform Game\Boss_Fase_1_Img\dragon_ph1_psychic_eye_attack_ring_0008.png")]

# BOSS "Grim Matchstick" ATAQUE FASE 2
Grim_Matchstick_attack_2 = [pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0001.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0002.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0003.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0004.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0005.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0006.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0007.png"),
                            pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\dragon_meteor_forward_0008.png"),]

# BOSS "Grim Matchstick" METEORITOS
Meteors = [pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0001.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0002.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0003.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0004.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0005.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0006.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0007.png"),
        pygame.image.load(r"Plataform Game\Boss_Fase_2_Img\meteor_0008.png")]

# Configuración Sprites

lista_animaciones_cuphead = [Cuphead_idle, Cuphead_idle_left, Cuphead_walk, Cuphead_walk_left, Cuphead_jump, Cuphead_jump_left, Cuphead_idle_shoot, Cuphead_idle_shoot_left,
                            Cuphead_run_shoot, Cuphead_run_shoot_left]

diccionario = {}
diccionario["quieto"] = Cuphead_idle
diccionario["quieto_izquierda"] = Cuphead_idle_left
diccionario["derecha"] = Cuphead_walk
diccionario["izquierda"] = Cuphead_walk_left
diccionario["salta"] = Cuphead_jump
diccionario["salta_izquierda"] = Cuphead_jump_left
diccionario["dispara"] = Cuphead_idle_shoot
diccionario["dispara_izquierda"] = Cuphead_idle_shoot_left
diccionario["dispara_corriendo"] = Cuphead_run_shoot
diccionario["dispara_corriendo_izquierda"] = Cuphead_run_shoot_left