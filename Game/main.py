import pygame
import sys
import PlanetObject
import random as rnd

pygame.init()

size = width, height = 1000, 800
speed = [2, 2]
black = 0, 0, 0
bounce = 1
planetDiameter = 10

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game')

ship = pygame.image.load("1.png")
shiprect = ship.get_rect()

planetList = []
for i in range(0, 10):
    temp = PlanetObject.Planet(rnd.randint(0, width),
                               rnd.randint(0, height),
                               (255, 0, 0))
    planetList.append(temp)

running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('speed: ' + str(speed))
            sys.exit()
    keys = pygame.key.get_pressed()

    for p in planetList:
        pygame.draw.circle(screen, p.color,
                           (p.pos[0], p.pos[1]), planetDiameter)
    pygame.display.update()

    if keys[pygame.K_LEFT]:
        speed[0] -= 1
    if keys[pygame.K_RIGHT]:
        speed[0] += 1
    if keys[pygame.K_DOWN]:
        speed[1] += 1
    if keys[pygame.K_UP]:
        speed[1] -= 1
    shiprect = shiprect.move(speed)
    if shiprect.left < 0 or shiprect.right > width:
        speed[0] = -bounce * speed[0]
    if shiprect.top < 0 or shiprect.bottom > height:
        speed[1] = -bounce * speed[1]
    # Round speed to zero when needed
    if(speed[0] < 0.01 and speed[0] > -0.01):
        speed[0] = 0
    if(speed[1] < 0.01 and speed[1] > -0.01):
        speed[1] = 0

    screen.fill(black)
    screen.blit(ship, shiprect)
    # pygame.display.flip()
