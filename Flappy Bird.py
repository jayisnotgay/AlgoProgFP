import pygame
import random
from sys import exit

# Dragon animation function
def dragon_animation():
    global dragon_surf, dragon_index
    dragon_index += 0.2
    if dragon_index >= len(dragon_fly):
        dragon_index = 0
    dragon_surf = dragon_fly[int(dragon_index)]

# Zombie animation function
def zombie_animation():
    global zombie_surf, zombie_index
    zombie_index += 0.2
    if zombie_index >= len(zombie_walk):
        zombie_index = 0
    zombie_surf = zombie_walk[int(zombie_index)]

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/goblin.ttf", 50)

# Game and UI states
game_active = False
game_over = False
shop = False
bird1 = True
bird2bought = False
buyfailed = False
FPS = 60
score = 0
coins = 0

#Menu UI
menu_surf = pygame.image.load("Graphics/main menu.png")
menu_rect = menu_surf.get_rect(topleft=(0, 0))

logo_surf = pygame.image.load("Graphics/flappy bird logo.png")
logo_rect = logo_surf.get_rect(center=(640, 360))

start_surf = font.render("Press space to start", False, "White")
start_rect = start_surf.get_rect(center=(640, 600))

shop_surf = font.render("Shop", False, "White")
shop_rect = shop_surf.get_rect(center=(125, 125))

# Shop UI
bird_shop_surf = pygame.transform.scale(pygame.image.load("Sprites/birdie.png").convert_alpha(),(240,180))
bird2_shop_surf = pygame.transform.scale(pygame.image.load("Sprites/birdie2.png").convert_alpha(),(240,180))
bird_shop_rect = bird_shop_surf.get_rect(center=(420, 360))
bird2_shop_rect = bird2_shop_surf.get_rect(center=(860, 360))

equip_surf = font.render("equip", False, "White")
equipped_surf = font.render("equipped", False, "White")

equipbird_rect = equip_surf.get_rect(center=(370, 500))
equipbird2_rect = equip_surf.get_rect(center=(860, 500))

buy_surf = font.render("buy", False, "White")
buy_rect = buy_surf.get_rect(center=(860, 500))

price_surf = font.render("10 coins", False, "White")
price_rect = price_surf.get_rect(center=(860, 200))

insufficient_surf = font.render("insufficient balance!", False, "White")
insufficient_rect = insufficient_surf.get_rect(center=(640, 600))

back_surf = font.render("Back", False, "White")
back_rect = back_surf.get_rect(center=(640, 50))

# Game UI
sky_surf = pygame.image.load('Graphics/background.png').convert()
sky_rect = sky_surf.get_rect(topleft=(0, 0))

ground_surf = pygame.image.load('Graphics/ground.png').convert_alpha()
ground_rect = ground_surf.get_rect(bottomleft=(0, 750))

coin_surf = pygame.image.load("Sprites/coin.png").convert_alpha()
coin_rect = coin_surf.get_rect(center=(1280, 300))

dragon_fly_1 = pygame.image.load("Sprites/dragon1.png").convert_alpha()
dragon_fly_2 = pygame.image.load("Sprites/dragon2.png").convert_alpha()
dragon_fly_3 = pygame.image.load("Sprites/dragon3.png").convert_alpha()
dragon_fly_4 = pygame.image.load("Sprites/dragon4.png").convert_alpha()
dragon_fly_5 = pygame.image.load("Sprites/dragon5.png").convert_alpha()
dragon_fly = [dragon_fly_1, dragon_fly_2, dragon_fly_3, dragon_fly_4, dragon_fly_5]
dragon_index = 0
dragon_surf = dragon_fly[dragon_index]
dragon_rect = dragon_surf.get_rect(center=(1280, 200))

zombie_walk_1 = pygame.transform.scale(pygame.image.load("Sprites/zombie1.png").convert_alpha(),(198,292.5))
zombie_walk_2 = pygame.transform.scale(pygame.image.load("Sprites/zombie2.png").convert_alpha(),(198,292.5))
zombie_walk_3 = pygame.transform.scale(pygame.image.load("Sprites/zombie3.png").convert_alpha(),(198,292.5))
zombie_walk_4 = pygame.transform.scale(pygame.image.load("Sprites/zombie4.png").convert_alpha(),(198,292.5))
zombie_walk = [zombie_walk_1, zombie_walk_2, zombie_walk_3, zombie_walk_4]
zombie_index = 0
zombie_surf = zombie_walk[zombie_index]
zombie_rect = zombie_surf.get_rect(midbottom=(640, 610))

