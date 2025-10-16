
from collections import Counter

class Node:
    def __init__(self, symb = "$", val = 0, left = None, right = None):
        self.symb = symb
        self.val = val
        self.left = left
        self.right = right        

def huffman(s: str) -> str:
    count = Counter(s)
    print(count)
    print(count["h"])
    return ""
    
huffman("hfbfr:hfffknre;drfjkl")