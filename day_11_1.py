# A more efficient implementation for finding the instr. to switch
# than the recursive one.

f = open("day_11.txt")
#f = open("test.txt")

rows = []

for l in f.readlines():
    rows.append([c for c in l.rstrip()])

nearest_map = {}

W = 0
NW = 1
N = 2
NE = 3
E = 4
SE = 5
S = 6
SW = 7


def getIndex(direction, i, j):
    if direction == W:
        return (i, j - 1)
    if direction == NW:
        return (i - 1, j - 1)
    if direction == N:
        return (i - 1, j)
    if direction == NE:
        return (i - 1, j + 1)
    if direction == E:
        return (i, j + 1)
    if direction == SE:
        return (i + 1, j + 1)
    if direction == S:
        return (i + 1, j)
    if direction == SW:
        return (i + 1, j - 1)

def is_seat(rows, i, j):
    return rows[i][j] == 'L' or rows[i][j] == '#'

def process_direction(direction, i, j):
    (adj_i, adj_j) = getIndex(direction, i, j)
    if (adj_i >= len(rows) or adj_i < 0 or
        adj_j < 0 or adj_j >= len(rows[0])):
        return
    if is_seat(rows, adj_i, adj_j):
        nearest_map[(i, j)][direction] = (adj_i, adj_j)
    else:
        nearest_map[(i, j)][direction] = nearest_map[(adj_i, adj_j)][direction]


def preprocess():
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            nearest_map[(i, j)] = [None]*8

    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            for direction in range(W, E):
                process_direction(direction, i, j)

    for i in reversed(range(0, len(rows))):
        for j in reversed(range(0, len(rows[i]))):
            for direction in range(E, SW + 1):
                process_direction(direction, i, j)
    
def getAdjacentOccupied(old_rows, i, j):
    directions = nearest_map[(i, j)]
    count = 0
    for i in range(W, SW + 1):
        if directions[i]:
            (r, c) = directions[i]
            if old_rows[r][c] == '#':
                count += 1
            
    return count

def new_label(old_rows, i, j):
    if old_rows[i][j] == '.':
        return '.'

    count = getAdjacentOccupied(old_rows, i, j)
    if old_rows[i][j] == '#' and count >= 5:
        return 'L'

    if old_rows[i][j] == 'L' and count == 0:
        return '#'
    return old_rows[i][j]

def equal_areas(old_rows, rows):
    if not old_rows:
        return False
    for i in range(0, len(old_rows)):
        for j in range(0, len(old_rows[i])):
            if old_rows[i][j] != rows[i][j]:
                return False
    return True

def countOccupied(rows):
    total = 0
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            if c == '#':
                total += 1
    return total

def simulate(rows):
    old_rows = []
    step = 0
    while not equal_areas(old_rows, rows):
        old_rows = [row[:] for row in rows]
        step += 1
        for i, row in enumerate(rows):
            for j, col in enumerate(rows[i]):
                rows[i][j] = new_label(old_rows, i, j)
    print(countOccupied(rows))


preprocess()
simulate(rows)
    
