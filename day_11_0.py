# A more efficient implementation for finding the instr. to switch
# than the recursive one.

f = open("day_11.txt")
#f = open("test.txt")

rows = []

for l in f.readlines():
    rows.append([c for c in l.rstrip()])

def getAdjacentOccupied(old_rows, i, j):
    count = 0
    start_row = i - 1 if i - 1 >= 0 else i
    end_row = i + 1 if i + 1 < len(old_rows) else i
    start_col = j - 1 if j - 1 >= 0 else j
    end_col = j + 1 if j + 1 < len(old_rows[0]) else j

    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if old_rows[r][c] == '#':
                count += 1
    return count

def new_label(old_rows, i, j):
    if old_rows[i][j] == '.':
        return '.'

    count = getAdjacentOccupied(old_rows, i, j)
    if old_rows[i][j] == '#' and count > 4:
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
    print(step)
    print(countOccupied(rows))


simulate(rows)
    
