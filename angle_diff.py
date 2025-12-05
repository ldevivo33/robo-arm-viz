import math

def angle_diff(current, target):
    diff = target - current

    diff = (diff+math.pi) % (2 * math.pi) - math.pi

    return diff
