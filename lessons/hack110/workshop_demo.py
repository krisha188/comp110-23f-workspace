import pygame, sys
import random

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

blue = (51, 153, 255)
red = (240, 20, 20)
gold = (255, 204, 0)

pygame.init()

clock = pygame.time.Clock()

player = pygame.Rect(5, height/2, 100, 100)

obstacle_top = pygame.Rect(0, -25, width, height/2)
obstacle_bottom = pygame.Rect(0, height/2 + 150, width, height/2)

obstacle_list = [obstacle_top, obstacle_bottom]

goal = pygame.Rect(width - 75, height/2, 50, 50)

running = True

pygame.mouse.set_visible(False)

colission_count = 0
coin_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(blue)

    pygame.draw.circle(screen, gold, goal)

    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, red, obstacle_top)
    pygame.draw.rect(screen, red, obstacle_bottom)

    for obstacle in obstacle_list:
        if player.colliderect(obstacle):
            pygame.mouse.set_pos(5, height/2)
            colission_count += 1
            if colission_count == 100:
                running = False

    if player.colliderect(goal):
        coin_count += 1
        goal.centerx = random.randint(75, width - 75)
        if coin_count == 10:
            print("YOU WON!")
            running = False

    player.center = pygame.mouse.get_pos()

    pygame.display.flip()

    clock.tick(60)