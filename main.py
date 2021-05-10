import os
import time
import termios, fcntl, sys, os
import curses, sys
from lib import get_direction
from player import Player
from food import Food
from grid import Grid

fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

curses.setupterm()
clear = str(curses.tigetstr('clear'), 'ascii')

HEIGHT = 15
WIDTH = 15

if __name__ == '__main__':
    try:
        frame = 0
        direction = ''
        p = Player(WIDTH, HEIGHT)
        p.spawn(7, 14, 'UP')
        f = Food(WIDTH, HEIGHT)
        f.spawn()

        while 1:
            frame += 1
            print('frame: {}'.format(frame))

            grid = Grid(WIDTH, HEIGHT)

            # get player input
            key = sys.stdin.read(20)[:1]
            if key:
                direction = get_direction(key)
            print('direction: {}'.format(direction))

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
            grid.draw()

            # 30 fps
            time.sleep(1 / 30)
            sys.stdout.write(clear)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
