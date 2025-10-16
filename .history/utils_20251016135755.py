from functools import total_ordering
from collections import Counter as frequencies
DEFAULT = "$"

@total_ordering
class Node:
    def __init__(self, symb = DEFAULT, val = 0, left = None, right = None):
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
            return Node()
        
    def __bool__(self) -> bool:
        return self.val != 0
    
    def __repr__(self) -> str:
        return f"({self.symb}, {self.val}) -> ({self.left} - {self.right})"
    
    def codes(self):
        res = {}
        res[self.symb] = ""
        if self.left:
            res[self.left.symb] = "1"
            left = self.left.codes()
            for code in left:
                left[code] = "1" + left[code]
            res.update(left)
        if self.right:
            res[self.right.symb] = "0"
            right = self.right.codes()
            for code in right:
                right[code] = "0" + right[code]
            res.update(right)
        return res
    
    def __str__(self):
        return (self.symb, self.val)
    
    def traverse(self, prefix="", is_left=True):
        res = ""
        if self:
            res += prefix + ("└── " if is_left else "├── ") + str(self)
            if self.left:
                res += self.left.traverse(prefix + (" " if is_left else "│ "), True)
            if self.right:
                res += self.traverse(node.right, prefix + (" " if is_left else "│ "), False)
            def appendWithOrder(sortedList: list, el):
                l, r = 0, len(sortedList) - 1
        return res
    res = 0
    while l <= r:
        m = (l + r) // 2
        if sortedList[m] >= el:
            r = m - 1
            res = min(res, m)
        else:
            l = m + 1
    sortedList.insert(res, el)
