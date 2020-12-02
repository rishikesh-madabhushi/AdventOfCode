
f = open("day_2_0.txt")
         
input_lines = f.readlines()

valid_strings = 0

for line in input_lines:
    split_line = line.split()
    
    indices = split_line[0].split("-")
    idx1 = int(indices[0]) - 1
    idx2 = int(indices[1]) - 1

    char_to_check = split_line[1][0]
    str_to_check = split_line[2]

    first_matches = str_to_check[idx1] == char_to_check;
    second_matches = str_to_check[idx2] == char_to_check; 
    if first_matches != second_matches:
        valid_strings += 1

print(valid_strings)
    
