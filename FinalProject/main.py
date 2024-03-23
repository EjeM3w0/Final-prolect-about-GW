import pygame
import pgzrun
import random

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

icon = pygame.image.load("images/test_char.jpg")
pygame.display.set_icon(icon)

char = pygame.image.load("images/test_char.png")

bg = pygame.image.load("images/bg.png")

pygame.display.set_caption("FinalProject")

myfont = pygame.font.Font("fonts/ofont.ru_Rostov.ttf", 40)
text = myfont.render("гав", False, "white")

player_x = 960   #350
player_y = 540   #300

gaw = pygame.mixer.Sound("sounds/gaw.mp3")

dws = [
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
    pygame.image.load("images/dw.png"),
    pygame.image.load("images/dw2.png"),
]

dws_count = False

running = True
while running:

    keys = pygame.key.get_pressed()

    clock.tick(7)

    screen.blit(bg, (0, 0))
    screen.blit(char, (player_x, player_y))

    if player_y == 480 and player_x == 960:
        dws_count = True
        screen.blit(dws[dws_count], (640, 740))
        if dws_count:
            screen.blit(text, (820, 800))
            gaw.play(loops=0, maxtime=1000, fade_ms=100)
            #dws_count += 1
            #if dws_count == 13:
            #    dws_count = False


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= 60
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += 60
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= 60
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += 60
    elif keys[pygame.K_e]:
        gaw.play(0, 1, 0)
    elif player_x <= 300:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= 0
    elif player_y <= 300:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= 0


    pygame.display.update()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()