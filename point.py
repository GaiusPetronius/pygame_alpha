from enum import IntEnum
import random


class PointType(IntEnum):
    Score = 1
    Speed = 2
    Size = 3


class Point:
    def __init__(self, x_pos, y_pos):
        self.type = PointType(random.randint(1, 3))
        self.size = random.randint(20, 40)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_color(self):
        colors_map = {
            1: (255, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 255)
        }
        return colors_map.get(self.type, (100, 100, 100))