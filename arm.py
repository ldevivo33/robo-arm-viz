import pygame
import math

class Arm:
    def __init__(self,L1:int ,L2:int):
        self.L1, self.L2 = L1,L2

    def forward_kinematics(self, theta1, theta2):
        #For now, return the two Joint points J1 and J2
        #Going to need equations to calculate this based off L1 & L2.
        #Assuming base is (0,0): 
        J1 = (self.L1 * math.cos(theta1), self.L1 * math.sin(theta1))
        J2 = (J1[0] + self.L2 * math.cos(theta2), J1[1] + self.L2 * math.sin(theta2))

        return J1, J2
    
    def Draw(self, screen, base_position, theta1, theta2):
        J1,J2 = self.forward_kinematics(theta1,theta2)

        #Draw from base to J1, J1 to J2
        pygame.draw.rect(screen, "blue", (base_position[0], base_position[1], self.L1, 200))
        pygame.draw.rect(screen, "red", (base_position[0] + J1[0], base_position[1] + J1[1], self.L2, 20))
        return

myarm = Arm(50,100)
print(f"Arm 1 Length: {myarm.L1}")
print(myarm.forward_kinematics(0,0))

