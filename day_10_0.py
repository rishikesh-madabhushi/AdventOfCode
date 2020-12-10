# A more efficient implementation for finding the instr. to switch
# than the recursive one.

import heapq

f = open("day_10.txt")
#f = open("test.txt")
         
input_volts = [int(l.rstrip()) for l in f.readlines()]
input_volts.sort()

start = 0

diff_map = {}
diff_map[3] = 1
for volt in input_volts:
    print(volt)
    if volt > start + 3:
        break
    else:
        diff = volt - start
        if diff in diff_map:
            diff_map[diff] += 1
        else:
            diff_map[diff] = 1
    start = volt

print(diff_map)
print(diff_map[1] * diff_map[3])
