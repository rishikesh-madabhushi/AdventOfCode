import re
import pprint

#layout = [3,8,9,1,2,5,4,6,7]

layout = [6,5,3,4,2,7,9,1,8]

idx = 0
cup_len = len(layout)
nturns = 100
max_cup = max(layout)
min_cup = min(layout)

def getIndex(idx):
    return idx % cup_len

for i in range(0, nturns):
    cur_val = layout[idx]
    next_val = cur_val - 1
    next_idx = -1
    while True:
        try:
            next_idx = layout.index(next_val)
        except ValueError:
            next_idx = -1
        if next_idx >= 0 and (next_idx - idx + cup_len) % cup_len > 3:
            break
        next_val -= 1
        if next_val < min_cup:
            next_val = max_cup
    
    move = [layout[getIndex(idx + 1)], layout[getIndex(idx + 2)], layout[getIndex(idx + 3)]]
    for e in move: 
        layout.remove(e)
    next_idx = layout.index(next_val)
    for i in range(0,3):
        layout.insert(next_idx + i + 1, move[i])
    idx = layout.index(cur_val)
    print(layout, idx)
    idx = getIndex(idx + 1)


final = layout.index(1)
res = []
i = getIndex(final + 1)
while i != final:
    res.append(str(layout[i]))
    i = getIndex(i + 1)

print("".join(res))