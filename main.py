import pygame
from arm import Arm
from angle_diff import angle_diff

pygame.init()

window = pygame.display.set_mode(size=(500,500))

clock = pygame.time.Clock()

myarm = Arm(150,150)

theta1_current, theta2_current = 0,0
theta1_target, theta2_target = None, None

target_pos = None

k = 0.05

BASE_POSITION = (250,250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            target_pos = pygame.mouse.get_pos()
            theta1_target, theta2_target = myarm.solve_ik(target_pos[0], target_pos[1], BASE_POSITION)
        if event.type == pygame.KEYDOWN:
            target_pos = None
            theta1_target, theta2_target = None, None

    window.fill("grey")

    if target_pos and theta1_target and theta2_target:
        pygame.draw.circle(window, "red", target_pos, 15)
        theta1_current += k * angle_diff(theta1_current,theta1_target)
        theta2_current += k * angle_diff(theta2_current,theta2_target)
    else:
        theta1_current += .01
        theta2_current += .3

    myarm.Draw(window, BASE_POSITION, theta1_current, theta2_current)
       
    pygame.display.flip()
    clock.tick(60)


