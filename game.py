from grid import Grid

class Game:
    def __init__(self, width, height, draw, player, food):
        self.w = width
        self.h = height
        self.draw = draw
        self._frame = 0
        self.p = player
        self.f = food

    def start(self):
        self.p.spawn(7, 14, 'UP')
        self.f.spawn()

    def update(self):
        p = self.p
        f = self.f

        self._frame += 1

        grid = Grid(self.w, self.h)

        p.update(self._frame)

        # write tail first so that we can check for conflicts
        for segment in p.tail():
            grid.write(segment, p.token)

        grid.write(p.head(), p.token)

        if p.alive is False:
            p.spawn(7, 14, 'UP')
            f.spawn()

        # player has eaten food, respawn food
        if p.head() == f.position():
            f.spawn()
            p.grow()

        # find a spawn position for the food
        fpos = f.position()
        while fpos == p.head() or fpos in p.tail():
            f.spawn()
            fpos = f.position()

        grid.write(f.position(), f.token)

        # draw
        self.draw([
            f'frame:     {self._frame}',
            f'direction: {p.direction.ljust(5)}',
            grid.render(),
        ])
