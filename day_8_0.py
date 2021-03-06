import re

f = open("day_8.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

commands = []
seen_pcs = set()

def parseInstr(instr):
    instr_str = instr.split()
    return (instr_str[0], int(instr_str[1]))

def execInstr(instrs, accum, pc, changed):
#    print (pc, changed)
    if pc >= len(instrs):
        print("END SEEN")
        print(accum)
        return True
    
    if pc in seen_pcs:
        return False
    else:
        seen_pcs.add(pc)

    (instr, offset) = parseInstr(instrs[pc])
    prev_pc = pc

    if instr == "acc":
        accum += offset
        pc += 1
    elif instr == "jmp":
        pc += offset
    elif instr == "nop":
        pc += 1 
    else: print("ERROR")
    result = execInstr(instrs, accum, pc, changed)
    if not result and not changed:
        if instr == "jmp":
            pc = pc - offset + 1
            changed = True
            execInstr(instrs, accum, pc, changed)
        elif instr == "nop":
            pc = pc - 1 + offset
            changed = True
            execInstr(instrs, accum, pc, changed)
        

for line in input_lines:
    commands.append(line.rstrip())

execInstr(commands, 0, 0, False)
