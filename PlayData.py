#!/usr/bin/env python3

from Grid import Grid
from GameDriver import GameDriver
import curses
from FileName import path_file

gameDriver = GameDriver()

datafile = open(path_file('DataManual'), "a")

def main(stdscr):

    moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    moves_count = 0
    line = ''

    while True:

        grid = gameDriver.getGrid()
        if grid.isGameOver():
            datafile.close()
            break

        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP:
            stdscr.addstr(0,0,'{} - Pressed up'.format(moves_count+1))
            moveCode = int(0)
            gameDriver.move(moveCode)
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0,0,'{} - Pressed down'.format(moves_count+1))
            moveCode = int(1)
            gameDriver.move(moveCode)
        elif key == curses.KEY_LEFT:
            stdscr.addstr(0, 0, '{} - Pressed left'.format(moves_count+1))
            moveCode = int(2)
            gameDriver.move(moveCode)
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(0, 0, '{} - Pressed right'.format(moves_count+1))
            moveCode = int(3)
            gameDriver.move(moveCode)
        else:
            continue

        if grid != gameDriver.getGrid():
            moves_count += 1
            line = '{},'.format(moves_count)

            for row in grid.matrix:
                for number in row:
                    line += str(number) + ','

            line += moves_str[moveCode]
            datafile.write('{}\n'.format(line))

        stdscr.refresh()

curses.wrapper(main)
