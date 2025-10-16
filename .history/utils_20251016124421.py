from functools import total_ordering
from collections import Counter as frequencies

@total_ordering
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
    
    def __add__(self, other):
        if type(self) == type(other):
            mini, maxi = sorted([self, other])
            return Node(val = self.val + other.val, 
                        left = mini,
                        right = maxi)
        else:
            return None
        
    def __bool__(self) -> bool:
        return self.val != 0
    
    def __repr__(self) -> str:
        return "f({self.symb}, {self.val}) -> {self.left} - {self.right}"

def appendWithOrder(sortedList: list, el):
    l, r = 0, len(sortedList) - 1
    res = 0
    while l <= r:
        m = (l + r) // 2
        if sortedList[m] >= el:
            r = m - 1
            res = min(res, m)
        else:
            l = m + 1
    sortedList.insert(res, el)
