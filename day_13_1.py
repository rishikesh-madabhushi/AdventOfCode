
f = open("day_13.txt")
#f = open("test.txt")

depart = int(f.readline().rstrip())
buses = [int(b) if b != 'x' else -1  for b in f.readline().rstrip().split(',')]
print(buses)

def calcClosest(static, mult, leftover, n):
    mod_s = static % n
    mod_m = mult % n
    num = mult
    while (mod_s + mod_m + leftover) % n:
        num += mult
        mod_m = num % n
    return num + static

def cycleLength(num, modder):
    initial = num % modder
    cur = num + num
    final = 1
    while (cur % modder) != initial:
        cur += num
        final += 1
    return final

static = 0
dynamic = 0
prev = 0
for i, b in enumerate(buses):
    if b == -1:
        continue
    elif i == 0:
        dynamic = b
        prev = 0
    else:
        static = calcClosest(static, dynamic, i - prev, b)
        print(static)
        static += i - prev
        prev = i

        if (dynamic < b):
            dynamic = b * cycleLength(b, dynamic)
        else:
            dynamic = dynamic * cycleLength(dynamic, b)

print(static - prev)

