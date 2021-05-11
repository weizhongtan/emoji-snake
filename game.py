from grid import Grid

class Game:
    PLAY = 0
    PAUSE = 1
    OVER = 2

    def __init__(self, width, height, player, food):
        self.w = width
        self.h = height
        self.p = player
        self.f = food

    def start(self):
        self._frame = 0
        self.p.spawn(self.w // 2, self.h // 3, 'UP')
        self.f.spawn()
        self._state = Game.PLAY

    def get_state(self):
        return self._state

    def update(self):
        p = self.p
        f = self.f

        self._frame += 1

        p.update(self._frame)

        if p.alive is False:
            self._state = Game.OVER
            return

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
        grid = Grid(self.w, self.h)
        grid.write(f.position(), f.token)
        grid.write(p.head(), p.token)
        for segment in p.tail():
            grid.write(segment, p.token)

        self._grid = grid

    def render(self):
        grid = self._grid.render()

        def center_align(str):
            return str.center(len(grid[0]) * 2)

        game_over_msg = 'game over! press SPACE to restart'
        score_msg = f'score: {str(self.p.score()).rjust(5)}'

        footer = center_align(game_over_msg if self._state == Game.OVER else score_msg)
        debug = center_align(f'frame: {self._frame} dir: {self.p.direction.ljust(5)}')

        return [
            *self._grid.render(),
            footer,
            debug
        ]
