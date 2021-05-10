class Player:
    def __init__(self, limit_x, limit_y):
        self.limit_x = limit_x
        self.limit_y = limit_y
        self.token = '🟨'

    def spawn(self, x, y, direction):
        self.alive = True
        self.vel = 1
        self._x = x
        self._y = y
        self.direction = direction
        self._tail = []

    def head(self):
        return self._x, self._y

    def tail(self):
        return self._tail

    def set_direction(self, direction):
        if direction:
            self.direction = direction

    def grow(self):
        self._tail.append(self.head())

    def update(self, frame):

        if (frame % 3 == 0):
            # update tail
            self._tail.insert(0, self.head())
            self._tail.pop()

            #  update head
            if self.direction == 'UP':
                self._y += self.vel
                if self._y >= self.limit_y:
                    self._y = 0
            elif self.direction == 'LEFT':
                self._x -= self.vel
                if self._x < 0:
                    self._x = self.limit_x - 1
            elif self.direction == 'DOWN':
                self._y -= self.vel
                if self._y < 0:
                    self._y = self.limit_y - 1
            elif self.direction == 'RIGHT':
                self._x += self.vel
                if self._x >= self.limit_x:
                    self._x = 0
            if self.head() in self.tail():
                self.alive = False
