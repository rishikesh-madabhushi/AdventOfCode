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

processed = {}

def processRule(rule):
    print("processing " + rule)
    if rule.strip().startswith("\""):
        alpha = rule[1]
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
                if idx not in processed:
                    processed[idx] = processRule(rules[idx])
                    if idx == 8:
                        print("here" + processed[idx])
                        processed[idx] = '(' + processed[idx] + ')+'
                    elif idx == 11:
                        processed[idx] = processed[42] + '(' + processed[idx] + ')*' + processed[31]

                result += processed[idx]
    return result


regex = processRule(rules[0])
print(regex)
rule_42 = re.compile(processed[42])
rule_31 = re.compile(processed[31])

def isValid(test_str):    
    count_42 = 0
    count_31 = 0
    start_31 = 0

    for match in re.finditer(rule_42, test_str):
        if match.start() != start_31:
            break
        count_42 += 1
        start_31 = match.end()
    last_match = 0 
    for match in re.finditer(rule_31, test_str[start_31:]):
        count_31 += 1
        last_match = match.end()

    print(count_42, count_31, start_31, last_match, len(test_str))
    if (start_31 + last_match == len(test_str) and count_31 < count_42
        and count_31):
        return True
    return False
  
match = 0
for l in f.readlines():
    print(l.rstrip())
    if isValid(l.rstrip()):
        print("Valid")
        match += 1
print(match)

                                  
                    

