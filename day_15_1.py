starting = [16, 1, 0, 18, 12, 14, 19]
index = 0
numbers = {}
for i, c in enumerate(starting):
    numbers[c] = i

index = len(starting)
was_seen = False
last = starting[index - 1]
diff = 0
next = 0
while index < 30000000:
    if was_seen:
        next = diff
    else:
        next = 0
    was_seen = next in numbers
    if was_seen:
        diff = index - numbers[next]
    numbers[next] = index
    index += 1

print(next)

