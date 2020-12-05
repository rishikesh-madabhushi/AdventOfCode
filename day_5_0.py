f = open("day_5_0.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

max_seat_id = 0

max_poss_id = 127 * 8 + 7

rows_seen = [0 for x in range(0, max_poss_id + 1) ]

print (len(rows_seen))

my_seat = -1

for line in input_lines:
    seat_num = 0
    col_num = 0
    for c in line.rstrip():
        if c == 'F':
            seat_num = seat_num << 1
        elif c == 'B':
            seat_num = seat_num << 1 | 1
        elif c == 'L':
            col_num = col_num << 1
        elif c == 'R':
            col_num = col_num << 1 | 1

    print(seat_num, col_num)
    seat_id = seat_num * 8 + col_num
    rows_seen[seat_id] = 1
    if seat_id > max_seat_id:
        max_seat_id = seat_id

for seat in range(1, max_poss_id):
 if (rows_seen[seat] == 0 and
     rows_seen[seat - 1] == 1 and
     rows_seen[seat + 1] == 1):
     print(seat)
     break
 
print (max_seat_id)



