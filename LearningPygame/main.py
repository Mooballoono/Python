import pygame
import os

(numpass,numfail) = pygame.init()
print("Pygame Modules enabled: " + str(numpass))

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Not Resizable")
color = (0,100,100)
screen.fill(color)
pygame.display.flip()
running = True
x = 60
y = 60
xv = 0
yv = 0
while running:

    screen.fill(color)

    if x >= 740 and xv > 0:
        xv = 0
        x = 740
    elif x <= 0 and xv < 0:
        xv = 0
        x = 0
    else: x += xv/1000

    if y >= 540 and yv > 0:
        yv = 0
        y = 540
    elif y <= 0 and yv < 0:
        yv = 0
        y = 0
    else: y += yv/1000

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            os.system('cls')

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if yv > -1000: yv -= 1
        if yv > 0: yv -= 1
    elif keys[pygame.K_s]:
        if yv < 1000: yv += 1
        if yv < 0: yv += 1
    else: 
        if yv > 0: yv -= 1
        if yv < 0: yv += 1

    if keys[pygame.K_a]:
        if xv > -1000: xv -= 1
        if xv > 0: xv -= 1
    elif keys[pygame.K_d]:
        if xv < 1000: xv += 1
        if xv < 0: xv += 1
    else:
        if xv > 0: xv -= 1
        if xv < 0: xv += 1
    
            

    