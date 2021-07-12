#!/usr/bin/env python3

from Grid import Grid
from FileName import path_file, last_file
import random
import pygame


# -----------------------------------------------------------------------------------------------------


def printMatrix(self):

    for row in self.matrix:
        line = ''
        for number in row:
            line += ' '*(6-len(str(number)))+str(number)
        print(line)
    print('\nMove #{},  Current score = {}\n\n'.format(moves_count,scoreGrid(self)[0]))

def getGrid(self) -> Grid:
    list_zeros = scoreGrid(self)[2]

    if len(list_zeros) > 0:
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
    matrix_list = []
    points = {0: 0, 2: 0, 4: 4, 8: 16, 16: 40, 32: 112, 64: 288, 128: 704, 256: 1664, 512: 3840, 1024: 8704,
              2048: 19456,4096: 43008, 8192: 94208, 16384: 204800, 32768: 441984, 65536: 948736, 131072: 2027006}

    for row in range(4):
        list_b = []
        for col in range(4):
            list_b.append(grid.matrix[row][col])
            number = self.matrix[row][col]
            if number == 0:
                list_zeros.append([row,col])
            score += points[number]
            if number > max_value:
                max_value = number
        matrix_list.append(list_b)

    return score, max_value, list_zeros, matrix_list


# -----------------------------------------------------------------------------------------------------


question = input('Do you want to start a new game?\n <y> <n>\n')
if question == 'y':
    datafile = open(path_file('DataManualPG'), "a")
    moves_count = 0
    matrix = [[0 for i in range(4)] for j in range(4)]
    new_move = 5
    grid = Grid(matrix)
    getGrid(grid)

elif question == 'n':
    datafile = open(last_file()[0]+last_file()[1], "a") #open(str(last_file()[0]), "a")
    moves_count = int(last_file()[2])-1
    matrix = last_file()[3]
    new_move = 5
    grid = Grid(matrix)

record_grid = []
record_move = []

key_print = {1: 'UP', 2: 'DOWN', 3: 'LEFT', 4: 'RIGHT'}


# -----------------------------------------------------------------------------------------------------


pygame.init()

gameDisplay = pygame.display.set_mode((378, 378))
pygame.display.set_caption('First Game')

clock = pygame.time.Clock()
crashed = False

images = { 16384: pygame.image.load('Tiles/16384.png'), 8192: pygame.image.load('Tiles/8192.png'),
           4096: pygame.image.load('Tiles/4096.png'), 2048: pygame.image.load('Tiles/2048.png'),
           1024: pygame.image.load('Tiles/1024.png'), 512: pygame.image.load('Tiles/512.png'),
           256: pygame.image.load('Tiles/256.png'), 128: pygame.image.load('Tiles/128.png'),
           64: pygame.image.load('Tiles/64.png'), 32: pygame.image.load('Tiles/32.png'),
           16: pygame.image.load('Tiles/16.png'), 8: pygame.image.load('Tiles/8.png'),
           4: pygame.image.load('Tiles/4.png'), 2: pygame.image.load('Tiles/2.png'),
           0: pygame.image.load('Tiles/0.png') }

def tile(img,x,y):
    gameDisplay.blit(img, (x,y))


# -----------------------------------------------------------------------------------------------------


run = True
while run:

    if new_move > 0:
        moves_count += 1
        getGrid(grid)
        printMatrix(grid)

        if len(record_grid) > 19:
            line = '{},'.format(moves_count-20)

            for row in record_grid[0]:
                for number in row:
                    line += str(number) + ','

            line += record_move[0]
            datafile.write('{}\n'.format(line))

            for i in range(len(record_grid)):
                if i < 19:
                    record_grid[i] = record_grid[i + 1]
                    if i < 18:
                        record_move[i] = record_move[i + 1]
                    else:
                        record_move[i] = key_print[new_move]
                else:
                    record_grid[19] = scoreGrid(grid)[3]

        else:
            record_grid.append(scoreGrid(grid)[3])
            if new_move <5:
                record_move.append(key_print[new_move])
        new_move = 0


    # -------------------------------------------------------------------------------------------------


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and grid.canMoveUp():
                grid.up()
                new_move = 1
            if event.key == pygame.K_DOWN and grid.canMoveDown():
                grid.down()
                new_move = 2
            if event.key == pygame.K_LEFT and grid.canMoveLeft():
                grid.left()
                new_move = 3
            if event.key == pygame.K_RIGHT and grid.canMoveRight():
                grid.right()
                new_move = 4
            if event.key == pygame.K_b and len(record_grid)>0 :
                moves_count -= 1
                record_grid.pop()
                record_move.pop()
                grid = Grid(record_grid[len(record_grid)-1])
                printMatrix(grid)
            if event.key == pygame.K_e:
                for i in range(len(record_move)):
                    line = '{},'.format(moves_count - 20 + i)
                    for row in record_grid[i]:
                        for number in row:
                            line += str(number) + ','
                    line += record_move[i]
                    datafile.write('{}\n'.format(line))
                datafile.close()
                run = False


    # -------------------------------------------------------------------------------------------------


    gameDisplay.fill((187,173,160))
    tile(images[grid.matrix[0][0]], 8, 8)
    tile(images[grid.matrix[0][1]], 98, 8)
    tile(images[grid.matrix[0][2]], 188, 8)
    tile(images[grid.matrix[0][3]], 278, 8)
    tile(images[grid.matrix[1][0]], 8, 98)
    tile(images[grid.matrix[1][1]], 98, 98)
    tile(images[grid.matrix[1][2]], 188, 98)
    tile(images[grid.matrix[1][3]], 278, 98)
    tile(images[grid.matrix[2][0]], 8, 188)
    tile(images[grid.matrix[2][1]], 98, 188)
    tile(images[grid.matrix[2][2]], 188, 188)
    tile(images[grid.matrix[2][3]], 278, 188)
    tile(images[grid.matrix[3][0]], 8, 278)
    tile(images[grid.matrix[3][1]], 98, 278)
    tile(images[grid.matrix[3][2]], 188, 278)
    tile(images[grid.matrix[3][3]], 278, 278)

    pygame.display.update()

pygame.quit()
