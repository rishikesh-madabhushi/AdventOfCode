import re

f = open("day_7_0.txt")
         
input_lines = f.readlines()

src_re = re.compile(r"(.+)\s+bags")
tgt_re = re.compile(r"\s*(\d+)\s+(.+)\s+bag")

graph = {}

visited = set ()

def DFS(node, count):
    visited.add(node)
    if node not in graph:
        return count
    for child in graph[node]:
        if child in visited:
            continue
        else:
            count = DFS(child, count + 1)
    return count

for line in input_lines:
    srctgts = line.rstrip().split(" contain ")
    src = src_re.match(srctgts[0]).group(1)
    print(src)
    tgts = srctgts[1].split(',')
    for tgt in tgts:
        print(tgt)
        if tgt == "no other bags.":
            continue
        target_match = tgt_re.match(tgt)
        target_count = target_match.group(1)
        target = target_match.group(2)
        if target in graph:
            graph[target].append(src)
        else:
            graph[target] = [src]

        print(target, target_count)


print(graph)
print(DFS("shiny gold", 0))


