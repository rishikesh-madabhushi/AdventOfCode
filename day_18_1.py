import re

f = open("day_18.txt")
#f = open("test.txt")

def expr(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b

def evaluate(terms, idx):
    value = 0
    new_idx = idx + 1
    if terms[idx].isnumeric():
        value = int(terms[idx])
    elif terms[idx] == '(':
        (value, new_idx) = evaluate(terms, new_idx)
        if terms[new_idx] == ')':
            new_idx = new_idx + 1
    else:
        raise("What's going on?")
    while new_idx < len(terms):
        if terms[new_idx] == ')':
            return(value, new_idx)
        operand2 = 0
        operand1 = value
        operator = terms[new_idx]
        new_idx += 1
        if operator == '*':
            (operand2, new_idx) = evaluate(terms, new_idx)
        else:
            if terms[new_idx].isnumeric():
                operand2 = int(terms[new_idx])
                new_idx += 1
            elif terms[new_idx] == '(':
                (operand2, new_idx) = evaluate(terms, new_idx + 1)
                if terms[new_idx] != ')':
                    raise("Hmmm")
                else:
                    new_idx = new_idx + 1
            else:
                raise("What's going on?")
        value = expr(operand1, operator, operand2)
    return (value, new_idx)

sumall = 0
for l in f.readlines():
    l = re.sub(r"(\(|\))", r" \1 ", l)
    terms = l.rstrip().split()
    print(terms)
    (value, new_idx) = evaluate(terms, 0)
    sumall += value

print(sumall)
                                  
                    

