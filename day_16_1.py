from interval import interval, inf, imath

f = open("day_16.txt")
#f = open("test.txt")

departure = interval()
non_departure = interval()

my_ticket = ""
overall_rules = interval()
rows = {} 
while True:
    l = f.readline()
    if not l.rstrip():
        break
    row = l.rstrip().split(':')
    intervals = row[1].split(' or ')
    rule_ivls = interval()
    for inter in intervals:
        interval_str = inter.split('-')
        rule_ivls = rule_ivls | interval[int(interval_str[0]),
                                         int(interval_str[1])]
    overall_rules = overall_rules | rule_ivls
    rows[row[0]] = rule_ivls

print(overall_rules)
rules_len = len(rows)

while True:
    l = f.readline().rstrip()
    if not l:
        break
    if l[0] == 'y':
        continue
    else:
        my_ticket = l

inferred = [set() for i in range(0, rules_len)]

firstRow = True
eliminated = set()
while True:
    l = f.readline()
    if not l:
        break
    if l[0] == 'n':
        continue
    valid = True
    for num in l.rstrip().split(','):
        if not num in overall_rules:
            valid = False
            break
    if valid:
        for i, num in enumerate(l.rstrip().split(',')):
            for k in rows:
                if num in rows[k]:
                    if firstRow:
                        inferred[i].add(k)
                else:
                    inferred[i].discard(k)
            if len(inferred[i]) == 1:
                eliminated.add(next(iter(inferred[i])))
            if len(inferred[i]) == 0:
                raise

    firstRow = False

print(eliminated)
while len(eliminated) != rules_len:
    for i in range(0, len(inferred)):
        if len(inferred[i]) == 1:
            continue
        inferred[i] = { x for x in inferred[i] if x not in eliminated }
        if len(inferred[i]) == 1:
            eliminated.add(next(iter(inferred[i])))
print(inferred)

count = 1
for i, num in enumerate(my_ticket.split(',')):
    if inferred[i].pop().startswith("departure"):
        count = count *int(num)
print(count)

        
