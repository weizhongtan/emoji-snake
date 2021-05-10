import termios, fcntl, sys, os, time
from curses import wrapper, flushinp
from lib import get_direction
from player import Player
from food import Food
from grid import Grid
from game import Game


HEIGHT = 20
WIDTH = 20
FPS = 30

def main(stdscr):
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    def draw(l):
        stdscr.addstr(0, 0, '\n'.join(l))
        stdscr.refresh()

    player = Player(WIDTH, HEIGHT)
    food = Food(WIDTH, HEIGHT)
    game = Game(WIDTH, HEIGHT, draw, player, food)

    game.start()

    # game loop
    while 1:
        # get the most recent key that was pressed
        user_input = sys.stdin.readline()
        if len(user_input) > 0:
            key = user_input[-1]
            flushinp() # discard other keys in this frame
            direction = get_direction(key)
            player.set_direction(direction)

        game.update()

        time.sleep(1 / FPS)

wrapper(main)
