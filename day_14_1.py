import ctypes

f = open("day_14.txt")
#f = open("test.txt")

address = {}

def applyMask(value, mask):
    next_value = '{0:036b}'.format(value)

    value_arr = [c for c in next_value]
    for i, c in enumerate(mask):
        if c == 'X' or c == '1':
            value_arr[i] = mask[i]

    return value_arr

def processAddresses(new_addr, value, idx):
    while idx < len(new_addr) and new_addr[idx] != 'X':
        idx += 1
    if idx >= len(new_addr):
        str = "".join(new_addr)
        address[int(str, 2)] = value
        return

    new_addr[idx] = '0'
    processAddresses(new_addr, value, idx)
    new_addr[idx] = '1'
    processAddresses(new_addr, value, idx)
    new_addr[idx] = 'X'

    
def processInstr(addr, value, mask):
    new_addr = applyMask(addr, mask);
    if value:
        processAddresses(new_addr, value, 0)

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
