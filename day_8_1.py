# A more efficient implementation for finding the instr. to switch
# than the recursive one.

import re

f = open("day_8.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

commands = []
seen_pcs = set()

reverse_graph = {}

def parseInstr(instr):
    instr_str = instr.split()
    return (instr_str[0], int(instr_str[1]))

def addEdge(x, y):
    if x in reverse_graph:
        reverse_graph[x].append(y)
    else:
        reverse_graph[x] = [y]

def build_graph(instrs):
    for pc, instr in enumerate(instrs):
        (instr, offset) = parseInstr(instrs[pc])
        if instr == "acc" or instr == "nop":
            addEdge(pc + 1, pc)
        elif instr == "jmp":
            addEdge(pc + offset, pc)


frontier = set()
def find_frontier(node):
    if node not in reverse_graph:
        return
    for child in reverse_graph[node]:
        frontier.add(child)
        find_frontier(child)

def run_instrs(instrs):
    pc = 0
    accum = 0
    changed = False
    for instr in instrs:
        if pc >= len(instrs):
            print(accum)
            return
        (instr, offset) = parseInstr(instrs[pc])
        if instr == "acc":
            accum += offset
            pc += 1
            alternate_pc = pc + 1            
        elif instr == "jmp":
            pc += offset
            alternate_pc = pc + 1
        elif instr == "nop":
            pc += 1
            alternate_pc = pc + offset            
        else: print("ERROR")

        if alternate_pc in frontier and not changed:
            print(instr, offset)
            changed = True
            pc = alternate_pc

        
for line in input_lines:
    commands.append(line.rstrip())

# Build a reverse graph between pcs, a -> b if executing b leads to a
build_graph(commands)
# Starting at the end, find all the pcs that lead to the end. These won't
# be cyclic
find_frontier(len(commands))
# Execute the instructions. If at any point, switching an op will take us
# into the frontier set, we know we can reach the end from there.
run_instrs(commands)
