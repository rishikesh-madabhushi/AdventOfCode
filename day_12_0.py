
f = open("day_12.txt")
#f = open("test.txt")
W = 0
N = 1
E = 2
S = 3

x = 0
y = 0
facing = E

def getLabel(c):
    if c == W:
        return 'W'
    if c == E:
        return 'E'
    if c == N:
        return 'N'
    if c == S:
        return 'S'

for l in f.readlines():
    direction = l[0]
    mag = int(l.rstrip()[1:])
    if direction == 'F':
        direction = getLabel(facing)
    elif direction == 'R':
        for i in range (0, int(mag / 90)):
            facing = (facing + 1) % 4
        continue
    elif direction == 'L':
        for i in range (0, int(mag / 90)):
            facing = facing - 1
            if facing < 0:
                facing = 3
        continue
    print(direction, mag)
    if direction == 'N':
        y += mag
    elif direction == 'S':
        y -= mag
    elif direction == 'E':
        x += mag
    elif direction == 'W':
        x -= mag
    print(x, y)

print (x, y)
print (abs(x) + abs(y))
