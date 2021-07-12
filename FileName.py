#!/usr/bin/env python3

from datetime import datetime
import os


def path_file(name):

    path = '/Users/David/Desktop/TFG/Data2048/'
    list_datafiles = os.listdir(path)
    manual_datafiles = [file for file in list_datafiles if file.startswith(name)]
    path_namefile = "{}{}{}.csv".format(path, name, len(manual_datafiles) + 1)
    print("\n{}{}.csv\n".format(name, len(manual_datafiles) + 1))
    datafile = open(path_namefile, "a")

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    datafile.write('{},{}\n'.format(str(dt_string[:10]), str(dt_string[11:16])))
    datafile.write('Row,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,Move\n')
    datafile.close()

    return path_namefile