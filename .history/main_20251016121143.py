
from collections import Counter, deque


class Node:
    def __init__(self, symb = "$", val = 0, left = None, right = None):
        self.symb = symb
        self.val = val
        self.left = left
        self.right = right       

    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other) -> bool:
        if type(self) == type(other): 
            return self.val == other.val
        else:
            return True

def huffman(s: str) -> str:
    count = Counter(s)
    count = sorted([Node(key, count[key]) for key in count])
    print(count)
    return ""
    
huffman("hfbfr:hfffknre;drfjkl")