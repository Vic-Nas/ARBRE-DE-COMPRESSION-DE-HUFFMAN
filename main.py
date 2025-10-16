
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

def encode(s: str, tree: FrequencyNode = None):
    if tree == None:
        tree = huffman(s)
    codes = tree.codes()
    return "".join(codes[c] for c in s), tree

def decode(code: str, tree: FrequencyNode):
    res = ""
    l, r = 0, len(code)
    codes = {
        value: key for key, value in tree.codes().items()
    }
    while l < r:
        if code[l: r] in codes:
            res += codes[code[l: r]]
            l = r
            r = len(code)
        else:
            r -= 1
    return res


if __name__ == "__main__":
    s = input("String to encode: ")
    code, tree = encode(s)
    print(code)
    print(tree)
    print(tree.codes())
    print("\nEncode string using previous tree:")
    while True:
        s = input("Input string: ")
        code, _ = encode(s, tree)
        print("\t" + code)
        