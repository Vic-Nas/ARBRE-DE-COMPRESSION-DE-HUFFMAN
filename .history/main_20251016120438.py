
from collections import Counter, deque


class Node:
    def __init__(self, symb = "$", val = 0, left = None, right = None):
        self.symb = symb
        self.val = val
        self.left = left
        self.right = right        

def huffman(s: str) -> str:
    count = Counter(s)
    count = sorted([Node(key, count[key]) for key in count])
    print(count)
    return ""
    
huffman("hfbfr:hfffknre;drfjkl")