bird_gravity = 0
bird_surf = pygame.image.load("Sprites/birdie.png").convert_alpha()
bird2_surf = pygame.image.load("Sprites/birdie2.png").convert_alpha()
bird_hitbox = pygame.transform.scale(pygame.image.load("Sprites/birdie.png").convert_alpha(),(25,25))
bird_rect = bird_surf.get_rect(center=(100, 200))
bird_hitbox_rect = bird_hitbox.get_rect(center=(100, 200))

# Game over UI
mainmenu_surf = font.render("Main menu", False, "White")
mainmenu_rect = mainmenu_surf.get_rect(center=(640, 600))

restart_surf = font.render("Restart", False, "White")
restart_rect = restart_surf.get_rect(center=(640, 500))

gameover_surf = pygame.image.load("Graphics/game over.png").convert_alpha()
gameover_rect = gameover_surf.get_rect(center=(640, 360))

# SFX
theme_song = pygame.mixer.Sound("SFX/theme song.wav")
coin_sound = pygame.mixer.Sound("SFX/coin.mp3")
wing_sound = pygame.mixer.Sound("SFX/wing.mp3")
gameover_sound = pygame.mixer.Sound("SFX/game over.mp3")
equip_sound = pygame.mixer.Sound("SFX/equip.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #In game controls
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird_gravity = -20
                    wing_sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and restart_rect.collidepoint(pygame.mouse.get_pos()) and game_over:
                    game_active = True
                    game_over = False
                    gameover_sound.stop()
                    dragon_rect.left = random.randint(1280, 2560)
                    dragon_rect.centery = random.randint(100, 200)
                    zombie_rect.left = random.randint(1280, 2560)
                    coin_rect.left = random.randint(1280, 2560)
                    bird_rect.centerx = 100
                    bird_hitbox_rect.centerx = 100
                    coins += score
                    score = 0
                if mouse_presses[0] and mainmenu_rect.collidepoint(pygame.mouse.get_pos()) and game_over:
                    game_active = False
                    coins += score
                    score = 0
                    bird_rect.centerx = 100
                    bird_hitbox_rect.centerx = 100
        else:
            # Menu Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not shop:
                    game_active = True
                    game_over = False
                    theme_song.stop()
                    dragon_rect.left = random.randint(1280, 2560)
                    dragon_rect.centery = random.randint(100, 200)
                    zombie_rect.left = random.randint(1280, 2560)
                    coin_rect.left = random.randint(1280, 2560)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and shop_rect.collidepoint(pygame.mouse.get_pos()):
                    shop = True
                if mouse_presses[0] and back_rect.collidepoint(pygame.mouse.get_pos()):
                    shop = False
                    buyfailed = False
                if mouse_presses[0] and buy_rect.collidepoint(pygame.mouse.get_pos()) and coins >= 10 and not bird2bought:
                    equip_sound.play()
                    bird2bought = True
                    coins -= 10
                if mouse_presses[0] and buy_rect.collidepoint(pygame.mouse.get_pos()) and coins < 10:
                    buyfailed = True
                    bird1 = True
                if mouse_presses[0] and equipbird_rect.collidepoint(pygame.mouse.get_pos()):
                    bird1 = True
                if mouse_presses[0] and equipbird2_rect.collidepoint(pygame.mouse.get_pos()) and bird2bought:
                    equip_sound.play()
                    bird1 = False

    if game_active:
        screen.blit(sky_surf, sky_rect)
        sky_rect.x -= 3
        if sky_rect.left <= -2560:
            sky_rect.left = 0

        screen.blit(ground_surf, ground_rect)
        ground_rect.x -= 7
        if ground_rect.left <= -2560:
            ground_rect.left = 0

        screen.blit(coin_surf, coin_rect)
        coin_rect.x -= 7
        if coin_rect.right < 0:
            coin_rect.left = random.randint(1280, 2560)
            coin_rect.centery = random.randint(200, 400)

        dragon_animation()
        screen.blit(dragon_surf, dragon_rect)
        dragon_rect.centerx -= 15
        if dragon_rect.right < 0:
            dragon_rect.left = random.randint(1280, 3840)
            dragon_rect.centery = random.randint(100,200)

        zombie_animation()
        screen.blit(zombie_surf, zombie_rect)
        zombie_rect.x -= 15
        if zombie_rect.right < 0:
            zombie_rect.left = random.randint(1280, 3840)

        bird_gravity += 1
        bird_rect.centery += bird_gravity
        bird_hitbox_rect.centery = bird_rect.centery
        if bird_rect.centery >= 550:
            bird_rect.centery = 550
            bird_gravity = 0
        if bird_rect.centery < 10:
            bird_rect.centery = 10
        if bird1:
            bird_surf_physics = pygame.transform.rotate(bird_surf, -bird_gravity)
            screen.blit(bird_hitbox, bird_hitbox_rect)
            screen.blit(bird_surf_physics, bird_rect)
        else:
            bird_surf_physics = pygame.transform.rotate(bird2_surf, -bird_gravity)
            screen.blit(bird_hitbox, bird_hitbox_rect)
            screen.blit(bird_surf_physics, bird_rect)

        screen.blit(coin_surf, (550, 50))

        score_surf = font.render(str(score), False, "White")
        score_rect = score_surf.get_rect(center=(700, 105))
        screen.blit(score_surf, score_rect)

        if 0 < dragon_rect.left-zombie_rect.left < 600:
            dragon_rect.centery -= 3
            dragon_rect.x += 5
        elif 0 < zombie_rect.left-dragon_rect.left < 600:
            dragon_rect.centery -= 3
            zombie_rect.x += 5
        else:
            dragon_rect.centery += random.randint(-1, 3)
            if dragon_rect.centery >= 500:
                dragon_rect.centery = 500

        if dragon_rect.centery < 75:
            dragon_rect.centery = 75

        if bird_hitbox_rect.colliderect(coin_rect):
            coin_sound.play()
            coin_rect.left = random.randint(1280, 2560)
            coin_rect.centery = random.randint(200, 400)
            score += 1

        if bird_hitbox_rect.colliderect(dragon_rect):
            game_over = True

        if bird_hitbox_rect.colliderect(zombie_rect):
            game_over = True

        if game_over:
            bird_rect.centerx -= 7
            bird_hitbox_rect.centerx -= 7
            bird_gravity = 0
            screen.blit(gameover_surf, gameover_rect)
            screen.blit(restart_surf, restart_rect)
            screen.blit(mainmenu_surf, mainmenu_rect)
            gameover_sound.play()

    else:
        gameover_sound.stop()
        if not shop:
            theme_song.play()
            equip_sound.stop()
        screen.blit(menu_surf, menu_rect)
        bird_gravity += 1
        bird_rect.bottom += bird_gravity
        if bird_rect.bottom >= 500:
            bird_gravity = -20
        if bird1:
            bird_surf_physics = pygame.transform.rotate(bird_surf, -bird_gravity)
            screen.blit(bird_surf_physics, bird_rect)
        else:
            bird_surf_physics = pygame.transform.rotate(bird2_surf, -bird_gravity)
            screen.blit(bird_surf_physics, bird_rect)
        screen.blit(logo_surf, logo_rect)
        screen.blit(start_surf, start_rect)
        screen.blit(shop_surf, shop_rect)
        coins_surf = font.render(str(coins), False, "White")
        coins_rect = coins_surf.get_rect(topleft=(100, 25))

        screen.blit(coin_surf, (0, 0))
        screen.blit(coins_surf, coins_rect)

        if shop:
            theme_song.stop()
            screen.blit(menu_surf, menu_rect)
            screen.blit(coin_surf, (0, 0))
            screen.blit(coins_surf, coins_rect)
            screen.blit(bird_shop_surf, bird_shop_rect)
            screen.blit(bird2_shop_surf, bird2_shop_rect)
            screen.blit(back_surf, back_rect)
            if bird2bought:
                if bird1:
                    screen.blit(equipped_surf, equipbird_rect)
                    screen.blit(equip_surf, equipbird2_rect)
                else:
                    screen.blit(equip_surf, equipbird_rect)
                    screen.blit(equipped_surf, equipbird2_rect)
            else:
                screen.blit(equipped_surf, equipbird_rect)
                screen.blit(buy_surf, buy_rect)
                screen.blit(price_surf, price_rect)
                if buyfailed:
                    screen.blit(insufficient_surf, insufficient_rect)

    pygame.display.update()
    clock.tick(FPS)