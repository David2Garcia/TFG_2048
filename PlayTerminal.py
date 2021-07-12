#!/usr/bin/env python3

from Grid import Grid
# from GameDriver import GameDriver
import curses
import random
import time
# from FileName import path_file

# gameDriver = GameDriver()

#datafile = open(path_file('DataPrueba'), "a")



def main(stdscr):

    moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    moves_count = 0
    new_grid = 0
    record = []
    matrix = [[0 for i in range(4)] for j in range(4)]
#    line = ''
    grid = Grid(matrix)
    getGrid(grid)
    getGrid(grid)

    while True:

        if grid.isGameOver():
        #    datafile.close()
        #   stdscr.addstr(1, 1, 'Do you want to finish?')
        #   stdscr.addstr(2, 1, '<y> <n>')
        #   end = input()
        #   if end == ('y'):
            break

        stdscr.addstr(1, 1, 'Move #{}, current score = {}'.format(moves_count,scoreGrid(grid)[0]))
        stdscr.addstr(3, 1, '{}'.format(printLine(grid,0)))
        stdscr.addstr(4, 1, '{}'.format(printLine(grid,1)))
        stdscr.addstr(5, 1, '{}'.format(printLine(grid,2)))
        stdscr.addstr(6, 1, '{}'.format(printLine(grid,3)))
        # stdscr.addstr(7, 1, '{}'.format(record))

        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and grid.canMoveUp():
            stdscr.refresh()
            grid.up()
            moves_count += 1
            stdscr.addstr(8,1,'Pressed up')
            new_grid = 1

        elif key == curses.KEY_DOWN and grid.canMoveDown():
            stdscr.refresh()
            grid.down()
            moves_count += 1
            stdscr.addstr(8,1,'Pressed down')
            new_grid = 2

        elif key == curses.KEY_LEFT and grid.canMoveLeft():
            stdscr.refresh()
            grid.left()
            moves_count += 1
            stdscr.addstr(8,1,'Pressed left')
            new_grid = 3

        elif key == curses.KEY_RIGHT and grid.canMoveRight():
            stdscr.refresh()
            grid.right()
            moves_count += 1
            stdscr.addstr(8,1,'Pressed right')
            new_grid = 4

        elif key == ord('f'):
            stdscr.addstr(8, 1, 'Forward')

        elif key == ord('b'):
            stdscr.addstr(8, 1, 'Backward')

        elif key == ord('e'):
            curses.cbreak()
            break
        else:
            continue

        if new_grid > 0:
            getGrid(grid)

            if len(record) > 19:
                for i in range(len(record)):
                    if i < 19:
                        record[i] = record[i + 1]
                    else:
                        record[19] = new_grid
            else:
                record.append(new_grid)
            new_grid = 0

'''
        if grid != gameDriver.getGrid():
            moves_count += 1
            line = '{},'.format(moves_count)

            for row in grid.matrix:
                for number in row:
                    line += str(number) + ','

            line += moves_str[moveCode]
            datafile.write('{}\n'.format(line))
'''

def printLine(self,row):
    line = ''
    for number in self.matrix[row]:
        line += ' '*(6-len(str(number)))+str(number)
    return line

def getGrid(self) -> Grid:
    list_zeros = scoreGrid(self)[2]

    place_new_tile = random.randint(0, len(list_zeros) - 1)

    if random.randint(0, 99) > 89:
        new_tile = 4
    else:
        new_tile = 2

    self.matrix[list_zeros[place_new_tile][0]][list_zeros[place_new_tile][1]] = new_tile


def scoreGrid(self) -> Grid:
    score = 0
    max_value = 0
    list_zeros = []
    points = {0: 0, 2: 0, 4: 4, 8: 16, 16: 40, 32: 112, 64: 288, 128: 704, 256: 1664, 512: 3840, 1024: 8704, 2048: 19456,4096: 43008, 8192: 94208, 16384: 204800, 32768: 441984, 65536: 948736, 131072: 2027006}

    for row in range(4):
        for col in range(4):
            number = self.matrix[row][col]
            if number == 0:
                list_zeros.append([row,col])
            score += points[number]
            if number > max_value:
                max_value = number

    return score, max_value, list_zeros

curses.wrapper(main)