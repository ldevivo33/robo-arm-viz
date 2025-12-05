import pygame
from arm import Arm

pygame.init()

window = pygame.display.set_mode(size=(500,500))

clock = pygame.time.Clock()

myarm = Arm(150,150)
theta1, theta2 = 0,0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    window.fill("grey")
    myarm.Draw(window, (250,250), theta1, theta2)
    theta1 += .01
    theta2 += .3

    pygame.display.flip()
    clock.tick(60)
