import numpy as np

WIDTH = 10
HEIGHT = 10

class Point:
    """
    Center points of non-is_colliding circles
    """
    def __init__(self):
        self.coordinates = np.random.rand(1, 2) * np.array([WIDTH, HEIGHT])

    def move(self):
        move_val = np.random.rand(1, 2) * np.array([3, 3])  # 3 is the move intensity
        self.coordinates += move_val
