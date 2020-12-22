import re
import pprint

f = open("day_22.txt")
#f = open("test.txt")


players = [[],[]]

current = -1

def countPoints(player):
    print(player)
    
    pos = len(player)
    score = 0
    while player:
        top = player.pop(0)
        score += top * pos
        pos -= 1
    return(score)


for l in f.readlines():
    if l.startswith("Player"):
        current += 1
        continue
    if not l.rstrip():
        continue
    players[current].append(int(l.rstrip()))

print(players)

while players[0] and players[1]:
    top0 = players[0].pop(0)
    top1 = players[1].pop(0)

    if top0 > top1:
        players[0].append(top0)
        players[0].append(top1)
    else:
        players[1].append(top1)
        players[1].append(top0)

    print(players[0])
    print(players[1])

if players[0]:
    print(countPoints(players[0]))
else:
    print(countPoints(players[1]))


