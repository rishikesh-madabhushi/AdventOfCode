import re
import pprint

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes[0])
            self.head = node
            for elem in nodes[1:]:
                node.next = Node(data=elem)
                node = node.next
            node.next = self.head
    
    def __iter__(self):
        node = self.head
        if not node:
            return
        yield node
        node = node.next
        while node != self.head:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = [str(node.data)]
        node = node.next
        while node != self.head:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("Back to Head")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

    def __repr__(self):
        return str(self.data)

#input = [3,8,9,1,2,5,4,6,7]


input = [6,5,3,4,2,7,9,1,8]
input = input + [d for d in range(len(input) + 1, 1000001)]
layout = LinkedList(input)
#print(layout, len(input))

nturns = 10000000
max_cup = 1000000
min_cup = min(input)

value_map = {}
for n in layout:
    value_map[n.data] = n

#print(value_map)

for i in range(0, nturns):
    if i % 100000 == 0:
        print("Did %d moves" % i)
    cur_val = layout.head.data
    next1 = layout.head.next
    next2 = next1.next
    next3 = next2.next
    next_val = cur_val - 1
    next = None
    while not next:
        if next_val in value_map:
           next_cand = value_map[next_val]
           if next1 != next_cand and next2 != next_cand and next3 != next_cand:
               next = next_cand
               continue     
        next_val -= 1
        if next_val < min_cup:
            next_val = max_cup
    tmp = next.next
    next.next = layout.head.next
    layout.head.next = next3.next
    next3.next = tmp
    layout.head = layout.head.next


final = value_map[1]
node1 = final.next
node2 = final.next.next

print(node1.data * node2.data)