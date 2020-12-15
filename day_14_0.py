import ctypes

f = open("day_14.txt")
#f = open("test.txt")

address = {}

def applyMask(value, mask):
    next_value = '{0:036b}'.format(value)
    print(next_value)

    value_arr = [c for c in next_value]
    for i, c in enumerate(mask):
        if c == '0' or c == '1':
            value_arr[i] = mask[i]

    return "".join(value_arr)


def processInstr(addr, value, mask):
    new_value = int(applyMask(value, mask), 2);
    print(value, new_value, addr)
    if new_value:
        address[addr] = new_value

mask = ""
for line in f.readlines():
    parts = [l.strip() for l in line.split('=')]
    if parts[0] == "mask":
        mask = parts[1]
    else:
        addr = int(parts[0][4:len(parts[0])-1])
        value = int(parts[1])
        processInstr(addr, value, mask)

sum = 0
for keys in address:
    sum += address[keys]
print(sum)
