f = open("day_17.txt")
#f = open("test.txt")

cubes = {}

y = 0
z = 0
w = 0
for l in f.readlines():
    x = 0
    for c in l.rstrip():
        if c == '#':
            cubes[(x, y, z, w)] = True
        x = x + 1
    y = y + 1

def countActive(pos):
    active = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    newpos = (pos[0]+i, pos[1]+j, pos[2]+k, pos[3]+l)
                    if newpos == pos:
                        continue
                    if newpos in cubes:
                        active += 1
    return active

def addTasks(pos, tasks, processed):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    newpos = (pos[0]+i, pos[1]+j, pos[2]+k, pos[3]+l)
                    if newpos == pos or newpos in processed:
                        continue
                    else:
                        tasks.add(newpos)

def simulateCycle(cubes):
    new_cubes = {}
    active_count = 0
    processed = set()
    tasks = set(cubes.keys())
    while tasks:
        task = tasks.pop()
        processed.add(task)
        active = countActive(task)
        if task in cubes:
            addTasks(task, tasks, processed)
            if active in [2, 3]:
                new_cubes[task] = True

        elif active == 3:
            new_cubes[task] = True
    return new_cubes

for i in range(0, 6):
    cubes = simulateCycle(cubes)
    print(cubes, len(cubes))
                                        
                    

