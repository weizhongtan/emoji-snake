import emojis

class Player:
    def __init__(self, limit_x, limit_y):
        self.limit_x = limit_x
        self.limit_y = limit_y

    def spawn(self, x, y, direction):
        self.head_token = '🔲'
        self.tail_token = '🔲'
        self.alive = True
        self.vel = 1
        self._x = x
        self._y = y
        self.direction = direction
        self._tail = []
        self._score = 0

    def score(self):
        return self._score

    def head(self):
        return self._x, self._y

    def tail(self):
        return self._tail

    def set_direction(self, direction):
        if direction and (
            direction == 'LEFT' and self.direction != 'RIGHT'
            or direction == 'RIGHT' and self.direction != 'LEFT'
            or direction == 'UP' and self.direction != 'DOWN'
            or direction == 'DOWN' and self.direction != 'UP'
        ):
            self.direction = direction

    def grow(self):
        self._tail.append(self.head())

    def increment_score(self):
        self._score += 1

    def update(self, frame):
        if (frame % 3 == 0):
            # update head
            nx, ny = self._x, self._y
            if self.direction == 'UP':
                ny += self.vel
                if ny >= self.limit_y:
                    ny = 0
            elif self.direction == 'LEFT':
                nx -= self.vel
                if nx < 0:
                    nx = self.limit_x - 1
            elif self.direction == 'DOWN':
                ny -= self.vel
                if ny < 0:
                    ny = self.limit_y - 1
            elif self.direction == 'RIGHT':
                nx += self.vel
                if nx >= self.limit_x:
                    nx = 0

            # revert if dead
            if (nx, ny) in self.tail():
                self.alive = False
                self.head_token = '😵'
                return

            # move start of tail into old head position
            self._tail.insert(0, self.head())

            # remove end of tail
            self._tail.pop()

            # update new head position
            self._x = nx
            self._y = ny
