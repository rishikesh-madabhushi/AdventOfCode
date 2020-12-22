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

def playGame(player1, player2):
    seen = set()
    while player1 and player2:
        key1 = str(player1)
        key2 = str(player2)
        if (key1, key2) in seen:
            print("Here")
            return 1
        seen.add((key1, key2))
        winner = 1
            
        top1 = player1.pop(0)
        top2 = player2.pop(0)
        if top1 <= len(player1) and top2 <= len(player2):
            copy_1 = player1[:top1]
            copy_2 = player2[:top2]
            print("Starting Subgame")
            winner = playGame(copy_1, copy_2)
        elif top2 > top1: 
            winner = 2
       
        if winner == 1:
            player1.append(top1)
            player1.append(top2)
        else:
            player2.append(top2)
            player2.append(top1)
    print(player1)
    print(player2)
    if player1:
        return 1
    else:
        return 2

playGame(players[0], players[1])
if players[0]:
    print(countPoints(players[0]))
else:
    print(countPoints(players[1]))


