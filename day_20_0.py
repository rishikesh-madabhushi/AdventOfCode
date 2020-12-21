import re
import pprint

f = open("day_20.txt")
#f = open("test.txt")

borders = {}
tiles = {}

def addBorder(border, tileno):
    if border not in borders:
        borders[border] = set()
    borders[border].add(tileno)

def readTile():
    l = f.readline()
    if not l:
        return False
    tile_str = l.split()[1]
    tileno = int(tile_str[:len(tile_str) - 1])
    top = ""
    left = ""
    right = ""
    bottom = ""
    row = 0
    while True:
        l = f.readline().rstrip()
        if not l:
            break
        tilelen = len(l)
        if row == 0:
            top = l
        elif row == tilelen - 1:
            bottom = l
        left = left + l[0]
        right = right + l[tilelen - 1]
        row += 1
    
    addBorder(left, tileno)
    addBorder(right, tileno)
    addBorder(bottom, tileno)
    addBorder(top, tileno)
    
    tiles[tileno] = (left, right, top, bottom)
    return True

def findMatch(border, tileno):
    count = len(borders[border]) - 1
    reversed = border[::-1]
    if reversed in borders:
        count += len(borders[reversed])
        if tileno in borders[reversed]:
            count -= 1
    return count

def countMatches(tileno):
    (left, right, top, bottom) = tiles[tileno]
    count = 0
    count += findMatch(left, tileno)
    count += findMatch(right, tileno)
    count += findMatch(top, tileno)
    count += findMatch(bottom, tileno)

    #print(tileno, count)
    return count

while readTile():
    continue

corners = 1
for tileno in tiles:
    count = countMatches(tileno)
    if count == 2:
        print(tileno)
        corners = corners * tileno

print(corners)
