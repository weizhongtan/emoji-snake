import termios, fcntl, sys, os, time, curses
from lib import get_action
from player import Player
from food import Food
from game import Game


HEIGHT = 20
WIDTH = 20
FPS = 30

def main(stdscr):
    # setup stdin to accept keyboard input as non-blocking
    fd = sys.stdin.fileno()

    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    # hide cursor
    curses.curs_set(0)

    def draw(l):
        # prevent it erroring if the terminal window is not big enough
        try:
            stdscr.addstr(0, 0, '\n'.join(l))
        except curses.error:
            pass
        stdscr.refresh()

    player = Player(WIDTH, HEIGHT)
    food = Food(WIDTH, HEIGHT)
    game = Game(WIDTH, HEIGHT, player, food)

    game.start()

    # game loop
    while 1:
        # get the most recent key that was pressed
        user_input = sys.stdin.readline()
        if len(user_input) > 0:
            key = user_input[-1]
            curses.flushinp() # discard other keys in this frame
            action = get_action(key)
            player.set_direction(action)

            if game.is_game_over() and action == 'SPACE':
                game.start()

        game.update()

        draw(game.render())

        time.sleep(1 / FPS)

curses.wrapper(main)
