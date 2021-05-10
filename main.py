import os
import time
import termios, fcntl, sys, os
from curses import wrapper, flushinp
from lib import get_direction
from player import Player
from food import Food
from grid import Grid


HEIGHT = 20
WIDTH = 20

def main(stdscr):
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    frame = 0
    direction = ''
    p = Player(WIDTH, HEIGHT)
    p.spawn(7, 14, 'UP')
    f = Food(WIDTH, HEIGHT)
    f.spawn()

    while 1:
        frame += 1
        stdscr.addstr(0, 0, 'frame: {}'.format(frame))

        grid = Grid(WIDTH, HEIGHT)

        # get the last key that
        user_input = sys.stdin.readline()
        key = ''
        if len(user_input) > 0:
            key = user_input[-1]
            flushinp()

        if key:
            direction = get_direction(key)
        stdscr.addstr(1, 0, 'direction: {}'.format(direction))

        p.set_direction(direction)
        p.update(frame)

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
        stdscr.addstr(2, 0, grid.render())
        stdscr.refresh()

        # 30 fps
        time.sleep(1 / 30)

wrapper(main)
