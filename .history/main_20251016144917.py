
from utils import *



def huffman(s: str):
    count = frequencies(s)
    count = sorted([Node(key, count[key]) for key in count])
    head = Node()
    while len(count) != 1:
        el1, el2 = count.pop(0), count.pop(0)
        newEl = el1 + el2
        head = newEl
        appendWithOrder(count, newEl)
    return head
    
head = huffman("abbccc")
print(head)
print(head.codes())
el = Node("c", 3)
print(el.level(head))
print(head.maxDepth())