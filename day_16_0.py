from interval import interval, inf, imath

#f = open("day_16.txt")
f = open("test.txt")

rules = {}

my_ticket = ""
overall_rules = interval()
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
        overall_rules = overall_rules | interval[int(interval_str[0]),
                                         int(interval_str[1])]
    print(row[0], rule_ivls)
    rules[row[0]] = rule_ivls

rules_len = len(rules)
print(overall_rules)

while True:
    l = f.readline()
    if not l.rstrip():
        break
    if l[0] == 'y':
        continue
    else:
        my_ticket = l

count = 0
while True:
    l = f.readline()
    if not l:
        break
    if l[0] == 'n':
        continue
    valid = True
    for num in l.rstrip().split(','):
        if not num in overall_rules:
            count += int(num)

                
            

print(count)
            
        
