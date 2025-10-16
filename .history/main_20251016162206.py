
from utils import *



def huffman(s: str):
    count = frequencies(s)
    count = sorted([FrequencyNode(key, count[key]) for key in count])
    head = FrequencyNode()
    while len(count) != 1:
        el1, el2 = count.pop(0), count.pop(0)
        newEl = el1 + el2
        head = newEl
        appendWithOrder(count, newEl)
    return head
    
head = huffman("abbcccdddd")
print(head)
print(head.codes())
print(head.maxLevel())