# A more efficient implementation for finding the instr. to switch
# than the recursive one.

import re

f = open("day_9.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

inputs = []
window = 25

for line in input_lines:
    inputs.append(int(line.rstrip()))

sums = {}
for i in range(0, window):
    for j in range(i + 1, window):
        sum = inputs[i] + inputs[j]
        if sum in sums:
            sums[sum] += 1
        else:
            sums[sum] = 1
#print(sums)
def fix_sums(current):
    for i in range(current - window + 1, current):
        sum = inputs[current - window] + inputs[i]
        sums[sum] -= 1
        if sums[sum] == 0:
            del sums[sum]
    for i in range(current - window + 1, current):
        sum = inputs[current] + inputs[i]
        if sum in sums:
            sums[sum] += 1
        else:
            sums[sum] = 1
#    print(sums)
weakness = 0
weakness_loc = 0
for i in range(window, len(inputs)):
    if inputs[i] not in sums:
        print(inputs[i])
        weakness = inputs[i]
        weakness_loc = i
        break
    else:
        fix_sums(i)


seq_start = 0
seq_end = 0
cursum = 0
for i in range(0, weakness_loc):
    cursum += inputs[i]
    if cursum == weakness:
        seq_end = i
        break
    elif cursum > weakness:
        while cursum != 0 and cursum > weakness:
            cursum -= inputs[seq_start]
            seq_start += 1
    if cursum == weakness:
        seq_end = i
        break
print(seq_start, seq_end)

minval = inputs[seq_start]
maxval = inputs[seq_start]
for i in range(seq_start, seq_end + 1):
    if inputs[i] < minval:
        minval = inputs[i]
    if inputs[i] > maxval:
        maxval = inputs[i]

print(minval + maxval)
