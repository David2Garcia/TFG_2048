#!/usr/bin/env python3

from Grid import Grid
from GameDriver import GameDriver
from Minimax import getBestMove
from FileName import path_file

gameDriver = GameDriver()
datafile = open(path_file('DataMinimax'), "a")

moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
moves_count = 1
blank = 8

while True:
    grid = gameDriver.getGrid()
    if grid.isGameOver():
        datafile.close()
        print("Unfortunately, I lost the game.")
        break
    if blank < 5:
        moveCode = getBestMove(grid, 10)
    else:
        moveCode = getBestMove(grid, 5)

    print(f'Move #{moves_count}: {moves_str[moveCode]}')
    gameDriver.move(moveCode)

    if grid != gameDriver.getGrid():
        moves_count += 1
        line = '{},'.format(moves_count)

        blank = 0
        for row in grid.matrix:
            for number in row:
                line += str(number) + ','
                if number == 0:
                    blank += 1

        line += moves_str[moveCode]
        datafile.write('{}\n'.format(line))



