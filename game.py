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
        self.f.spawn(self.p.head(), self.p.tail())
        self.set_state(Game.PLAY)

    def get_state(self):
        return self._state

    def set_state(self, s):
        self._state = s

    def update(self):
        p = self.p
        f = self.f

        if p.alive is False:
            self.set_state(Game.OVER)

        if self.get_state() in (Game.PAUSE, Game.OVER):
            return

        self._frame += 1

        p.update(self._frame)

        # player has eaten food, respawn food
        if p.head() == f.position():
            f.spawn(p.head(), p.tail())
            p.grow()
            p.increment_score()

    def render(self):
        p = self.p
        f = self.f

        # generate grid
        grid = Grid(self.w, self.h)
        grid.write(f.position(), f.token)
        grid.write(p.head(), p.token)
        for segment in p.tail():
            grid.write(segment, p.token)
        grid_list = grid.render()

        def center_align(str):
            return str.center(len(grid_list[0]) * 2)

        messages = {
            Game.PLAY: f'score: {str(p.score()).rjust(5)}',
            Game.PAUSE: 'press SPACE to start',
            Game.OVER: 'game over! press SPACE to restart',
        }

        footer = center_align(messages[self._state])
        debug = center_align(f'frame: {self._frame} dir: {p.direction.ljust(5)}')

        return [
            *grid_list,
            footer,
            debug
        ]
