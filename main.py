import pygame
from arm import Arm
from helpers import angle_diff, reset_target
from collections import deque

pygame.init()

window = pygame.display.set_mode(size=(500,500))

clock = pygame.time.Clock()

myarm = Arm(150,150)

theta1_current, theta2_current = 0,0
theta1_target, theta2_target = None, None

target_pos = None
targets = deque([])

trail = deque([])

k = 0.05

BASE_POSITION = (250,250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            targets.append(pygame.mouse.get_pos())

    window.fill("grey")

    if targets:
        target_pos = targets[0] 
        theta1_target, theta2_target = myarm.solve_ik(target_pos[0], target_pos[1], BASE_POSITION)

    if target_pos and theta1_target and theta2_target:
        for target in targets:
            if target == target_pos:
                COLOR = "red"
            else:
                COLOR = "darksalmon"

            pygame.draw.circle(window, COLOR, target, 15)
            if target == target_pos:
                pygame.draw.circle(window, "darkolivegreen2", target, 3)

        theta1_current += k * angle_diff(theta1_current,theta1_target)
        theta2_current += k * angle_diff(theta2_current,theta2_target)
    else:
        theta1_current += .01
        theta2_current += .3

    end = myarm.Draw(window, BASE_POSITION, theta1_current, theta2_current)
    trail.append(end)
    if len(trail) > 75:
        trail.popleft()
    for i,dot in enumerate(trail):
        pygame.draw.circle(window, "lemonchiffon", dot, 3 - ((200-i) * .01))

    if target_pos and abs(end[0] - target_pos[0]) <= 3 and abs(end[1] - target_pos[1]) <= 3:
        theta1_target, theta2_target = reset_target(theta1_target, theta2_target)
        targets.popleft() 

    pygame.display.flip()
    clock.tick(60)


