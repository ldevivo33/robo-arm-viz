import math

def angle_diff(current, target):
    diff = target - current

    diff = (diff+math.pi) % (2 * math.pi) - math.pi

    return diff

def reset_target(theta1_target, theta2_target):
    theta1_target, theta2_target = None, None
    return theta1_target, theta2_target
