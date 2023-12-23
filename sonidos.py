import pygame


def player_damage():
        
    pygame.mixer.init()
    sonido_damage = pygame.mixer.Sound(r"Plataform Game\Sonidos\Player_Damage.mp3")
    sonido_damage.set_volume(0.4)
    sonido_damage.play()

def player_pickup_coin():
        
    pygame.mixer.init()
    sonido_pickup_coin = pygame.mixer.Sound(r"Plataform Game\Sonidos\Coin_PickUp.mp3")
    sonido_pickup_coin.set_volume(0.4)
    sonido_pickup_coin.play()

def player_drink_coffee():
        
    pygame.mixer.init()
    sonido_drink_coffee = pygame.mixer.Sound(r"Plataform Game\Sonidos\Drink_Coffee.mp3")
    sonido_drink_coffee.set_volume(0.4)
    sonido_drink_coffee.play()

def boss_explote():

    pygame.mixer.init()
    sonido_boss_explote = pygame.mixer.Sound(r"Plataform Game\Sonidos\Boss_Explote.mp3")
    sonido_boss_explote.set_volume(0.3)
    sonido_boss_explote.play()

def cuphead_parry():
        
    pygame.mixer.init()
    sonido_cuphead_parry = pygame.mixer.Sound(r"Plataform Game\Sonidos\Cuphead_Parry.mp3")
    sonido_cuphead_parry.set_volume(0.4)
    sonido_cuphead_parry.play()

def knockout():
        
    pygame.mixer.init()
    sonido_knockout = pygame.mixer.Sound(r"Plataform Game\Sonidos\KNOCKOUT!.mp3")
    sonido_knockout.set_volume(0.7)
    sonido_knockout.play()

def boss_shoot():

    pygame.mixer.init()
    sonido_boss_shoot = pygame.mixer.Sound(r"Plataform Game\Sonidos\Boss_shoot.mp3")
    sonido_boss_shoot.set_volume(0.5)
    sonido_boss_shoot.play()