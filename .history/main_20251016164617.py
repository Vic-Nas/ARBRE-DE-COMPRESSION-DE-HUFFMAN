
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

def codeAndTree(s: str):
    head = huffman(s)
    codes = head.codes()
    res = "".join(codes[c] for c in s)
    return res, head

    
print(code("abbcccdddd"))