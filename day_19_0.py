import re

def cleanRule(rule):
    parts = rule.strip().split(':')
    return (parts[0], parts[1].strip())

f = open("day_19.txt")
#f = open("test.txt")
rules = {}
l = f.readline()
while l.rstrip():
    (ruleno, rule) = cleanRule(l.rstrip())
    rules[int(ruleno)] = rule
    l = f.readline()

processed = [None] * len(rules)

def processRule(rule):
    print("processing " + rule)
    if rule.strip().startswith("\""):
        alpha = rule[1]
        print(alpha)
        return alpha
    else:
        subexprs = rule.split('|')
        if len(subexprs) > 1:
            result = '(' + processRule(subexprs[0])
            for i in range(1, len(subexprs)):
                result += '|' + processRule(subexprs[i])
            result += ')'
            return result
        else:
            subrules = rule.split()
            result = ""
            for subrule in subrules:
                idx = int(subrule)
                if not processed[idx]:
                    processed[idx] = processRule(rules[idx])
                result += processed[idx]
    return result


regex = processRule(rules[0])
print(regex)
the_re = re.compile(regex)
match = 0
for l in f.readlines():
    print(l.rstrip())
    if re.fullmatch(the_re, l.rstrip()):
        print("Valid")
        match += 1
print(match)

                                  
                    

