
f = open("day_13.txt")
#f = open("test.txt")

depart = int(f.readline().rstrip())
buses = [int(b) if b != 'x' else -1  for b in f.readline().rstrip().split(',')]
print(buses)
min_depart = float('inf')
best = 0
for b in buses:
    if b == -1:
        continue
    closest = int(depart / b) * b + b - depart
    if closest == b:
        closest = 0
    if closest < min_depart:
        min_depart = closest
        best = b

print(best, min_depart, best * min_depart)

