import re
import pprint

def doLoop(start):
    for i in range(0, 20201227):
        start = start * 7
        start = start % 20201227
        if start in [17115212, 3667832, 5764801, 17807724]:
            print(i + 1, start)


def findKey(subject, loop):
    value = 1
    for i in range(0, loop):
        value = value * subject
        value = value % 20201227
    print(value)




#8217635 17115212
#20035918 3667832

findKey(17807724, 8)
findKey(3667832, 8217635)
findKey(17115212, 20035918)