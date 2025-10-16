
from collections import Counter, deque
import bissect


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
        return False

def huffman(s: str) -> str:
    count = Counter(s)
    count = sorted([Node(key, count[key]) for key in count])
    head = Node()
    now = head
    while count:
        el1, el2 = count[:2]
        count = count[2:]
        
    
    print(count)
    return ""
    
huffman("hfbfr:hfffknre;drfjkl")