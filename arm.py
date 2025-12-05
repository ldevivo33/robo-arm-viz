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
        J2 = (J1[0] + self.L2 * math.cos(theta1+theta2), J1[1] + self.L2 * math.sin(theta1+theta2))

        return J1, J2
    
    def Draw(self, screen, base_position, theta1, theta2):
        J1_offset , J2_offset = self.forward_kinematics(theta1,theta2)
        
        J0 = (int(base_position[0]), int(base_position[1]))
        J1 = (int(J1_offset[0] + base_position[0]), int(base_position[1] - J1_offset[1]))
        J2 = (int(J2_offset[0] + base_position[0]), int(base_position[1] - J2_offset[1]))

        #Draw from base to J1, J1 to J2
        pygame.draw.line(screen, "orange", J0,J1, width = 8)
        pygame.draw.line(screen, "blue", J1, J2, width = 8)
        return

    def solve_ik(self, target_x, target_y, base_position):
        x, y = target_x - base_position[0], base_position[1] - target_y
        r = math.sqrt(x ** 2 + y ** 2)

        if r > self.L1 + self.L2:
            raise ValueError(f"Dist to Target: {r} Arm Length: {self.L1 + self.L2}")

        elif r < abs(self.L1 - self.L2):
            raise ValueError("The arm is too long!")

        theta2 = math.acos((r ** 2 - self.L1 ** 2 - self.L2 ** 2)/(2* self.L1 * self.L2))
        
        psi = math.atan2(self.L2 * math.sin(theta2), self.L1 + self.L2 * math.cos(theta2))
        phi = math.atan2(y,x)
        #Assuming plus! neglecting minus (accepting elbow up for now...)
        theta1 = phi - psi

        return theta1, theta2

#TEST solve_ik
#my_arm = Arm(10,10)
#theta1, theta2 = my_arm.solve_ik(1,1)
#print(my_arm.forward_kinematics(theta1, theta2))
