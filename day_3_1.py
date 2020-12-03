
f = open("day_3_0.txt")
         
input_lines = f.readlines()

tree_array = []

for line in input_lines:
    tree_array.append([char for char in line.rstrip()])

rows = len(tree_array)
cols = len(tree_array[0])

def slope_cost(row_delta, col_delta):
    tree_count = 0
    current_row = 0
    current_col = 0
    while current_row < rows - row_delta:
        current_row += row_delta
        current_col = (current_col + col_delta) % cols
        if tree_array[current_row][current_col] == '#':
            tree_count += 1
        print(current_row, current_col, tree_count)
    return tree_count


total_cost = slope_cost(1, 1)
total_cost *= slope_cost(1, 3)
total_cost *= slope_cost(1, 5)
total_cost *= slope_cost(1, 7)
total_cost *= slope_cost(2, 1)

print(total_cost)

    

    
