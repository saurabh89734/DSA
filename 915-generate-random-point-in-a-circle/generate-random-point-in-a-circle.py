import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        theta = random.random() * 2 * math.pi
        r = self.radius * math.sqrt(random.random())

        x = self.x + r * math.cos(theta)
        y = self.y + r * math.sin(theta)

        return [x, y]