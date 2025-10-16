
from utils import *



def huffman(s: str):
    count = frequencies(s)
    count = sorted([Node(key, count[key]) for key in count])
    head = Node()
    res = {}
    while len(count) != 1:
        el1, el2 = count.pop(0), count.pop(0)
        newEl = el1 + el2
        head = newEl
        appendWithOrder(count, newEl)
    return head, res
    
huffman("abbccc")