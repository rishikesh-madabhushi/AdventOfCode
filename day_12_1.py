
#f = open("day_12.txt")
f = open("test.txt")
W = 0
N = 1
E = 2
S = 3

x = 0
y = 0

way_x = 10
way_y = 1

for l in f.readlines():
    direction = l[0]
    mag = int(l.rstrip()[1:])
    if direction == 'F':
        x += mag * way_x
        y += mag * way_y
    elif direction == 'R':
        for i in range (0, int(mag / 90)):
            tmp = way_y
            way_y = -way_x
            way_x = tmp
        continue
    elif direction == 'L':
        for i in range (0, int(mag / 90)):
            tmp = way_y
            way_y = way_x
            way_x = -tmp
        continue

    if direction == 'N':
        way_y += mag
    elif direction == 'S':
        way_y -= mag
    elif direction == 'E':
        way_x += mag
    elif direction == 'W':
        way_x -= mag
    print(x, y)

print (x, y)
print (abs(x) + abs(y))
