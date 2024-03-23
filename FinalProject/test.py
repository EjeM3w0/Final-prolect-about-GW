player_x = 0
player_y = 0

dws_count = False
timer_running = False

def show_dws():
    screen.blit(dws[dws_count], (640, 740))
    screen.blit(text, (820, 800))
    pygame.display.flip()

def set_timer():
    show_dws()
    pygame.time.set_timer(pygame.USEREVENT, 2000)

clock = pygame.time.Clock()
running = True

while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            timer_running = False

    clock.tick(30)

    screen.blit(bg, (0, 0))
    screen.blit(char, (player_x, player_y))

    if player_y == 480 and player_x == 960 and not timer_running:
        set_timer()
        timer_running = True

    pygame.display.flip()

pygame.quit()

 #

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 960))

player_x = 960
player_y = 480
timer_running = False
image_visible = False
image = pygame.image.load('image.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Условие для отображения картинки
    if player_y == 480 and player_x == 960 and not timer_running and not image_visible:
        image_visible = True
        start_time = time.time()
    
    # Проверка времени отображения картинки
    if image_visible:
        screen.blit(image, (player_x, player_y))
        
        if time.time() - start_time > 2:
            image_visible = False
            timer_running = True
    
    pygame.display.update()