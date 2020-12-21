import re
import pprint
import math

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
    rest = []
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
        else: 
            rest.append(l[1:tilelen-1])
        left = left + l[0]
        right = right + l[tilelen - 1]
        row += 1
    
    addBorder(left, tileno)
    addBorder(right, tileno)
    addBorder(bottom, tileno)
    addBorder(top, tileno)
    
    tile_borders = [left, top, right, bottom]
    tiles[tileno] = (tile_borders, rest)
    return True

def findMatch(border, tileno):
    result = set()
    if len(borders[border]) > 1:
        result.update(borders[border].copy())
        result.discard(tileno)
        return result.pop()

    reversed = border[::-1]
    if reversed in borders:
        result.update(borders[reversed].copy())
        return result.pop()
    return None
    

def findMatches(tileno):
    (tile_border, Any) = tiles[tileno]
    results = [None] * 4
    for i in range(0, 4):
        results[i] = findMatch(tile_border[i], tileno)
    
    return results

def findRow(row, tileno, prev, seen):
    seen.add(tileno)
    row.append(tileno)
    results = findMatches(tileno)
    print(tileno, results)
    
    idx = results.index(prev)
    opp = (idx + 2) % 4
    if results[opp]:
        findRow(row, results[opp],tileno, seen)
   
def findLeft(start, seen):
    results = findMatches(start)
    print(start, results)
    for i, r in enumerate(results):
        if r in seen:
            next = (i + 1) % 4
            prev = (i - 1 + 4) % 4
            if results[next]:
                return results[next]
            else:
                assert(results[prev])
                return results[prev]
    # Should only be the first time
    for i, r in enumerate(results):
        next = (i + 1) % 4
        if r and results[next]:
            return r

def findNextStart(start, seen):
    results = findMatches(start)
    print(start, results)
    for r in results:
        if r and not r in seen:
           return r

def findRotation(tileno, idx, next_tile):
    result = findMatches(tileno)
    print(result)
    rotation = 0
    while result[idx] != next_tile:
        rotation += 90
        idx = (idx - 1 + 4) % 4
    return rotation

def findTranslation(tileno, idx, next_tile, rotations):
    result = findMatches(tileno)
    rotation = rotations[tileno]
    while rotation:
        idx = (idx - 1 + 4) % 4
        rotation = rotation - 90
    print(idx, next_tile)
    if result[idx] == next_tile:
        return False
    assert(result[(idx+2)%4] == next_tile)
    return True


def rotateTiles(tilemap, rotations, translations):
    boardlen = len(tilemap)
    for i, row in enumerate(tilemap):
        for j, t in enumerate(row):
            if j < boardlen - 1:
                rotations[t] = findRotation(t, 2, tilemap[i][j+1])
            else:
                rotations[t] = findRotation(t, 0, tilemap[i][j-1])
            print(t, rotations[t])
            if i < boardlen - 1:
                translations[t] = findTranslation(t, 3, tilemap[i+1][j], rotations)
            else: 
                translations[t] = findTranslation(t, 1, tilemap[i-1][j], rotations)

def processTile(tileno, rotations, translations):
    rest = tiles[tileno][1] 
    rotation = rotations[tileno]
    print(tileno, rotation, translations[tileno])
    pprint.pprint(rest)
    while rotation:
        rest = list(zip(*rest[::-1]))
        rotation = rotation - 90
    if translations[tileno]:
        rest = list(reversed(rest))
    return ["".join(s) for s in rest]

def findSeaMonster(map):
    longre = re.compile(r"#....##....##....###")
    shortre = re.compile(r"#..#..#..#..#..#")
    matches = 0
    for i, l in enumerate(map):
        startIndex = 0
        if i == 0 or i == len(map) - 1:
            continue
        while True:
            matcher = longre.search(l, startIndex)
            if not matcher:
                break
            startIndex = matcher.start() + 1
            if map[i - 1][matcher.end() - 2] != '#':
                continue
            if re.match(shortre, map[i+1][matcher.start() + 1:]):
                print("Saw a monster")
                matches += 1
     
    return matches



while readTile():
    continue

print(len(tiles))

start = 1489 
#start = 1171

nRows = int(math.sqrt(len(tiles)))
tilemap = [None] * nRows
seen = set()
for i in range(0, nRows):
    row = []
    row.append(start)
    seen.add(start)
    next = findLeft(start, seen)
    findRow(row, next, start, seen)  
    tilemap[i] = row
    start = findNextStart(start, seen)
print(tilemap)
rotations = {}
translations = {}
rotateTiles(tilemap, rotations, translations)
pprint.pprint(rotations)
pprint.pprint(translations)

joinedTiles = []
for i, r in enumerate(tilemap):
    tilerow = []
    for j, t in enumerate(r):
        result = processTile(t, rotations, translations)
        if tilerow:
            tilerow = ["".join(s) for s in zip(tilerow, result)]
        else: 
            tilerow = result
        pprint.pprint(result)
    joinedTiles.extend(tilerow)

pprint.pprint(joinedTiles)

map = joinedTiles

hash_count = 0
for l in map:
    hash_count += l.count('#')

for i in range(0, 360, 90):
    rmap = reversed(map)
    matches = findSeaMonster(map)

    if matches:
        print(matches)
        print(hash_count)
        print(hash_count - matches * 15)

    map = list(zip(*map[::-1]))
    map = ["".join(s) for s in map]

  



    
 


