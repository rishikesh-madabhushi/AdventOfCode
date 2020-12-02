
f = open("day_2_0.txt")
         
input_lines = f.readlines()

valid_strings = 0

for line in input_lines:
    split_line = line.split()
    
    minmax = split_line[0].split("-")
    range_min = int(minmax[0])
    range_max = int(minmax[1])

    char_to_check = split_line[1][0]
    str_to_check = split_line[2]

    count = 0
    for c in str_to_check:
      if c == char_to_check:
          count += 1
    if count >= range_min and count <= range_max:
        valid_strings += 1

print(valid_strings)
    
