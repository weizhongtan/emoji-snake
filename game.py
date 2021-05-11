from grid import Grid

class Game:
    def __init__(self, width, height, player, food):
        self.w = width
        self.h = height
        self._frame = 0
        self.p = player
        self.f = food

    def start(self):
        self.spawn_player()
        self.f.spawn()

    def spawn_player(self):
        self.p.spawn(self.w // 2, self.h // 3, 'UP')

    def update(self):
        p = self.p
        f = self.f

        self._frame += 1

        grid = Grid(self.w, self.h)

        p.update(self._frame)

        if p.alive is False:
            self.spawn_player()
            f.spawn()

        # player has eaten food, respawn food
        if p.head() == f.position():
            f.spawn()
            p.grow()
            p.increment_score()

        # find a spawn position for the food
        fpos = f.position()
        while fpos == p.head() or fpos in p.tail():
            f.spawn()
            fpos = f.position()

        # generate grid
        grid.write(f.position(), f.token)
        grid.write(p.head(), p.token)
        for segment in p.tail():
            grid.write(segment, p.token)

        self._grid = grid

    def render(self):
        return [
            f'frame:     {self._frame}',
            f'direction: {self.p.direction.ljust(5)}',
            self._grid.render(),
            f'score:     {self.p.score()}',
        ]
