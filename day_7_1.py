import re

f = open("day_7_0.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

src_re = re.compile(r"(.+)\s+bags")
tgt_re = re.compile(r"\s*(\d+)\s+(.+)\s+bag")

graph = {}

def DFS(node):
    count = 1
    if node not in graph:
        return 1
    for (child, c_count) in graph[node]:
        print ("Processing %s %d" % (child, c_count))
        count += c_count * DFS(child)
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
        target_count = int(target_match.group(1))
        target = target_match.group(2)
        if src in graph:
            graph[src].append((target, target_count))
        else:
            graph[src] = [(target, target_count)]

        print(target, target_count)


print(graph)
print(DFS("shiny gold") - 1)


