import re
import pprint

import re;
f = open("day_24.txt")
#f = open("test.txt")
tiles = {}

def count_neighbors(t, tiles, whites):
    count = 0
    for x in [(1, -2), (-1, -2), (-2, 0), (-1, 2), (1, 2), (2, 0)]:
        neighbor = (t[0] + x[0], t[1] + x[1])
        if neighbor in tiles:
            count += 1
        else:
            whites.add(neighbor)
    return count

def one_day(day_no, tiles):
    whites = set()
    new_tiles = {}
    for t in tiles.keys():
        count_n = count_neighbors(t, tiles, whites)
        if count_n in [1, 2]:
            new_tiles[t] = True
    dummy = set()
    for w in whites:
        count_n = count_neighbors(w, tiles, dummy)
        if count_n == 2:
            new_tiles[w] = True

    print(day_no, len(new_tiles))
    return new_tiles


def process_dirs(dir):
    start = (0, 0)
    for d in dir:
        if d == 'sw':
            start = (start[0] + 1, start[1] - 2)
        elif d == 'se':
            start = (start[0] - 1, start[1] - 2)
        elif d == 'e':
            start = (start[0] - 2, start[1])
        elif d == 'ne':
            start = (start[0] - 1, start[1] + 2)
        elif d == 'nw':
            start = (start[0] + 1, start[1] + 2)
        elif d == 'w':
            start = (start[0] + 2, start[1])
        else:
            raise("wha?")
    if start in tiles:
        del tiles[start]
    else:
        tiles[start] = True
    print(dir, start)
        

for l in f.readlines():
    start = (0, 0)
    idx = 0
    dirs = []
    while idx < len(l.rstrip()):
        if l[idx] == 's' or l[idx] == 'n':
            dirs.append(l[idx:idx+2])
            idx += 2
        else:
            dirs.append(l[idx])
            idx += 1
    process_dirs(dirs)
print(len(tiles))
for day in range(1, 101):
    tiles = one_day(day, tiles)


      