#!/usr/bin/env python3

import os
import time

path = '/Users/David/Desktop/TFG/Data2048/DataExpectimaxMIT_txt/'

list_datafiles = os.listdir(path)
MIT_txt = [file for file in list_datafiles]

for file in MIT_txt:

    file_origin = open('{}{}'.format(path, file), "r")
    file_destination = open('{}{}.csv'.format(path[:-22], file[:-4]), "a")

    dt_string = time.strftime('%d/%m/%Y %H:%M', time.gmtime(os.path.getmtime('{}{}'.format(path, file))))

    file_destination.write('{},{}\n'.format(str(dt_string[:10]), str(dt_string[11:])))
    file_destination.write('Row,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,Move\n')

    max_value_move = []
    move = {0: 'UP', 1: 'DOWN', 2: 'LEFT', 3: 'RIGHT'}
    line_destination = ''

    for row in file_origin:
        line_origin = row.split()
        try:
            if line_origin[0] == 'Game':
                continue
            elif line_origin[1][0] == '#':
                line_destination += line_origin[1][1:]
            elif line_origin[0].isdigit():
                for number in line_origin:
                    line_destination += number
                    line_destination += ','
            elif line_origin[0] == 'Move':
                max_value_move.append(float(line_origin[3][:-1]))
                if len(max_value_move) == 4:
                    line_destination += move[max_value_move.index(max(max_value_move))]
                    file_destination.write('{}\n'.format(line_destination))

                    line_destination = ''
                    max_value_move = []
        except:
            continue

    file_origin.close()
    file_destination.close()