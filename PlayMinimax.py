#!/usr/bin/env python3

from Grid import Grid
from GameDriver import GameDriver
from Minimax import getBestMove
from FileName import path_file
import time

gameDriver = GameDriver()
datafile = open(path_file('DataMinimaxIV'), "a")

moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
moves_count = 1
click_keep_going = 0

while True:
    grid = gameDriver.getGrid()
    if grid.isGameOver():
        datafile.close()
        print("Unfortunately, I lost the game.")
        break

    if click_keep_going == 0:
        for row in grid.matrix:
            for number in row:
                if number == 2048:
                    time.sleep(2)
                    try:
                        gameDriver.keep_going()
                        click_keep_going += 1
                    except:
                        continue

    moveCode = getBestMove(grid, 5)

    print(f'Move #{moves_count}: {moves_str[moveCode]}')
    gameDriver.move(moveCode)

    if grid != gameDriver.getGrid():
        moves_count += 1
        line = '{},'.format(moves_count)

        for row in grid.matrix:
            for number in row:
                line += str(number) + ','

        line += moves_str[moveCode]
        datafile.write('{}\n'.format(line))


