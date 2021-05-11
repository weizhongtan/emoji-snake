import random

class Food:
    def __init__(self, limit_x, limit_y):
        self._limit_x = limit_x
        self._limit_y = limit_y
        self.token = '🍗'

    def position(self):
        return self._x, self._y

    def spawn(self):
        self._x = random.randint(0, self._limit_x - 1)
        self._y = random.randint(0, self._limit_y - 1)

