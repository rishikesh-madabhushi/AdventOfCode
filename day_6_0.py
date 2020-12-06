f = open("day_6_0.txt")
         
input_lines = f.readlines()

count = 0
questions = {}

group_count = 0

for line in input_lines:
    stripped_line = line.strip()
    if stripped_line:
        print(stripped_line)
        group_count += 1
        for c in stripped_line:
            if c in questions.keys():
                questions[c] += 1
            else:
                questions[c] = 1
            
    else:
        for k in questions.keys():
            if questions[k] == group_count:
                count += 1
        questions = {}
        group_count = 0

print (count)



