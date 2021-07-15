#!/usr/bin/env python3

import matplotlib.pyplot as plt

tiles = [2,2]

while True:
    print(tiles)

    try:
        difficult.append(len(tiles))
        time.append(time[-1] + 1)
    except:
        difficult = [2]
        time = [1]

    if tiles[0] == 2**11:
        break
    else:
        tile_list = []
        pos = 0
        tiles.append(0)
        while True:
            if pos == len(tiles)-1:
                break
            if tiles[pos]==tiles[pos+1]:
                tile_list.append(tiles[pos]*2)
                pos += 2
            else:
                tile_list.append(tiles[pos])
                pos += 1
        tiles = tile_list
        tiles.append(2)

    difficult.append(len(tiles))
    time.append(time[-1] + 1)

plt.plot(time,difficult)
plt.show()