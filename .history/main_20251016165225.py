
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
    tree = huffman(s)
    codes = tree.codes()
    res = "".join(codes[c] for c in s)
    return res, tree

def decode(s: str, tree: FrequencyNode):
    res = ""
    binaryList = list(s)
    l, r = 0, len(s)
    codes = tree.codes()
    while l < r:
        if s[l: r] in codes:
            res += codes[s[l: r]]
            l = r
            r = len(s)
        else:
            r -= 1
    pass

    
print(codeAndTree("abbcccdddd"))