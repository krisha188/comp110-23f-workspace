import pygame, sys 
import random 

CREAM = (225, 225, 215)
RED = (238, 0, 0)

pygame.init()
pygame.mouse.set_visible(False)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

curtain = pygame.image.load("curtain.jpg")
resized_image = pygame.transform.scale(curtain, (width/6, height/6))
goal = pygame.Rect(534, 0, 106, 80)

player = pygame.Rect(0, 0, 20, 20)
enemy_kid = pygame.image.load("scary.jpg")
resized_image2 = pygame.transform.scale(enemy_kid, (50, 50))

rand1 = random.randint(0,500)
rand1_1 = random.randint(0,400)
rand2 = random.randint(0,500)
rand2_2 = random.randint(0,400)
rand3 = random.randint(0,500)
rand3_3 = random.randint(0,400)
rand4 = random.randint(0,500)
rand4_4 = random.randint(0,400)
rand5 = random.randint(0,500)
rand5_5 = random.randint(0,400)
rand6 = random.randint(0,500)
rand6_6 = random.randint(0,400)
rand7 = random.randint(0,500)
rand7_7 = random.randint(0,400)
rand8 = random.randint(0,500)
rand8_8 = random.randint(0,400)
rand9 = random.randint(0,500)
rand9_9 = random.randint(0,400)
rand10 = random.randint(0,500)
rand10_10 = random.randint(0,400)


enemy1 = pygame.Rect(rand1, rand1_1, 50, 50)
enemy2 = pygame.Rect(rand2, rand2_2, 50, 50)
enemy3 = pygame.Rect(rand3, rand3_3, 50, 50)
enemy4 = pygame.Rect(rand4, rand4_4, 50, 50)
enemy5 = pygame.Rect(rand5, rand5_5, 50, 50)
enemy6 = pygame.Rect(rand6, rand6_6, 50, 50)
enemy7 = pygame.Rect(rand7, rand7_7, 50, 50)
enemy8 = pygame.Rect(rand8, rand8_8, 50, 50)
enemy9 = pygame.Rect(rand9, rand9_9, 50, 50)
enemy10 = pygame.Rect(rand10, rand10_10, 50, 50)

enemy_image1 = pygame.Rect(rand1, rand1_1, 50, 50)
enemy_image2 = pygame.Rect(rand2, rand2_2, 50, 50)
enemy_image3 = pygame.Rect(rand3, rand3_3, 50, 50)
enemy_image4 = pygame.Rect(rand4, rand4_4, 50, 50)
enemy_image5 = pygame.Rect(rand5, rand5_5, 50, 50)
enemy_image6 = pygame.Rect(rand6, rand6_6, 50, 50)
enemy_image7 = pygame.Rect(rand7, rand7_7, 50, 50)
enemy_image8 = pygame.Rect(rand8, rand8_8, 50, 50)
enemy_image9 = pygame.Rect(rand9, rand9_9, 50, 50)
enemy_image10 = pygame.Rect(rand10, rand10_10, 50, 50)


running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    
    screen.fill(CREAM)

    if player.colliderect(goal):
        print("YOU WON!")
        running = False

    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, goal)
    pygame.draw.rect(screen, RED, enemy1)
    pygame.draw.rect(screen, RED, enemy2)
    pygame.draw.rect(screen, RED, enemy3)
    pygame.draw.rect(screen, RED, enemy4)
    pygame.draw.rect(screen, RED, enemy5)
    pygame.draw.rect(screen, RED, enemy6)
    pygame.draw.rect(screen, RED, enemy7)
    pygame.draw.rect(screen, RED, enemy8)
    pygame.draw.rect(screen, RED, enemy9)
    pygame.draw.rect(screen, RED, enemy10)

    pygame.Surface.blit(screen, resized_image2, (rand1, rand1_1))
    pygame.Surface.blit(screen, resized_image2, (rand2, rand2_2))
    pygame.Surface.blit(screen, resized_image2, (rand3, rand3_3))
    pygame.Surface.blit(screen, resized_image2, (rand4, rand4_4))
    pygame.Surface.blit(screen, resized_image2, (rand5, rand5_5))
    pygame.Surface.blit(screen, resized_image2, (rand6, rand6_6))
    pygame.Surface.blit(screen, resized_image2, (rand7, rand7_7))
    pygame.Surface.blit(screen, resized_image2, (rand8, rand8_8))
    pygame.Surface.blit(screen, resized_image2, (rand9, rand9_9))
    pygame.Surface.blit(screen, resized_image2, (rand10, rand10_10))



    if player.colliderect(enemy1):
        running = False
    if player.colliderect(enemy2):
        running = False
    if player.colliderect(enemy3):
        running = False
    if player.colliderect(enemy4):
        running = False
    if player.colliderect(enemy5):
        running = False
    if player.colliderect(enemy6):
        running = False
    if player.colliderect(enemy7):
        running = False
    if player.colliderect(enemy8):
        running = False
    if player.colliderect(enemy9):
        running = False
    if player.colliderect(enemy10):
        running = False


    pygame.Surface.blit(screen, resized_image, (530, 0))

    player.center = pygame.mouse.get_pos()

    pygame.display.flip()

    
